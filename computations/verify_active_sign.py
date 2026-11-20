#!/usr/bin/env python3
"""Exact Hesse-group identities used in the active sign argument.

The calculation is over QQ(zeta)/(zeta^2+zeta+1), with symbolic p,q.
It checks the finite group and field-degree certificate.  It does not
prove the categorical specialization or the all-dimensional witness.
"""

import sympy as sp


p, q, zeta = sp.symbols("p q zeta")
minimal_polynomial = sp.Poly(zeta**2 + zeta + 1, zeta)


def reduce_coefficient(expression):
    return sp.rem(
        sp.Poly(sp.expand(expression), zeta), minimal_polynomial
    ).as_expr().expand()


def reduce_matrix(matrix):
    return matrix.applyfunc(reduce_coefficient)


def invariants(first, second):
    return (
        second * (second**3 - 8 * first**3),
        second**6 + 20 * first**3 * second**3 - 8 * first**6,
    )


def main():
    # (zeta^2-zeta)^(-1) = (1+2*zeta)/3.
    inverse_sqrt_minus_three = (1 + 2 * zeta) / 3
    a = sp.diag(zeta, 1)
    a_inverse = sp.diag(zeta**2, 1)
    b = inverse_sqrt_minus_three * sp.Matrix([[1, 1], [2, -1]])
    c = reduce_matrix(a * b * a_inverse)
    d = reduce_matrix(a_inverse * b * a)
    identity = sp.eye(2)
    zero = sp.zeros(2)

    s, t = invariants(p, q)
    for matrix in (a, b):
        first, second = matrix * sp.Matrix([p, q])
        assert all(
            reduce_coefficient(new - old) == 0
            for new, old in zip(invariants(first, second), (s, t))
        )
    print("PASS: both generators preserve c4 and -c6 exactly")

    for relation in (
        a**3 - identity,
        b**2 + identity,
        c**2 + identity,
        d**2 + identity,
        b * c - d,
        c * b + d,
        a * c * a_inverse - d,
        a * d * a_inverse - b,
        (a * b)**3 + identity,
    ):
        assert reduce_matrix(relation) == zero
    print("PASS: quaternion relations, C3 conjugation, and (AB)^3=B^2")

    quaternion = [identity, -identity, b, -b, c, -c, d, -d]
    group = [reduce_matrix(element * a**j)
             for element in quaternion for j in range(3)]
    keys = {tuple(element) for element in group}
    assert len(keys) == 24
    assert all(tuple(reduce_matrix(x * y)) in keys for x in group for y in group)
    print("PASS: the displayed matrices form a group of order 24")

    u = q**2
    assert sp.expand(27 * u**4 - 18 * s * u**2 - 8 * t * u - s**2) == 0
    assert sp.expand(8 * p**3 * q - q**4 + s) == 0
    print("PASS: quartic and cubic identities give the field-degree bound 24")

    # The two elementary relations force every sign character to be trivial.
    characters = [(alpha, beta) for alpha in (-1, 1) for beta in (-1, 1)
                  if alpha**3 == 1 and (alpha * beta)**3 == beta**2]
    assert characters == [(1, 1)]
    print("PASS: the Hesse group has no nontrivial character to mu2")

    # The smoothness proof for F_* reduces to these two nonzero integers,
    # for k the number of central coordinates taking the value -2.
    k = sp.symbols("k", integer=True, nonnegative=True)
    assert (1 + 4 * k).is_positive is True
    assert (2 + 4 * k).is_positive is True
    print("PASS: both branches of the uniform smoothness argument are nonzero")
    print("All active-sign finite identities verified over exact coefficients.")


if __name__ == "__main__":
    main()
