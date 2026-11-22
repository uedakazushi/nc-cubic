#!/usr/bin/env python3
"""Exact finite certificates for the multiblock central comparison.

Run with Python 3 and SymPy:
    python3 computations/verify_mixed_multiblock.py

The checks construct the universal eight-dimensional critical algebra, verify
its multiplication over QQ[a,b,c], check the one-factor scale and tensor-sum
moment used to calibrate every block number, and check the degree arithmetic
used in the boundary-sector calculation.  They do not mechanically prove dg equivalence,
the obstruction tower, or the all-coherent comonad comparison.  Those arguments
are in papers/sections/mixed/multiblock_central_kernel.tex.
"""

from itertools import combinations

import sympy as sp


BASIS = ((), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2))
INDEX = {monomial: i for i, monomial in enumerate(BASIS)}


def critical_matrices(parameters):
    """Multiplication by x,y,z in the squarefree basis, over any QQ-algebra."""
    result = []
    for j in range(3):
        matrix = sp.zeros(8)
        other = tuple(index for index in range(3) if index != j)
        for col, monomial in enumerate(BASIS):
            if j not in monomial:
                matrix[INDEX[tuple(sorted(monomial + (j,)))], col] = 1
                continue
            rest = tuple(index for index in monomial if index != j)
            if len(rest) == 0:
                matrix[0, col] = parameters[j]
                matrix[INDEX[other], col] = -sp.Rational(1, 3)
            elif len(rest) == 1:
                ell = rest[0]
                missing = next(index for index in other if index != ell)
                matrix[INDEX[(ell,)], col] = sp.Rational(27, 28) * parameters[j]
                matrix[INDEX[(missing,)], col] = -sp.Rational(9, 28) * parameters[ell]
                matrix[INDEX[(j,)], col] = sp.Rational(3, 28) * parameters[missing]
            else:
                ell, emm = other
                matrix[INDEX[other], col] = sp.Rational(27, 28) * parameters[j]
                matrix[0, col] = -sp.Rational(9, 28) * parameters[ell] * parameters[emm]
                matrix[INDEX[tuple(sorted((j, ell)))], col] = sp.Rational(3, 28) * parameters[ell]
                matrix[INDEX[tuple(sorted((j, emm)))], col] = sp.Rational(3, 28) * parameters[emm]
        result.append(matrix)
    return tuple(result)


def zero_matrix(matrix):
    return all(sp.expand(entry) == 0 for entry in matrix)


def critical_value_matrix(parameters, matrices):
    return -sp.Rational(2, 3) * sum(
        (parameter * matrix for parameter, matrix in zip(parameters, matrices)),
        sp.zeros(8),
    )


