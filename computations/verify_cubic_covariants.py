"""Exact finite certificates for low-degree ternary cubic covariants.

2026-11-20 / v9. Standard library only. Graph constants are evaluated separately
in verify_mixed_fifth.py; this file supplies the common contraction and weight counts.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial

PERMS = list(permutations(range(3)))
SIGN = {
    p: (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    for p in PERMS
}


def weight_counts(m, d=3):
    weights = [(a, b, d-a-b) for a in range(d+1) for b in range(d+1-a)]
    counts = Counter()

    def visit(i, left, weight):
        v = weights[i]
        if i == len(weights) - 1:
            counts[tuple(weight[j] + left * v[j] for j in range(3))] += 1
            return
        for k in range(left + 1):
            visit(i + 1, left - k, tuple(weight[j] + k * v[j] for j in range(3)))

    visit(0, m, (0, 0, 0))
    return counts


def highest_weight_multiplicity(m, highest):
    counts = weight_counts(m)
    delta = (2, 1, 0)
    terms = [
        counts[tuple(highest[j] + delta[j] - delta[p[j]] for j in range(3))]
        for p in PERMS
    ]
    return sum(SIGN[p] * n for p, n in zip(PERMS, terms)), terms


def tensor_denominator(alpha):
    return factorial(3) // (factorial(alpha[0]) * factorial(alpha[1]) * factorial(alpha[2]))


def tensor_alpha(indices):
    return tuple(indices.count(j) for j in range(3))


def tetrahedron_invariant():
    """Return 54*t_abc*t_def*t_ghi*t_jkl*eps_adg*eps_bej*eps_chk*eps_fil.

    t_ijk = (partial_i partial_j partial_k g)/6.
    Polynomial keys are sorted multisets of the four cubic coefficients.
    """
    coefficients = Counter()
    for p1, p2, p3, p4 in product(PERMS, repeat=4):
        a, d, g = p1
        b, e, j = p2
        c, h, k = p3
        f, i, ell = p4
        factors = tuple(sorted(map(tensor_alpha, [(a, b, c), (d, e, f), (g, h, i), (j, k, ell)])))
        denominator = 1
        for alpha in factors:
            denominator *= tensor_denominator(alpha)
        coefficients[factors] += Fraction(54 * SIGN[p1] * SIGN[p2] * SIGN[p3] * SIGN[p4], denominator)
    return {monomial: coefficient for monomial, coefficient in coefficients.items() if coefficient}


def check_cubic():
    expected = [1, 0, 1, 0, 1, 0, 2, 0]
    for m, want in enumerate(expected, start=1):
        value, terms = highest_weight_multiplicity(m, (m + 2, m - 1, m - 1))
        assert value == want
        print(f"cubic covariants degree {m}: multiplicity {value}; alternating counts {terms}")
    for m, want in [(2, 0), (4, 1), (6, 1)]:
        value, terms = highest_weight_multiplicity(m, (m, m, m))
        assert value == want
        print(f"invariants degree {m}: multiplicity {value}; alternating counts {terms}")
    invariant = tetrahedron_invariant()
    assert len(invariant) == 25
    assert invariant[((1, 1, 1),) * 4] == 1
    assert all(coefficient.denominator == 1 for coefficient in invariant.values())
    hesse = Counter()
    allowed = {(3, 0, 0), (0, 3, 0), (0, 0, 3), (1, 1, 1)}
    for factors, coefficient in invariant.items():
        if all(alpha in allowed for alpha in factors):
            power = factors.count((1, 1, 1))
            hesse[power] += coefficient * Fraction(1, 3) ** (4 - power)
    assert dict(hesse) == {1: Fraction(-8), 4: Fraction(1)}
    print("Normalized S: 25 integer terms; S(xyz)=1; S(g_lambda)=lambda^4-8*lambda.")



def multiply(left, right):
    out = Counter()
    for a, ca in left.items():
        for b, cb in right.items():
            out[tuple(a[i] + b[i] for i in range(3))] += ca * cb
    return out


def sign(p):
    return SIGN[p]


def weyl_terms(character, highest):
    rho = (2, 1, 0)
    return [sign(p) * character[tuple(highest[i] + rho[i] - rho[p[i]]
                                     for i in range(3))]
            for p in permutations(range(3))]


def contraction(tensors, edges):
    answer = 0
    for ps in product(tuple(permutations(range(3))), repeat=4):
        labels = [[] for _ in tensors]
        coefficient = 1
        for edge, p in zip(edges, ps):
            coefficient *= sign(p)
            for vertex, index in zip(edge, p):
                labels[vertex].append(index)
        for tensor, indices in zip(tensors, labels):
            coefficient *= tensor.get(tuple(indices), 0)
        answer += coefficient
    return Fraction(1, 24) * answer


SE = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))
IE = ((0, 1, 2), (0, 1, 2), (0, 3, 4), (1, 3, 4))
JE = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 4))


def determinant(matrix):
    return sum(sign(p) * matrix[0][p[0]] * matrix[1][p[1]]
               * matrix[2][p[2]] for p in permutations(range(3)))


def check_mixed():
    a = multiply(weight_counts(1, 1), weight_counts(4, 3))
    b = multiply(weight_counts(2, 2), weight_counts(3, 3))
    c = weight_counts(5, 3)
    rows = [weyl_terms(a, (5, 4, 4)), weyl_terms(b, (5, 4, 4)),
            weyl_terms(c, (7, 4, 4))]
    expected = [[67, -58, -55, 41, 42, -36],
                [158, -136, -126, 94, 92, -80],
                [41, -35, -30, 23, 21, -19]]
    assert rows == expected
    assert list(map(sum, rows)) == [1, 2, 1]
    print('PASS: exact Weyl multiplicities 1, 2, 1; terms =', rows)

    # T is the third derivative of (x^3+y^3+z^3)/3 + xyz.
    T = {(i, i, i): 2 for i in range(3)}
    T.update({p: 1 for p in permutations(range(3))})
    S = contraction([T] * 4, SE)
    assert S == -7
    q = {(0,): 1}
    M = {(0, 0): 1, (0, 1): 1, (1, 0): 1}
    dI, dJ = [], []
    for k in range(3):
        Tk = {(i, j): T.get((i, j, k), 0) for i in range(3)
              for j in range(3)}
        Mk = {(i,): M.get((i, k), 0) for i in range(3)}
        dI.append(sum(contraction([T, T] +
                                 [Tk if j == slot else M for j in range(3)], IE)
                      for slot in range(3)))
        dJ.append(contraction([T, T, T, Tk, q], JE)
                   + contraction([T, T, T, M, Mk], JE))
    matrix = [[S * q.get((i,), 0), dI[i], dJ[i]] for i in range(3)]
    assert matrix == [[-7, Fraction(-2, 3), Fraction(-10, 3)],
                      [0, Fraction(-2, 3), -1], [0, Fraction(5, 3), 0]]
    assert determinant(matrix) == Fraction(-35, 3)
    print('PASS: three gradient covariants independent; determinant = -35/3')

    # At x=(1,0,0) for that homogeneous cubic, f=1/3, q=(1,0,0), M=T[:,:,0].
    M0 = {(i, j): T.get((i, j, 0), 0) for i in range(3) for j in range(3)}
    I0 = contraction([T, T, M0, M0, M0], IE)
    J0 = contraction([T, T, T, M0, q], JE)
    assert I0 == J0 == S / 3
    print('PASS: active-restriction constants I|g=J|g=S(g)g')
    first = multiply(multiply(weight_counts(1, 1), weight_counts(1, 2)),
                     weight_counts(3, 3))
    second = multiply(weight_counts(3, 2), weight_counts(2, 3))
    scalar_rows = [weyl_terms(first, (4, 4, 4)),
                   weyl_terms(second, (4, 4, 4))]
    assert scalar_rows == [[156, -136, -136, 100, 109, -92],
                           [122, -105, -105, 78, 84, -73]]
    assert list(map(sum, scalar_rows)) == [1, 1]
    print('PASS: fourth-potential scalar jet multiplicities 1, 1; terms =', scalar_rows)
    print('Graph coefficients and fourth potential: see verify_mixed_fifth.py and verify_fourth_potential.py.')



if __name__ == "__main__":
    check_cubic()
    check_mixed()
