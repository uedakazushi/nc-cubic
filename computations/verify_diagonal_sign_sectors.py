#!/usr/bin/env python3
"""Enumerate HH_1 sectors using the two independent prime-power components."""
from itertools import combinations, product


def determinant(left, right):
    return left[0] * right[1] - left[1] * right[0]


def sectors(signs, thirds):
    weights = {2: signs, 3: thirds}
    coordinates = range(5)
    # The identity sector consists of invariant linear residues det(V) times V.
    direct = [i for i in coordinates if all(
        (sum(w[k] for w in block) + block[i][k]) % prime == 0
        for prime, block in weights.items() for k in range(2))]
    planes = []
    for triple in combinations(coordinates, 3):
        levels = {}
        for prime, block in weights.items():
            total = tuple(sum(block[i][k] for i in triple) for k in range(2))
            levels[prime] = [determinant(w, total) % prime for w in block]
        first = triple[0]
        if levels[2][first] != 0:
            continue  # The cubic vanishes on an odd-sign eigenspace.
        fixed = tuple(i for i in coordinates if all(
            row[i] == row[first] for row in levels.values()))
        if fixed == triple:
            planes.append(triple)
    return direct, planes


zero = (0, 0)
a, b, c = (1, 0), (0, 1), (1, 1)
two_flips = [a, b, zero, zero, zero]  # x,y,u,v,w
three_even_flips = [a, b, c, zero, zero]  # x,y,z,u,v
assert sectors(two_flips, [zero] * 5) == ([], [])
assert sectors(three_even_flips, [zero] * 5) == (
    [3, 4], [(0, 3, 4), (1, 3, 4), (2, 3, 4)])
points = list(product(range(3), repeat=2))
count = 0
for u, v, w in product(points, repeat=3):
    vu = tuple(y - x for x, y in zip(u, v))
    wu = tuple(y - x for x, y in zip(u, w))
    if determinant(vu, wu) % 3 == 0:
        continue
    assert sectors(two_flips, [u, v, u, v, w]) == (
        [], [(0, 2, 3), (0, 2, 4), (1, 2, 3), (1, 3, 4)])
    count += 1
assert count == 432
print("Independent sign flips: HH_1=0 with trivial three-part, 4 in all 432 affine frames.")
print("Even sign changes on three variables: two linear residues and three elliptic sectors.")
