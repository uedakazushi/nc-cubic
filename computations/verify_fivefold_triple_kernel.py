#!/usr/bin/env python3
"""Recover the odd Jacobian relations from the triple product, over Q."""
from itertools import combinations_with_replacement, product

import sympy as sy
from sympy.matrices.normalforms import smith_normal_form

v = sy.symbols("v1:4")
w = sy.Symbol("w")
variables = (*v, w)


def monomials(weight):
    return [
        v[0]**a * v[1]**b * v[2]**(weight - 2*d - a - b) * w**d
        for d in range(weight//2 + 1)
        for a in range(weight - 2*d + 1)
        for b in range(weight - 2*d - a + 1)
    ]


def rows(forms, basis):
    polynomials = [sy.Poly(f, *variables) for f in forms]
    return sy.Matrix([[f.coeff_monomial(m) for m in basis] for f in polynomials])


def check_sextic(name, h):
    q = h.diff(w)
    gradients = [h.diff(x) for x in v]
    b2, b4, b5, b6 = map(monomials, (2, 4, 5, 6))
    j6 = rows([a*q for a in b2] + [a*f for a in v for f in gradients], b6)
    j5 = rows([a*q for a in v] + gradients, b5)
    assert j6.rank() == 16 and j5.rank() == 6

    # Columns test membership in J6 by pairing with its orthogonal space.
    tests = sy.Matrix.hstack(*j6.nullspace())
    constraints = sy.Matrix.vstack(*[(rows([a*m for m in b5], b6)*tests).T for a in v])
    assert constraints.rank() == 28 and constraints*j5.T == sy.zeros(constraints.rows, 6)

    pairs = [a*b for a, b in combinations_with_replacement(b2, 2)]
    triples = [a*b*c for a, b, c in combinations_with_replacement(b2, 3)]
    triple_map = rows(triples, b6)*tests
    assert triple_map.rank() == 34 and len(triples) - triple_map.rank() == 50
    colon = sy.Matrix.hstack(*[rows([a*m for m in pairs], b6)*tests for a in b2])
    quadratic_tests = sy.Matrix.hstack(*rows([q], b4).nullspace())
    quadratic_map = rows(pairs, b4)*quadratic_tests
    # Both maps have the same kernel on the left.
    assert colon.rank() == quadratic_map.rank() == colon.row_join(quadratic_map).rank() == 21
    print(f"{name}: triple rank 34, quadratic kernel dimension 7, "
          "recovered all six weight-five relations.")


fermat = w**3 + sum(a**6 for a in v)
check_sextic("double plane with nilpotents", fermat)
# Smooth in characteristic zero: modulo 5 the four derivatives are pure powers.
mixed = fermat + 5*w*(v[0]**3*v[1]+v[2]**4) + 5*v[0]*v[1]**2*v[2]**3
check_sextic("mixed quartic and sextic", mixed)

# At each devissage step the hypersurface relation specializes to zero
# in the tensor product of C[z]/z^3 and the two shorter truncations.
for i in range(3):
    others = [j for j in range(3) if j != i]
    for e in product((1, 2), repeat=2):
        caps = dict(zip(others, e))
        caps[i] = 3
        for powers in combinations_with_replacement(range(4), 3):
            if 3 not in powers:  # w=0 already kills all other cubics.
                assert any(2*powers.count(j) >= caps[j] for j in range(3))
print("The intermediate quotient maps exist for all 20 cubic monomials and 12 truncations.")

# Present the degree-three identity sector modulo all cubic products of
# central variables; compute its torsion over the whole parameter line.
x = sy.symbols("x1:4")
u = sy.symbols("u1:4")
lam = sy.Symbol("lambda")
central = (*u, w)
potential = sum(a*b*b for a, b in zip(u, x)) + lam*sy.prod(x) + sum(a**3 for a in central)
basis = [a**2*b for a in x for b in central] + [sy.prod(x)]
relations = [b*potential.diff(a) for b in central for a in central]
relations += [a*potential.diff(a) for a in x]
presentation = sy.Matrix([[sy.Poly(f, *x, *central).coeff_monomial(m) for m in basis]
                          for f in relations])
smith = smith_normal_form(presentation, domain=sy.QQ.poly_ring(lam))
diagonal = list(smith.diagonal())
assert all(g in (1, -1) for g in diagonal[:-1]) and diagonal[-1] in (lam, -lam)
print("Identity sector modulo central cubics: 12 unit pivots and one lambda pivot.")

# In the scalar sector formula isolated primitives contribute only when
# b + 3*(j-c) is a weight in the fixed Jacobian. At the order-two sector
# exactly one of the moving directions carries the negative deck character.
weights = (1, 1, 1, 2, 3)
for power in range(1, 6):
    moving = [d for d in weights if power*d % 6]
    fixed_weights = (0, 2) if power == 3 else (0,)
    hits = []
    for fixed_weight in fixed_weights:
        numerator = fixed_weight - sum(moving)
        if numerator % 6 == 0:
            hits.append(len(moving) + numerator//3)
    assert hits == ([2] if power == 3 else [])
    if hits:
        assert 3 in moving
print("All five nonidentity scalar sectors checked; the extra HH^2 line is deck-odd.")
