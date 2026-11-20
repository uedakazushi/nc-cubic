#!/usr/bin/env python3
"""Exact low products at the Hesse boundary, v25 (2026-11-21).

Run from the repository root:
    python3 computations/verify_boundary_low_products.py

All identities and minors are over QQ(p), with the MF curvature normalized
to the actual point cubic.  This file regenerates its finite Hom matrices,
first-order cocycle lifts, product homotopies and cubic witness.  It needs
only Python 3 and SymPy; no external data, numeric sampling or finite fields.

The right-window identification, Koszul tensor quasi-isomorphism, extension
of the active presentation isomorphism and Kummer interpretation are proved
in the manuscript.  The finite checks here do not replace those arguments.
"""

from itertools import product
from time import perf_counter

import sympy as sp


P, X, Y, Z = sp.symbols("p X Y Z")
VARIABLES = (X, Y, Z)
MONOMIALS = {
    0: (sp.Integer(1),),
    1: (X, Y, Z),
    2: (X**2, X*Y, X*Z, Y**2, Y*Z, Z**2),
    3: (X**3, X**2*Y, X**2*Z, X*Y**2, X*Y*Z, X*Z**2,
        Y**3, Y**2*Z, Y*Z**2, Z**3),
}

# Row and column indices use the precise coefficient order generated below.
# Explicit kernel witnesses supply the matching rank upper bounds.
MINORS = {
    "degree_1_minus_1": {
        "shape": (108, 36),
        "rows": (0, 1, 2, 3, 4, 5, 8, 10, 11, 14, 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 34, 35,
                 36, 37, 38, 43, 49),
        "columns": (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                    30, 31, 32, 33, 34),
        "determinant": -256*P**2,
    },
    "degree_2_minus_2": {
        "shape": (144, 54),
        "rows": (0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 14, 16, 17, 18, 19,
                 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 49),
        "columns": (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                    28, 30, 32, 34, 35, 36, 37, 39, 41, 43, 44, 45, 46, 48),
        "determinant": -64*P**3,
    },
    "boundaries_2_minus_2": {
        "shape": (54, 9),
        "rows": (2, 5, 8, 9, 11, 12, 14, 15, 17),
        "columns": tuple(range(9)),
        "determinant": sp.Integer(-8),
    },
    "degree_2_minus_3": {
        "shape": (81, 18),
        "rows": (0, 1, 2, 5, 8, 9, 10, 11, 12, 13, 14, 15, 17,
                 18, 19, 20, 23),
        "columns": tuple(range(17)),
        "determinant": -8*P**2,
    },
}


def zero(expression):
    assert sp.cancel(expression) == 0, expression


def zero_matrix(matrix):
    for entry in matrix:
        zero(entry)


def unit_matrix(i, j):
    """A 3 by 3 matrix unit, with mathematical one-based indices."""
    result = sp.zeros(3)
    result[i-1, j-1] = 1
    return result


def coefficients(matrix, degree):
    return [sp.Poly(entry, *VARIABLES).coeff_monomial(monomial)
            for entry in matrix for monomial in MONOMIALS[degree]]


def linear_matrix(variables):
    return sp.Matrix(3, 3, [sum(variables[3*i+j]*VARIABLES[j]
                               for j in range(3)) for i in range(9)])


def hom_matrices(line, adjugate):
    variables = sp.symbols("c:36")
    upper = sp.Matrix(3, 3, variables[:9])
    lower = linear_matrix(variables[9:])
    equations = (coefficients(line*lower-upper*adjugate, 2)
                 + coefficients(lower*line-adjugate*upper, 2))
    differential_one = sp.linear_eq_to_matrix(equations, variables)[0]

    variables = sp.symbols("c:54")
    upper, lower = linear_matrix(variables[:27]), linear_matrix(variables[27:])
    equations = (coefficients(line*lower-upper*line, 2)
                 + coefficients(adjugate*upper-lower*adjugate, 3))
    differential_two = sp.linear_eq_to_matrix(equations, variables)[0]

    boundaries = []
    for i in range(3):
        for j in range(3):
            matrix_unit = unit_matrix(i+1, j+1)
            boundaries.append(sp.Matrix(coefficients(line*matrix_unit, 1)
                                        + coefficients(matrix_unit*line, 1)))

    variables = sp.symbols("c:18")
    upper = sp.Matrix(3, 3, variables[:9])
    lower = sp.Matrix(3, 3, variables[9:])
    equations = (coefficients(line*lower-upper*line, 1)
                 + coefficients(adjugate*upper-lower*adjugate, 2))
    differential_period = sp.linear_eq_to_matrix(equations, variables)[0]
    return {
        "degree_1_minus_1": differential_one,
        "degree_2_minus_2": differential_two,
        "boundaries_2_minus_2": sp.Matrix.hstack(*boundaries),
        "degree_2_minus_3": differential_period,
    }


