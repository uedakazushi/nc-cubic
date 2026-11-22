#!/usr/bin/env python3
"""Exact finite certificates for the linear boundary comparison (2026-11-22).

The quadratic-dual multiplication is derived from the three defining
relations of S(1,-1,-1), rather than a chosen multiplication table.  The
left and right zero-arity primitives are independent.  Their unary gauge
image is diagonal plus skew-symmetric; its intersection with symmetric
PBW corrections is exactly diagonal.  Thus the normalized three PBW
directions cannot be removed by such a primitive.

The second calculation checks the degree inequalities in the *non-split*
fixed-counit tower, including the adjacent group needed for the long exact
sequence.  Nonnegative symbolic variables give certificates for every
k >= 2 and every arity, not a test on a finite sample of k or arities.

These computations do not identify the actual categorical Bockstein with
the deformation cochain.  That identification and the construction of a
coherent Morita comparison require the proofs in the mixed manuscript.
No PI assertion, explicit comparison polynomial, or formal proof-assistant
verification is supplied by this script.

Requires Python 3 and SymPy.  From the repository root run:
  python3 computations/verify_mixed_linear_bockstein.py
"""

from itertools import product

import sympy as sp


def negative_on_orthant(expression, variables):
    """Sufficient exact certificate: constant < 0, all coefficients <= 0."""
    poly = sp.Poly(sp.expand(expression), *variables)
    assert poly.TC() < 0
    assert all(coefficient <= 0 for coefficient in poly.coeffs())


def main():
    words = list(product(range(3), repeat=2))
    relations = sp.zeros(3, 9)
    for i, (j, k) in enumerate(((1, 2), (2, 0), (0, 1))):
        relations[i, words.index((j, k))] = 1
        relations[i, words.index((k, j))] = -1
        relations[i, words.index((i, i))] = -1
    assert relations.rank() == 3

    # Identify (S!)_2 with R*, using xi_x^2, xi_y^2, xi_z^2 as basis.
    # Each of these evaluates to -1 on its corresponding primal relation.
    def dual_product(i, j):
        return -relations[:, words.index((i, j))]

    for i in range(3):
        assert dual_product(i, i) == sp.eye(3)[:, i]
    for i, j in ((0, 1), (1, 2), (2, 0)):
        assert dual_product(i, j) + dual_product(j, i) == sp.zeros(3, 1)
    print("PASS quadratic-dual products derived from the relation pairing")

    left = sp.symbols("Lx Ly Lz")
    right = sp.symbols("Rx Ry Rz")
    gauge = sp.zeros(3, 3)
    for j in range(3):
        gauge[:, j] = sum(
            (left[i] * dual_product(i, j)
             + right[i] * dual_product(j, i) for i in range(3)),
            sp.zeros(3, 1),
        )
    for i in range(3):
        assert gauge[i, i] == left[i] + right[i]
    assert gauge + gauge.T == 2 * sp.diag(
        *(left[i] + right[i] for i in range(3))
    )
    gauge_matrix = sp.Matrix(list(gauge)).jacobian(left + right)
    assert gauge_matrix.rank() == 6
    print("PASS independent left/right primitives span diagonal plus skew matrices")

    p, q, r = sp.symbols("p q r")
    pbw = -sp.Matrix(((0, p, r), (p, 0, q), (r, q, 0)))
    pbw_matrix = sp.Matrix(list(pbw)).jacobian((p, q, r))
    combined = gauge_matrix.row_join(pbw_matrix)
    assert combined.det() == -64
    symmetry = sp.Matrix((gauge[0, 1] - gauge[1, 0],
                          gauge[1, 2] - gauge[2, 1],
                          gauge[2, 0] - gauge[0, 2])).jacobian(left + right)
    symmetric_gauge = gauge_matrix * sp.Matrix.hstack(*symmetry.nullspace())
    assert symmetric_gauge.rank() == 3
    assert all(symmetric_gauge[3 * i + j, :] == sp.zeros(1, 3)
               for i in range(3) for j in range(3) if i != j)
    print("PASS symmetric PBW/gauge intersection is diagonal; complementary determinant -64")

    # These two bidegree equations exclude every negative Tate power as well.
    exterior_degree, t_power = sp.symbols("exterior_degree t_power")
    answer = sp.solve((exterior_degree + 2 * t_power - 1,
                       -exterior_degree - 3 * t_power + 1),
                      (exterior_degree, t_power))
    assert answer == {exterior_degree: 1, t_power: 0}
    print("PASS zero-arity primitives of bidegree (1,-1) lie in F_1 with Tate power 0")

    # Put k=2+K, arity=2+R, i=I.  All variables below are nonnegative.
    K, R, I, H = sp.symbols("K R I H", nonnegative=True, integer=True)
    k, arity = 2 + K, 2 + R
    degree = 2 - arity - I
    a_A, b_A = degree - arity, 2 * arity
    a_B, b_B = degree - arity + 1, 2 * arity - 2
    narrow_expressions = (
        2 * b_A + 3 * a_A - 3 * k,
        2 * b_B + 3 * a_B - 3 * k,
        2 * b_B + 3 * (a_B - 1) - 3 * k,
    )
    for expression in narrow_expressions:
        negative_on_orthant(expression, (K, R, I))
    print("PASS no narrow sectors in A_r^d, B_r^d or B_r^(d-1), for all k>=2")

    # Identity sectors have even cohomological degree.  In B_r^d this
    # requires I odd, while B_r^(d-1) and A_r^d require I even.
    jac_A = sp.expand(b_A + 3 * a_A / 2).subs(I, 2 * H)
    jac_B = sp.expand(b_B + 3 * a_B / 2).subs(I, 1 + 2 * H)
    jac_B_previous = sp.expand(b_B + 3 * (a_B - 1) / 2).subs(I, 2 * H)
    for expression in (jac_B, jac_B_previous):
        negative_on_orthant(expression, (R, H))
    assert sp.expand(jac_A) == 1 - R - 3 * H
    assert jac_A.subs({R: 0, H: 0}) == 1
    assert jac_A.subs({R: 1, H: 0}) == 0
    negative_on_orthant(jac_A.subs(R, R + 2), (R, H))
    negative_on_orthant(jac_A.subs(H, H + 1), (R, H))
    print("PASS non-split tower has only arity 2 Jac_1 and arity 3 Jac_0; higher homotopy zero")

    print("6 PASS (exact rational and symbolic degree certificates)")


if __name__ == "__main__":
    main()
