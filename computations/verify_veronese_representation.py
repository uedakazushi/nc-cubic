#!/usr/bin/env python3
"""Check the two-block third-Veronese representation, not its full automorphism group.

The Heisenberg group law is imported from the existing exact twist checker.
We compute the character of A_3 from the four bidegree pieces and the invariant
cubic relation. All arithmetic in Z[zeta]/(zeta^2+zeta+1) is integral.
We also enumerate the block similitudes used for the ambient linear normalizer.
"""

from collections import Counter
from itertools import product

from verify_multiblock_twists import CentralProduct


# a + b*zeta, where zeta^2 = -1-zeta.
ONE = (1, 0)
ZERO = (0, 0)
ZETA = (0, 1)
ZETA2 = (-1, -1)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def scale(n, x):
    return (n * x[0], n * x[1])


def multiply(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def conjugate(x):
    return (x[0] - x[1], -x[1])


def root(exponent):
    return (ONE, ZETA, ZETA2)[exponent % 3]


def standard_character(a, b, c):
    return scale(3, root(c)) if a == b == 0 else ZERO


def cubic_character(a, b):
    # End(W) plus one trivial summand, obtained from the Koszul resolution.
    return (10, 0) if a == b == 0 else ONE


def veronese_character(element):
    a1, a2, b1, b2, c1 = element
    # The quotient by the diagonal center is normalized by c2=0.
    w1 = standard_character(a1, b1, c1)
    w2 = standard_character(a2, b2, 0)
    result = add(cubic_character(a1, b1), cubic_character(a2, b2))
    result = add(result, (-1, 0))  # the fixed central cubic relation
    result = add(result, scale(2, multiply(conjugate(w1), w2)))
    result = add(result, scale(2, multiply(w1, conjugate(w2))))
    return result


def inner_product(characters, other):
    total = ZERO
    for element, value in characters.items():
        total = add(total, multiply(value, conjugate(other(element))))
    assert total[1] == 0 and total[0] % len(characters) == 0
    return total[0] // len(characters)


def check_characters():
    group = CentralProduct(2)
    elements = list(product(range(3), repeat=group.width))
    characters = {element: veronese_character(element) for element in elements}
    distribution = Counter(characters.values())
    assert distribution == {(55, 0): 1, (10, 0): 48, (1, 0): 194}

    one_dimensional = Counter()
    multiplicities = {}
    for character in product(range(3), repeat=4):
        def value(element, character=character):
            return root(sum(x * y for x, y in zip(character, element[:4])))

        multiplicity = inner_product(characters, value)
        support = sum(
            character[i] != 0 or character[2 + i] != 0 for i in range(2)
        )
        assert multiplicity == {0: 3, 1: 1, 2: 0}[support]
        multiplicities[character] = multiplicity
        one_dimensional[multiplicity] += 1

    for sign in (1, -1):
        def nonlinear(element, sign=sign):
            return scale(9, root(sign * element[4])) if not any(element[:4]) else ZERO

        assert inner_product(characters, nonlinear) == 2

    assert sum(multiplicities.values()) + 2 * 2 * 9 == 55
    central_eigenspaces = []
    for weight in range(3):
        total = ZERO
        for c in range(3):
            element = (0, 0, 0, 0, c)
            total = add(total, multiply(characters[element], root(-weight * c)))
        assert total[1] == 0 and total[0] % 3 == 0
        central_eigenspaces.append(total[0] // 3)
    assert central_eigenspaces == [19, 18, 18]

    # Any scalar element of a finite-order representation has |trace|=dimension.
    # The exact square norm in Z[zeta] is a^2-a*b+b^2.
    scalar_candidates = [
        element for element, (a, b) in characters.items()
        if a * a - a * b + b * b == 55 * 55
    ]
    assert scalar_candidates == [group.one]
    print("K2 order=243; character distribution={55: 1, 10: 48, 1: 194}")
    print("linear irreducibles: multiplicity 3 once, 1 sixteen times, 0 sixty-four times")
    print("nonlinear irreducibles: dimension 9, multiplicity 2 for each central sign")
    print("central eigenspaces=[19, 18, 18]; projective action is faithful")


def determinant(matrix):
    a, b, c, d = matrix
    return (a * d - b * c) % 3


def apply_matrix(matrix, vector):
    a, b, c, d = matrix
    x, y = vector
    return ((a * x + b * y) % 3, (c * x + d * y) % 3)


def omega(x, y):
    return (x[0] * y[1] - x[1] * y[0]
            - x[2] * y[3] + x[3] * y[2]) % 3


def check_block_similitudes():
    gl2 = [m for m in product(range(3), repeat=4) if determinant(m) != 0]
    assert len(gl2) == 48
    basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    maps = set()
    for left, right in product(gl2, repeat=2):
        if determinant(left) != determinant(right):
            continue
        for swap in (False, True):
            def transform(vector):
                first, second = vector[:2], vector[2:]
                if swap:
                    first, second = second, first
                return apply_matrix(left, first) + apply_matrix(right, second)

            columns = tuple(transform(vector) for vector in basis)
            multiplier = determinant(left) * (-1 if swap else 1) % 3
            for i in range(4):
                for j in range(4):
                    assert omega(columns[i], columns[j]) == (
                        multiplier * omega(basis[i], basis[j])
                    ) % 3
            maps.add(columns)

    assert len(maps) == 2304
    print("block similitudes=2304; ambient normalizer/centralizer order=186624")
    print("Exact finite checks passed; no full algebra-automorphism claim is made.")


if __name__ == "__main__":
    check_characters()
    check_block_similitudes()
