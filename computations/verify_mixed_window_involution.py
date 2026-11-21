#!/usr/bin/env python3
"""Exact stable-Hom characters for the involution on the mixed cubic window.

2026-11-22 / v51. Python 3 standard library only.

Mathematical input: the equivariant minimal Shamash resolution, with invariant
cubic period. This script checks its finite character consequences and compares
the ordinary Euler matrix with a separate line-bundle projection calculation.
It does not compute Hochschild homology or the higher A-infinity operations.
"""

from collections import Counter
from math import comb, factorial, prod


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def polynomial_binomial(n, k):
    """The binomial polynomial at any integral n, including negative n."""
    numerator = prod(n - j for j in range(k))
    denominator = factorial(k)
    assert numerator % denominator == 0
    return numerator // denominator


def sign(degree):
    return 1 if degree % 2 == 0 else -1


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(left, right):
    assert len(left[0]) == len(right)
    return [[sum(x * y for x, y in zip(row, column))
             for column in zip(*right)] for row in left]


def congruence(matrix, basis):
    return multiply(multiply(transpose(basis), matrix), basis)


def euler_projection(line_matrix, exceptional_count, j):
    """Right-orthogonal projection of O(j) past a unit triangular collection."""
    coefficients = [0] * exceptional_count
    for i in range(exceptional_count - 1, -1, -1):
        assert line_matrix[i][i] == 1
        assert all(line_matrix[i][k] == 0 for k in range(i))
        coefficients[i] = line_matrix[i][j] - sum(
            line_matrix[i][k] * coefficients[k]
            for k in range(i + 1, exceptional_count)
        )
    result = [-c for c in coefficients] + [0] * (
        len(line_matrix) - exceptional_count
    )
    result[j] = 1
    assert all(sum(row[k] * result[k] for k in range(len(result))) == 0
               for row in line_matrix[:exceptional_count])
    return result


dimensions = [choose(7, i) for i in range(8)]
characters = [choose(6, i) - choose(6, i - 1) for i in range(8)]
assert dimensions == [1, 7, 21, 35, 35, 21, 7, 1]
assert characters == [1, 5, 9, 5, -5, -9, -5, -1]
assert all(dim >= abs(trace) and (dim + trace) % 2 == 0
           for dim, trace in zip(dimensions, characters))
print("PASS Koszul dimensions and involution characters:", characters)

# Each row is (cohomological degree r, Koszul degree i, period exponent p,
#              dimension, trace, invariant dimension, anti-invariant dimension).
blocks = {}
for difference in range(-2, 3):
    rows = []
    for i in range(8):
        if (-difference - i) % 3:
            continue
        p = (-difference - i) // 3
        r = i + 2 * p
        dim, trace = dimensions[i], characters[i]
        assert i + 3 * p == -difference
        rows.append((r, i, p, dim, trace, (dim + trace) // 2,
                     (dim - trace) // 2))
    blocks[difference] = rows

expected_blocks = {
    -2: [(2, 2, 0, 21, 9, 15, 6), (3, 5, -1, 21, -9, 6, 15)],
    -1: [(1, 1, 0, 7, 5, 6, 1), (2, 4, -1, 35, -5, 15, 20),
         (3, 7, -2, 1, -1, 0, 1)],
    0: [(0, 0, 0, 1, 1, 1, 0), (1, 3, -1, 35, 5, 20, 15),
        (2, 6, -2, 7, -5, 1, 6)],
    1: [(0, 2, -1, 21, 9, 15, 6), (1, 5, -2, 21, -9, 6, 15)],
    2: [(-1, 1, -1, 7, 5, 6, 1), (0, 4, -2, 35, -5, 15, 20),
        (1, 7, -3, 1, -1, 0, 1)],
}
assert blocks == expected_blocks
print("PASS all 13 nonzero stable-Hom rows")
for difference, rows in blocks.items():
    print("  b-a =", difference, ":", rows)

total, invariant, anti_invariant = Counter(), Counter(), Counter()
for a in range(3):
    for b in range(3):
        for r, i, p, dim, trace, plus, minus in blocks[b - a]:
            total[r] += dim
            invariant[r] += plus
            anti_invariant[r] += minus
aggregate = [(r, total[r], invariant[r], anti_invariant[r])
             for r in sorted(total)]
assert aggregate == [(-1, 7, 6, 1), (0, 80, 48, 32),
                     (1, 162, 84, 78), (2, 112, 48, 64), (3, 23, 6, 17)]
assert sum(total.values()) == 384
print("PASS 384-dimensional generator cohomology (degree, dimension, +, -):",
      aggregate)

ordinary = [[sum(sign(row[0]) * row[3] for row in blocks[b - a])
             for b in range(3)] for a in range(3)]
equivariant = [[sum(sign(row[0]) * row[4] for row in blocks[b - a])
                for b in range(3)] for a in range(3)]
assert ordinary == [[-27, 0, 27], [27, -27, 0], [0, 27, -27]]
assert equivariant == [[-9, 18, -9], [-9, -9, 18], [18, -9, -9]]
invariant_euler = [[(ordinary[a][b] + equivariant[a][b]) // 2
                    for b in range(3)] for a in range(3)]
anti_invariant_euler = [[(ordinary[a][b] - equivariant[a][b]) // 2
                         for b in range(3)] for a in range(3)]
assert invariant_euler == [[-18, 9, 9], [9, -18, 9], [9, 9, -18]]
assert anti_invariant_euler == [[-9, -9, 18], [18, -9, -9], [-9, 18, -9]]
print("PASS ordinary Hom Euler matrix:", ordinary)
print("PASS involution Hom Euler matrix:", equivariant)
print("PASS invariant and anti-invariant Hom Euler matrices:",
      invariant_euler, anti_invariant_euler)

# Independent calculation from the cubic Hilbert polynomial and four line
# exceptions. No stable-Hom table enters this projection calculation.
def line_euler(difference):
    return (polynomial_binomial(difference + 6, 6)
            - polynomial_binomial(difference + 3, 6))


line_matrix = [[line_euler(j - i) for j in range(7)] for i in range(7)]
projection = transpose([euler_projection(line_matrix, 4, j)
                        for j in (4, 5, 6)])
line_gram = congruence(line_matrix, projection)
assert [row[:2] for row in line_gram[:2]] == [
    [-27, -189], [-162, -1161]
]

# The section-window filtration gives
# e4=-K1, e5=-7*K1-K2, e6=-K0-28*K1-7*K2.
window_basis = [[0, 0, -1], [-1, -7, -28], [0, -1, -7]]
assert line_gram == congruence(ordinary, window_basis)
normalized_basis = [[1, -7], [0, 1]]
normalized_gram = congruence([row[:2] for row in line_gram[:2]],
                            normalized_basis)
assert normalized_gram == [[-27, 0], [27, -27]]
assert (line_gram[0][0] * line_gram[1][1]
        - line_gram[0][1] * line_gram[1][0]) == 729
print("PASS independent line-bundle projection and full 3-object Euler match")
print("PASS existing 2-object Gram matrix, normalization, and determinant 729")
print("LIMIT: stable Hom characters only; no Hochschild character or "
      "categorical equivalence computed.")
