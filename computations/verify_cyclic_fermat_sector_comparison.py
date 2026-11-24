#!/usr/bin/env python3
"""Exact twisted-sector/plane tests for the cyclic five-vertex Fermat comparison.

Eisenstein integer matrices are represented by pairs (A,B) meaning A+B*zeta.
All matrix entries are integers; the transforms below are unnormalized.
"""
from collections import Counter
from itertools import combinations, product

import numpy as np


def roots(exponents):
    degrees = exponents % 3
    # zeta^2 = -1-zeta
    return ((degrees == 0).astype(int) - (degrees == 2),
            (degrees == 1).astype(int) - (degrees == 2))


def multiply(x, y, operation=np.multiply):
    a, b = x
    c, d = y
    bd = operation(b, d)
    return operation(a, c) - bd, operation(a, d) + operation(b, c) - bd


def transpose(x):
    return tuple(m.T for m in x)


def restrict(x, indices):
    return tuple(m[np.ix_(indices, indices)] for m in x)


points = np.array([p + (-sum(p) % 3,) for p in product(range(3), repeat=4)])
order = len(points)
assert order == 81
point_index = {tuple(p): i for i, p in enumerate(points)}
cyclic = np.array([[0 if i == j else 1 if (j-i) % 5 in (1,2) else -1
                    for j in range(5)] for i in range(5)])
inverse = {tuple((cyclic @ t) % 3): t for t in points}
alpha = np.array([inverse[tuple(g)] for g in points]) @ points.T % 3
edges = np.array([np.roll((0,0,2,0,1), -i) for i in range(5)])
target_index = [point_index[tuple(v)] for v in points @ edges.T % 3]
assert len(set(target_index)) == order


def fixed_traces():
    """Rows index g, columns h; coefficients give trace on HH_i(Y^g), minus
    the two linearized exceptional objects' contributions in degree zero."""
    arrays = {i: (np.zeros((order,order), dtype=int), np.zeros((order,order), dtype=int))
              for i in (-1,0,1)}
    arrays[0][0][:] = -2

    def add(i, row, weights):
        a,b = roots(weights)
        arrays[i][0][row] += a
        arrays[i][1][row] += b

    for row, g in enumerate(points):
        for level in range(3):
            block = np.flatnonzero(g == level)
            size = len(block)
            determinant = points[:,block].sum(axis=1)
            if size == 5:
                arrays[0][0][row] += 4
                for j in block:
                    add(1,row,points[:,j])
                    add(-1,row,-points[:,j])
            elif size == 4:
                arrays[0][0][row] += 3
                for j,k in combinations(block,2):
                    add(0,row,determinant + points[:,j] + points[:,k])
            elif size == 3:
                arrays[0][0][row] += 2
                add(1,row,determinant)
                add(-1,row,-determinant)
            elif size == 2:
                j,k = block
                arrays[0][0][row] += 3 * (points[:,j] == points[:,k])
    return arrays


