#!/usr/bin/env python3
"""Exact finite certificates for elliptic center lifting (2026-11-22).

The mathematical statements and all-parameter proofs are in
papers/sections/mixed/elliptic_center_obstruction.tex.  This program checks
seven finite certificates over QQ and QQ(tau); it does not formally verify
the cited PBW/CY theorems, elliptic geometry, or any categorical comparison.

Run: python3 computations/verify_elliptic_center_obstruction.py
Dependency: SymPy.
"""

from functools import lru_cache
from itertools import product

import sympy as sp
from sympy.polys.matrices import DomainMatrix


TAU = sp.Symbol("tau")
LETTERS = range(3)
W3 = list(product(LETTERS, repeat=3))
W4 = list(product(LETTERS, repeat=4))
B3 = [
    (0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 1), (1, 1, 1),
    (1, 1, 2), (0, 2, 2), (1, 2, 2), (2, 2, 2), (0, 1, 2),
]


def add(left, right, scale=1):
    result = dict(left)
    for word, coefficient in right.items():
        result[word] = result.get(word, 0) + scale * coefficient
    return {word: value for word, value in result.items() if value != 0}


def sandwich(polynomial, prefix=(), suffix=()):
    return {prefix + word + suffix: value for word, value in polynomial.items()}


def commutator(polynomial, generator):
    """Return [generator, polynomial] as a free-word dictionary."""
    return add(sandwich(polynomial, (generator,)),
               sandwich(polynomial, suffix=(generator,)), -1)


def vector(polynomial, words):
    return sp.Matrix([polynomial.get(word, 0) for word in words])


def assert_zero(matrix):
    assert all(sp.cancel(entry) == 0 for entry in matrix)


def relations(tau):
    return [
        {(1, 2): 1, (2, 1): 1, (0, 0): tau},
        {(2, 0): 1, (0, 2): 1, (1, 1): tau},
        {(0, 1): 1, (1, 0): 1, (2, 2): tau},
    ]


def omega(tau):
    signs = {
        (0, 1, 2): -1, (1, 2, 0): -1, (2, 0, 1): -1,
        (1, 0, 2): 1, (0, 2, 1): 1, (2, 1, 0): 1,
    }
    return {word: sp.Rational(sign, 3) * (tau**3 - 1)
            for word, sign in signs.items()}


def homogeneous_relation_matrix(rels, degree):
    words = list(product(LETTERS, repeat=degree))
    columns, labels = [], []
    for j, relation in enumerate(rels):
        for left_length in range(degree - 1):
            for prefix in product(LETTERS, repeat=left_length):
                for suffix in product(LETTERS, repeat=degree - 2 - left_length):
                    columns.append(vector(sandwich(relation, prefix, suffix), words))
                    labels.append((j, prefix, suffix))
    return sp.Matrix.hstack(*columns), labels


def check_geometry():
    x, y, z = sp.symbols("x y z")
    d = 2 + TAU**3
    equation = TAU * (x**3 + y**3 + z**3) - d * x*y*z
    matrix = sp.Matrix([[TAU*x, z, y], [z, TAU*y, x], [y, x, TAU*z]])
    assert sp.expand(matrix.det() + equation) == 0
    discriminant = sp.expand(d**3 - 27*TAU**3)
    assert sp.factor(discriminant) == (TAU - 1)**2 * (TAU + 2) * (
        TAU**2 - 2*TAU + 4) * (TAU**2 + TAU + 1)**2
    assert sp.expand(discriminant - (TAU**3 - 1)**2*(TAU**3 + 8)) == 0
    hessian = sp.hessian(equation, (x, y, z)).det()
    assert sp.expand(hessian + 6*d**2*equation + 8*discriminant*x*y*z) == 0
    assert sp.expand(equation.subs({x: 1, y: 1, z: TAU})) == 0
    assert_zero(matrix.subs({x: 1, y: -1, z: 0}) * sp.Matrix([1, 1, TAU]))
    print("PASS 1: smooth Hesse condition, graph matrix, and elliptic input identities")


