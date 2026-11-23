#!/usr/bin/env python3
"""Exact checks for the deformation-connected fivefold and its rotation products."""
from itertools import combinations

import sympy as sy


def equal(left, right):
    return (left - right).applyfunc(sy.expand).is_zero_matrix


def verify_clifford_products():
    dimension = 8
    eye = sy.eye(dimension)
    zero = sy.zeros(dimension)
    period = sy.symbols("t", nonzero=True)
    x = sy.symbols("x1:4")
    u = sy.symbols("u1:4")
    wedges = []
    for index in range(3):
        bit = 1 << index
        matrix = sy.zeros(dimension)
        for mask in range(dimension):
            if not mask & bit:
                matrix[mask | bit, mask] = (-1)**((mask & (bit-1)).bit_count())
        wedges.append(matrix)
    contractions = [matrix.T for matrix in wedges]
    differential = sum((v*i + period*h*v*e for v,h,i,e in
                        zip(x, u, contractions, wedges)), sy.zeros(dimension))
    assert equal(differential**2, period*sum(h*v*v for v,h in zip(x,u))*eye)
    theta = [i-period*h*e for i,h,e in zip(contractions,u,wedges)]
    assert all(equal(differential*a+a*differential, zero) for a in theta)
    j = sy.diag(1,-1)
    k = sy.Matrix([[0,1],[1,0]])
    eta = [sy.kronecker_product(a,p) for a,p in zip(theta,(j,k,sy.I*j*k))]
    pairs = list(combinations(range(3), 2))
    for a in range(3):
        assert equal(eta[a]**2, -period*u[a]*sy.eye(16))
    for a,b in pairs:
        assert equal(eta[a]*eta[b], eta[b]*eta[a])
    z = {(a,b): -eta[a]*eta[b]/period for a,b in pairs}
    def entry(a,b):
        return z[tuple(sorted((a,b)))]
    for a,b in pairs:
        assert equal(entry(a,b)**2, u[a]*u[b]*sy.eye(16))
    for a in range(3):
        b,c = [i for i in range(3) if i != a]
        assert equal(entry(a,b)*entry(a,c), u[a]*entry(b,c))
    origin = {h:0 for h in u} | {period:1}
    evaluations = [matrix.subs(origin).reshape(256,1) for matrix in z.values()]
    assert sy.Matrix.hstack(*evaluations).rank() == 3
    print("Closed Clifford operators, six product identities, origin evaluation rank three.")


def verify_quadrics():
    u,v,w,a,b,c = variables = sy.symbols("u v w a b c")
    quadrics = [a*a-u*v, b*b-u*w, c*c-v*w,
               a*b-u*c, a*c-v*b, b*c-w*a]
    monomials = [x*y for i,x in enumerate(variables) for y in variables[i:]]
    polys = [sy.Poly(q,*variables) for q in quadrics]
    assert sy.Matrix([[p.coeff_monomial(m) for m in monomials] for p in polys]).rank() == 6
    s,t,h = sy.symbols("s t h")
    cover = dict(zip(variables,(s*s,t*t,h*h,s*t,s*h,t*h)))
    assert all(sy.expand(q.xreplace(cover)) == 0 for q in quadrics)
    jac = sy.Matrix(list(cover.values())).jacobian((s,t,h))
    assert jac.subs({s:1,t:1,h:1}).rank() == 3
    print("Six independent quadrics vanish on a three-dimensional affine Veronese cone.")


def verify_smooth_fibers():
    x,y,z,u,v,h,w = variables = sy.symbols("x y z u v h w")
    g = u**3+v**3+h**3+w**3
    f0 = u*x*x+v*y*y+h*z*z+g
    f2 = f0+2*x*y*z
    dual = u*x*x+v*y*y-h*z*z+2*x*y*z+g+u*v*h
    lam = sy.symbols("lambda", nonzero=True)
    a,b,c = sy.symbols("a b c")  # entries (12), (13), (23)
    transformed = u*x*x+v*y*y-h*z*z+lam*x*y*z+g+4*u*v*h/lam**2
    change = {x:2*sy.I*c/lam, y:-2*sy.I*b/lam, z:2*a/lam}
    determinant = sy.Matrix([[u,a,b], [a,v,c], [b,c,h]]).det()
    assert sy.expand(lam**2*transformed.xreplace(change)/4 -
                     determinant-lam**2*g/4) == 0
    for polynomial in (f0,f2,dual):
        ideal = sy.groebner([polynomial.diff(i) for i in variables],
                            *variables, order="grevlex", domain=sy.QQ)
        assert ideal.is_zero_dimensional
    print("The three endpoint equations have zero-dimensional affine gradient scheme over Q.")


if __name__ == "__main__":
    verify_clifford_products()
    verify_quadrics()
    verify_smooth_fibers()
