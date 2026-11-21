#!/usr/bin/env python3
"""Exact self-Ext calculation for the mixed one-centre example.

The certificate is universal over QQ[a,b,c].  In the shifted generators
X=x-a, Y=y-b, Z=z-c the relations are

    [Y,Z]=X^2+2aX, [Z,X]=Y^2+2bY, [X,Y]=Z^2+2cZ.

We verify a free resolution differential, two higher homotopies for the
central cubic minus its character value, and the resulting contraction.
Only finite polynomial identities are machine checked.  Exactness in all
degrees uses the PBW/Koszul argument and the central Shamash construction
proved in the paper.  Bounded self-Ext is NOT a proof of finite projective
dimension, homological smoothness, or a Kuznetsov comparison.

Run: python3 computations/verify_mixed_character_ext.py
Dependency: SymPy.  All arithmetic is exact; no sampling or interpolation.
"""

from functools import lru_cache
from itertools import permutations, product

import sympy as sp


PARAMETERS = sp.symbols("a b c")
LETTERS = sp.symbols("X Y Z", commutative=False)
a, b, c = PARAMETERS
X, Y, Z = LETTERS
ZERO_EXPONENT = (0, 0, 0)


def polynomial(expression):
    """Encode central parameter exponents and an ordered noncommutative word."""
    result = {}
    for term in sp.Add.make_args(sp.expand(expression)):
        coefficient = sp.Integer(1)
        exponent = [0, 0, 0]
        word = []
        for factor in sp.Mul.make_args(term):
            if factor.is_Number:
                coefficient *= factor
                continue
            base, power = factor.as_base_exp()
            assert power.is_Integer and power >= 0
            if base in PARAMETERS:
                exponent[PARAMETERS.index(base)] += int(power)
            else:
                assert base in LETTERS
                word.extend([LETTERS.index(base)] * int(power))
        key = (tuple(exponent), tuple(word))
        result[key] = result.get(key, 0) + coefficient
    return {key: value for key, value in result.items() if value}


def add(*polynomials):
    result = {}
    for current in polynomials:
        for monomial, coefficient in current.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return {key: value for key, value in result.items() if value}


def scale(coefficient, current):
    return {key: coefficient * value for key, value in current.items()
            if coefficient * value}


def multiply(left, right):
    result = {}
    for (left_exponent, left_word), left_coefficient in left.items():
        for (right_exponent, right_word), right_coefficient in right.items():
            monomial = (
                tuple(x + y for x, y in zip(left_exponent, right_exponent)),
                left_word + right_word,
            )
            result[monomial] = (result.get(monomial, 0)
                                + left_coefficient * right_coefficient)
    return {key: value for key, value in result.items() if value}


RELATIONS = tuple(polynomial(expression) for expression in (
    Y*Z-Z*Y-X**2-2*a*X,
    Z*X-X*Z-Y**2-2*b*Y,
    X*Y-Y*X-Z**2-2*c*Z,
))


def parameter_exponents(degree):
    return tuple(exponent for exponent in product(range(degree + 1), repeat=3)
                 if sum(exponent) == degree)


@lru_cache(maxsize=None)
def relation_reducer(degree):
    """Reduce by every homogeneous relation multiple of this total degree.

    All six variables have total weight one; a,b,c are central.  The
    relation rows are exact certificates in the two-sided relation ideal.
    The quotient dimensions also agree with the separate PBW proof.
    """
    monomials = tuple(
        (exponent, word)
        for word_degree in range(degree, -1, -1)
        for word in product(range(3), repeat=word_degree)
        for exponent in parameter_exponents(degree - word_degree)
    )
    positions = {monomial: index for index, monomial in enumerate(monomials)}
    rows = []
    for extra_word_degree in range(degree - 1):
        for exponent in parameter_exponents(degree - 2 - extra_word_degree):
            for left_degree in range(extra_word_degree + 1):
                right_degree = extra_word_degree - left_degree
                for left in product(range(3), repeat=left_degree):
                    for right in product(range(3), repeat=right_degree):
                        for relation in RELATIONS:
                            row = {}
                            for (parameter_power, word), coefficient in relation.items():
                                monomial = (
                                    tuple(x + y for x, y in zip(exponent, parameter_power)),
                                    left + word + right,
                                )
                                row[positions[monomial]] = coefficient
                            rows.append(row)
    matrix = sp.polys.matrices.DomainMatrix.from_dod(
        dict(enumerate(rows)), (len(rows), len(monomials)), sp.QQ)
    echelon, pivots = matrix.rref()
    echelon = echelon.to_Matrix()
    pivot_rows = {pivot: row for row, pivot in enumerate(pivots)}
    free_columns = tuple(index for index in range(len(monomials))
                         if index not in pivot_rows)
    reductions = []
    for index, monomial in enumerate(monomials):
        if index not in pivot_rows:
            reductions.append({monomial: sp.Integer(1)})
        else:
            row = pivot_rows[index]
            reductions.append({monomials[column]: -echelon[row, column]
                               for column in free_columns if echelon[row, column]})

    def reduce(current):
        return add(*(scale(coefficient, reductions[positions[monomial]])
                     for monomial, coefficient in current.items()))

    return len(free_columns), reduce


