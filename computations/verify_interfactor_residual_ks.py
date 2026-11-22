#!/usr/bin/env python3
"""Exact Jacobian certificates for the Clifford interfactor KS calculation.

Current result: 2026-11-23 / v63.

Run from the repository root with Python 3 and SymPy:
    python3 computations/verify_interfactor_residual_ks.py

The two normalized Hesse cubics are sum(x_i^3)-3*h*x_1*x_2*x_3
and sum(y_i^3)-3*k*y_1*y_2*y_3.  The calculation is symbolic over
Q[h,k], localized only at (1-h^3)(1-k^3).  Thus the displayed basis
certificates hold on every smooth Hesse fiber, including k=0.
For the Clifford factor S(1,1,tau), k=(tau^3+2)/(3*tau).

The script checks the actual Jacobian relation spaces, their complete
degree-three complement, block characters, the tensor-product linear
algebra, and the failure of literal coordinate squares at tau^3=-2.
It does NOT construct a comparison kernel or verify the full-cochain
cup-product identity identifying the categorical Kodaira--Spencer map.
Those are separate mathematical inputs in the mixed manuscript.  In
particular the categorical images of central y_i^2 are not replaced by
their literal commutative coordinate classes.  No proof assistant is used.
"""

from itertools import product

import sympy as sp


def exponents(number, degree):
    return [powers for powers in product(range(degree + 1), repeat=number)
            if sum(powers) == degree]


def monomial(variables, powers):
    return sp.prod(variable ** power for variable, power
                   in zip(variables, powers))


def coefficient_matrix(polynomials, variables, powers):
    columns = []
    for expression in polynomials:
        polynomial = sp.Poly(expression, *variables)
        columns.append(sp.Matrix([polynomial.coeff_monomial(power)
                                  for power in powers]))
    return sp.Matrix.hstack(*columns)


def hesse_relations(variables, parameter):
    return [variables[i] ** 2 - parameter * variables[j] * variables[k]
            for i, (j, k) in enumerate(((1, 2), (2, 0), (0, 1)))]


def off_diagonal(variables):
    return [variables[1] * variables[2], variables[2] * variables[0],
            variables[0] * variables[1]]


