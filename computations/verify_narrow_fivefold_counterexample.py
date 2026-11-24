#!/usr/bin/env python3
"""Exact checks for the deformation-connected fivefold and its rotation products."""
from itertools import combinations, combinations_with_replacement

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


def invariant_jacobian_piece(polynomial, variables, signs, active_count, degree):
    """Ranks of the invariant quotient, central products, and odd active part."""
    def products(size):
        return list(combinations_with_replacement(range(len(variables)), size))

    indices = []
    for factors in products(degree):
        character = 0
        for index in factors:
            character ^= signs[index]
        if character == 0:
            indices.append(factors)
    monomials = [sy.prod(variables[i] for i in factors) for factors in indices]
    relations = []
    if degree >= 2:
        for i, variable in enumerate(variables):
            for factors in products(degree-2):
                character = signs[i]
                for j in factors:
                    character ^= signs[j]
                if character == 0:
                    poly = sy.Poly(polynomial.diff(variable) *
                                   sy.prod(variables[j] for j in factors), *variables)
                    relations.append([poly.coeff_monomial(m) for m in monomials])
    ideal = sy.Matrix(relations) if relations else sy.zeros(0, len(indices))
    standard = sy.eye(len(indices))
    central = [j for j, factors in enumerate(indices)
               if all(i >= active_count for i in factors)]
    odd = [j for j, factors in enumerate(indices)
           if sum(i < active_count for i in factors) % 2]

    def image_dimension(rows):
        return ideal.col_join(standard[rows, :]).rank() - ideal.rank()

    return len(indices)-ideal.rank(), image_dimension(central), image_dimension(odd)


def verify_sector_triple_products():
    active = sy.symbols("x1:4")
    central = sy.symbols("u1:4") + (sy.Symbol("w"),)
    cubic = sum(v**3 for v in central)
    products = sum(u*x**2 for u,x in zip(central, active))
    for parameter, expected_rank in ((0, 34), (2, 35)):
        polynomial = cubic + products + parameter*sy.prod(active)
        ranks = {}
        for degree in (1,3):
            ranks[degree] = [
                invariant_jacobian_piece(polynomial, active+central,
                                         (1,2,3,0,0,0,0), 3, degree)]
            for i, x in enumerate(active):
                fixed = cubic + central[i]*x**2
                # After the determinant and multiplier characters cancel,
                # each moving pair contributes fixed degree degree-1.
                ranks[degree].append(invariant_jacobian_piece(
                    fixed, (x,)+central, (i+1,0,0,0,0), 1, degree-1))
        assert sum(dim for dim, _, _ in ranks[1]) == 7
        assert sum(dim for dim, _, _ in ranks[3]) == 35
        assert sum(span for _, span, _ in ranks[3]) == expected_rank
        if parameter == 0:
            assert all(odd == 0 for _, _, odd in ranks[1])
            assert [odd for _, _, odd in ranks[3]] == [1, 0, 0, 0]
        print(f"b={parameter}: four Jacobian sectors, triple product rank {expected_rank}/35.")


def verify_sector_hilbert_series():
    """Average traces of the gradient Koszul resolution on each fixed space."""
    z = sy.symbols("z")
    total = 0
    for sector in range(4):
        # Nonzero characters label the three active coordinates.
        fixed = [0] * 4 + [c for c in range(1, 4)
                            if (c & sector).bit_count() % 2 == 0]
        for element in range(4):
            signs = [(-1) ** ((c & element).bit_count() % 2) for c in fixed]
            trace = sy.prod((1 - sign*z**2)/(1 - sign*z) for sign in signs)
            total += trace * (z if sector else 1) / 4
    assert sy.cancel(total - (1 + z)**7) == 0
    print("All four averaged sector series sum to (1+z)^7.")


if __name__ == "__main__":
    verify_clifford_products()
    verify_quadrics()
    verify_smooth_fibers()
    verify_sector_triple_products()
    verify_sector_hilbert_series()