def transformed(raw):
    characters = points @ points.T
    twisted = multiply(raw,roots(alpha))
    left = multiply(roots(characters), transpose(twisted), np.matmul)
    numerator = multiply(left, roots(-characters), np.matmul)
    assert all(np.all(m % order == 0) for m in numerator)
    return tuple(m // order for m in numerator)


def trace_average(kernel, subgroup, twist):
    a,b = multiply(restrict(kernel,subgroup),roots(twist))
    assert b.sum() == 0 and a.sum() % len(subgroup) == 0
    return int(a.sum() // len(subgroup))


raw = fixed_traces()
def verify_residue_product(traces):
    """Expand the five local factors, including the empty level's constant."""
    for row, geometric in enumerate(points):
        coefficients = {i: np.zeros((2, order), dtype=int) for i in traces}
        for level in range(3):
            fixed = np.flatnonzero(geometric == level)
            for signs in product((1, -1), repeat=len(fixed)):
                degree = sum(signs)
                if degree % 3 == 0:
                    weight = points[:, fixed] @ np.asarray(signs, dtype=int)
                    coefficients[degree // 3] += np.array(roots(weight))
        for i, pair in traces.items():
            assert np.array_equal(coefficients[i], [component[row] for component in pair])


verify_residue_product(raw)
print("Laurent product agrees with geometric traces on all 6561 ordered pairs.")
source = {i: transformed(k) for i,k in raw.items()}
target = {i: restrict(k,target_index) for i,k in raw.items()}
upper = np.triu(np.ones((4,4),dtype=int), 1)
beta = points[:,:4] @ (upper-upper.T) @ points[:,:4].T % 3
for i in raw:
    expected = multiply(target[i], roots(beta))
    assert all(np.array_equal(a,b) for a,b in zip(source[i],expected))
print("Exact pair identity in HH degrees -1, 0, 1:", 3*order**2, "entries.")


# Average only over H=<e0-e1>. The complement J=r^perp acts geometrically.
root = np.array([1,-1,0,0,0])
projected = (2*(points @ root))[:,None] * root % 3
orthogonal = (points-projected) % 3
root_source = {d: tuple(np.zeros_like(m) for m in kernel) for d,kernel in raw.items()}
for k,l in product(range(3),repeat=2):
    g,h = k*root, l*root
    rows = [point_index[tuple(v)] for v in (orthogonal+g) % 3]
    cols = [point_index[tuple(v)] for v in (orthogonal+h) % 3]
    cross = roots((points @ h)[:,None] - (points @ g)[None,:])
    for d,kernel in raw.items():
        part = multiply(tuple(m[np.ix_(rows,cols)] for m in kernel),cross)
        for total,term in zip(root_source[d],part):
            total += term
for d,kernel in root_source.items():
    assert all(np.array_equal(m,3*n) for m,n in zip(kernel,raw[d]))
print("The elementary root transform preserves all three trace tables exactly.")

# On a plane, a form is determined by its value on one ordered basis.
pairs = list(combinations(range(4),2))
forms = np.array(list(product(range(3),repeat=6)),dtype=int)
ordinary_matches = np.ones(len(forms),dtype=bool)
twisted_matches = ordinary_matches.copy()
plane_coords = np.array(list(product(range(3),repeat=2)))
u,v = plane_coords.T
area = np.outer(u,v) - np.outer(v,u)
root_matches = ordinary_matches.copy()
planes = set()
unique_restrictions = Counter()
for i,j in combinations(range(1,order),2):
    subgroup = [point_index[tuple(p)] for p in plane_coords @ points[[i,j]] % 3]
    key = frozenset(subgroup)
    if len(key) != 9 or key in planes:
        continue
    planes.add(key)
    wedge = [points[i,a]*points[j,b]-points[i,b]*points[j,a] for a,b in pairs]
    restrictions = forms @ wedge % 3

    def plane_table(kernels):
        return [tuple(trace_average(kernels[d],subgroup,t*area) for d in (0,1))
                for t in range(3)]

    actual, geometric = plane_table(source), plane_table(target)
    ordinary = [actual[0] == geometric[t] for t in range(3)]
    all_twists = [all(actual[s] == geometric[(s+t)%3] for s in range(3))
                  for t in range(3)]
    # The elementary transform equals raw exactly. Untwisted plane averages
    # already rule out every nonzero global coherence discrepancy.
    root_table = plane_table(raw)
    root_matches &= np.array([root_table[0] == rank for rank in root_table])[restrictions]
    ordinary_matches &= np.array(ordinary)[restrictions]
    twisted_matches &= np.array(all_twists)[restrictions]
    unique_restrictions[sum(all_twists)] += 1

assert len(planes) == 130 and unique_restrictions == {1:130}
assert forms[ordinary_matches].tolist() == [[1]*6, [2]*6]
assert forms[twisted_matches].tolist() == [[1]*6]
print("130 planes and three twists: of 729 global forms, unsigned tests retain +/-beta, all tests retain beta.")

assert forms[root_matches].tolist() == [[0]*6]
print("Elementary transport: the zero coherence class is the only possible class.")

# The four root enlargements realize the commutator of the five-vertex example.
simple = np.eye(5,dtype=int)
tree = np.array([simple[i]-simple[j] for i,j in ((0,1),(0,3),(1,2),(1,4))])
assert len({tuple(v) for v in points[:,:4] @ tree % 3}) == order
indices = [point_index[tuple(v % 3)] for v in tree]
expected_upper = np.triu(tree @ tree.T,1)
assert np.array_equal(alpha[np.ix_(indices,indices)],
                      (expected_upper-expected_upper.T) % 3)
print("Four independent roots reproduce alpha on the full group.")
