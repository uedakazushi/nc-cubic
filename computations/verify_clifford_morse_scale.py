#!/usr/bin/env python3
"""Exact finite checks for the Clifford/Hesse critical comparison (v65).

Python 3 + SymPy; rational polynomial and quotient-algebra arithmetic only.
The script checks the adjugate identities, two invariant moment coefficients,
a nondegenerate example, and the calibrated mixed cubes. It does not certify
Azumaya descent, categorical comparison, coherence, or any formal proof.
"""

from itertools import product

import sympy as sp


def zero(expr):
    assert sp.cancel(expr) == 0, sp.factor(expr)


def matrix_zero(mat):
    for entry in mat:
        zero(entry)


def critical_matrix(potential, observable, variables, domain):
    """Multiplication by observable in the full finite gradient quotient."""
    groebner = sp.groebner(
        [sp.diff(potential, z) for z in variables],
        *variables, order="grevlex", domain=domain,
    )
    leading = [p.LM(order=groebner.order).exponents for p in groebner.polys]
    bounds = []
    for i in range(len(variables)):
        bounds.append(min(e[i] for e in leading
                          if e[i] and all(e[j] == 0 for j in range(len(e)) if j != i)))
    exponents = [e for e in product(*(range(b) for b in bounds))
                 if not any(all(e[i] >= a[i] for i in range(len(e))) for a in leading)]
    assert len(exponents) == 8
    basis = [sp.prod(z**n for z, n in zip(variables, e)) for e in exponents]
    columns = []
    for monomial in basis:
        remainder = sp.Poly(groebner.reduce(sp.expand(observable * monomial))[1], *variables)
        columns.append(sp.Matrix([remainder.coeff_monomial(m) for m in basis]))
    return sp.Matrix.hstack(*columns)


def main():
    tau = sp.symbols("tau", nonzero=True)
    x = sp.symbols("x1 x2 x3")
    f = tau * sum(z**3 for z in x) - (2 + tau**3) * sp.prod(x)
    h = sp.Matrix([[tau*x[0], x[2], x[1]],
                   [x[2], tau*x[1], x[0]],
                   [x[1], x[0], tau*x[2]]])
    q = -h.adjugate()
    omega = -f
    zero(h.det() + f)
    zero(q.det() + omega**2)
    matrix_zero(q.adjugate() - omega*h)
    matrix_zero(h.adjugate().adjugate() - h.det()*h)
    print("PASS 1: determinant and adjugate identities over Q[tau,x].")

    alpha = [sp.diff(f, z) for z in x]
    for a in range(3):
        b, c = (a+1) % 3, (a+2) % 3
        zero(q[a, a] - (x[a]**2 - tau**2*x[b]*x[c]))
        zero(2*q[b, c] + tau*q[a, a] - alpha[a])
        zero(q.adjugate()[a, a] - tau*q.adjugate()[b, c])
    critical_value = f - sum(alpha[i]*x[i] for i in range(3))
    zero(critical_value - 2*omega)
    zero(2*(1-tau**3)*omega - (1-tau**3)*critical_value)
    print("PASS 2: inverse critical map, gradient projection, exact value scaling.")

    a_coef = 8*(tau**9 + 6*tau**6 - 96*tau**3 + 8)/(27*tau*(tau**3+8))
    b_coef = -16*(tau**3+2)**2/(tau**3+8)
    moment_values = []
    for linear in (x[0], sum(x)):
        potential = f - linear
        mat = critical_matrix(potential, potential**2, x, sp.QQ.frac_field(tau))
        moment_values.append(sp.factor(sp.trace(mat)))
    zero(moment_values[0] - a_coef/(tau**3-1)**2)
    zero(moment_values[1] - (3*a_coef+b_coef)/(tau**3-1)**2)
    print("PASS 3: both invariant Hesse second-moment coefficients in the full rank-8 quotients.")

    num_a = sp.fraction(sp.factor(a_coef))[0]
    num_b = sp.fraction(sp.factor(b_coef))[0]
    assert sp.degree(sp.gcd(num_a, num_b), tau) == 0
    print("PASS 4: the two moment coefficients have no simultaneous zero on the allowed tau-open.")

    # A separate exact example checks the central critical algebra directly.
    big_x = sp.symbols("X1 X2 X3")
    parameters = (sp.Integer(1), sp.Integer(2), sp.Integer(3))
    p = [parameters[i]-2*big_x[i] for i in range(3)]
    determinant = sp.expand(sp.prod(big_x) + sp.prod(p)/4
                            - sum(big_x[i]*p[i]**2/4 for i in range(3)))
    det_matrix = critical_matrix(determinant, determinant, big_x, sp.QQ)
    z = sp.symbols("z")
    expected = (756142128*z**4 - 1069915392*z**3 - 672757191*z**2
                - 80682966*z - 2798978)/sp.Integer(756142128)
    zero(det_matrix.charpoly(z).as_expr() - z**4*expected)
    assert expected.subs(z, 0) != 0
    assert sp.discriminant(expected, z) != 0
    omega_polynomial = sp.expand((-196)**4 * expected.subs(z, z**2/(-196)))
    assert sp.gcd(sp.Poly(omega_polynomial, z), sp.Poly(sp.diff(omega_polynomial, z), z)).degree() == 0
    print("PASS 5: four nonzero central critical values and eight distinct volume values at tau=2.")

    specialized = sp.expand(f.subs(tau, 2) - sum(parameters[i]*x[i] for i in range(3)))
    value_matrix = critical_matrix(specialized, specialized, x, sp.QQ)
    zero(omega_polynomial - sp.expand((-7)**8 * value_matrix.charpoly(z).as_expr().subs(z, z/(-7))))
    print("PASS 6: the complete degree-8 critical polynomials match the exact factor 1-tau^3.")

    t1, t2, a1, a2, theta = sp.symbols("t1 t2 a1 a2 theta", nonzero=True)
    d1, d2 = t1**3-1, t2**3-1
    k12 = 2*a1*d1/(3*t2*theta)
    k21 = 2*a2*d2*theta/(3*t1)
    theta_rule = sp.Poly(theta**3-d1/d2, theta, domain=sp.QQ.frac_field(t1,t2,a1,a2))

    def zero_on_cover(expr):
        numerator = sp.fraction(sp.cancel(expr))[0]
        remainder = sp.Poly(numerator, theta, domain=sp.QQ.frac_field(t1,t2,a1,a2)).rem(theta_rule)
        assert remainder.is_zero

    zero(k12*k21 - 4*a1*a2*d1*d2/(9*t1*t2))
    zero_on_cover(k12**3 - 8*a1**3*d1**2*d2/(27*t2**3))
    zero_on_cover(k21**3 - 8*a2**3*d2**2*d1/(27*t1**3))
    zero_on_cover(a2*t2*k12/(a1*t1*k21) - theta)
    print("PASS 7: mixed cubes, exact product, and the degree-3 Kummer parameter.")

    # The zero at t1=1 has order one; the remaining factors are units there.
    numerator, denominator = sp.fraction(sp.cancel(d1/d2))
    assert numerator.subs(t1,1) == 0 and sp.diff(numerator,t1).subs(t1,1) != 0
    assert denominator.subs(t1,1) != 0
    zero(k12.subs({t2:t1,a2:a1,theta:1}) - 2*a1*d1/(3*t1))
    zero(k21.subs({t2:t1,a2:a1,theta:1}) - 2*a1*d1/(3*t1))
    print("PASS 8: valuation-one obstruction and the symmetric normalized specialization.")
    print("8 PASS. LIMIT: finite identities only; categorical arguments are in the manuscript.")


if __name__ == "__main__":
    main()
