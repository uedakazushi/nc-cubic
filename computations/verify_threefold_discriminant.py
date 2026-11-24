#!/usr/bin/env python3
"""Compute the projective singular schemes on four components over Q."""
from itertools import product

import sympy as sy

x, y, z, u, v = variables = sy.symbols("x y z u v")
p = u*v*(u+v)
repeated = (u-v)**2*(u+2*v)


def count_nodes(cubic):
    derivatives = [cubic.diff(a) for a in variables]
    total = 0
    # Use disjoint projective charts to count each point exactly once.
    for i, pivot in enumerate(variables):
        affine = variables[:i] + variables[i+1:]
        cut = {a: 0 for a in variables[:i]}
        cut[pivot] = 1
        equations = [f.subs(cut) for f in derivatives]
        free = variables[i+1:]
        if not free:
            if any(equations):
                continue
            dimension = 1
        else:
            basis = sy.groebner(equations, *free, order="grevlex", domain=sy.QQ)
            if basis.contains(sy.Integer(1)):
                continue
            assert basis.is_zero_dimensional
            leads = [g.LM(order=basis.order).exponents for g in basis.polys]
            bounds = [min(m[j] for m in leads if m[j] and sum(m) == m[j])
                      for j in range(len(free))]
            dimension = sum(not any(all(a >= b for a, b in zip(m, n)) for n in leads)
                            for m in product(*(range(b) for b in bounds)))
        # Differentiate before the chart cuts to keep every tangent direction.
        matrix = sy.hessian(cubic, affine).subs(cut)
        determinant = matrix.det(method="berkowitz").expand()
        if free:
            remainder = basis.reduce(determinant)[1]
            assert sy.groebner([*equations, remainder], *free, domain=sy.QQ).contains(sy.Integer(1))
        else:
            assert determinant
        total += dimension
    return total


for component, coefficient, g, expected in [
    ("lambda", 0, u**3+2*v**3, 4),
    ("Disc(g)", 2, repeated, 1),
    ("Disc(h)", 2, repeated-p, 4),
    ("Res(L1,g)", 2, u*(u**2+v**2), 2),
    ("smooth complement", 2, u**3+2*v**3, 0),
]:
    cubic = u*x**2+v*y**2+(u+v)*z**2+coefficient*x*y*z+g
    assert count_nodes(cubic) == expected
    print(f"{component}: {expected} ordinary double points.")
