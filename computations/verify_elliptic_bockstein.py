#!/usr/bin/env python3
"""Exact low-arity certificates for smooth Sklyanin boundary Bocksteins.

Current result: 2026-11-22 / v58.

Run from the repository root with Python 3 and SymPy:
    python3 computations/verify_elliptic_bockstein.py

The parameters a,b,c below belong to S(a,b,c), not to the coefficients
of the sum of central cubics.  Smoothness of its standard point cubic
implies abc != 0.  The degree-two dual basis is q_i = r_i^*, so xi_i^2
= c q_i.  All left and right zero-arity primitives are independent.

The script proves polynomial identities and exact determinant formulas;
it does not sample a generic parameter or finitely many tensor powers.
The passage from the actual self-intersection class to full Hochschild
cochains, its derived Tate localization, and the comparison with Jac(G)
are proved in papers/sections/mixed/elliptic_bockstein.tex, not by this
finite calculation.  No formal proof-assistant verification is claimed.
"""

from itertools import permutations, product

import sympy as sp


def flat(matrix):
    """Row-major vectorization, fixing all determinant conventions."""
    return sp.Matrix(list(matrix))


def sign_of_permutation(values):
    inversions = sum(values[i] > values[j]
                     for i in range(len(values))
                     for j in range(i + 1, len(values)))
    return (-1) ** inversions