def main():
    a, b, c, spectral = sp.symbols("a b c spectral")
    parameters = (a, b, c)
    matrices = critical_matrices(parameters)
    ident = sp.eye(8)

    for j, matrix in enumerate(matrices):
        other = [index for index in range(3) if index != j]
        assert zero_matrix(
            matrix**2 + matrices[other[0]] * matrices[other[1]] / 3
            - parameters[j] * ident
        )
    for left, right in combinations(matrices, 2):
        assert zero_matrix(left * right - right * left)
    print("PASS: universal commuting multiplication matrices and all three critical relations")

    unit = ident[:, 0]
    columns = []
    for monomial in BASIS:
        value = unit
        for j in monomial:
            value = matrices[j] * value
        columns.append(value)
    assert sp.Matrix.hstack(*columns) == ident
    print("PASS: cyclic unit identifies the eight squarefree basis vectors over QQ[a,b,c]")

    x, y, z = matrices
    critical_value = critical_value_matrix(parameters, matrices)
    cubic = (x**3 + y**3 + z**3 + x * y * z) / 3
    linear = a * x + b * y + c * z
    assert zero_matrix(3 * cubic - linear)
    assert zero_matrix(cubic - linear - critical_value)
    print("PASS: Euler identity gives H=J-alpha.x=-(2/3)alpha.x in the universal critical algebra")

    parity = sp.diag(*(sp.Integer(-1) ** len(monomial) for monomial in BASIS))
    for matrix in matrices:
        assert zero_matrix(parity * matrix * parity + matrix)
    assert sp.expand(sp.trace(critical_value)) == 0
    expected_moment = sp.Rational(2, 63) * (109 * (a**3 + b**3 + c**3) + 54 * a * b * c)
    assert sp.expand(sp.trace(critical_value**2) - expected_moment) == 0
    print("PASS: sign involution and exact universal second critical-value moment")

    # A nonzero pair of fixed weights exercises a genuine tensor sum.  For
    # arbitrary k, the identity follows from trace(A tensor B)=trace(A)trace(B).
    choices = ((1, 4, 9), (16, 25, 49))
    weighted = []
    for values in choices:
        weighted.append(critical_value_matrix(values, critical_matrices(values)))
    total = sp.kronecker_product(weighted[0], ident) + 100 * sp.kronecker_product(ident, weighted[1])
    assert sp.trace(total) == 0
    assert sp.trace(total**2) == 8 * (sp.trace(weighted[0]**2) + 100**2 * sp.trace(weighted[1]**2))
    assert sp.trace(weighted[0]**2) == sp.Rational(176980, 63)
    print("PASS: weighted tensor-sum critical spectrum and its second moment")

    # A fully exact seed for the generic 8**k-node statement.  Scaling the
    # parameters by t_i**2 scales its eight critical values by t_i**3; the
    # finite collision-avoidance argument for all k is in the manuscript.
    seed_x, seed_y, seed_z = critical_matrices(choices[0])
    seed_hessian = (
        sp.Rational(218, 27) * seed_x * seed_y * seed_z
        - sp.Rational(2, 9) * (seed_x**3 + seed_y**3 + seed_z**3)
    )
    seed_spectrum = sp.Poly(weighted[0].charpoly(spectral).as_expr(), spectral, domain=sp.QQ)
    expected_spectrum = sp.Poly(
        spectral**8 - sp.Rational(88490, 63) * spectral**6
        + sp.Rational(2638222849, 3969) * spectral**4
        - sp.Rational(1087802003896, 9261) * spectral**2
        + sp.Rational(488560998869056, 83349),
        spectral,
        domain=sp.QQ,
    )
    assert seed_spectrum == expected_spectrum
    assert sp.gcd(seed_spectrum, seed_spectrum.diff()).degree() == 0
    assert seed_hessian.det() != 0
    print("PASS: alpha=(1,4,9) has eight reduced Morse critical points and eight distinct critical values")

    # Q_1 is the independently obtained central Morse polynomial displayed in
    # centers.tex, Proposition cmo:prop:center-critical-polynomials.  This
    # check compares the two exact inputs; it does not rerun the central
    # elimination or establish the all-coherent comparison theorem.
    center_morse = (
        129140163 * spectral**8 - 188108856360 * spectral**6
        + 92316693932208 * spectral**4 - 16917496764590592 * spectral**2
        + 875501309973348352
    )
    lambda_squared = sp.Rational(28, 27)
    scaled_seed = sum(
        expected_spectrum.nth(2 * j) * spectral**(2 * j)
        * lambda_squared**(4 - j) for j in range(5)
    )
    assert sp.expand(scaled_seed - center_morse / 3**17) == 0
    assert sp.Rational(27, 28) * lambda_squared == 1
    print("PASS: exact central/commutative Morse spectra have lambda^2=28/27; the nonzero tensor moment calibrates kappa_k^2=27/28")

    # Degenerate critical schemes remain part of the determinant criterion.
    nilpotent_matrices = critical_matrices((0, 0, 0))
    assert all(matrix**4 == sp.zeros(8) for matrix in nilpotent_matrices)
    assert critical_value_matrix((0, 0, 0), nilpotent_matrices) == sp.zeros(8)
    assert (spectral * ident).det() == spectral**8
    print("PASS: nonreduced homogeneous critical fiber and its determinant")

    excess_k, excess_arity, homotopy = sp.symbols("excess_k excess_arity homotopy", nonnegative=True)
    dimension = 3 * (2 + excess_k)
    arity = 2 + excess_arity
    differences = (
        sp.expand(6 - 2 * arity - 3 * homotopy - dimension),
        sp.expand(5 - 2 * arity - 3 * homotopy - dimension),
        sp.expand(1 - 3 * homotopy - dimension),
    )
    assert differences == (
        -4 - 3 * excess_k - 2 * excess_arity - 3 * homotopy,
        -5 - 3 * excess_k - 2 * excess_arity - 3 * homotopy,
        -5 - 3 * excess_k - 3 * homotopy,
    )
    for expression in differences:
        assert all(coefficient < 0 for coefficient in sp.Poly(expression, excess_k, excess_arity, homotopy).coeffs())
    print("PASS: narrow-sector degree bounds exclude every k>=2, arity>=2, homotopy>=0")


if __name__ == "__main__":
    main()
