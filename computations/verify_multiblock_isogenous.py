#!/usr/bin/env python3
"""Exact checks for the isogenous-factor and three-plane lattice arguments.

This checks finite integer/polynomial identities: the Orlov-coordinate
matrices, the annihilator used for k>=3, mixed isometries for k=2, and the
three-plane Mukai lattice.  It does not prove Orlov surjectivity, existence
or descent of Fourier--Mukai kernels, higher coherence, or the geometric
realization/sphericity of the three-plane classes.

The weighted form models an isogeny u of degree d by u=d, u^dagger=1 after
rational identification via u^dagger; the second principal polarization
then has weight d.

Run: python3 computations/verify_multiblock_isogenous.py
Dependency: sympy.
"""

from math import isqrt

import sympy as sp


def pell_solution(discriminant: int) -> tuple[int, int]:
    """Find a positive norm-one solution using continued fractions."""
    root = isqrt(discriminant)
    assert root * root != discriminant and discriminant > 0
    m, denominator, partial = 0, 1, root
    numerator_prev, numerator = 1, partial
    denominator_prev, denominator_cf = 0, 1
    while numerator * numerator - discriminant * denominator_cf**2 != 1:
        m = denominator * partial - m
        denominator = (discriminant - m * m) // denominator
        partial = (root + m) // denominator
        numerator_prev, numerator = numerator, partial * numerator + numerator_prev
        denominator_prev, denominator_cf = (
            denominator_cf,
            partial * denominator_cf + denominator_prev,
        )
    return numerator, denominator_cf