def main():
    a, b, c = sp.symbols("a b c", nonzero=True)
    words = list(product(range(3), repeat=2))
    relations = sp.zeros(3, 9)
    for i, (j, k) in enumerate(((1, 2), (2, 0), (0, 1))):
        relations[i, words.index((j, k))] = a
        relations[i, words.index((k, j))] = b
        relations[i, words.index((i, i))] = c

    # Pairing xi_j xi_l with a primal quadratic relation gives its word
    # coefficient.  The square minor is c^3, valid on every smooth fiber.
    def dual_product(j, l):
        return relations[:, words.index((j, l))]

    squares = sp.Matrix.hstack(*(dual_product(i, i) for i in range(3)))
    assert squares == c * sp.eye(3)
    assert squares.det() == c ** 3
    for i, (j, k) in enumerate(((1, 2), (2, 0), (0, 1))):
        assert dual_product(j, k) == a * sp.eye(3)[:, i]
        assert dual_product(k, j) == b * sp.eye(3)[:, i]
    print("PASS general quadratic-dual pairing and constant-class minor c^3")

    # The cyclic overlap sends M to sum M_ij (x_j x_i - x_i x_j).
    # Its diagonal coordinates vanish, whereas the relation square minor
    # is invertible.  Thus this overlap lies in R only when it vanishes.
    entries = sp.symbols("m00:03 m10:13 m20:23")
    matrix = sp.Matrix(3, 3, entries)
    overlap = sp.zeros(9, 1)
    for i, j in product(range(3), repeat=2):
        overlap[words.index((j, i))] += matrix[i, j]
        overlap[words.index((i, j))] -= matrix[i, j]
    assert all(overlap[words.index((i, i))] == 0 for i in range(3))
    for i in range(3):
        for j in range(i + 1, 3):
            assert overlap[words.index((i, j))] == matrix[j, i] - matrix[i, j]
    print("PASS cyclic PBW overlap is zero exactly for symmetric M")

    def translation(s):
        sx, sy, sz = s
        return sp.Matrix(((2*c*sx, (a+b)*sz, (a+b)*sy),
                          ((a+b)*sz, 2*c*sy, (a+b)*sx),
                          ((a+b)*sy, (a+b)*sx, 2*c*sz)))

    left = sp.symbols("Lx Ly Lz")
    right = sp.symbols("Rx Ry Rz")
    gauge = sp.zeros(3, 3)
    for j in range(3):
        gauge[:, j] = sum((left[i] * dual_product(i, j)
                           + right[i] * dual_product(j, i)
                           for i in range(3)), sp.zeros(3, 1))
    symmetric_part = (gauge + gauge.T) / 2
    mean = tuple((left[i] + right[i]) / 2 for i in range(3))
    assert sp.simplify(symmetric_part - translation(mean)) == sp.zeros(3)
    assert sp.simplify(gauge.subs(dict(zip(right, left)))
                       - translation(left)) == sp.zeros(3)
    s = sp.symbols("sx sy sz")
    translation_matrix = flat(translation(s)).jacobian(s)
    assert translation_matrix.extract((0, 4, 8), (0, 1, 2)).det() == 8*c**3
    print("PASS symmetric independent-object gauge image equals translations")

    p, q, r = sp.symbols("p q r")
    pbw = sp.Matrix(((0, p, r), (p, 0, q), (r, q, 0)))
    gauge_matrix = flat(gauge).jacobian(left + right)
    pbw_matrix = flat(pbw).jacobian((p, q, r))
    determinant = sp.factor(gauge_matrix.row_join(pbw_matrix).det())
    assert determinant == -8*c**3*(a-b)**3
    clifford_gauge = gauge_matrix.subs(b, a)
    assert clifford_gauge.rank() == 3
    assert clifford_gauge[:, :3] == translation_matrix.subs(b, a) / 2
    assert clifford_gauge[:, 3:] == clifford_gauge[:, :3]
    print("PASS non-two-torsion determinant -8*c^3*(a-b)^3 and Clifford rank 3")

    # F_j t^m has degree (j+2m,-j-3m).  m is any integer: this
    # solves over all Tate inverse powers, not only the ordinary Ext part.
    j, m = sp.symbols("j m", integer=True)

    def solve_degree(cohomological, internal):
        return sp.solve((j + 2*m - cohomological,
                         -j - 3*m - internal), (j, m))

    assert solve_degree(1, -1) == {j: 1, m: 0}  # h_0
    assert solve_degree(1, -2) == {j: -1, m: 1}  # h_1(F_1): impossible
    assert solve_degree(2, -3) == {j: 0, m: 1}  # h_1(F_2)
    assert solve_degree(2, -2) == {j: 2, m: 0}  # constant Bockstein value
    print("PASS all Tate primitive bidegrees and the constant F_2 component")

    # A Clifford volume tensor is a nonzero scalar multiple of epsilon.
    # Inserting three independent h_0 values at the three different
    # objects gives a sum of alternating matrices, for ANY insertion signs.
    epsilon = {word: sign_of_permutation(word)
               for word in permutations(range(3))}
    primitives = sp.symbols("h00:03 h10:13 h20:23")
    insertion_matrices = []
    for slot in range(3):
        contraction = sp.zeros(3)
        for v, w in product(range(3), repeat=2):
            for index in range(3):
                word = [v, w]
                word.insert(slot, index)
                contraction[v, w] += (primitives[3*slot + index]
                                       * epsilon.get(tuple(word), 0))
        assert contraction + contraction.T == sp.zeros(3)
        insertion_matrices.append(contraction)
    print("PASS each object-dependent insertion in the cubic volume is alternating")

    tau = sp.symbols("tau", nonzero=True)
    lambdas = sp.symbols("lambda_x lambda_y lambda_z")
    beta = sp.symbols("beta_x beta_y beta_z")
    skew_parameters = sp.symbols("z01 z12 z20")
    relation_matrix = sp.Matrix(((tau*lambdas[0], lambdas[2], lambdas[1]),
                                 (lambdas[2], tau*lambdas[1], lambdas[0]),
                                 (lambdas[1], lambdas[0], tau*lambdas[2])))
    z01, z12, z20 = skew_parameters
    skew = sp.Matrix(((0, z01, -z20), (-z01, 0, z12), (z20, -z12, 0)))
    center_matrix = sp.diag(*beta)
    combined = flat(relation_matrix + skew + center_matrix).jacobian(
        lambdas + skew_parameters + beta)
    center_determinant = sp.factor(combined.det())
    assert center_determinant == 8
    print("PASS Clifford relation-plus-alternating gauge meets diagonal beta only at zero (det 8)")

    # Low bar pairing: only length-two terms of a relation contribute to
    # a Yoneda product of two degree-one classes.  w_0 is length three;
    # the perturbation u*sum beta_j*x_j^2 has precisely this length-two part.
    u, weight = sp.symbols("u weight", nonzero=True)
    quadratic_center = {word: u * weight * beta[word[0]]
                        if word[0] == word[1] else 0 for word in words}
    coefficient_matrix = sp.Matrix(3, 3,
                                  lambda v, w: quadratic_center[(v, w)])
    assert coefficient_matrix.diff(u) == weight * center_matrix
    # For s_n, removing the one u factor still leaves active degree n>=1.
    n = sp.symbols("n", integer=True, positive=True)
    total_degree = sp.expand(3*n - (2*n - 1))
    assert total_degree == n + 1
    assert sp.expand(total_degree - 1) == n
    print("PASS center perturbation's quadratic pairing and Shamash augmentation degrees")

    print("8 PASS (exact symbolic certificates; categorical bridges are proved in the manuscript)")


if __name__ == "__main__":
    main()