def matrix(expressions):
    return [[polynomial(expression) for expression in row] for row in expressions]


def matrix_add(*matrices):
    return [[add(*(current[i][j] for current in matrices))
             for j in range(len(matrices[0][0]))]
            for i in range(len(matrices[0]))]


def matrix_multiply(left, right):
    return [[add(*(multiply(left[i][k], right[k][j]) for k in range(len(right))))
             for j in range(len(right[0]))] for i in range(len(left))]


def diagonal(current, size):
    return [[current if i == j else {} for j in range(size)] for i in range(size)]


def assert_equal(left, right, degree):
    _, reduce = relation_reducer(degree)
    assert len(left) == len(right) and len(left[0]) == len(right[0])
    for left_row, right_row in zip(left, right):
        for left_entry, right_entry in zip(left_row, right_row):
            assert not reduce(add(left_entry, scale(-1, right_entry)))


def evaluate_at_character(current):
    return sp.expand(sum(coefficient * sp.prod(parameter**power
                                               for parameter, power in zip(PARAMETERS, exponent))
                         for (exponent, word), coefficient in current.items() if not word))


def evaluate_matrix(current):
    return sp.Matrix([[evaluate_at_character(entry) for entry in row] for row in current])


def higher_homotopy_certificate():
    """Explicit universal certificate; row matrices act on free left modules."""
    differential = (
        matrix([[X], [Y], [Z]]),
        matrix([[-X-2*a, -Z, Y], [Z, -Y-2*b, -X], [-Y, X, -Z-2*c]]),
        matrix([[X, Y, Z]]),
    )
    first = (
        matrix([[
            a*X/3-2*b*c/3-b*Z/3-2*c*Y/3+2*Y*Z/3-2*Z*Y/3,
            -2*a*c/3-a*Z/3+b*Y/3,
            -2*a*b/3-a*Y/3-b*X/3-2*c**2/3-2*Y*X/3,
        ]]),
        matrix([
            [-a*X+b*Z/3+c*Y/3+5*Y*Z/6-Z*Y/2,
             a*Y/3+4*c*Z/3+Y*X/6+Z**2/2,
             a*Z/3-2*b*Y-c*X/3-5*Y**2/6+Z*X/2],
            [-b*X/3-c*Z+Y*X/2-Z**2/3,
             a*Z/3-2*b*Y/3+c*X/3-Y**2/6+Z*X/3,
             a*X/3-b*Z/3-c*Y/3+Y*Z/2-Z*Y/3],
            [b*Y+Y**2/3, -a*X/3-Y*Z/3, a*Y/3+b*X/3+Y*X/3],
        ]),
        matrix([
            [2*a**2/3+2*a*X/3-2*b*c/3-2*b*Z/3-c*Y/3+5*Y*Z/6-2*Z*Y/3],
            [-2*a*c/3-2*a*Z/3-2*b**2/3+5*b*Y/3-c*X/3+5*Y**2/6-5*Z*X/6],
            [-2*a*b/3-Z**2/6],
        ]),
    )
    second = matrix([[
        a**2*X/3+16*a*b*c/9+8*a*b*Z/9+10*a*c*Y/9
        -5*a*Y*Z/18+7*a*Z*Y/9-4*b**2*Y/9+4*b*c*X/3
        -5*b*Y**2/18+13*b*Z*X/18+8*c**2*Z/9+7*c*Y*X/9
        +8*c*Z**2/9-Y*Z*X/3+5*Z*Y*X/9+2*Z**3/9
    ]])
    return differential, first, second