def main():
    h, k, tau = sp.symbols("h k tau")
    x = sp.symbols("x1:4")
    y = sp.symbols("y1:4")
    variables = x + y
    rx, ry = hesse_relations(x, h), hesse_relations(y, k)

    # This is the actual standard point cubic of S(1,1,tau), up to
    # nonzero scalar.  The factorization recovers the smoothness exclusions.
    clifford_cubic = tau * sum(value ** 3 for value in y) - (
        tau ** 3 + 2) * sp.prod(y)
    for index, relation in enumerate(ry):
        assert sp.expand(sp.diff(clifford_cubic, y[index]) -
                         3 * tau * relation.subs(k, (tau**3 + 2)/(3*tau))) == 0
    assert sp.expand((tau**3 + 2)**3 - 27*tau**3 -
                     (tau**3 - 1)**2 * (tau**3 + 8)) == 0
    print("PASS Clifford point cubic, Jacobian quadrics, and smoothness factorization")

    # The three off-diagonal monomials complement the three Jacobian
    # relations over the ENTIRE parameter line; no division by h or k.
    for block, parameter, relations in ((x, h, rx), (y, k, ry)):
        matrix = coefficient_matrix(relations + off_diagonal(block), block,
                                    exponents(3, 2))
        assert matrix.det() in (1, -1)
        inverse = matrix.inv()
        for i in range(3):
            square = coefficient_matrix([block[i]**2], block, exponents(3, 2))
            coordinates = inverse * square
            expected = sp.zeros(6, 1)
            expected[i] = 1
            expected[3 + i] = parameter
            assert coordinates == expected
    print("PASS universal degree-two off-diagonal bases and [z_i^2]=parameter*[z_j*z_k]")

    # Use all six partial derivatives multiplied by all six variables.
    # Their bidegree decomposition has 9 relation columns in each block.
    # Appending the proposed quotient basis produces a square 56x56 matrix.
    blocks = []
    pure_x = [value * relation for relation in rx for value in x]
    pure_y = [value * relation for relation in ry for value in y]
    xy2 = [value * relation for value in x for relation in ry]
    x2y = [relation * value for relation in rx for value in y]
    q_xy2 = [value * quadric for value in x for quadric in off_diagonal(y)]
    q_x2y = [quadric * value for quadric in off_diagonal(x) for value in y]
    data = [
        (3, pure_x, [sp.prod(x)]),
        (2, x2y, q_x2y),
        (1, xy2, q_xy2),
        (0, pure_y, [sp.prod(y)]),
    ]
    all_powers = exponents(6, 3)
    determinant_product = 1
    quotient_basis = []
    all_relations = []
    for x_degree, relations, quotient in data:
        powers = [power for power in all_powers if sum(power[:3]) == x_degree]
        block_matrix = coefficient_matrix(relations + quotient, variables, powers)
        determinant = sp.factor(block_matrix.det())
        if x_degree == 3:
            assert sp.factor(determinant**2 - (1-h**3)**4) == 0
        elif x_degree == 0:
            assert sp.factor(determinant**2 - (1-k**3)**4) == 0
        else:
            assert determinant in (1, -1)
        assert len(relations) == 9
        assert len(powers) == len(relations) + len(quotient)
        blocks.append(block_matrix)
        determinant_product *= determinant
        all_relations.extend(relations)
        quotient_basis.extend(quotient)

    # Compare the complete relation set, not a selected ideal subspace.
    actual_relations = [value * relation for relation in rx + ry for value in variables]
    assert {sp.expand(value) for value in all_relations} == {
        sp.expand(value) for value in actual_relations}
    ordered_powers = [power for x_degree, _, _ in data for power in all_powers
                      if sum(power[:3]) == x_degree]
    ordered_columns = [value for _, relations, quotient in data
                       for value in relations + quotient]
    full_matrix = coefficient_matrix(ordered_columns, variables, ordered_powers)
    assert full_matrix == sp.diag(*blocks)
    expected_determinant = (1-h**3)**2 * (1-k**3)**2
    assert sp.factor(determinant_product**2 - expected_determinant**2) == 0
    assert full_matrix.shape == (56, 56)
    assert len(all_relations) == 36 and len(quotient_basis) == 20
    print("PASS complete degree-three Jacobian quotient: 56 monomials, 36 relations, dimension 20")
    print("PASS nine x_i*y_j*y_l classes form the entire bidegree-(1,2) summand")

    # Under x -> zeta*x and y fixed, the source action is Lambda ->
    # zeta*Lambda (the algebra-isomorphism convention in the manuscript).
    dimensions = {degree: len(quotient) for degree, _, quotient in data}
    assert dimensions == {3: 1, 2: 9, 1: 9, 0: 1}
    characters = {residue: sum(dimension for degree, dimension in dimensions.items()
                               if degree % 3 == residue) for residue in range(3)}
    assert characters == {0: 2, 1: 9, 2: 9}
    assert (-2) % 3 == 1  # r_x scales by zeta^2; Lambda scales inversely.
    print("PASS block dimensions (1,9,9,1), character dimensions (2,9,9), and source weight 1")

    # A dense LDU chart gives a polynomial certificate for det(A tensor C).
    # Its diagonal entries may vanish in the identity; the proof extends
    # from the dense chart to all matrices by polynomiality.
    def ldu(prefix):
        lower_values = sp.symbols(f"{prefix}l0:3")
        upper_values = sp.symbols(f"{prefix}u0:3")
        diagonal_values = sp.symbols(f"{prefix}d0:3")
        lower = sp.Matrix(((1, 0, 0), (lower_values[0], 1, 0),
                           (lower_values[1], lower_values[2], 1)))
        upper = sp.Matrix(((1, upper_values[0], upper_values[1]),
                           (0, 1, upper_values[2]), (0, 0, 1)))
        diagonal = sp.diag(*diagonal_values)
        return lower, diagonal, upper

    la, da, ua = ldu("a")
    lc, dc, uc = ldu("c")
    left = sp.kronecker_product(la*da*ua, lc*dc*uc)
    kl, kd, ku = (sp.kronecker_product(first, second)
                  for first, second in ((la, lc), (da, dc), (ua, uc)))
    assert all(sp.expand(entry) == 0 for entry in left - kl*kd*ku)
    assert kl.is_lower and ku.is_upper
    assert all(kl[i, i] == ku[i, i] == 1 for i in range(9))
    assert sp.prod(kd[i, i] for i in range(9)) == da.det()**3 * dc.det()**3
    print("PASS symbolic tensor determinant det(A tensor C)=det(A)^3*det(C)^3")

    # tau^3=-2 is a smooth Clifford fiber with a Fermat point cubic.
    # Work in Q[tau]/(tau^3+2); inverse(3*tau)=-tau^2/6 there.
    def reduce_tau(expression):
        return sp.rem(sp.expand(expression), tau**3 + 2, tau)

    inverse_three_tau = -tau**2 / 6
    assert reduce_tau(inverse_three_tau * 3*tau - 1) == 0
    for i in range(3):
        assert reduce_tau(inverse_three_tau * sp.diff(clifford_cubic, y[i]) - y[i]**2) == 0
    assert reduce_tau((tau**3-1)**2 * (tau**3+8)) == 54
    literal_square_matrix = k * sp.eye(3)
    assert literal_square_matrix.subs(k, 0) == sp.zeros(3)
    fermat_complement = coefficient_matrix(
        [relation.subs(k, 0) for relation in ry] + off_diagonal(y), y,
        exponents(3, 2))
    assert fermat_complement.det() in (1, -1)
    print("PASS smooth tau^3=-2 fiber: literal squares vanish, off-diagonal classes remain a basis")

    print("Scope: exact finite Jacobian/tensor certificates only; categorical KS identification is a separate proof.")


if __name__ == "__main__":
    main()