def relative_line_first_jet():
    """Differentiate the actual rational lift, before expanding its entries."""
    q = sp.symbols("q")
    scalar = (P**3+8)/3
    active_a = P*(1-q**2/4)
    active_b = q+P**3/3+q**3/12
    point_denominator = P*(P**3+q**3)/3
    xf, yf = X+Y, X-Y
    wf = active_a*(X+Y)-active_b*Z
    point_u, point_v = -q/point_denominator, 2/point_denominator
    a0 = -4*active_a*(active_a**3+active_b**3)/(3*active_b**3)
    a2 = 1+4*active_a**3/active_b**3
    a4 = -4*active_a**2/active_b**3
    normal = sp.Matrix([
        [xf-point_u*wf, yf-point_v*wf, 0],
        [0, a0*xf+(a0*point_u+a2)*wf, wf],
        [yf+point_v*wf, (a0*point_u**2+a2*point_u+a4)*wf, -xf],
    ])
    left = sp.Matrix([[4, -2, -2*P], [-4*scalar*P, 0, 0], [4, -2, 2*P]])
    right = sp.Matrix([[0, -P, -1], [2*P, P, -1], [2*P, -P, 1]])
    jets = []
    for degree in range(2):
        normal_jet = normal.applyfunc(
            lambda entry: sp.factor(sp.diff(entry, q, degree).subs(q, 2)))
        jets.append((left.inv()*normal_jet*right).applyfunc(sp.factor))
    return jets


def cubic_relation_matrix(quadrics):
    words = list(product(range(3), repeat=3))
    indices = {word: index for index, word in enumerate(words)}
    rows = []
    for relation in quadrics:
        for letter in range(3):
            for on_left in (True, False):
                row = [sp.Integer(0)]*27
                for word, coefficient in relation.items():
                    extended = (letter,)+word if on_left else word+(letter,)
                    row[indices[extended]] += coefficient
                rows.append(row)
    return sp.Matrix(rows), words, indices


