#!/usr/bin/env python3
"""Exact critical spectra of the commutative candidate for the mixed family.

Run from any directory with Python 3 and SymPy. The sibling centre checker
supplies the already verified fixed quartics; its expensive PBW computation
is not repeated here. This script constructs the commutative Jacobi algebras
and all multiplication matrices over QQ, without numerical root matching.
It verifies a discriminant and local-singularity comparison, not a Ku
equivalence or the classification of all Poisson tensors.
"""
from hashlib import sha256
from itertools import product

import sympy as sp

from verify_mixed_center_geometry import EXAMPLES


X = sp.symbols("x y z")
T, W, C = sp.symbols("t W c")
SCALE_SQUARED = sp.Rational(28, 27)
RESULTANT_HASH = (
    "20923491b92e21c3fceb0b30b0f331e500d83f898f756d0cb853ace75de42dbb"
)


def monomial(exponents):
    return sp.prod(v**e for v, e in zip(X, exponents))


def jacobi_matrices(alpha):
    x, y, z = X
    potential = (x**3+y**3+z**3+x*y*z)/3-sum(
        a*v for a, v in zip(alpha, X))
    gradient = [sp.diff(potential, v) for v in X]
    basis_gb = sp.groebner(gradient, *X, order="grevlex", domain=sp.QQ)
    leading = [p.LM(order=basis_gb.order).exponents for p in basis_gb.polys]
    # The pure leading powers give rigorous finite bounds for every standard
    # monomial. This is not a truncated search for a quotient basis.
    bounds = []
    for j in range(3):
        pure = [e[j] for e in leading if e[j] and
                all(e[k] == 0 for k in range(3) if k != j)]
        assert pure, "Jacobi algebra is not certified zero dimensional"
        bounds.append(min(pure))
    basis = sorted((e for e in product(*(range(b) for b in bounds))
                    if not any(all(a >= b for a, b in zip(e, lead))
                               for lead in leading)),
                   key=lambda e: (sum(e), e))
    assert len(basis) == 8
    positions = {e: i for i, e in enumerate(basis)}

    def multiplication(polynomial):
        matrix = sp.zeros(8)
        for j, e in enumerate(basis):
            remainder = basis_gb.reduce(sp.expand(polynomial*monomial(e)))[1]
            for exponent, coefficient in sp.Poly(remainder, *X).terms():
                if coefficient:
                    matrix[positions[exponent], j] = coefficient
        return matrix

    assert all(multiplication(g) == sp.zeros(8) for g in gradient)
    print("  PASS: the exact Jacobi quotient has dimension eight")
    hessian = sp.det(sp.hessian(potential, X))
    assert multiplication(hessian).det() != 0
    spectrum = sp.Poly(multiplication(potential).charpoly(T).as_expr(), T)
    assert spectrum.degree() == 8
    assert sp.gcd(spectrum, spectrum.diff()).degree() == 0
    assert all(e[0] % 2 == 0 for e, _ in spectrum.terms())
    print("  PASS: eight distinct critical values and invertible Hessian")
    # lambda^8 H(t/lambda), using lambda^2=28/27, stays over QQ.
    scaled = sp.Poly(sum(coefficient*SCALE_SQUARED**((8-e[0])//2)*T**e[0]
                         for e, coefficient in spectrum.terms()), T)
    return spectrum, scaled


def main():
    spectra = []
    for alpha, _, _, coefficients in EXAMPLES:
        print("alpha =", alpha)
        spectrum, scaled = jacobi_matrices(alpha)
        target = sp.Poly.from_list(coefficients, W)
        assert sp.expand(scaled.as_expr()-target.as_expr().subs(W, T**2)
                         /target.LC()) == 0
        spectra.append(scaled)
        print("  PASS: lambda-scaled critical spectrum equals Q(t^2)/3^17")
        print("  unscaled spectrum =", spectrum.as_expr())

    z = sp.Symbol("s")
    resultant = sp.resultant(spectra[0].as_expr().subs(T, -C-100*z),
                            spectra[1].as_expr().subs(T, z), z)
    polynomial = sp.Poly(resultant, C).clear_denoms()[1].primitive()[1]
    if polynomial.LC() < 0:
        polynomial = -polynomial
    assert polynomial.degree() == 64
    assert sp.gcd(polynomial, polynomial.diff()).degree() == 0
    canonical = ",".join(map(str, polynomial.all_coeffs())).encode("ascii")
    assert sha256(canonical).hexdigest() == RESULTANT_HASH
    print("PASS: the candidate's degree-64 discriminant is the existing P64")

    # A rational coefficient giving the reduced point-scheme obstruction.
    coefficient = -44828
    points = [(-1, -2, -3), (-4, -5, -7)]
    values = []
    for (alpha, _, _, _), point in zip(EXAMPLES, points):
        assert tuple(a*a for a in point) == alpha
        x, y, z = point
        omega = sp.Rational(x**3+y**3+z**3, 3)-sp.Rational(2*x*y*z, 3)
        omega -= sum(a*b for a, b in zip(alpha, point))
        values.append(omega)
    assert values == [28, 448]
    assert values[0]+100*values[1]+coefficient == 0
    assert polynomial.eval(coefficient) != 0
    first = [sign*a for sign in (-1, 1)
             for a in (28, 16, sp.Rational(56, 3), sp.Rational(28, 3))]
    second = [sign*a for sign in (-1, 1)
              for a in (448, 196, 176, sp.Rational(284, 3))]
    roots = [-a-100*b for a in first for b in second]
    assert len(set(roots)) == 64 and coefficient in roots
    assert all(polynomial.eval(c) != 0 for c in roots)
    assert polynomial.eval(0) != 0
    print("PASS: c=0 and all 64 norm roots avoid the common discriminant")
    print("PASS: c=-44828 has the displayed unique stationary character")
    print("P64 SHA256:", RESULTANT_HASH)


if __name__ == "__main__":
    main()
