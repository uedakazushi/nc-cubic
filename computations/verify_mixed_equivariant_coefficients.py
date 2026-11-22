#!/usr/bin/env python3
"""Exact Heisenberg certificates for the linear comparison (2026-11-22).

The point-action convention is g: B_(p,alpha) -> B_(gp,galpha), with
active generators sent to g(x).  We verify that convention against the
free-algebra relations and the explicit centre, then compute all four
low-degree intertwiner spaces by rational linear algebra and weights
modulo three.  Independent centre characters exclude mixed-block terms.
At these degrees every possible support uses at most three blocks, so
the support enumeration is exhaustive for arbitrary k, not an experiment
at a sample value of k.

This script does not compute the seven categorical scalars or construct
the comparison kernel.  In particular, the abelianised centre's 53/54
is not asserted to be the categorical scalar chi_k.  Equivariance of
the actual comparison classes is proved in the mixed manuscript.

Requires Python 3 and SymPy.  From the repository root run:
  python3 computations/verify_mixed_equivariant_coefficients.py
"""

from itertools import permutations, product

import sympy as sp


p, q, r, alpha1, alpha2, alpha3, u, omega = sp.symbols(
    "p q r alpha1 alpha2 alpha3 u omega"
)
parameters = (p, q, r, alpha1, alpha2, alpha3)


def cyclotomic(expression):
    """Reduce a polynomial exactly modulo omega**2 + omega + 1."""
    return sp.Poly(sp.expand(expression), omega).rem(
        sp.Poly(omega**2 + omega + 1, omega)
    ).as_expr().expand()


def add_word(poly, word, coefficient):
    poly[word] = poly.get(word, 0) + coefficient


def relations():
    matrix = ((0, p, r), (p, 0, q), (r, q, 0))
    alphas = (alpha1, alpha2, alpha3)
    result = []
    for i, (j, k) in enumerate(((1, 2), (2, 0), (0, 1))):
        polynomial = {(j, k): 1, (k, j): -1, (i, i): -1}
        for column, coefficient in enumerate(matrix[i]):
            add_word(polynomial, (column,), -u * coefficient)
        add_word(polynomial, (), u**2 * alphas[i])
        result.append(polynomial)
    return result


def centre():
    polynomial = {(i, i, i): sp.Rational(1, 3) for i in range(3)}
    for word in permutations(range(3)):
        add_word(polynomial, word, -sp.Rational(1, 9))
    for coefficient, i, j, k in ((p, 0, 1, 2), (q, 1, 2, 0), (r, 2, 0, 1)):
        add_word(polynomial, (i, j), u * coefficient / 2)
        add_word(polynomial, (j, i), u * coefficient / 2)
        add_word(polynomial, (k, k), u * coefficient / 18)
    for i, coefficient in enumerate((
        q**2 / 6 - p * r / 18 - alpha1,
        r**2 / 6 - p * q / 18 - alpha2,
        p**2 / 6 - q * r / 18 - alpha3,
    )):
        add_word(polynomial, (i,), u**2 * coefficient)
    return polynomial


def change_generators(polynomial, permutation, phases):
    result = {}
    for word, coefficient in polynomial.items():
        changed = tuple(permutation[i] for i in word)
        phase = sum(phases[i] for i in word) % 3
        add_word(result, changed, coefficient * omega**phase)
    return result


def change_parameters(polynomial, images):
    substitutions = dict(zip(parameters, images))
    return {
        word: sp.sympify(coefficient).subs(substitutions, simultaneous=True)
        for word, coefficient in polynomial.items()
    }


def assert_equal_words(left, right, factor=1):
    for word in set(left) | set(right):
        assert cyclotomic(left.get(word, 0) - factor * right.get(word, 0)) == 0


def monomials(variables, degree):
    return [exponents for exponents in product(range(degree + 1), repeat=variables)
            if sum(exponents) == degree]


def verify_intertwiners(name, variables, exponents, weights, permutation,
                        output_weights, output_permutation, expected_basis):
    """Solve F(cp)=cF(p), F(dp)=dF(p), and verify the displayed basis."""
    dimension = len(output_weights)
    columns = [
        (powers, j) for powers in exponents for j in range(dimension)
        if sum(a * w for a, w in zip(powers, weights)) % 3 == output_weights[j]
    ]
    rows = [(powers, j) for powers in exponents for j in range(dimension)]
    indices = {value: i for i, value in enumerate(rows)}
    matrix = sp.zeros(len(rows), len(columns))
    for column, (powers, j) in enumerate(columns):
        changed = [0] * len(powers)
        for i, power in enumerate(powers):
            changed[permutation[i]] = power
        matrix[indices[tuple(changed), j], column] += 1
        matrix[indices[powers, output_permutation[j]], column] -= 1

    assert len(matrix.nullspace()) == len(expected_basis)
    vectors = []
    for output in expected_basis:
        polynomials = [sp.Poly(coefficient, *variables) for coefficient in output]
        vector = sp.Matrix([
            polynomials[j].coeff_monomial(powers) for powers, j in columns
        ])
        # No coefficient may be lost by the preliminary diagonal-weight cut.
        for powers, j in rows:
            if (powers, j) not in columns:
                assert polynomials[j].coeff_monomial(powers) == 0
        assert matrix * vector == sp.zeros(len(rows), 1)
        vectors.append(vector)
    assert sp.Matrix.hstack(*vectors).rank() == len(expected_basis)
    print(f"PASS {name}: dimension {len(expected_basis)}, displayed basis verified")


