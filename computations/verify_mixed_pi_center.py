#!/usr/bin/env python3
"""Exact universal degree-six centre lifts for S(1,-1,-1).

Let a,b,c be independent central variables of weight 2 and x,y,z have
weight 1.  This script verifies three explicit central elements for
    [y,z]=x*x-a, [z,x]=y*y-b, [x,y]=z*z-c.
It also checks that their highest active parts, together with Omega_0^2,
are linearly independent in S(1,-1,-1)_6.  Smith--Tate, Theorem 3.7,
then supplies the separate all-degree centre-generation input.

All arithmetic uses fractions.Fraction over QQ; no parameter evaluation,
sampling, interpolation, numerical rank, or finite-field inference is used.
The row span consists of every two-sided relation multiple in the given
homogeneous weight, hence every successful reduction is an exact ideal
membership certificate.  Requires SymPy only for one 4-by-28 matrix.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
import sympy as sp

ZERO = (0, 0, 0)
ALPHABET = "xyz"


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(coefficient, polynomial):
    return {m: coefficient*c for m, c in polynomial.items() if coefficient*c}


def multiply(left, right):
    result = {}
    for (p, w), a in left.items():
        for (q, v), b in right.items():
            monomial = (tuple(x+y for x, y in zip(p, q)), w+v)
            result[monomial] = result.get(monomial, 0) + a*b
    return {m: c for m, c in result.items() if c}


def power(polynomial, exponent):
    result = {(ZERO, ()): Fraction(1)}
    for _ in range(exponent):
        result = multiply(result, polynomial)
    return result


def word(text):
    return {(ZERO, tuple(ALPHABET.index(c) for c in text)): Fraction(1)}


def parameter(index):
    return {(tuple(int(i == index) for i in range(3)), ()): Fraction(1)}


def linear_words(terms):
    return add(*(scale(Fraction(c), word(w)) for c, w in terms))


def reverse_yz(polynomial):
    """Anti-automorphism fixing x,a and interchanging y,z and b,c."""
    permutation = (0, 2, 1)
    return {((p[0], p[2], p[1]), tuple(permutation[i] for i in reversed(w))): c
            for (p, w), c in polynomial.items()}


def central_elements():
    x, y, z = (word(t) for t in ALPHABET)
    a, b, c = (parameter(i) for i in range(3))
    omega = add(scale(Fraction(1, 3), linear_words([(1, "xxx"), (1, "yyy"), (1, "zzz")])),
                scale(Fraction(-1, 9), add(*(word("".join(p)) for p in permutations(ALPHABET)))),
                scale(-1, add(multiply(a, x), multiply(b, y), multiply(c, z))))
    # C0 = z(z^2-c)(xzy+a*x+b*y)+ab*z^2.
    zero = add(multiply(multiply(z, add(power(z, 2), scale(-1, c))),
                        add(word("xzy"), multiply(a, x), multiply(b, y))),
               multiply(multiply(a, b), power(z, 2)))
    positive = add(
        linear_words([(1, "yzzzzy"), (1, "zyzzzy"), (1, "zzyyzz"),
                      (2, "zzyzzy"), (-1, "zzzzyy"), (1, "zzzzzx")]),
        multiply(a, linear_words([(1, "zyzz"), (2, "zzyz"), (2, "zzzy")])),
        multiply(b, linear_words([(-1, "yzzx"), (-2, "zyyy"), (4, "zzyx"), (4, "zzzz")])),
        multiply(c, linear_words([(-1, "yyzz"), (-3, "yzzy"), (-1, "zzyy"), (-2, "zzzx")])),
        multiply(power(a, 2), word("zz")),
        multiply(power(b, 2), linear_words([(-1, "yz"), (3, "zy")])),
        multiply(power(c, 2), linear_words([(2, "yy"), (1, "zx")])),
        multiply(multiply(a, b), scale(2, word("zx"))),
        multiply(multiply(a, c), linear_words([(-1, "yz"), (-2, "zy")])),
        multiply(multiply(b, c), linear_words([(-1, "yx"), (-5, "zz")])),
    )
    return omega, zero, positive, reverse_yz(positive)


@lru_cache(None)
def parameter_exponents(degree):
    return tuple((a, b, degree-a-b) for a in range(degree+1) for b in range(degree-a+1))


@lru_cache(None)
def all_words(degree):
    return tuple(product(range(3), repeat=degree))


def homogeneous_monomials(degree):
    return tuple((p, w) for n in range(degree, -1, -1) if (degree-n) % 2 == 0
                 for w in all_words(n) for p in parameter_exponents((degree-n)//2))


def relations():
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        p = tuple(int(h == i) for h in range(3))
        yield ((ZERO, (j, k), 1), (ZERO, (k, j), -1),
               (ZERO, (i, i), -1), (p, (), 1))


@lru_cache(None)
def relation_reducer(degree):
    monomials = homogeneous_monomials(degree)
    positions = {m: i for i, m in enumerate(monomials)}
    echelon = {}

    def reduce_vector(current):
        current = {j: Fraction(c) for j, c in current.items() if c}
        while current:
            pivot = next((j for j in sorted(current) if j in echelon), None)
            if pivot is None:
                break
            coefficient = current.pop(pivot)
            for j, c in echelon[pivot].items():
                if j == pivot:
                    continue
                value = current.get(j, 0)-coefficient*c
                if value:
                    current[j] = value
                else:
                    current.pop(j, None)
        return current

    number_rows = 0
    for length in range(degree-2, -1, -1):
        if (degree-2-length) % 2:
            continue
        for p in parameter_exponents((degree-2-length)//2):
            for left_degree in range(length+1):
                for left in all_words(left_degree):
                    for right in all_words(length-left_degree):
                        for relation in relations():
                            row = {positions[(tuple(a+b for a, b in zip(p, q)), left+w+right)]: c
                                   for q, w, c in relation}
                            row = reduce_vector(row)
                            if row:
                                pivot = min(row)
                                coefficient = row[pivot]
                                echelon[pivot] = {j: c/coefficient for j, c in row.items()}
                            number_rows += 1
    free = tuple(j for j in range(len(monomials)) if j not in echelon)

    def reduce_polynomial(polynomial):
        return reduce_vector({positions[m]: c for m, c in polynomial.items()})

    return monomials, free, reduce_polynomial, (number_rows, len(monomials), len(echelon))


def main():
    omega, zero, positive, negative = central_elements()
    for polynomial, degree in ((omega, 3), (zero, 6), (positive, 6), (negative, 6)):
        _, _, reduce, _ = relation_reducer(degree+1)
        for letter in ALPHABET:
            commutator = add(multiply(word(letter), polynomial), scale(-1, multiply(polynomial, word(letter))))
            assert not reduce(commutator)
    print("PASS: Omega, C0, C+, C- commute with x,y,z over QQ[a,b,c]")

    monomials, free, reduce, shape = relation_reducer(6)
    assert len(free) == 119
    assert len(relation_reducer(7)[1]) == 189
    pure = [j for j in free if monomials[j][0] == ZERO]
    assert len(pure) == 28
    vectors = []
    for polynomial in (power(omega, 2), zero, positive, negative):
        highest = {m: c for m, c in polynomial.items() if m[0] == ZERO}
        remainder = reduce(highest)
        vectors.append([remainder.get(j, 0) for j in pure])
    matrix = sp.Matrix(vectors)
    _, pivots = matrix.rref()
    assert len(pivots) == 4
    minor = matrix[:, list(pivots)]
    determinant = minor.det()
    column_words = ["".join(ALPHABET[i] for i in monomials[pure[j]][1]) for j in pivots]
    assert column_words == ["yyzzzy", "yzzyyy", "yzzzzy", "zzzyyy"]
    assert minor == sp.Matrix([[sp.Rational(4, 9), 0, 0, sp.Rational(4, 3)],
                              [0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, 0]])
    assert determinant == sp.Rational(-4, 9)
    assert shape == (1476, 1036, 917)
    assert relation_reducer(7)[3] == (5454, 3108, 2919)
    print("PASS: highest parts Omega_0^2,C0_0,C+_0,C-_0 are independent in S_6")
    print("  minor columns:", column_words)
    print("  minor:", minor.tolist(), "determinant:", determinant)
    print("PASS: universal relation spaces have dimensions", shape, relation_reducer(7)[3])
    print("  quotient dimensions: 119 at weight 6, 189 at weight 7")


if __name__ == "__main__":
    main()
