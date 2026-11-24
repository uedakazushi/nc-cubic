#!/usr/bin/env python3
"""Check the symmetrizer on the two-elliptic-block slice and its j-map."""
from itertools import combinations
import sympy as sy

coords = sy.symbols("x0:7")
u = coords[-1]


def symmetrizer_dimension(cubic):
    # For each Hessian coefficient H, impose H A = A^t H once per pair.
    n = len(coords)
    entries = sy.hessian(cubic, coords)
    rows = []
    for variable in coords:
        hessian = entries.diff(variable)
        for i, j in combinations(range(n), 2):
            row = [0] * (n*n)
            for k in range(n):
                row[k*n+j] += hessian[i, k]
                row[k*n+i] -= hessian[j, k]
            rows.append(row)
    return n*n - sy.Matrix(rows).to_DM().rank()


# All the test cubics have smooth reduction modulo 2: the u-derivative
# gives u^2, then the remaining six equations give the six coordinate squares.
for mixed, support, expected in [
    (True, (), 3), (True, (0,), 2), (True, (0, 3), 1),
    (False, (), 7), (False, (0,), 7), (False, (0, 3), 5),
    (False, tuple(range(6)), 1),
]:
    cubic = sum(x**3 for x in coords) + u**2*sum(coords[i] for i in support)
    if mixed:
        cubic += 2*sy.prod(coords[:3]) + 2*sy.prod(coords[3:6])
    assert symmetrizer_dimension(cubic) == expected

s, t, d = sy.symbols("s t d")
x, y = (s+t)/2, (s-t)/2
assert sy.expand(4*(x**3+y**3+u**2*(x+y)+d*u**3) -
                 (s**3+3*s*t**2+4*s*u**2+4*d*u**3)) == 0
X = sy.Symbol("X")
rhs = X**3 + 4*X**2 + 16*d**2
assert sy.factor(16*sy.discriminant(rhs, X) + 4096*d**2*(16+27*d**2)) == 0
assert sy.cancel(256**3 / (16*sy.discriminant(rhs, X)) +
                 4096/(d**2*(16+27*d**2))) == 0
print("Seven smooth fibers: symmetrizer dimensions 3, 2, 1, 7, 7, 5, 1.")
print("Fermat slice: ternary equation, Weierstrass discriminant and j-map verified.")