def verify_supports():
    # At parameter degree <=3, inputs and one output together use at most
    # three distinct blocks.  Relabel their support by 0,1,2.  Each test below
    # is therefore an exhaustive congruence test, for any number of blocks.
    units = [tuple(int(i == j) for i in range(3)) for j in range(3)]

    def character(counts):
        return tuple(2 * count % 3 for count in counts)

    # P_i -> pure Jac(J_j)_2, or -> U_j tensor U_l.
    for i in range(3):
        own = character(units[i])
        for j in range(3):
            assert (own == character(units[j])) == (i == j)
        for j in range(3):
            for k in range(j + 1, 3):
                mixed = tuple(units[j][ell] + units[k][ell] for ell in range(3))
                assert own != mixed

    # Sym^2(direct sum P_i) -> U_j.
    for counts in monomials(3, 2):
        possible = [j for j in range(3) if character(counts) == units[j]]
        assert possible == [j for j in range(3) if counts[j] == 2]

    # P_i tensor Alpha_j -> scalars.
    for i in range(3):
        for j in range(3):
            invariant = all(
                (2 * units[i][ell] + units[j][ell]) % 3 == 0 for ell in range(3)
            )
            assert invariant == (i == j)

    # Sym^3(direct sum P_i) -> scalars.
    for counts in monomials(3, 3):
        assert (character(counts) == (0, 0, 0)) == (3 in counts)
    print("PASS independent centre characters exclude all mixed-block terms")


def main():
    cyclic = ((1, 2, 0), (0, 0, 0), (r, p, q, alpha3, alpha1, alpha2))
    diagonal = ((0, 1, 2), (0, 1, 2),
                (omega * p, q, omega**2 * r,
                 alpha1, omega * alpha2, omega**2 * alpha3))
    central = ((0, 1, 2), (1, 1, 1),
               (omega**2 * p, omega**2 * q, omega**2 * r,
                omega * alpha1, omega * alpha2, omega * alpha3))
    defining = relations()
    for permutation, phases, images in (cyclic, diagonal, central):
        target = [change_parameters(relation, images) for relation in defining]
        for i, relation in enumerate(defining):
            assert_equal_words(change_generators(relation, permutation, phases),
                               target[permutation[i]], omega**(2 * phases[i] % 3))
    print("PASS source-to-target parameter actions follow from the PBW relations")

    central_polynomial = centre()
    for permutation, phases, images in (cyclic, diagonal, central):
        assert_equal_words(change_generators(central_polynomial, permutation, phases),
                           change_parameters(central_polynomial, images))
    print("PASS the universal centre is strictly equivariant, with no u^3 shift")

    # Basis x^2,y^2,z^2,xy,yz,zx; gradient(J) is the graph of -1/3.
    jacobian = sp.Matrix(((1, 0, 0, 0, sp.Rational(1, 3), 0),
                          (0, 1, 0, 0, 0, sp.Rational(1, 3)),
                          (0, 0, 1, sp.Rational(1, 3), 0, 0)))
    section = sp.zeros(3, 6)
    section[:, 3:] = sp.eye(3)
    assert jacobian.col_join(section).det() == 1
    print("PASS cross monomials give the standard degree-two Jacobian section")

    verify_intertwiners(
        "P -> Jac(J)_2", (p, q, r), monomials(3, 1), (1, 0, 2), (2, 0, 1),
        (1, 0, 2), (1, 2, 0), ((p, q, r),),
    )
    verify_intertwiners(
        "Sym^2 P -> U", (p, q, r), monomials(3, 2), (1, 0, 2), (2, 0, 1),
        (0, 1, 2), (1, 2, 0), ((q**2, r**2, p**2), (p * r, p * q, q * r)),
    )
    bilinear = [left + right for left in monomials(3, 1) for right in monomials(3, 1)]
    verify_intertwiners(
        "P tensor Alpha -> scalars", parameters, bilinear, (1, 0, 2, 0, 1, 2),
        (2, 0, 1, 5, 3, 4), (0,), (0,), ((q * alpha1 + r * alpha2 + p * alpha3,),),
    )
    verify_intertwiners(
        "Sym^3 P -> scalars", (p, q, r), monomials(3, 3), (1, 0, 2), (2, 0, 1),
        (0,), (0,), ((p**3 + q**3 + r**3,), (p * q * r,)),
    )
    verify_supports()

    x, y, z, scale = sp.symbols("x y z scale")
    covariants = (
        p * x * y + q * y * z + r * z * x,
        q**2 * x + r**2 * y + p**2 * z,
        p * r * x + p * q * y + q * r * z,
        q * alpha1 + r * alpha2 + p * alpha3,
        p**3 + q**3 + r**3, p * q * r,
        alpha1 * x + alpha2 * y + alpha3 * z,
    )
    rescaling = {variable: scale * variable for variable in (x, y, z, p, q, r)}
    rescaling.update({variable: scale**2 * variable for variable in (alpha1, alpha2, alpha3)})
    for polynomial in covariants:
        changed = polynomial.subs(rescaling, simultaneous=True)
        assert sp.expand(changed - scale**3 * polynomial) == 0
    print("PASS cube-root normalization restores exactly one factor a_i per block")

    # This quotient is only the commutativised explicit centre correction.
    q_nc = p * (x * y + z**2 / 18) + q * (y * z + x**2 / 18) + r * (z * x + y**2 / 18)
    reduced = q_nc.subs({x**2: -y * z / 3, y**2: -z * x / 3, z**2: -x * y / 3},
                       simultaneous=True)
    assert sp.expand(reduced - sp.Rational(53, 54) * covariants[0]) == 0
    print("PASS abelianised Q_nc has scalar 53/54; categorical chi_k is not computed")


if __name__ == "__main__":
    main()
