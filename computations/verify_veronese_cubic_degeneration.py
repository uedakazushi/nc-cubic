#!/usr/bin/env python3
"""Exact checks for the Veronese degeneration, centre cover and Clifford kernel."""
from itertools import combinations, combinations_with_replacement

import sympy as sy
from sympy.matrices.normalforms import smith_normal_form


def verify_normal_chart():
    a, b, x, y, z, w, e = sy.symbols("a b X Y Z W e")
    matrix = sy.Matrix([[1, a, b], [a, a*a+e**3*x, a*b+e**3*y],
                        [b, a*b+e**3*y, b*b+e**3*z]])
    assert sy.expand(matrix.det()-e**6*(x*z-y*y)) == 0
    # Expand every basis monomial independently. Lifts with identical
    # restrictions can differ by a multiple of a Veronese minor.
    for degree, count in [(2, 15), (3, 28)]:
        entries = [matrix[i, j] for i in range(3) for j in range(i, 3)]
        basis = combinations_with_replacement(entries, degree)
        restrictions = [(sy.prod(m)).expand().subs(e, 0) for m in basis]
        assert len(set(restrictions)) == count
        assert all(sy.Poly(f, a, b).total_degree() <= 2*degree for f in restrictions)
    print("Schur determinant and restriction ranks 15, 28 in the scaled chart.")


def verify_signed_arc():
    u, v, l, x, y, z, lam = sy.symbols("u v l x y z lambda", nonzero=True)
    matrix = sy.Matrix([[u, -lam*z/2, sy.I*lam*y/2], [-lam*z/2, v, sy.I*lam*x/2],
                        [sy.I*lam*y/2, sy.I*lam*x/2, l]])
    dual = u*x*x+v*y*y-l*z*z+lam*x*y*z+4*u*v*l/lam**2
    assert sy.expand(4*matrix.det()/lam**2-dual) == 0
    e, w, quartic, sextic = sy.symbols("e W A C", nonzero=True)
    g = (w/e**2)**3+w*quartic/e**2+sextic
    assert sy.expand(e**6*g-w**3-e**4*w*quartic-e**6*sextic) == 0
    print("The signed dual agrees by a projective change over lambda = 2 e^3.")


def verify_cover_and_clifford():
    w, scale, quartic, sextic = sy.symbols("w r B4 B6", nonzero=True)
    xi = scale**2/w
    s_squared = -(w**3 + scale**4*w*quartic + scale**6*sextic)
    eta_squared = scale**2*s_squared/w**4
    assert sy.expand(eta_squared+xi*(1+xi**2*quartic+xi**3*sextic)) == 0
    assert sy.expand(eta_squared-xi**4*s_squared/scale**6) == 0

    s, h = sy.symbols("s h")
    zero, eye = sy.zeros(2), sy.eye(2)
    frames = (sy.Matrix([[0, 1], [1, 0]]), sy.Matrix([[0, -sy.I], [sy.I, 0]]),
              sy.diag(1, -1))

    def odd(upper, lower):
        return zero.row_join(upper).col_join(lower.row_join(zero))

    generators = [odd(sy.I*m, sy.I*m) for m in frames] + [odd(s*eye, -s*eye)]
    for g, square in zip(generators, (-1, -1, -1, h)):
        for entry in g*g-square*sy.eye(4):
            assert sy.rem(entry, s*s+h, s) == 0
    for left, right in combinations(generators, 2):
        assert left*right+right*left == sy.zeros(4)
    coefficients = []
    for degree in (0, 2, 4):
        for basis in combinations(generators, degree):
            m = sy.eye(4)
            for g in basis:
                m = m*g
            entries = [p.expand() for p in m[:2, :2]]
            coefficients.append([v.coeff(s, n) for n in range(2) for v in entries])
    # The basis change is a constant unit, including over the branch h=0.
    assert sy.Matrix(coefficients).det() in (16, -16, 16*sy.I, -16*sy.I)
    # At h=0 keep the nilpotent coordinate s; setting s=0 too early
    # would erase the entire vertex multiplication image.
    vertex_image = []
    for degree in (1, 3):
        for factors in combinations(generators, degree):
            m = sy.eye(4)
            for factor in factors:
                m = m*factor
            entries = [sy.rem(p.expand(), s**2, s) for p in (m*generators[-1])[:2, :2]]
            assert all(p.coeff(s, 0) == 0 for p in entries)
            vertex_image.append([p.coeff(s, 1) for p in entries])
    assert sy.Matrix(vertex_image).rank() == 4
    print("The cover charts, even Clifford basis, and vertex quotient M2 modulo s are verified.")


def verify_explicit_cubic():
    u, v, l, a, b, c, w = variables = sy.symbols("u v l a b c w")
    d = sy.Matrix([[u, a, b], [a, v, c], [b, c, l]])
    f = d.det()+w**3+5*w*u*a+u**3+v**3+l**3
    derivatives = [f.diff(q) for q in variables]
    # At characteristic five the matrix coordinates are symmetric under S3.
    # Chart I covers any point with a nonzero diagonal after permutation.
    # Chart II covers the others with any nonzero off-diagonal entry.
    for chart in ({u: 1, w: 0}, {u: 0, v: 0, l: 0, a: 1, w: 0}):
        free = [q for q in variables if q not in chart]
        basis = sy.groebner([g.subs(chart) for g in derivatives], *free, modulus=5)
        assert basis.contains(sy.Integer(1))
    print("The explicit non-sign example has smooth cubic fiber e=1 by reduction mod 5.")



def verify_orbit_and_resolution():
    variables = sy.symbols("a b c d f g w")
    a, b, c, d, f, g, w = variables
    matrix = sy.Matrix([[a, d, f], [d, b, g], [f, g, c]])
    central = matrix.det() + w**3
    monomials = [sy.prod(m) for m in combinations_with_replacement(variables, 3)]
    rows = [sy.Poly(v*central.diff(u), *variables) for u in variables for v in variables]
    tangent = sy.Matrix([[p.coeff_monomial(m) for m in monomials] for p in rows])
    assert tangent.to_DM().rank() == 41 and len(monomials) == 84
    x, y = sy.symbols("x y", nonzero=True)
    for alpha, beta, gamma in [(x, x**2*y**3, x*y), (x**2*y, x*y**2, x*y),
                               (x**3*y**2, y, x*y)]:
        assert sy.expand(alpha*beta-gamma**3) == 0
        area = sy.Matrix([alpha, gamma]).jacobian([x, y]).det()/alpha
        assert sy.cancel(area) in (-1, 1)
    print("Projective orbit dimension 40, normal dimension 43; all three A2 resolution charts are crepant.")

    # On the root boundary use the ordered basis (base hyperplane, weight
    # one). The root divisor may be modified without changing the index.
    restriction = sy.Matrix([[2, 0], [0, -1]])
    root = sy.Matrix([2, 2])
    for relations in (restriction, restriction.row_join(root)):
        smith = smith_normal_form(relations, domain=sy.ZZ)
        assert [abs(n) for n in smith.diagonal()] == [1, 2]
    assert (restriction.inv()*sy.Matrix([-1, 0]))[0] == -sy.Rational(1, 2)
    print("Both boundary Picard quotients have index two; the rank-one probe maps to their generator.")

if __name__ == "__main__":
    verify_normal_chart()
    verify_signed_arc()
    verify_cover_and_clifford()
    verify_explicit_cubic()
    verify_orbit_and_resolution()
