#!/usr/bin/env python3
"""Exact checks for the horizontal mutation and the four-component toric model."""
from itertools import combinations, product
from math import gcd

import sympy as sy


def check_mutation():
    x, y, z = variables = sy.symbols("x y z", nonzero=True)
    last = sy.Matrix([[x, y, z]])
    middle = sy.Matrix([[-y, -z, 0], [x, 0, -z], [0, x, y]])
    first = sy.Matrix([z, -y, x])
    assert last*middle == sy.zeros(1, 3) and middle*first == sy.zeros(3, 1)
    minors = {sy.expand(middle.extract(i, j).det()) for i in combinations(range(3), 2)
              for j in combinations(range(3), 2)}
    assert all(v**2 in minors or -v**2 in minors for v in variables)

    # Local splittings of the Euler surjection represent its connecting
    # class on the three coordinate opens.
    lifts = [sy.eye(3)[:, i]/v for i, v in enumerate(variables)]
    assert all(last*lift == sy.ones(1, 1) for lift in lifts)
    transitions = [lifts[j]-lifts[i] for i, j in ((0, 1), (1, 2), (2, 0))]
    assert all(last*c == sy.zeros(1) for c in transitions)
    assert sum(transitions, sy.zeros(3, 1)) == sy.zeros(3, 1)
    # Chi(K(tH)) has its forced roots 0,-1 and leading coefficient rank/6.
    t, r, k = sy.symbols("t r k")
    polynomial = t*(t+1)*(r*(t+2)+3*k)/6
    assert sy.expand(3*polynomial.subs(t, 1)-polynomial.subs(t, 2)) == -r
    print("Koszul syzygies, the Euler connecting cocycle, and the mutation coefficient -rank.")


def primitive_ray(vector):
    divisor = gcd(*(abs(int(a)) for a in vector))
    return tuple(int(a)//divisor for a in vector)


def normal_cones():
    axes = [sy.eye(3)[:, i] for i in range(3)]
    exponents = [(3, 0, 0), (1, 1, 0), (1, 0, 1),
                 (0, 3, 0), (0, 2, 1), (0, 1, 2), (0, 0, 3)]
    # Weight 2,1,1. A minimal monomial must have each exponent <=3.
    invariants = [m for m in product(range(4), repeat=3) if any(m) and
                  (2*m[0]+m[1]+m[2]) % 3 == 0]
    minimal = [m for m in invariants if not any(other != m and all(a <= b for a, b in zip(other, m))
                                                for other in invariants)]
    assert set(minimal) == set(exponents)
    weights = list(map(sy.Matrix, exponents))
    cones = set()
    for weight in weights:
        inequalities = axes + [m-weight for m in weights if m != weight]
        rays = set()
        for left, right in combinations(inequalities, 2):
            cross = left.cross(right)
            if cross == sy.zeros(3, 1):
                continue
            for candidate in (cross, -cross):
                if all(f.dot(candidate) >= 0 for f in inequalities):
                    rays.add(primitive_ray(candidate))
        if len(rays) >= 3 and sy.Matrix(list(rays)).rank() == 3:
            cones.add(frozenset(rays))
    return cones


def check_fan():
    a, b, c = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    v, vp = (1, 2, 2), (2, 1, 1)
    cones = normal_cones()
    expected = [(a, vp, c), (a, b, vp), (v, vp, c), (vp, b, v), (v, b, c)]
    assert cones == {frozenset(cone) for cone in expected}
    rays = {r: sy.Matrix(r)/(3 if r in (v, vp) else 1) for r in (a, b, c, v, vp)}
    for cone in cones:
        assert abs(sy.Matrix.hstack(*(rays[r] for r in cone)).det()) == sy.Rational(1, 3)
    A, B, C, U, Uprime = [rays[r] for r in (a, b, c, v, vp)]
    assert [p[0]+p[2] for p in (A, B, C, U, Uprime)] == [1, 0, 1, 1, 1]
    assert Uprime+B+C == 2*U and A+U == 2*Uprime and B+C == 2*U-Uprime

    # (rank, H coefficient of c1) after the two left mutations.
    O, H = sy.Matrix([1, 0]), sy.Matrix([1, 1])
    point = 2*O-H
    curve = H-3*O
    assert curve+2*point == sy.Matrix([0, -1])
    # Degree zero along the fiber of F2 forces its two section degrees
    # to agree. The two lines of P2 must also have equal degrees.
    degree_y, degree_vp, degree_v = 0, 0, -1
    assert degree_y-2*degree_vp != degree_v
    # Columns are hyperplane, S, Dprime in the basis (l,h) on S.
    restriction = sy.Matrix([[2, -2, 6], [0, -1, 2]])
    minus_z0 = sy.Matrix([-1, 2, 1])
    assert restriction.nullspace() == [minus_z0]
    fiber_degrees = sy.Matrix([[0, 1, -3]])
    assert (fiber_degrees * minus_z0)[0] == -1
    r, k = sy.symbols("r k")
    assert sy.solve(sy.Eq(sy.Symbol("d") - 2*r, k - 3*r), sy.Symbol("d")) == [k - r]
    print("Boundary Picard kernel and the forced determinant degree k-r.")
    print("Five unimodular cones, four reduced components, and rank-zero probe degrees 0,-1.")


if __name__ == "__main__":
    check_mutation()
    check_fan()
