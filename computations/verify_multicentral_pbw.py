#!/usr/bin/env python3
"""Two-central-variable certificates for the multi-center PBW normal form.

Current result: 2026-11-22 / v59.
Run from the repository root:
    python3 computations/verify_multicentral_pbw.py
Requires Python 3 and SymPy.

This reuses the existing exact universal S(1,-1,-1) center certificate;
it does not introduce another ideal-reduction implementation.  New checks
concern a general Sklyanin translation with linear central forms, its
quadratic mixed coefficient, the Clifford obstruction in these coordinates,
and the genuine uv term of the polarized center.

The S(1,-1,-1) part keeps the imported seed's convention
    [y,z] = x^2 + p*y + r*z - a,
and its cyclic companions.  For the manuscript convention
    r_x + sum M_xj*x_j - alpha_x = 0,
its p,q,r and a,b,c are the negatives of the corresponding manuscript
coefficients.  The displayed mixed-term checks use the seed convention.

The all-m, all-degree statements, arbitrary nonreduced coefficient rings,
classification by the central ideal's associated graded, and regular
sequences are proved in multicentral_pbw.tex.  They are not inferred from
sampling rays or from this finite two-variable calculation.
"""

import sympy as sp

import verify_mixed_linear_pbw as seed


def linear_form(name, u, v):
    first, second = sp.symbols(f"{name}_u {name}_v")
    return first*u + second*v


def quadratic_form(name, u, v):
    aa, ab, bb = sp.symbols(f"{name}_uu {name}_uv {name}_vv")
    return aa*u**2 + ab*u*v + bb*v**2


def main():
    u, v = sp.symbols("u v")
    a, b, c = sp.symbols("a b c", nonzero=True)
    x = sp.symbols("X Y Z", commutative=False)
    entries = {(i, j): linear_form(f"m{i}{j}", u, v)
               for i in range(3) for j in range(i, 3)}
    matrix = sp.Matrix(3, 3, lambda i, j: entries[min(i, j), max(i, j)])
    alpha = sp.Matrix([quadratic_form(f"alpha{i}", u, v) for i in range(3)])
    shift = sp.Matrix([-matrix[i, i]/(2*c) for i in range(3)])
    sx, sy, sz = shift
    translation = sp.Matrix(((2*c*sx, (a+b)*sz, (a+b)*sy),
                             ((a+b)*sz, 2*c*sy, (a+b)*sx),
                             ((a+b)*sy, (a+b)*sx, 2*c*sz)))
    normalized = matrix + translation
    assert normalized.diagonal() == sp.zeros(1, 3)
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        constant_shift = c*shift[i]**2 + (a+b)*shift[j]*shift[k]
        new_alpha = sp.expand(alpha[i] - (matrix*shift)[i] - constant_shift)
        original = (a*(x[j]+shift[j])*(x[k]+shift[k])
                    + b*(x[k]+shift[k])*(x[j]+shift[j])
                    + c*(x[i]+shift[i])**2
                    + sum(matrix[i, l]*(x[l]+shift[l]) for l in range(3))
                    - alpha[i])
        normal = (a*x[j]*x[k] + b*x[k]*x[j] + c*x[i]**2
                  + sum(normalized[i, l]*x[l] for l in range(3)) - new_alpha)
        assert sp.expand(original - normal) == 0
        assert all(sum(monomial) == 2
                   for monomial in sp.Poly(new_alpha, u, v).monoms())
    print("PASS general Sklyanin translation, including all mixed quadratic constants")

    # At a=b=1,c=tau the old normalized obstruction is
    # (M_xx-tau*M_yz,M_yy-tau*M_xz,M_zz-tau*M_xy).
    # After zero-diagonal normalization it detects every linear form.
    tau = sp.symbols("tau", nonzero=True)
    p, q, r = (linear_form(name, u, v) for name in ("p", "q", "r"))
    essential = sp.Matrix(((0, p, r), (p, 0, q), (r, q, 0)))
    obstruction = sp.Matrix((essential[0, 0]-tau*essential[1, 2],
                              essential[1, 1]-tau*essential[0, 2],
                              essential[2, 2]-tau*essential[0, 1]))
    variables = sp.symbols("p_u p_v q_u q_v r_u r_v")
    coefficient_map = sp.Matrix([
        sp.expand(obstruction[i]).coeff(variable)
        for variable in (u, v) for i in range(3)
    ]).jacobian(variables)
    assert sp.factor(coefficient_map.det()) == -tau**6
    print("PASS Clifford obstruction detects all six normalized two-variable directions")

    # Reuse, rather than duplicate, the full ideal-membership certificate.
    omega = seed.central_cubic()
    _, _, reduce_polynomial, _ = seed.relation_reducer(4)
    for letter in seed.LETTERS:
        assert not reduce_polynomial(seed.commutator(seed.word(letter), omega))
    forms = [p, q, r] + [quadratic_form(name, u, v) for name in ("a", "b", "c")]
    substituted = {}
    for (powers, word), coefficient in omega.items():
        assert sum(weight*power for weight, power in zip(seed.WEIGHTS, powers)) + len(word) == 3
        value = sp.Rational(coefficient.numerator, coefficient.denominator)
        for form, power in zip(forms, powers):
            value *= form**power
        substituted[word] = substituted.get(word, 0) + value
    substituted = {word: sp.expand(value) for word, value in substituted.items()}
    for word, value in substituted.items():
        assert all(sum(monomial) + len(word) == 3
                   for monomial in sp.Poly(value, u, v).monoms())
    assert "" not in substituted
    print("PASS existing universal center identity and homogeneous two-variable coefficient substitution")

    pu, pv, qu, qv, ru, rv = variables
    auv, buv, cuv = sp.symbols("a_uv b_uv c_uv")
    expected_uv = {
        "x": -auv + qu*qv/3 - (pu*rv+pv*ru)/18,
        "y": -buv + ru*rv/3 - (pu*qv+pv*qu)/18,
        "z": -cuv + pu*pv/3 - (qu*rv+qv*ru)/18,
    }
    for word, value in substituted.items():
        actual = sp.Poly(value, u, v).coeff_monomial(u*v)
        assert sp.expand(actual - expected_uv.get(word, 0)) == 0
    # The off-axis term is not the sum of the u-only and v-only centers.
    assert any(sp.expand(value + correction) != 0
               for value, correction in zip(expected_uv.values(), (auv, buv, cuv)))
    print("PASS exact mixed uv polarization coefficients of the central cubic")

    print("4 PASS (exact two-variable checks; arbitrary-base and all-degree proofs are in the manuscript)")


if __name__ == "__main__":
    main()
