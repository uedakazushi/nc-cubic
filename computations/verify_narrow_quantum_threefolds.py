#!/usr/bin/env python3
"""Classify balanced five-variable commutation matrices over F_3 by HH_1."""
from collections import Counter
from itertools import combinations, permutations, product

indices = range(5)
pairs = tuple(combinations(range(4), 2))
triples = tuple(combinations(indices, 3))


def balanced_matrix(entries):
    matrix = [[0]*5 for _ in indices]
    for (i, j), value in zip(pairs, entries):
        matrix[i][j] = value
        matrix[j][i] = -value % 3
    for i in range(4):
        matrix[i][4] = -sum(matrix[i][:4]) % 3
        matrix[4][i] = -matrix[i][4] % 3
    assert all(sum(row) % 3 == 0 for row in matrix)
    return tuple(map(tuple, matrix))


def rank(entries):
    a,b,c,d,e,f = entries
    if (a*f-b*e+c*d) % 3:
        return 4
    return 2 if any(entries) else 0


def elliptic_sectors(matrix):
    for triple in triples:
        values = tuple(sum(row[j] for j in triple) % 3 for row in matrix)
        if not any(values):
            continue
        level = tuple(i for i in indices if values[i] == values[triple[0]])
        if level == triple:
            yield values


def dimension(matrix):
    invariant_linear_forms = sum(not any(row) for row in matrix)
    return invariant_linear_forms + sum(1 for _ in elliptic_sectors(matrix))


def relabel(matrix, permutation):
    return tuple(tuple(matrix[i][j] for j in permutation) for i in permutation)


def orbit(matrix):
    return {relabel(matrix, p) for p in permutations(indices)}


triangle = balanced_matrix((1,2,0,1,0,0))
cyclic = tuple(tuple((0 if i == j else 1 if (j-i) % 5 in (1,2) else 2)
                     for j in indices) for i in indices)
survivors = {0:set(), 2:set(), 4:set()}
counts = Counter()
for entries in product(range(3), repeat=len(pairs)):
    matrix = balanced_matrix(entries)
    r, h = rank(entries), dimension(matrix)
    counts[r,h] += 1
    if h == 5:
        survivors[r].add(matrix)

assert survivors[0] == {balanced_matrix((0,)*6)}
assert survivors[2] == orbit(triangle) and len(survivors[2]) == 20
assert survivors[4] == orbit(cyclic) and len(survivors[4]) == 24
assert sum(counts.values()) == 729
print("rank   HH1=0,1,2,3,4,5")
for r in (0,2,4):
    print(r, [counts[r,h] for h in range(6)])
print("HH1=5: zero (1), triangle (20), cyclic tournament (24).")


# The five elliptic sectors of the final representative detect the character group.
levels = tuple(elliptic_sectors(cyclic))
edge = (0,0,2,0,1)
assert set(levels) == {edge[i:] + edge[:i] for i in indices}
span = {tuple(sum(a*v[i] for a,v in zip(coeffs,levels)) % 3 for i in indices)
        for coeffs in product(range(3),repeat=5)}
assert len(span) == 81 and all(sum(v) % 3 == 0 for v in span)
print("The five sectors span the entire group of order 81.")
