#!/usr/bin/env python3
"""Smith bounds for alternating commutation factors of five-variable central cubics."""
from collections import Counter
from itertools import permutations, product

from sympy import ZZ, eye
from sympy.matrices.normalforms import smith_normal_form


def relabel(successor, permutation):
    result = [0] * len(successor)
    for vertex, target in enumerate(successor):
        result[permutation[vertex]] = permutation[target]
    return tuple(result)


def exterior_square_exponent(successor):
    matrix = 2 * eye(len(successor))
    for vertex, target in enumerate(successor):
        matrix[vertex, target] += 1
    diagonal = smith_normal_form(matrix, domain=ZZ).diagonal()
    orders = [abs(int(value)) for value in diagonal]
    assert all(orders) and all(b % a == 0 for a, b in zip(orders, orders[1:]))
    return orders[-2]


def main():
    vertices = range(5)
    permutations_of_vertices = list(permutations(vertices))
    covered = set()
    orbit_counts = Counter()
    labelled_counts = Counter()
    for successor in product(vertices, repeat=5):
        if successor in covered:
            continue
        orbit = {relabel(successor, p) for p in permutations_of_vertices}
        assert covered.isdisjoint(orbit)
        covered.update(orbit)
        exponent = exterior_square_exponent(successor)
        if exponent == 4:
            assert successor == (0, 0, 0, 1, 2)
        orbit_counts[exponent] += 1
        labelled_counts[exponent] += len(orbit)
    assert len(covered) == 5**5 and sum(orbit_counts.values()) == 47
    assert set(orbit_counts) == {1, 2, 3, 4, 6}
    for exponent in sorted(orbit_counts):
        print(f"exponent {exponent}: {orbit_counts[exponent]} orbits, "
              f"{labelled_counts[exponent]} labelled maps")


if __name__ == "__main__":
    main()
