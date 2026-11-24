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

# Keep the original two boundary blocks fixed. Work in the pure quadratic
# complement of the gradient quadrics of the ternary J.
left, right = coords[:3], coords[3:6]
boundary = sum(x**3 for x in coords[:6]) + sy.prod(left) + sy.prod(right)
for quadratic, linear, constant, expected in [
    (left[0]*left[1] + right[0]*right[1], 0, 1, 1),
    (left[0]*left[1], right[0], 1, 1),
    (left[0]*left[1], 0, 1, 2),
    (left[0]*left[1], 3*left[2], 0, 3),
]:
    target = boundary + u*quadratic + u**2*linear + constant*u**3
    assert symmetrizer_dimension(target) == expected

x, y, z = left
m = sy.Symbol("m")
on_curve = x**3+y**3+z**3+(z+u)*x*y + m*u**2*z + (3*m-m**2)*u**3/9
split = (x**3+y**3+(z+u)*x*y + m*(z+u)**3/(m+3)
         + 3*(z-m*u/3)**3/(m+3))
assert sy.cancel(on_curve-split) == 0
print("Quadratic slice: symmetrizer dimensions 1, 1, 2, 3 and the splitting parabola verified.")

h1 = z**3 + m*z + d
h2 = h1 + (z+1)**3/27
discriminants = [sy.discriminant(h, z) for h in (h1, h2)]
assert all(delta.subs({m: 0, d: 1}) != 0 for delta in discriminants)
restricted = sy.prod(discriminants).subs(d, (3*m-m**2)/9)
assert sy.Poly(restricted, m).sqf_part().monic() == sy.Poly(m*(m+3)*(m+sy.Rational(3,28)), m)
print("Both cubic discriminants cut precisely three excluded points on the parabola.")


def check_plane_incidence():
    # A polynomial coefficient is forbidden exactly when both triples occur.
    from itertools import combinations_with_replacement

    monomials = list(combinations_with_replacement(range(7), 3))
    mixed = [indices for indices in monomials
             if any(i < 3 for i in indices) and any(3 <= i < 6 for i in indices)]
    assert len(monomials) == 84 and len(mixed) == 45

    # Differential of the mixed-polar condition for a fixed equation. Keep
    # the third argument fixed and vary the first and second planes as graphs.
    target = sum(x**3 for x in coords) + 2*u*(coords[0]*coords[1] + coords[3]*coords[4])
    hessians = [sy.hessian(target.diff(w), coords) for w in coords]
    graphs = (sy.Matrix(4, 3, sy.symbols("p0:12")), sy.Matrix(4, 3, sy.symbols("q0:12")))
    first, second = graphs
    equations = []
    for hessian in hessians:
        for i in range(3):
            for j in range(3):
                assert hessian[i, 3+j] == 0
                vary_first = hessian.extract([3, 4, 5, 6], [3+j]).dot(first[:, i])
                vary_second = hessian.extract([i], [0, 1, 2, 6]).dot(second[:, j])
                equations.append(vary_first + vary_second)
    differential = sy.Matrix(equations).jacobian(list(first) + list(second))
    assert differential.to_DM().rank() == 24
    print("Plane incidence: 45 independent monomial conditions and tangent rank 24.")


check_plane_incidence()
