#!/usr/bin/env python3
"""Exact active-invariant and period-boundary identities, v24 (2026-11-21).

Run from the repository root:
    python computations/verify_active_invariants.py

Conventions: g=p(x^3+y^3+z^3)/3+qxyz, S=c4(g), T=-c6(g),
and phi(g)=g+det(Hess(g))/24. Fisher's ternary invariants use
S=q(q^3-8p^3), T=q^6+20p^3q^3-8p^6.

The rational polynomial identities below are checked coefficient by
coefficient, without numerical specialization. They certify the formulas
used in the manuscript's degree-nine invariant map. Geometric generic
integrality, opposite invariance, and degree 18e_n use the written proofs.
The boundary checks include the local third-division Kummer coordinates,
the special-fibre line matrix, and its explicit rational relative lift.
They do not calculate the full period
phase, prove integral Ext flatness, or prove extension of a comparison kernel.
"""

import sympy as sp


def zero_polynomial(expression, variables):
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    assert polynomial.is_zero, polynomial


def main():
    p, q, S, T = sp.symbols("p q S T")
    ration = sp.Rational
    s = q * (q**3 - 8 * p**3)
    t = q**6 + 20 * p**3 * q**3 - 8 * p**6
    p_new = p * (1 - q**2 / 4)
    q_new = q + p**3 / 3 + q**3 / 12
    a4 = (S + T / 3 + S**2 / 24 + S*T / 432
          - S**3 / 6912 + T**2 / 5184)
    a6_minus = (T + S**2 / 2 + 5*S*T / 48 + 5*T**2 / 432
               + 5*S**2*T / 6912 + S**4 / 13824
               + S**3*T / 331776 - S*T**2 / 20736
               - T**3 / 373248)
    discriminant_ratio = 1 - S / 24 - T / 216 - S**2 / 6912

    zero_polynomial(
        sp.Matrix([s, t]).jacobian([p, q]).det()
        + 384*p**2*(p**3+q**3)**2, (p, q))
    print("PASS: dominant Hesse invariant map, det Dr=-384 p^2(p^3+q^3)^2")

    for target, formula in ((s, a4), (t, a6_minus)):
        zero_polynomial(
            target.subs({p: p_new, q: q_new}, simultaneous=True)
            - formula.subs({S: s, T: t}, simultaneous=True), (p, q))
    print("PASS: r o psi = a o r, both invariant coordinates")

    zero_polynomial(
        a4**3-a6_minus**2-(S**3-T**2)*discriminant_ratio**3,
        (S, T))
    print("PASS: discriminant identity (a4^3-a6minus^2)=(S^3-T^2)D^3")

    zero_polynomial(
        sp.Matrix([a4, a6_minus]).jacobian([S, T]).det()
        - (1-S/16)*discriminant_ratio**2, (S, T))
    zero_polynomial(
        sp.Matrix([p_new, q_new]).jacobian([p, q]).det()
        - (1-s/16), (p, q))
    print("PASS: Jacobian identities det Da=(1-S/16)D^2, det Dpsi=1-s/16")

    zero_polynomial(s.subs({p: -p, q: -q}, simultaneous=True)-s, (p, q))
    zero_polynomial(t.subs({p: -p, q: -q}, simultaneous=True)-t, (p, q))
    print("PASS: both primitive invariants are unchanged by the opposite sign")

    zero_polynomial(s**3-t**2-(-4*p*(p**3+q**3))**3, (p, q))
    print("PASS: the discriminant becomes the specified cube on the Hesse field")

    zeta = sp.symbols("zeta")
    boundary = discriminant_ratio.subs({S: s, T: t}, simultaneous=True)
    eight_lines = -(q**2-4)*sp.prod(
        (2*zeta**i*p-q)**2+12 for i in range(3)) / 6912
    reduced = sp.rem(sp.expand(boundary-eight_lines), zeta**2+zeta+1, zeta)
    zero_polynomial(reduced, (p, q, zeta))
    print("PASS: the additional boundary is the product of eight Hesse lines")

    zero_polynomial(boundary.subs(q, 2), (p,))
    zero_polynomial(sp.diff(boundary, q).subs(q, 2)+(p**3+8)**2/27, (p,))
    zero_polynomial(s.subs(q, 2)-(16-16*p**3), (p,))
    zero_polynomial(t.subs(q, 2)-(64+160*p**3-8*p**6), (p,))
    print("PASS: the q=2 boundary has multiplicity one and the stated residue map")

    center_u = 1+q**2/2+p**3*q/6-q**4/48
    center_v = (4-q**2)*(12*q+q**3-8*p**3)/48
    zero_polynomial(center_u.subs(q, 2)-(p**3+8)/3, (p,))
    zero_polynomial(center_v.subs(q, 2), (p,))
    zero_polynomial(p_new.subs(q, 2), (p,))
    zero_polynomial(q_new.subs(q, 2)-(p**3+8)/3, (p,))
    zero_polynomial(-2*center_u.subs(q, 2)+2*q_new.subs(q, 2), (p,))
    print("PASS: the specified active center becomes -2 times the boundary point cubic")

    x, y, z = sp.symbols("x y z")
    point_cubic = p_new*(x**3+y**3+z**3)/3 + q_new*x*y*z
    point = {x: 1-q/2, y: -1-q/2, z: -p}
    zero_polynomial(point_cubic.subs(point, simultaneous=True), (p, q))
    # At each node of xyz=0, the transverse derivative is -p/3, a unit.
    nodes = ({x: 1, y: 0, z: 0}, {x: 0, y: 1, z: 0},
             {x: 0, y: 0, z: 1})
    for node in nodes:
        zero_polynomial(sp.diff(point_cubic, q).subs(q, 2).subs(node)+p/3, (p,))
    intersection = sp.ones(3)-3*sp.eye(3)
    multidegree = sp.Matrix([1, 0, -1])
    assert intersection*multidegree == -3*multidegree
    component_character = sp.Matrix([[0, 1, 2]])
    assert all(int(entry) % 3 == 0 for entry in component_character*intersection)
    assert int((component_character*multidegree)[0]) % 3 != 0
    print("PASS: point section, regular I3 nodes and nonzero order-three component class")

    aa, bb, w = sp.symbols("aa bb w")
    y_local = -1+bb*w/aa-(aa**3+bb**3)*w**3/(3*aa**3)
    local_curve = aa*(1+y_local**3+w**3)/3+bb*y_local*w
    for power in range(4):
        assert sp.cancel(sp.expand(local_curve).coeff(w, power)) == 0
    ell_o_local = aa*(1+y_local)-bb*w
    ell_o_lead = -(aa**3+bb**3)/(3*aa**2)
    assert sp.cancel(sp.expand(ell_o_local).coeff(w, 3)-ell_o_lead) == 0
    tangent_curve = aa*(x**3+y**3+z**3)/3+bb*x*y*z
    assert sp.cancel(tangent_curve.subs(y, -x+bb*z/aa)
                     -(aa**3+bb**3)*z**3/(3*aa**2)) == 0
    ct = 3*aa**2*(aa+bb)/(aa**3+bb**3)
    cu = -3*aa**3*(1-zeta**2)/(aa**3+bb**3)
    assert sp.cancel((-aa-bb)/ell_o_lead-ct) == 0
    assert sp.cancel(aa*(1-zeta**2)/ell_o_lead-cu) == 0
    print("PASS: flex tangent contact and normalized leading coefficients at the origin")

    ell_o = p_new*(x+y)-q_new*z
    ell_t = -q_new*x+p_new*(y+z)
    ell_u = p_new*x+p_new*zeta**2*y-q_new*zeta*z
    ct_pq = ct.subs({aa: p_new, bb: q_new}, simultaneous=True)
    cu_pq = cu.subs({aa: p_new, bb: q_new}, simultaneous=True)
    ft_point = sp.cancel(ell_t.subs(point, simultaneous=True)
                         /ell_o.subs(point, simultaneous=True)/ct_pq)
    fu_point = sp.cancel(ell_u.subs(point, simultaneous=True)
                         /ell_o.subs(point, simultaneous=True)/cu_pq)
    ft_lead = sp.cancel((q-2)*ft_point).subs(q, 2)
    fu_lead = sp.cancel((q-2)**3*fu_point).subs(q, 2)
    assert sp.cancel(ft_lead-((p+2)/(3*p))**3*(p**3+8)/2) == 0
    fu_expected = zeta/(3*(1-zeta**2))*((p**3+8)/(3*p))**3
    numerator, denominator = sp.fraction(sp.cancel(fu_lead-fu_expected))
    zero_polynomial(sp.rem(sp.expand(numerator), zeta**2+zeta+1, zeta),
                    (p, zeta))
    assert denominator != 0
    # The nontrivial Kummer coordinate has valuation -1, hence exact order 3.
    # The other leading coefficient is a constant cube times a rational cube.
    print("PASS: third-division Kummer coordinates [(p^3+8)/(2(q-2))] and 1")

    line_matrix = sp.Matrix([[z, 0, 0], [p*y, -2*z, x], [-x, y, 0]])
    zero_polynomial(line_matrix.det()+x*y*z, (p, x, y, z))
    rows = ((x, sp.Matrix([[-p*y**2, y*z, 2*z**2]])),
            (y, sp.Matrix([[x, 0, z]])),
            (z, sp.Matrix([[x+y, 0, 0]])))
    for component, row in rows:
        for entry in (row*line_matrix).subs(component, 0):
            zero_polynomial(entry, (p, x, y, z))
    for node in nodes:
        assert line_matrix.subs(node).rank() == 2
    # The rational sections agree at the three nodes. On C_x divide by 2z-py.
    sx = rows[0][1]/(2*z-p*y)
    sy, sz = rows[1][1], rows[2][1]
    assert sx.subs(nodes[2]) == sy.subs(nodes[2])
    assert sy.subs(nodes[0]) == sz.subs(nodes[0])
    assert sx.subs(nodes[1]) == sz.subs(nodes[1])
    print("PASS: boundary line resolution, node ranks and gluing of the three sections")

    # A direct relative lift avoids solving formal deformation equations.
    # Verify its determinant first with independent Weierstrass coefficients,
    # then check the short rational coordinate identities.  Expanding the
    # determinant after substituting all Hesse coefficients is unnecessary.
    fx, fy, fw, pu, pv, wa0, wa2, wa4, wa6 = sp.symbols(
        "fx fy fw pu pv wa0 wa2 wa4 wa6")
    normal_matrix = sp.Matrix([
        [fx-pu*fw, fy-pv*fw, 0],
        [0, wa0*fx+(wa0*pu+wa2)*fw, fw],
        [fy+pv*fw, (wa0*pu**2+wa2*pu+wa4)*fw, -fx],
    ])
    normal_cubic = fy**2*fw-wa0*fx**3-wa2*fx**2*fw-wa4*fx*fw**2-wa6*fw**3
    point_relation = wa0*pu**3+wa2*pu**2+wa4*pu+wa6-pv**2
    zero_polynomial(normal_matrix.det()-normal_cubic-point_relation*fw**3,
                    (fx, fy, fw, pu, pv, wa0, wa2, wa4, wa6))
    # The transpose before dualizing is the matrix of the line at -P.
    # Its left-kernel row consists of the slope at -P, -1, and a linear
    # function of the affine x-coordinate; this fixes the sign of P.
    affine_matrix = normal_matrix.T.subs(fw, 1)
    line_sections = sp.Matrix([[(fy-pv)/(fx-pu), -1,
                               wa0*(fx+pu)+wa2]])
    section_relations = line_sections*affine_matrix
    for entry in section_relations[:, :2]:
        assert sp.cancel(entry) == 0
    assert sp.cancel((fx-pu)*section_relations[0, 2]
                     -(fy**2-wa0*fx**3-wa2*fx**2-wa4*fx-wa6)
                     -point_relation) == 0

    aa_lift, bb_lift = p_new, q_new
    cc_lift = p*(p**3+q**3)/3
    b0 = (p**3+8)/3
    lift_parameters = {
        wa0: -4*aa_lift*(aa_lift**3+bb_lift**3)/(3*bb_lift**3),
        wa2: 1+4*aa_lift**3/bb_lift**3,
        wa4: -4*aa_lift**2/bb_lift**3,
        wa6: 4*aa_lift/(3*bb_lift**3),
        pu: -q/cc_lift, pv: 2/cc_lift,
    }
    lift_coordinates = {fx: x+y, fy: x-y,
                        fw: aa_lift*(x+y)-bb_lift*z}
    assert sp.cancel(point_relation.subs(lift_parameters, simultaneous=True)) == 0
    assert sp.cancel(normal_cubic.subs(lift_parameters, simultaneous=True)
                     .subs(lift_coordinates, simultaneous=True)-4*point_cubic) == 0
    # All denominators in these parameters and coordinate changes are units
    # at q=2.  The following matrices are constant over the trait.
    for denominator_unit in (p, bb_lift, cc_lift, b0):
        assert sp.factor(denominator_unit.subs(q, 2)) != 0
    uu_lift = sp.Matrix([[4, -2, -2*p], [-4*b0*p, 0, 0], [4, -2, 2*p]])
    vv_lift = sp.Matrix([[0, -p, -1], [2*p, p, -1], [2*p, -p, 1]])
    zero_polynomial(uu_lift.det()+32*b0*p**2, (p,))
    zero_polynomial(vv_lift.det()-8*p**2, (p,))
    special_parameters = {variable: sp.cancel(value.subs(q, 2))
                          for variable, value in lift_parameters.items()}
    special_coordinates = {variable: value.subs(q, 2)
                           for variable, value in lift_coordinates.items()}
    special_matrix = normal_matrix.subs(special_parameters, simultaneous=True)\
        .subs(special_coordinates, simultaneous=True)
    for entry in special_matrix*vv_lift-uu_lift*line_matrix:
        assert sp.cancel(entry) == 0
    assert sp.cancel(4*vv_lift.det()/uu_lift.det()+1/b0) == 0
    print("PASS: explicit relative line matrix, point orientation and determinant normalization")

    # The adjugate entries span every quadratic form at the boundary.
    # Row-major order of its six nonzero entries fixes the determinant sign.
    boundary_adjugate = line_matrix.adjugate()
    quadratic_monomials = (x**2, x*y, x*z, y**2, y*z, z**2)
    adjugate_entries = [entry for entry in boundary_adjugate if entry != 0]
    assert len(adjugate_entries) == 6
    quadratic_pairing = sp.Matrix([
        [sp.Poly(entry, x, y, z).coeff_monomial(monomial)
         for monomial in quadratic_monomials]
        for entry in adjugate_entries
    ])
    zero_polynomial(quadratic_pairing.det()-2*p, (p,))

    # Tensor the active MF with two elementary center factorizations.
    # The symbols g1_mf,g2_mf are arbitrary commuting coefficients, so this
    # checks the identity for any quadratic center complements by substitution.
    u1_mf, u2_mf, g1_mf, g2_mf = sp.symbols("u1_mf u2_mf g1_mf g2_mf")
    differential_mf = sp.zeros(6)
    differential_mf[:3, 3:] = line_matrix
    differential_mf[3:, :3] = -b0*boundary_adjugate
    parity_mf = sp.diag(1, 1, 1, -1, -1, -1)
    elementary_parity = sp.diag(1, -1)
    for center_variable, center_complement in ((u1_mf, g1_mf), (u2_mf, g2_mf)):
        elementary_mf = sp.Matrix([[0, center_variable], [center_complement, 0]])
        differential_mf = (sp.kronecker_product(differential_mf, sp.eye(2))
                           + sp.kronecker_product(parity_mf, elementary_mf))
        parity_mf = sp.kronecker_product(parity_mf, elementary_parity)
    assert sum(parity_mf[i, i] == 1 for i in range(24)) == 12
    assert sum(parity_mf[i, i] == -1 for i in range(24)) == 12
    full_curvature = b0*x*y*z+u1_mf*g1_mf+u2_mf*g2_mf
    tensor_defect = differential_mf**2-full_curvature*sp.eye(24)
    for entry in tensor_defect:
        zero_polynomial(entry, (p, x, y, z, u1_mf, u2_mf, g1_mf, g2_mf))
    print("PASS: rank-six adjugate pairing and rank-12 two-center tensor MF curvature")

    # The exact Fermat specialization fixes the sign convention c6=-T.
    assert (s.subs({p: 1, q: 0}), t.subs({p: 1, q: 0})) == (0, -8)
    assert a4.subs({S: 0, T: -8}) == -ration(215, 81)
    print("All identities verified over QQ or QQ(zeta_3); no sampling or formal proof assistant used.")


if __name__ == "__main__":
    main()