def check_pbw_translation():
    rels = relations(TAU)
    overlap = {}
    for j, relation in enumerate(rels):
        overlap = add(overlap, commutator(relation, j))
    assert_zero(sp.Matrix(list(overlap.values())))
    a, b, c, d, e, f = sp.symbols("m11 m22 m33 m12 m13 m23")
    matrix = sp.Matrix([[a, d, e], [d, b, f], [e, f, c]])
    linear_overlap = {}
    for j in LETTERS:
        linear_overlap = add(linear_overlap,
                             commutator({(i,): matrix[j, i] for i in LETTERS}, j))
    assert_zero(sp.Matrix(list(linear_overlap.values())))
    sx, sy, sz = -f/2, -e/2, -d/2
    translated = matrix + sp.Matrix([
        [2*TAU*sx, 2*sz, 2*sy],
        [2*sz, 2*TAU*sy, 2*sx],
        [2*sy, 2*sx, 2*TAU*sz],
    ])
    assert translated == sp.diag(a - TAU*f, b - TAU*e, c - TAU*d)
    print("PASS 2: cyclic PBW overlap and the three translation-normal parameters")


def build_homogeneous_model():
    rels = relations(TAU)
    m2, _ = homogeneous_relation_matrix(rels, 2)
    m3, _ = homogeneous_relation_matrix(rels, 3)
    m4, labels4 = homogeneous_relation_matrix(rels, 4)
    assert m2.subs(TAU, 2).rank() == 3
    pivots3 = m3.subs(TAU, 2).rref()[1]
    pivots4 = m4.subs(TAU, 2).rref()[1]
    assert len(pivots3) == 17 and len(pivots4) == 66
    basis3 = sp.Matrix.hstack(*(vector({word: 1}, W3) for word in B3))
    change = m3[:, list(pivots3)].row_join(basis3)
    inverse = DomainMatrix.from_Matrix(change).to_field().inv().to_Matrix()
    projection = inverse[-10:, :]
    assert_zero(projection*m3)
    assert projection*basis3 == sp.eye(10)
    # The selected quotient coordinates extend to every tau^3 != 1.
    for entry in inverse:
        denominator = sp.denom(sp.cancel(entry))
        assert sp.rem((TAU**3 - 1)**5, denominator, TAU) == 0
    for g in LETTERS:
        for j in LETTERS:
            assert_zero(projection * vector(commutator({(j, j): 1}, g), W3))
    print("PASS 3: homogeneous degree-three basis and central-square identities")
    return m4[:, list(pivots4)], [labels4[i] for i in pivots4], projection


def check_first_order(model):
    homogeneous, labels, projection = model
    corrections = []
    for parameter in LETTERS:
        corrections.append(sp.Matrix.hstack(*(
            vector({prefix + (j,) + suffix: 1} if j == parameter else {}, W3)
            for j, prefix, suffix in labels)))
    deltas = []
    for g in LETTERS:
        target = vector(commutator(omega(TAU), g), W4)
        echelon, pivots = DomainMatrix.from_Matrix(
            homogeneous.row_join(target)).to_field().rref()
        assert len(pivots) == 66
        coefficients = echelon.to_Matrix()[:66, -1]
        assert_zero(homogeneous*coefficients - target)
        deltas.append(sp.Matrix.hstack(*(
            (-projection*correction*coefficients).applyfunc(sp.cancel)
            for correction in corrections)))
    expected_px = [
        sp.Matrix([0, 0, 0, 0, TAU**3, 0, 0, 0, -TAU**3, 0]),
        sp.Matrix([0, -2, 0, 0, 0, -TAU**2, -3*TAU, 0, 0, 0]),
        sp.Matrix([0, 0, 2, 3*TAU, 0, 0, 0, TAU**2, 0, 0]),
    ]
    for actual, expected in zip(deltas, expected_px):
        assert actual[:, 0] == expected
    diagnostics = sp.Matrix.vstack(deltas[0][5, :], deltas[1][6, :], deltas[2][1, :])
    assert diagnostics == -3*TAU*sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    all_quadratics = list(product(LETTERS, repeat=2))
    for g, row in [(0, 5), (1, 6), (2, 1)]:
        adjoint = projection * sp.Matrix.hstack(*(
            vector(commutator({word: 1}, g), W3) for word in all_quadratics))
        assert_zero(adjoint[row, :])
    assert sp.factor(diagnostics.det()) == -27*TAU**3
    print("PASS 4: universal first-order obstruction and all quadratic-correction annihilators")


