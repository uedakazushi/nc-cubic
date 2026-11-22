#!/usr/bin/env python3
"""Exact small certificates for the original central coefficient direction.

This verifies the commutative Knorrer homotopy, a nonzero Jacobian class,
the second moment of the existing 64 critical values, and the normal
one-variable cubic Massey certificate. It does not verify the whole
noncommutative comparison kernel or its higher coherences.
"""
import sympy as sp

from verify_mixed_center_geometry import EXAMPLES


def main():
    a, b, r, s, t, ell, v, tau = sp.symbols("a b r s t ell v tau")
    ys = (a, b, r, s, t)
    linear = 4*a+9*b+1600*r+2500*s+4900*t
    g = (-linear**3+a**3+b**3-linear*a*b)/3
    g += 100*(r**3+s**3+t**3+r*s*t)/3
    q0 = linear**2+a*b/3
    q = q0-linear*ell+ell**2/3
    x = ell-linear
    G = (x**3+a**3+b**3+x*a*b)/3
    G += 100*(r**3+s**3+t**3+r*s*t)/3
    assert sp.expand(G-g-ell*q) == 0
    assert sp.expand((G-v*ell).subs(v, tau+q)-(g-ell*tau)) == 0
    print("PASS exact Knorrer coordinate identity G-vL = g-ell*tau")

    d = sp.Matrix([[0, ell], [-tau, 0]])
    q1 = -linear+ell/3
    h = -d.diff(ell)-q1*d.diff(tau)
    assert d*d == -ell*tau*sp.eye(2)
    residual = d*h+h*d-(tau+q-q0)*sp.eye(2)
    assert residual.applyfunc(sp.expand) == sp.zeros(2)
    print("PASS explicit homotopy from multiplication v to the normal quadric")

    rows = (a*a, a*b, a*r, r*r, r*s, r*t)
    polynomials = [sp.diff(g, y) for y in ys]+[q0]
    certificate = sp.Matrix([
        [sp.Poly(f, *ys).coeff_monomial(m) for f in polynomials]
        for m in rows
    ])
    determinant = certificate.det()
    assert determinant == -sp.Rational(11200000000, 9)
    print("PASS nonzero degree-two Jacobian class; 6x6 determinant =", determinant)

    w = sp.Symbol("w")
    spectra = [sp.Poly.from_list(item[3], w).monic() for item in EXAMPLES]
    lambda2 = sp.Rational(28, 27)
    a1, a2 = sp.Rational(88490, 63), sp.Rational(5343910, 21)
    assert spectra[0].nth(3) == -lambda2*a1
    assert spectra[1].nth(3) == -lambda2*a2
    second_moment = -16*(spectra[0].nth(3)+10000*spectra[1].nth(3))
    assert second_moment == sp.Rational(10260312863360, 243)
    assert -second_moment/2 == -sp.Rational(5130156431680, 243)
    print("PASS nonzero second moment of P64 roots =", second_moment)
    print("PASS monic P64 coefficient c^62 =", -second_moment/2)

    u, c = sp.symbols("u c")
    # Even/odd basis order agrees with central_formal_comparison.tex:
    # the odd-to-even component u has cokernel supported on u=0.
    d_normal = sp.Matrix([[0, u], [c*u*u, 0]])
    theta = sp.Matrix([[0, 1], [-c*u, 0]])
    h_normal = sp.Matrix([[0, 0], [-c, 0]])
    assert d_normal*d_normal == c*u**3*sp.eye(2)
    assert d_normal*theta+theta*d_normal == sp.zeros(2)
    assert theta*theta == -c*u*sp.eye(2)
    assert d_normal*h_normal+h_normal*d_normal == theta*theta
    assert theta*h_normal+h_normal*theta == -c*sp.eye(2)
    print("PASS cubic normal factor: closed theta, theta^2 nullhomotopy, Massey scalar -c")

    # A polynomial of weight three in six weight-two alpha variables and
    # one weight-three c variable is a scalar multiple of c.
    from itertools import product
    weighted_monomials = [
        e for e in product(range(2), repeat=7)
        if 2*sum(e[:6])+3*e[6] == 3
    ]
    assert weighted_monomials == [(0, 0, 0, 0, 0, 0, 1)]
    print("PASS the unique weight-three parameter monomial is c")
    print("Verified 7 exact certificates; no whole categorical equivalence is inferred.")


if __name__ == "__main__":
    main()
