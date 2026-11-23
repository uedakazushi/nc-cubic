#!/usr/bin/env python3
"""Check the finite representation computations in qfo:thm:obstruction."""
from collections import defaultdict
from fractions import Fraction
from itertools import product

G = tuple(product(range(3), repeat=2))
weights = ((1, 0), (2, 0), (0, 1), (0, 2), (0, 0))


def dot(a, b):
    return sum(i*j for i,j in zip(a,b)) % 3


def commutator(g, h):
    return (g[0]*h[1] - g[1]*h[0]) % 3


def sub(a, b):
    return tuple((x-y) % 3 for x,y in zip(a,b))


def invariant_dimension(character):
    """Average a character expressed as the multiplicities of 1,zeta,zeta^2."""
    s = [sum(character(h)[i] for h in G) for i in range(3)]
    assert s[1] == s[2]
    value = Fraction(s[0] - s[1], len(G))
    assert value.denominator == 1
    return int(value)


def twisted_dimension(exponents, g):
    def character(h):
        values = [(dot(h,w) + commutator(g,h)) % 3 for w in exponents]
        return [values.count(i) for i in range(3)]
    return invariant_dimension(character)


def sector(g):
    if g == (0,0):
        return twisted_dimension(weights,g), 4
    eigenspaces = defaultdict(list)
    for w in weights:
        eigenspaces[dot(g,w)].append(w)
    h1 = h0 = 0
    for ws in eigenspaces.values():
        if len(ws) == 3:
            canonical = tuple(sum(w[j] for w in ws) % 3 for j in range(2))
            h1 += twisted_dimension([canonical],g)
            h0 += twisted_dimension([(0,0)]*2,g)
        elif len(ws) == 2:
            char = sub(ws[0], ws[1])
            # The three Fermat ratios are one mu3-torsor: its permutation
            # representation contains the three characters 0, char, -char.
            h0 += twisted_dimension([(0,0),char,sub((0,0),char)],g)
        else:
            assert len(ws) == 1
    return h1,h0


assert all(sum(w[j] for w in weights) % 3 == 0 for j in range(2))
# Ad(P^a Q^b) on P^v Q^-u cancels the coordinate character.
for g,w in product(G,G):
    assert (dot(g,w) + commutator(g,(w[1],-w[0]))) % 3 == 0
counts = [sector(g) for g in G]
assert counts == [(1,4),(0,0),(0,0),(0,0),(0,2),(0,2),(0,0),(0,2),(0,2)]
h1,h0 = map(sum,zip(*counts))
assert (h1,h0-2) == (1,10)
print("Nine sectors (HH1, HH0):", list(zip(G,counts)))
print("Residual (HH1, HH0): quantum (1,10), commutative (5,2).")


def check_full_center():
    from itertools import combinations_with_replacement

    central = [word for word in combinations_with_replacement(range(5), 3)
               if all(sum(weights[i][j] for i in word) % 3 == 0 for j in range(2))]
    assert set(central) == {(i,i,i) for i in range(5)} | {(0,1,4),(2,3,4)}


def check_critical_values():
    """Compute multiplication by the affine equation in its gradient algebra."""
    import sympy as sp

    x, y = sp.symbols('x y')
    a, b, c, d, e, lam, mu = sp.symbols('a b c d e lam mu')
    basis = (1, x, y, x*y)

    def critical_operator(A, B, mix):
        field = sp.QQ.frac_field(A, B, mix)
        cubic = A*x**3+B*y**3+mix*x*y
        gb = sp.groebner([sp.diff(cubic,x),sp.diff(cubic,y)],
                         x,y,order='grlex',domain=field)
        columns = []
        for mon in basis:
            remainder = sp.Poly(gb.reduce(cubic*mon)[1],x,y)
            columns.append(sp.Matrix([remainder.coeff_monomial(term) for term in basis]))
        return sp.Matrix.hstack(*columns)

    # The two gradient ideals use disjoint variables; the quotient is a tensor product.
    first = critical_operator(a,b,lam)
    second = critical_operator(c,d,mu)
    operator = (e*sp.eye(16) + sp.kronecker_product(first,sp.eye(4))
                + sp.kronecker_product(sp.eye(4),second))
    L, M = lam**3/(27*a*b), mu**3/(27*c*d)
    expected = e*(e+L)**3*(e+M)**3*(e+L+M)**9
    assert sp.factor(operator.det()-expected) == 0


check_full_center()
check_critical_values()
print("Seven central monomials and the exact degree-16 critical determinant verified.")
