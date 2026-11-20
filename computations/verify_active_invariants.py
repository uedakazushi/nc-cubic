#!/usr/bin/env python3
"""Exact active-invariant identities for nc-cubic-n-fold, v12 (2026-11-20).

Run from the repository root:
    python computations/verify_active_invariants.py

Conventions: g=p(x^3+y^3+z^3)/3+qxyz, S=c4(g), T=-c6(g),
and phi(g)=g+det(Hess(g))/24. Fisher's ternary invariants use
S=q(q^3-8p^3), T=q^6+20p^3q^3-8p^6.

The rational polynomial identities below are checked coefficient by
coefficient, without numerical specialization. They certify the formulas
used in the manuscript's degree-nine invariant map. Geometric generic
integrality, opposite invariance, and degree 18e_n use the written proofs.
"""

import sympy as sp


def zero_polynomial(expression, variables):
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    assert polynomial.is_zero, polynomial


def main():
    p, q, S, T = sp.symbols("p q S T")
    ration = sp.Rational
    s = q * (q**3 - 8 * p**3)
    t = q**6 + 20 * p**3 * q**3 - 8 * p**6
    p_new = p * (1 - q**2 / 4)
    q_new = q + p**3 / 3 + q**3 / 12
    a4 = (S + T / 3 + S**2 / 24 + S*T / 432
          - S**3 / 6912 + T**2 / 5184)
    a6_minus = (T + S**2 / 2 + 5*S*T / 48 + 5*T**2 / 432
               + 5*S**2*T / 6912 + S**4 / 13824
               + S**3*T / 331776 - S*T**2 / 20736
               - T**3 / 373248)
    discriminant_ratio = 1 - S / 24 - T / 216 - S**2 / 6912

    zero_polynomial(
        sp.Matrix([s, t]).jacobian([p, q]).det()
        + 384*p**2*(p**3+q**3)**2, (p, q))
    print("PASS: dominant Hesse invariant map, det Dr=-384 p^2(p^3+q^3)^2")

    for target, formula in ((s, a4), (t, a6_minus)):
        zero_polynomial(
            target.subs({p: p_new, q: q_new}, simultaneous=True)
            - formula.subs({S: s, T: t}, simultaneous=True), (p, q))
    print("PASS: r o psi = a o r, both invariant coordinates")

    zero_polynomial(
        a4**3-a6_minus**2-(S**3-T**2)*discriminant_ratio**3,
        (S, T))
    print("PASS: discriminant identity (a4^3-a6minus^2)=(S^3-T^2)D^3")

    zero_polynomial(
        sp.Matrix([a4, a6_minus]).jacobian([S, T]).det()
        - (1-S/16)*discriminant_ratio**2, (S, T))
    zero_polynomial(
        sp.Matrix([p_new, q_new]).jacobian([p, q]).det()
        - (1-s/16), (p, q))
    print("PASS: Jacobian identities det Da=(1-S/16)D^2, det Dpsi=1-s/16")

    zero_polynomial(s.subs({p: -p, q: -q}, simultaneous=True)-s, (p, q))
    zero_polynomial(t.subs({p: -p, q: -q}, simultaneous=True)-t, (p, q))
    print("PASS: both primitive invariants are unchanged by the opposite sign")

    # The exact Fermat specialization fixes the sign convention c6=-T.
    assert (s.subs({p: 1, q: 0}), t.subs({p: 1, q: 0})) == (0, -8)
    assert a4.subs({S: 0, T: -8}) == -ration(215, 81)
    print("All identities verified over QQ; no sampling or formal proof assistant used.")


if __name__ == "__main__":
    main()