def check_clifford_volume():
    q0, q1, q2, b01, b02, b12 = sp.symbols("q0 q1 q2 b01 b02 b12")
    diagonal = [q0, q1, q2]
    off_diagonal = {(0, 1): b01, (0, 2): b02, (1, 2): b12}

    @lru_cache(None)
    def reduce_word(word):
        for position in range(len(word) - 1):
            left, right = word[position:position + 2]
            if left < right:
                continue
            prefix, suffix = word[:position], word[position + 2:]
            if left == right:
                return {key: diagonal[left]*value
                        for key, value in reduce_word(prefix + suffix).items()}
            swapped = reduce_word(prefix + (right, left) + suffix)
            removed = reduce_word(prefix + suffix)
            return add({key: -value for key, value in swapped.items()},
                       removed, 2*off_diagonal[(right, left)])
        return {word: sp.Integer(1)}

    for g in LETTERS:
        normal = {}
        for word, coefficient in commutator(omega(TAU), g).items():
            normal = add(normal, reduce_word(word), coefficient)
        assert_zero(sp.Matrix(list(normal.values())))
    print("PASS 5: odd Clifford volume is central for arbitrary central quadratic coefficients")

    # This same ordering model certifies the universal center presentation.
    # Generic center equality and its behavior at every alpha are proved in the text.
    volume = {(0, 1, 2): 1, (2,): -b01, (1,): b02, (0,): -b12}
    normal_omega, square = {}, {}
    for word, coefficient in omega(TAU).items():
        normal_omega = add(normal_omega, reduce_word(word), coefficient)
    assert_zero(sp.Matrix(list(add(normal_omega, volume, 2*(TAU**3 - 1)).values())))
    for left, lc in volume.items():
        for right, rc in volume.items():
            square = add(square, reduce_word(left + right), lc*rc)
    q = sp.Matrix([[q0, b01, b02], [b01, q1, b12], [b02, b12, q2]])
    assert_zero(sp.Matrix(list(add(square, {(): q.det()}).values())))
    u, ax, ay, az = sp.symbols("u alpha_x alpha_y alpha_z")
    specialized = q.subs({b01: (u**2*az - TAU*q2)/2,
                          b02: (u**2*ay - TAU*q1)/2,
                          b12: (u**2*ax - TAU*q0)/2})
    leading = -TAU**2*(q0**3 + q1**3 + q2**3)/4 + (1 - TAU**3/4)*q0*q1*q2
    assert sp.expand(specialized.det().subs(u, 0) - leading) == 0
    assert sp.Poly(leading, q0, q1, q2).coeff_monomial(q0**3) == -TAU**2/4
    print("PASS 6: universal Clifford volume-square, center normalization, and nonzero determinant")


def check_rational_counterexample():
    words = [word for degree in range(5) for word in product(LETTERS, repeat=degree)]
    rels = relations(sp.Integer(2))
    rels[0][(0,)] = 1
    ideal_columns = []
    for relation in rels:
        for total in range(3):
            for left_length in range(total + 1):
                for prefix in product(LETTERS, repeat=left_length):
                    for suffix in product(LETTERS, repeat=total - left_length):
                        ideal_columns.append(vector(sandwich(relation, prefix, suffix), words))
    ideal = sp.Matrix.hstack(*ideal_columns)
    assert ideal.shape == (121, 102) and ideal.rank() == 86
    projection = sp.Matrix.hstack(*ideal.T.nullspace()).T
    assert projection.rows == 35
    lower_words = [word for degree in (2, 1) for word in product(LETTERS, repeat=degree)]
    coefficients = sp.Matrix.vstack(*(
        projection*sp.Matrix.hstack(*(
            vector(commutator({word: 1}, g), words) for word in lower_words))
        for g in LETTERS))
    rhs = sp.Matrix.vstack(*(
        -projection*vector(commutator(omega(sp.Integer(2)), g), words)
        for g in LETTERS))
    assert coefficients.rank() == 8
    assert coefficients.row_join(rhs).rank() == 9
    for g in LETTERS:
        assert_zero(projection*vector(commutator({(0, 0): 7, (0,): 4}, g), words))
    print("PASS 7: rational PBW example, no lift with any lower corrections, and quadratic center")


def main():
    check_geometry()
    check_pbw_translation()
    model = build_homogeneous_model()
    check_first_order(model)
    check_clifford_volume()
    check_rational_counterexample()
    print("All 7 exact certificates passed.")


if __name__ == "__main__":
    main()
