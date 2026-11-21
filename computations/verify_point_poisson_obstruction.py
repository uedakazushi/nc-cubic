#!/usr/bin/env python3
"""Exact finite certificates for point/Poisson comparison obstructions.

Checks the 24-variable integrability matrix in dimension N=8 and the
polynomial identities used to classify the Hessian-rank-two points of a
split Hesse cubic threefold.  Also checks their kernel cubic forms and the
nonzero j-invariant difference used to distinguish local Artin algebras.

The complete geometric case split, the local associated-graded argument,
and categorical comparison/Torelli theorems are not proved by this script.

Run: python3 computations/verify_point_poisson_obstruction.py
Requires: SymPy.
"""

import sympy as sp


def verify_quadratic_net():
    x, y, z = sp.symbols("x y z")
    central = sp.symbols("u1:6")
    coords = (x, y, z, *central)
    g = (x**3 + y**3 + z**3) / 3 + x*y*z
    Q1 = sum(u**2 for u in central)
    Q2 = sum(i*u**2 for i, u in enumerate(central, 1))
    Q3 = 2*central[0]*central[1] + 2*central[2]*central[3]
    F = g + x*Q1 + y*Q2 + z*Q3
    quadrics = tuple(sp.diff(F, a) for a in (x, y, z))
    matrices = tuple(sp.hessian(q, coords) / 2 for q in quadrics)
    A1, A2, A3 = matrices
    assert all(A == A.T for A in matrices)
    assert A1.det() != 0

    skew = A3*A1.inv()*A2 - A2*A1.inv()*A3
    assert skew.T == -skew
    expected_active = sp.Matrix([
        [0, 0, 0],
        [0, 0, -sp.Rational(7, 4)],
        [0, sp.Rational(7, 4), 0],
    ])
    block = sp.Matrix([[0, 1], [-1, 0]])
    expected = sp.diag(expected_active, block, block, sp.zeros(1))
    assert skew == expected
    assert skew.rank() == 6
    print("PASS: exact 8-by-8 skew matrix has rank 6 and nullity 2")

    zero = sp.zeros(8)
    full = sp.BlockMatrix([
        [A2, -A1, zero],
        [A3, zero, -A1],
        [zero, A3, -A2],
    ]).as_explicit()
    assert full.shape == (24, 24)
    assert full.rank() == 22
    lifted = []
    for v1 in skew.nullspace():
        triple = sp.Matrix.vstack(v1, A1.inv()*A2*v1, A1.inv()*A3*v1)
        assert full*triple == sp.zeros(24, 1)
        lifted.append(triple)
    assert sp.Matrix.hstack(*lifted).rank() == 2
    print("PASS: the full integrability matrix has rank 22 and the same kernel")

    standard = sp.Matrix.vstack(*[sp.eye(8)[:, i] for i in range(3)])
    assert full*standard == sp.zeros(24, 1)
    assert 8 - skew.rank() >= 2
    print("PASS: the original active support is one nonzero integrable solution")


def verify_hesse_hessian():
    x, y, z, u, v, t, e, s, h = sp.symbols("x y z u v t e s h")
    active = (x, y, z)
    coords = (*active, u, v)
    g = (x**3 + y**3 + z**3) / 3 + t*x*y*z
    F = g + (u**3 + v**3) / 3
    H = sp.hessian(g, active)
    HF = sp.hessian(F, coords)
    assert HF == sp.diag(H, 2*u, 2*v)

    # If all 2-by-2 minors vanish and t*(t^3-8) is invertible,
    # these three identities force x=y=z=0 over a field.
    for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        mixed = H.extract([a, b], [a, c]).det()
        principal = H.extract([b, c], [b, c]).det()
        q = 2*active[a]**2 - t*active[b]*active[c]
        assert sp.expand(mixed - t*q) == 0
        assert sp.expand(t*principal + 4*q - (8-t**3)*active[a]**2) == 0
    assert sp.expand(H.det() + 6*t**2*g - 8*(1+t**3)*x*y*z) == 0
    print("PASS: exact minor identities exclude active Hessian rank <= 1")
    print("PASS: the active Hessian determinant on the cubic is 8*(1+t^3)*xyz")

    def cube_reduce(expr):
        return sp.expand(sp.rem(sp.expand(expr), e**3-1, e))

    # The variable e represents all three roots of unity at once.
    center = {x: 0, y: 0, z: 0, u: 1, v: -e}
    center_hessian = HF.subs(center)
    center_kernel = sp.Matrix.hstack(*(sp.eye(5)[:, i] for i in range(3)))
    assert cube_reduce(F.subs(center)) == 0
    assert center_hessian*center_kernel == sp.zeros(5, 3)
    assert cube_reduce(center_hessian.extract([3, 4], [3, 4]).det() * (-e**2/4)) == 1
    assert sp.expand(F.subs({u: 0, v: 0}) - g) == 0

    for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        p = [sp.Integer(0)]*5
        p[a], p[b] = sp.Integer(1), -e
        r = [sp.Integer(0)]*5
        r[a], r[b], r[c] = t*e/2, t*e**2/2, sp.Integer(1)
        point = dict(zip(coords, p))
        tangent_kernel = sp.Matrix.hstack(sp.Matrix(r), sp.eye(5)[:, 3], sp.eye(5)[:, 4])
        hessian_at_point = HF.subs(point)
        assert cube_reduce(F.subs(point)) == 0
        assert (hessian_at_point*tangent_kernel).applyfunc(cube_reduce) == sp.zeros(5, 3)
        minor = hessian_at_point.extract([a, b], [a, b]).det()
        assert cube_reduce(minor*(-e**2/4)) == 1
        substitution = {active[i]: s*r[i] for i in range(3)}
        kernel_cubic = F.subs(substitution, simultaneous=True)
        expected = ((1+t**3)*s**3 + u**3 + v**3) / 3
        assert cube_reduce(kernel_cubic - expected) == 0
    print("PASS: all three central and nine flex points have the stated rank-two kernels")
    print("PASS: kernel cubics are Hesse at central points and Fermat at flex points")

    def j(value):
        value = sp.sympify(value)
        return 27*value**3*(8-value**3)**3/(1+value**3)**3

    lam = (h + h**2/3 + h**5/12)/(1-h**4/4)
    difference = sp.cancel(j(lam)-j(h))
    numerator, denominator = sp.fraction(difference)
    valuation = min(monomial[0] for monomial, coefficient in sp.Poly(numerator, h).terms())
    assert valuation == 4 and denominator.subs(h, 0) != 0
    assert sp.cancel(numerator/h**4).subs(h, 0) / denominator.subs(h, 0) == 13824
    assert sp.cancel(j(h)) != 0 and j(0) == 0
    for forbidden in (lam, 1+lam**3, 8-lam**3):
        assert sp.cancel(forbidden) != 0
    print("PASS: j(lambda)-j(h) has exact leading term 13824*h^4, and j(h) != 0")


def main():
    verify_quadratic_net()
    verify_hesse_hessian()
    print("Scope: finite polynomial certificates; full geometric and categorical proofs are in the paper.")


if __name__ == "__main__":
    main()