def verify_universal_certificate():
    d, h, second = higher_homotopy_certificate()
    d1, d2, d3 = d
    h0, h1, h2 = h
    x, y, z = X+a, Y+b, Z+c
    sym_xyz = sum(sp.Mul(*(triple[i] for i in order))
                  for triple in ((x, y, z),) for order in permutations(range(3)))/6
    omega = (x**3+y**3+z**3)/3-sp.Rational(2, 3)*sym_xyz-a**2*x-b**2*y-c**2*z
    value = -sp.Rational(2, 3)*(a**3+b**3+c**3+a*b*c)
    central = polynomial(omega-value)
    assert not evaluate_at_character(central)
    for degree, expected_dimension in ((2, 21), (3, 56), (4, 126)):
        assert relation_reducer(degree)[0] == expected_dimension
    assert_equal(matrix_multiply(d2, d1), matrix([[0], [0], [0]]), 2)
    assert_equal(matrix_multiply(d3, d2), matrix([[0, 0, 0]]), 2)
    for letter in LETTERS:
        assert_equal([[multiply(central, polynomial(letter))]],
                     [[multiply(polynomial(letter), central)]], 4)
    first_equations = (
        matrix_multiply(h0, d1),
        matrix_add(matrix_multiply(d1, h0), matrix_multiply(h1, d2)),
        matrix_add(matrix_multiply(d2, h1), matrix_multiply(h2, d3)),
        matrix_multiply(d3, h2),
    )
    for equation, size in zip(first_equations, (1, 3, 3, 1)):
        assert_equal(equation, diagonal(central, size), 3)
    assert_equal(matrix_add(matrix_multiply(second, d3), matrix_multiply(h0, h1)),
                 matrix([[0, 0, 0]]), 4)
    assert_equal(matrix_add(matrix_multiply(d1, second), matrix_multiply(h1, h2)),
                 matrix([[0], [0], [0]]), 4)
    # Higher identities vanish by homological degree: the resolution has length three.
    print("PASS: universal free differential, centrality, and all higher-homotopy identities over QQ[a,b,c]")

    middle = evaluate_matrix(d2)
    assert middle == sp.diag(-2*a, -2*b, -2*c)
    assert evaluate_matrix(h1) == sp.zeros(3)
    coefficient = sp.factor((evaluate_matrix(second)
                             - evaluate_matrix(h0)*middle.inv()*evaluate_matrix(h2))[0])
    expected = sp.Rational(2, 9)*(a**3*b**3+b**3*c**3+c**3*a**3+9*a*a*b*b*c*c)/(a*b*c)
    assert sp.cancel(coefficient-expected) == 0
    print("PASS: exact contraction gives kappa=2*((ab)^3+(bc)^3+(ca)^3+9a^2b^2c^2)/(9abc)")
    return coefficient


def cochain_dimensions(first, second, bound=12):
    """Dimensions of the two-block effective complex, as a vector space.

    This checks finite initial ranks only.  The paper's change of odd basis
    proves the stated cohomology in every degree.  No Yoneda product is asserted.
    """
    def basis(degree):
        return tuple((power, subset) for subset in ((), (0,), (1,), (0, 1))
                     for power in range(degree//2+1)
                     if 2*power+3*len(subset) == degree)

    ranks = []
    for degree in range(bound+1):
        domain, codomain = basis(degree), basis(degree+1)
        positions = {entry: index for index, entry in enumerate(codomain)}
        differential = sp.zeros(len(codomain), len(domain))
        for column, (power, subset) in enumerate(domain):
            for position, index in enumerate(subset):
                target = (power+2, subset[:position]+subset[position+1:])
                differential[positions[target], column] += (-1)**position*(first, second)[index]
        ranks.append(differential.rank())
    return tuple(len(basis(degree))-ranks[degree]-(ranks[degree-1] if degree else 0)
                 for degree in range(bound+1))


def verify_all_characters(coefficient):
    blocks = []
    for roots in ((1, 2, 3), (4, 5, 7)):
        positive = 9*sp.prod(value**2 for value in roots)
        remaining = sum((roots[i]*roots[j])**3 for i, j in ((0, 1), (1, 2), (2, 0)))
        assert positive > remaining
        characters = []
        for signs in product((-1, 1), repeat=3):
            point = tuple(sign*value for sign, value in zip(signs, roots))
            kappa = coefficient.subs(dict(zip(PARAMETERS, point)))
            central_value = -sp.Rational(2, 3)*(sum(value**3 for value in point)+sp.prod(point))
            assert kappa != 0
            characters.append((point, central_value, kappa))
        blocks.append(characters)
    print("PASS: all sixteen factor characters have nonzero kappa (324>251 and 176400>72827)")

    parameters = set()
    expected = tuple(1 if degree in (0, 2, 3, 5) else 0 for degree in range(13))
    for _, value1, kappa1 in blocks[0]:
        for _, value2, kappa2 in blocks[1]:
            parameters.add(-value1-100*value2)
            # Scaling a central equation by 100 scales the SECOND homotopy by 100^2.
            scaled_second = 10000*kappa2
            assert cochain_dimensions(kappa1, scaled_second) == expected
            # eta -> eta/kappa1, zeta -> eta2-(10000*kappa2/kappa1)*eta1
            # gives d(eta)=t^2, d(zeta)=0.  Its determinant is nonzero.
            assert sp.Matrix([[1/kappa1, -scaled_second/kappa1], [0, 1]]).det() != 0
    assert len(parameters) == 64 and 0 not in parameters
    print("PASS: every one of the 64 exceptional characters has self-Ext dimensions 1 in degrees 0,2,3,5 and 0 otherwise")
    print("SCOPE: no assertion of finite projective dimension, global smoothness, or a commutative Ku target")


def main():
    coefficient = verify_universal_certificate()
    verify_all_characters(coefficient)


if __name__ == "__main__":
    main()