def main():
    started = perf_counter()
    scalar, delta_p = (P**3+8)/3, P**3+8
    line = sp.Matrix([[Z, 0, 0], [P*Y, -2*Z, X], [-X, Y, 0]])
    adjugate = line.adjugate()
    differential = sp.zeros(6)
    differential[:3, 3:] = line
    differential[3:, :3] = -scalar*adjugate
    zero_matrix(differential**2-scalar*X*Y*Z*sp.eye(6))

    uppers = [-unit_matrix(2, 1), -unit_matrix(3, 1), -unit_matrix(2, 2)]
    lowers = [Y*unit_matrix(3, 1), X*unit_matrix(2, 1)+2*Z*unit_matrix(3, 1),
              X*unit_matrix(3, 1)+Z*unit_matrix(3, 3)]
    cycles = []
    for upper, lower in zip(uppers, lowers):
        cycle = sp.zeros(6)
        cycle[:3, 3:], cycle[3:, :3] = upper, scalar*lower
        zero_matrix(differential*cycle+cycle*differential)
        cycles.append(cycle)
    homotopy = sp.zeros(6)
    homotopy[3:, :3] = -scalar*unit_matrix(3, 1)
    for i in range(3):
        for j in range(3):
            expected = (differential*homotopy+homotopy*differential
                        if (i, j) == (2, 1) else sp.zeros(6))
            zero_matrix(cycles[i]*cycles[j]-expected)
    for cycle in cycles:
        assert cycle*homotopy == homotopy*cycle == sp.zeros(6)
    print("PASS: three active cocycles, nine pair products and zero constant cubic trees")

    matrices = hom_matrices(line, adjugate)
    for name, matrix in matrices.items():
        certificate = MINORS[name]
        assert matrix.shape == certificate["shape"]
        minor = matrix.extract(certificate["rows"], certificate["columns"])
        zero(minor.det()-certificate["determinant"])
    kernel_one = sp.Matrix.hstack(*[
        sp.Matrix(list(upper)+coefficients(lower, 1))
        for upper, lower in zip(uppers, lowers)])
    zero_matrix(matrices["degree_1_minus_1"]*kernel_one)
    assert kernel_one.rank() == 3
    boundaries = matrices["boundaries_2_minus_2"]
    linear_periods = sp.Matrix.hstack(*[
        sp.Matrix(coefficients(variable*sp.eye(3), 1)
                  + coefficients(variable*sp.eye(3), 1)) for variable in VARIABLES])
    kernel_two = boundaries.row_join(linear_periods)
    zero_matrix(matrices["degree_2_minus_2"]*kernel_two)
    assert kernel_two.rank() == 12
    period = sp.Matrix(list(sp.eye(3))+list(sp.eye(3)))
    zero_matrix(matrices["degree_2_minus_3"]*period)
    print("PASS: four exact rank minors and matching kernels; active low Hom ranks 3,3,0,1")

    # This is the induced matrix after the proved Koszul/exterior identification.
    full_product = sp.zeros(7, 25)
    for active in range(3):
        for center in range(2):
            full_product[2*active+center, 5*active+3+center] = 1
            full_product[2*active+center, 5*(3+center)+active] = -1
    full_product[6, 19], full_product[6, 23] = 1, -1
    assert full_product[:, [3, 4, 8, 9, 13, 14, 19]] == sp.eye(7)
    assert full_product.rank() == 7
    print("PASS: separated full binary product has rank seven and a unit minor")

    line_zero, line_one = relative_line_first_jet()
    zero_matrix(line_zero-line)
    epsilon = sp.symbols("epsilon")
    adjugate_one = (line+epsilon*line_one).adjugate().applyfunc(
        lambda entry: sp.factor(sp.diff(entry, epsilon).subs(epsilon, 0)))
    differential_one = sp.zeros(6)
    differential_one[:3, 3:] = line_one
    differential_one[3:, :3] = -scalar*adjugate_one
    curvature_one = -P*(X**3+Y**3+Z**3)/3+2*X*Y*Z
    zero_matrix(differential*differential_one+differential_one*differential
                -curvature_one*sp.eye(6))
    print("PASS: actual relative line matrix and its first-order specified-curvature identity")

    # Normalize the first derivatives of C21,C31,C22 to zero.
    rows = list(MINORS["degree_1_minus_1"]["rows"])
    normalizing_matrix = matrices["degree_1_minus_1"][rows, :]
    normalization = sp.zeros(3, 36)
    for i, column in enumerate((3, 6, 4)):
        normalization[i, column] = 1
    normalizing_inverse = normalizing_matrix.col_join(normalization).inv()
    upper_jets, lower_jets = [], []
    for upper, lower in zip(uppers, lowers):
        rhs = -sp.Matrix(coefficients(line_one*lower-upper*adjugate_one, 2)
                         + coefficients(lower*line_one-adjugate_one*upper, 2))
        solution = (normalizing_inverse*rhs[rows, :].col_join(sp.zeros(3, 1)))\
            .applyfunc(sp.factor)
        zero_matrix(matrices["degree_1_minus_1"]*solution-rhs)
        upper_jets.append(sp.Matrix(3, 3, solution[:9]))
        lower_jets.append(linear_matrix(solution[9:]))
    expected_uppers = [
        sp.Matrix([[-1, 0, 1/P], [0, 0, -2/P], [0, -2/P, 0]])/delta_p,
        sp.Matrix([[P, P, 0], [0, 0, -2], [0, 0, -2/P]])/delta_p,
        sp.Matrix([[-1, -1, 0], [0, 0, 0], [0, -2/P, P/4]])/delta_p,
    ]
    for obtained, expected in zip(upper_jets, expected_uppers):
        zero_matrix(obtained-expected)
    for obtained, expected in zip(lower_jets, (-2*Z/P, -P*X, -Y-2*Z/P)):
        zero(obtained[0, 2]-expected/delta_p)
    print("PASS: all three normalized first-order cocycle lifts satisfy both closure equations")

    # Products are reduced in the same boundary-plus-period splitting.
    _, projection_rows = kernel_two.T.rref()
    projection_rows = list(projection_rows)
    projection_inverse = kernel_two[projection_rows, :].inv()
    homotopies_zero = [sp.zeros(3) for _ in range(9)]
    homotopies_zero[7] = -unit_matrix(3, 1)
    products_one, homotopies_one = [], []
    for i in range(3):
        for j in range(3):
            upper = upper_jets[i]*lowers[j]+uppers[i]*lower_jets[j]
            lower = lower_jets[i]*uppers[j]+lowers[i]*upper_jets[j]
            upper -= line_one*homotopies_zero[3*i+j]
            lower -= homotopies_zero[3*i+j]*line_one
            vector = sp.Matrix(coefficients(upper, 1)+coefficients(lower, 1))
            answer = (projection_inverse*vector[projection_rows, :]).applyfunc(sp.factor)
            zero_matrix(kernel_two*answer-vector)
            homotopies_one.append(sp.Matrix(3, 3, answer[:9]))
            products_one.append(answer[9:, :])
    first_binary = (scalar*sp.Matrix.hstack(*products_one)).applyfunc(sp.factor)
    expected_binary = sp.Matrix([
        [0, 0, 1/P, 0, P, 0, 0, 0, 0],
        [1/P, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 2/P, 0, 0, 0, 0, P/4],
    ])/3
    zero_matrix(first_binary-expected_binary)
    zero(first_binary[:, [0, 2, 3]].det()+2/(27*P**3))
    print("PASS: first binary jet and unit minor -2/(27p^3); active Smith orders (1,1,1)")

    # For three odd degree-one inputs with d h(ab)=ab, the two Massey trees
    # have a SUM: d(h(ab)c)=abc and d(a h(bc))=-abc.  Choose the overall
    # minus sign so that -(h(ab)c+a h(bc)) gives the positive x^3 relation.
    # The projection reads upper entry 11.  In the active block calculation
    # h(ab)c has zero upper block, so only -a h(bc) contributes there.
    one_d = sp.Matrix([[0, X], [X**2, 0]])
    one_phi = sp.Matrix([[0, 1], [-X, 0]])
    one_h = sp.Matrix([[0, 0], [-1, 0]])
    zero_matrix(one_phi**2-one_d*one_h-one_h*one_d)
    one_cubic = -(one_h*one_phi+one_phi*one_h)
    assert one_cubic == sp.eye(2)
    zero_matrix(one_d*one_cubic-one_cubic*one_d)
    first_cubic = {}
    for i, j, k in product(range(3), repeat=3):
        coefficient = sp.factor(-scalar*(
            upper_jets[i]*homotopies_zero[3*j+k]
            + uppers[i]*homotopies_one[3*j+k])[0, 0])
        if coefficient:
            first_cubic[(i, j, k)] = coefficient
    assert first_cubic == {(0, 2, 1): 1/(3*P)}
    print("PASS: positive x^3 transfer normalization; first cubic jet acb/(3p)")

    saturated_quadrics = [
        {(0, 2): sp.Integer(1), (1, 1): P**2},
        {(0, 0): sp.Integer(1), (2, 1): P},
        {(1, 0): sp.Integer(1), (2, 2): P**2/8},
    ]
    cubic_relations, words, word_indices = cubic_relation_matrix(saturated_quadrics)
    witness_values = {
        (0, 0, 0): -P, (0, 2, 1): 1, (1, 0, 2): 1,
        (2, 1, 0): 1, (1, 1, 1): -1/P**2, (2, 2, 2): -8/P**2,
    }
    witness = sp.Matrix([witness_values.get(word, 0) for word in words])
    zero_matrix(cubic_relations*witness)
    assert witness[word_indices[(0, 2, 1)]] == 1
    assert cubic_relations.rank() == 17
    print("PASS: eighteen quadratic multiples and an explicit nonzero cubic dual witness")

    # Generator comparison: a -> x, b -> y/p, c -> 2z/p.
    source_quadrics = [
        {(0, 2): sp.Integer(1), (1, 1): P/2},
        {(2, 1): sp.Integer(1), (0, 0): P/2},
        {(1, 0): sp.Integer(1), (2, 2): P/2},
    ]
    generator_scales = (sp.Integer(1), 1/P, 2/P)
    for original, target, factor in zip(saturated_quadrics, source_quadrics,
                                        (2/P, 2/P, 1/P)):
        for word in set(original) | set(target):
            zero(original.get(word, 0)*generator_scales[word[0]]*generator_scales[word[1]]
                 -factor*target.get(word, 0))
    source_cubics, _, _ = cubic_relation_matrix(source_quadrics)
    image_acb_plus_cube = sp.zeros(1, 27)
    image_acb_plus_cube[0, word_indices[(0, 2, 1)]] = 2/P**2
    image_acb_plus_cube[0, word_indices[(0, 0, 0)]] = 1/P
    # It is (2/p^2) times x(zy+(p/2)x^2), one explicit quadratic multiple.
    zero_matrix(image_acb_plus_cube-(2/P**2)*source_cubics[6, :])
    for cube in ((1, 1, 1), (2, 2, 2)):
        difference = sp.zeros(27, 1)
        difference[word_indices[cube]], difference[word_indices[(0, 0, 0)]] = 1, -1
        solution, _ = source_cubics.T.gauss_jordan_solve(difference)
        zero_matrix(source_cubics.T*solution-difference)
    q = sp.symbols("q")
    center_u = 1+q**2/2+P**3*q/6-q**4/48
    center_v = (4-q**2)*(12*q+q**3-8*P**3)/48
    zero(center_u.subs(q, 2)-scalar)
    zero(center_v.subs(q, 2))
    print("PASS: saturated source quadratic relations and boundary central cubic normalization")

    # First cubic maps to -x^3/(3p^2), whereas the source center is p*b*x^3.
    first_scalar_ratio = (-1/(3*P**2))/(P*scalar)
    boundary_d_leading = -delta_p**2/27
    zero(first_scalar_ratio/boundary_d_leading-(3/(P*delta_p))**3)
    print("PASS: first scalar ratio divided by the D leading coefficient is a specified cube")
    print(f"All exact boundary low-product checks passed in {perf_counter()-started:.3f} seconds.")


if __name__ == "__main__":
    main()