def main() -> None:
    identity = sp.eye(2)
    zero = sp.zeros(2)
    j = sp.Matrix([[0, 1], [-1, 0]])
    fourier = sp.Matrix([[0, -1], [1, 0]])
    degree_one = sp.Matrix([[1, 0], [1, 1]])
    degree_three = sp.Matrix([[1, 0], [3, 1]])
    twist_o = fourier * degree_one * fourier.inv()
    r = twist_o * degree_three
    assert r == sp.Matrix([[-2, -1], [3, 1]])
    assert r**2 + r + identity == zero
    assert (r - identity) * (r + 2 * identity) == -3 * identity
    assert r.T * j * r == j
    print("PASS: Orlov rotation, order three, and integral block annihilator")

    reflection = sp.Matrix([[-1, -1], [0, 1]])
    blocks = {1: reflection, 3: reflection * (r - r.inv())}
    q = sp.diag(r.inv(), r)
    d, a, b = sp.symbols("d a b", real=True)
    weighted_j = sp.diag(j, d * j)
    for norm, block in blocks.items():
        assert r.inv() * block == block * r
        assert r * block == block * r.inv()
        assert j.inv() * block.T * j == -block
        assert block**2 == norm * identity
        n = zero.row_join(d * block).col_join(block.row_join(zero))
        assert n * q == q * n
        assert n**2 == d * norm * sp.eye(4)
        assert n.T * weighted_j + weighted_j * n == sp.zeros(4)
        g = a * sp.eye(4) + b * n
        difference = (
            g.T * weighted_j * g
            - (a**2 - d * norm * b**2) * weighted_j
        )
        assert difference.applyfunc(sp.expand) == sp.zeros(4)
    print("PASS: symbolic Rosati/isometry identities for both norms 1 and 3")

    for degree in (1, 2, 3, 4, 5, 9, 12, 16, 97):
        norm = 3 if isqrt(degree) ** 2 == degree else 1
        discriminant = degree * norm
        pell_a, pell_b = pell_solution(discriminant)
        assert pell_a > 1 and pell_b > 0
        assert pell_a**2 - discriminant * pell_b**2 == 1
        block = blocks[norm]
        n = zero.row_join(degree * block).col_join(block.row_join(zero))
        g = pell_a * sp.eye(4) + pell_b * n
        assert g * q == q * g
        form = sp.diag(j, degree * j)
        assert g.T * form * g == form
        assert g * (pell_a * sp.eye(4) - pell_b * n) == sp.eye(4)
        assert g[:2, 2:] != zero and g[2:, :2] != zero
    print("PASS: exact Pell examples for square and nonsquare isogeny degrees")

    # A second mixed example at equal factors: a nontrivial unipotent.
    t = r.inv() - r
    unipotent = (identity + t).row_join(-t * reflection).col_join(
        (reflection * t).row_join(reflection * (identity - t) * reflection)
    )
    assert unipotent != sp.eye(4)
    assert (unipotent - sp.eye(4)) ** 2 == sp.zeros(4)
    assert unipotent * q == q * unipotent
    assert unipotent.T * sp.diag(j, j) * unipotent == sp.diag(j, j)
    print("PASS: independent mixed unipotent example for equal factors")

    # A degree-two isogeny can also yield an H-inverting normalizer.
    # In coordinates via phi:E1->E2, phi=1 and phi^dagger=2.
    reflection_inverting = sp.Matrix([[1, 0], [-3, -1]])
    assert reflection_inverting**2 == identity
    assert reflection_inverting * r == r.inv() * reflection_inverting
    normalizer = reflection_inverting.row_join(2 * identity).col_join(
        identity.row_join(reflection_inverting)
    )
    normalizer_inverse = (-reflection_inverting).row_join(2 * identity).col_join(
        identity.row_join(-reflection_inverting)
    )
    q_inverse_order = sp.diag(r, r.inv())
    degree_two_form = sp.diag(j, 2 * j)
    assert normalizer * normalizer_inverse == sp.eye(4)
    assert normalizer.T * degree_two_form * normalizer == degree_two_form
    assert normalizer * q_inverse_order == q_inverse_order.inv() * normalizer
    print("PASS: degree-two isogeny example inverting the cyclic action")

    # Three classes with <delta_i,delta_i>=-2 and off-diagonal pairing 2.
    gram = 2 * sp.ones(3) - 4 * sp.eye(3)
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    e0, e1 = sp.eye(3)[:, 0], sp.eye(3)[:, 1]
    reflection0 = sp.eye(3) + e0 * (e0.T * gram)
    reflection1 = sp.eye(3) + e1 * (e1.T * gram)
    assert gram.det() == 32
    assert cycle**3 == sp.eye(3)
    assert cycle.T * gram * cycle == gram
    for reflection_i in (reflection0, reflection1):
        assert reflection_i**2 == sp.eye(3)
        assert reflection_i.T * gram * reflection_i == gram
    conjugate = reflection0 * cycle * reflection0
    assert conjugate != cycle and conjugate != cycle.inv()
    assert conjugate * e0 == -2 * e0 - e1
    print("PASS: three-plane Gram determinant and non-normality witness")

    product = reflection0 * reflection1
    nilpotent = product - sp.eye(3)
    assert nilpotent**3 == sp.zeros(3)
    exponent = sp.symbols("m", integer=True)
    power = (
        sp.eye(3)
        + exponent * nilpotent
        + exponent * (exponent - 1) * nilpotent**2 / 2
    )
    fixed_vector = sp.ones(3, 1)
    assert (power * fixed_vector).applyfunc(sp.expand) == sp.Matrix(
        [1 + 4 * exponent**2 + 2 * exponent,
         1 + 4 * exponent**2 - 2 * exponent,
         1]
    )
    assert (
        product * power - power.subs(exponent, exponent + 1)
    ).applyfunc(sp.expand) == sp.zeros(3)
    assert sp.solve(
        [4 * exponent**2 + 2 * exponent,
         4 * exponent**2 - 2 * exponent],
        [exponent],
    ) == [(0,)]
    print("PASS: unipotent reflection product and distinct conjugate-subgroup test")
    print(f"All exact identities passed (SymPy {sp.__version__}).")


if __name__ == "__main__":
    main()
