#!/usr/bin/env python3
"""Exact identities for the two-dimensional simple D_alpha modules.

Date: 2026-11-22 / v45.  Dependency: SymPy.  All checks are symbolic or
rational, without numerical sampling.  Classification and exactness of
the Ext calculation are proved in the manuscript, not by these checks.
"""
from itertools import permutations
import sympy as s


def q(v):
    a, b, c = v
    return s.Matrix([a*a-b*c, b*b-c*a, c*c-a*b])


def F(v):
    a, b, c = v
    return a**3+b**3+c**3-3*a*b*c


def zero(expr):
    if isinstance(expr, s.MatrixBase):
        assert all(s.cancel(x) == 0 for x in expr)
    else:
        assert s.cancel(expr) == 0


def main():
    a, b, c, r = s.symbols('a b c r', nonzero=True)
    v = s.Matrix([a, b, c])
    zero(q(q(v))-F(v)*v)
    zero(F(q(v))-F(v)**2)
    zero(q(v).jacobian(v).det()+2*F(v))
    print('PASS quadratic inverse, cubic norm and Jacobian identities')

    # Work on r^2=-bc, using c=-r^2/b.  This parametrizes the entire
    # abc != 0 locus after adjoining the chosen square root.
    cv = -r*r/b
    alpha = q([a, b, cv])
    I = s.eye(2)
    U = s.diag(r, -r)
    V = s.Matrix([[0, 1], [-cv*a, 0]])
    W = s.Matrix([[0, r/cv], [r*a, 0]])
    X, Y, Z = a*I+U, b*I+V, cv*I+W
    for L, M, N, al in [(Y, Z, X, alpha[0]),
                       (Z, X, Y, alpha[1]),
                       (X, Y, Z, alpha[2])]:
        zero(L*M-M*L-N*N+al*I)
    print('PASS universal representation matrices')

    matrices = [X, Y, Z]
    sym = sum((matrices[p[0]]*matrices[p[1]]*matrices[p[2]]
               for p in permutations(range(3))), s.zeros(2))/6
    omega = (X**3+Y**3+Z**3)/3-s.Rational(2,3)*sym
    omega -= sum((alpha[i]*matrices[i] for i in range(3)), s.zeros(2))
    lam = -s.Rational(2,3)*(a**3+b**3+cv**3+a*b*cv)
    zero(omega-lam*I)
    print('PASS universal central scalar')

    expected = [s.Rational(73728,343),
                s.Rational(37623589339922432,748505944125)]
    for alpha, target in zip([(1,4,9),(16,25,49)],expected):
        Q, D = q(alpha), F(alpha)
        assert D and all(Q)
        K = D*D+4*s.prod(Q)
        squared = s.Rational(4,9)*K*K/D**3
        zero(squared-target)
        print(f'PASS alpha={alpha}: D={D}, Q={tuple(Q)}, lambda^2={squared}')


if __name__ == '__main__':
    main()
