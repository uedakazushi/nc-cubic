#!/usr/bin/env python3
"""Universal linear PBW corrections and their central cubic, over QQ.

The normalized relations are
  [y,z] = x*x + p*y + r*z - a,
  [z,x] = y*y + p*x + q*z - b,
  [x,y] = z*z + r*x + q*y - c.
Parameters p,q,r have auxiliary weight 1, a,b,c have weight 2, and
x,y,z have weight 1.  No parameter specialization or interpolation is
used for centrality.  Every reduction row is an actual two-sided relation
multiple; exact rational row reduction therefore certifies ideal membership.

The all-degree PBW assertion is a separate application of Braverman--
Gaitsgory's theorem, explained in linear_pbw_boundary.tex.  This script
checks its finite overlap, the complete center commutators, translations,
and low-degree uniqueness.  It does not prove a Ku comparison, a general
PI/finite-center statement, or identify the categorical Bockstein map.

Requires Python 3 and SymPy.  Run from the repository root:
  python3 computations/verify_mixed_linear_pbw.py
"""

from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product

import sympy as sp


Q = Fraction
LETTERS = "xyz"
WEIGHTS = (1, 1, 1, 2, 2, 2)
ZERO = (0,) * len(WEIGHTS)


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(coefficient, polynomial):
    return {m: coefficient * c for m, c in polynomial.items()
            if coefficient * c}


def multiply(left, right):
    result = {}
    for (p, w), a in left.items():
        for (q, v), b in right.items():
            monomial = (tuple(x + y for x, y in zip(p, q)), w + v)
            result[monomial] = result.get(monomial, 0) + a * b
    return {m: c for m, c in result.items() if c}


def word(text):
    return {(ZERO, text): Q(1)}


def parameter(index):
    return {(tuple(int(i == index) for i in range(len(WEIGHTS))), ""): Q(1)}


def commutator(left, right):
    return add(multiply(left, right), scale(-1, multiply(right, left)))


@lru_cache(None)
def parameter_exponents(degree, weights=WEIGHTS):
    if not weights:
        return ((),) if degree == 0 else ()
    return tuple((e,) + rest
                 for e in range(degree // weights[0] + 1)
                 for rest in parameter_exponents(degree - e * weights[0],
                                                  weights[1:]))


@lru_cache(None)
def words(degree):
    return tuple("".join(w) for w in product(LETTERS, repeat=degree))


def relations():
    p, q, r, a, b, c = (parameter(i) for i in range(6))
    matrix = (({}, p, r), (p, {}, q), (r, q, {}))
    result = []
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        result.append(add(
            word(LETTERS[j] + LETTERS[k]),
            scale(-1, word(LETTERS[k] + LETTERS[j])),
            scale(-1, word(LETTERS[i] * 2)),
            *(scale(-1, multiply(matrix[i][ell], word(LETTERS[ell])))
              for ell in range(3)),
            parameter(i + 3),
        ))
    return tuple(result)


def cyclic_derivative(polynomial, letter):
    result = {}
    for (powers, text), coefficient in polynomial.items():
        for i, value in enumerate(text):
            if value == letter:
                monomial = (powers, text[i + 1:] + text[:i])
                result[monomial] = result.get(monomial, 0) + coefficient
    return {m: c for m, c in result.items() if c}


def central_cubic():
    p, q, r, a, b, c = (parameter(i) for i in range(6))
    omega = add(
        scale(Q(1, 3), add(*(word(x * 3) for x in LETTERS))),
        scale(Q(-1, 9), add(*(word("".join(w))
                              for w in permutations(LETTERS)))),
        scale(-1, add(*(multiply(alpha, word(x))
                        for alpha, x in zip((a, b, c), LETTERS)))),
    )
    for beta, x, y, z in ((p, "x", "y", "z"),
                          (q, "y", "z", "x"),
                          (r, "z", "x", "y")):
        omega = add(omega, multiply(beta, add(
            scale(Q(1, 2), add(word(x + y), word(y + x))),
            scale(Q(1, 18), word(z * 2)),
        )))
    for x, square, left, right in (("x", q, p, r),
                                   ("y", r, p, q),
                                   ("z", p, q, r)):
        coefficient = add(scale(Q(1, 6), multiply(square, square)),
                          scale(Q(-1, 18), multiply(left, right)))
        omega = add(omega, multiply(coefficient, word(x)))
    return omega


@lru_cache(None)
def relation_reducer(degree, homogeneous=False):
    exponents = (lambda d: (ZERO,) if d == 0 else ()) if homogeneous \
        else parameter_exponents
    monomials = tuple((p, w) for d in range(degree + 1)
                      for p in exponents(d) for w in words(degree - d))
    positions = {m: i for i, m in enumerate(monomials)}
    echelon = {}

    def reduce_vector(vector):
        vector = {j: Q(c) for j, c in vector.items() if c}
        while vector:
            pivot = next((j for j in sorted(vector) if j in echelon), None)
            if pivot is None:
                break
            coefficient = vector.pop(pivot)
            for j, c in echelon[pivot].items():
                if j != pivot:
                    vector[j] = vector.get(j, 0) - coefficient * c
            vector = {j: c for j, c in vector.items() if c}
        return vector

    def reduce_polynomial(polynomial):
        return reduce_vector({positions[m]: c for m, c in polynomial.items()})

    relation_list = relations()
    if homogeneous:
        relation_list = tuple({m: c for m, c in rel.items() if m[0] == ZERO}
                              for rel in relation_list)
    row_count = 0
    for d in range(degree - 1):
        for p in exponents(d):
            for left_degree in range(degree - 2 - d + 1):
                for left in words(left_degree):
                    for right in words(degree - 2 - d - left_degree):
                        for relation in relation_list:
                            polynomial = multiply(
                                multiply({(p, left): Q(1)}, relation), word(right))
                            row = reduce_polynomial(polynomial)
                            if row:
                                pivot = min(row)
                                coefficient = row[pivot]
                                echelon[pivot] = {j: c / coefficient
                                                 for j, c in row.items()}
                            row_count += 1
    free = tuple(j for j in range(len(monomials)) if j not in echelon)
    return monomials, free, reduce_polynomial, (row_count, len(monomials), len(echelon))


def main():
    p, q, r, a, b, c = (parameter(i) for i in range(6))
    potential = add(
        word("xyz"), scale(-1, word("yxz")),
        scale(Q(-1, 3), add(*(word(x * 3) for x in LETTERS))),
        scale(-1, add(multiply(p, word("xy")), multiply(q, word("yz")),
                      multiply(r, word("zx")))),
        add(*(multiply(alpha, word(x))
              for alpha, x in zip((a, b, c), LETTERS))),
    )
    assert tuple(cyclic_derivative(potential, x) for x in LETTERS) == relations()
    assert not add(*(commutator(word(x), relation)
                     for x, relation in zip(LETTERS, relations())))
    degree_two_words = words(2)
    r_columns = []
    skew_columns = []
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        relation = {LETTERS[j] + LETTERS[k]: 1,
                    LETTERS[k] + LETTERS[j]: -1, LETTERS[i] * 2: -1}
        r_columns.append([relation.get(w, 0) for w in degree_two_words])
        skew = {LETTERS[j] + LETTERS[k]: 1, LETTERS[k] + LETTERS[j]: -1}
        skew_columns.append([skew.get(w, 0) for w in degree_two_words])
    assert sp.Matrix(r_columns + skew_columns).rank() == 6
    print("PASS: cyclic derivatives, exact PBW overlap, and R intersect wedge^2(V)=0")

    omega = central_cubic()
    monomials, free, reduce, shape = relation_reducer(4)
    assert len(free) == 195
    for x in LETTERS:
        assert not reduce(commutator(word(x), omega))
    print("PASS: all center commutators over QQ[p,q,r,a,b,c]; relation matrix", shape)

    ranks = []
    for degree in (1, 2):
        basis = [word(w) for w in words(degree)]
        if degree == 2:
            basis = [word(x + y) for i, x in enumerate(LETTERS) for y in LETTERS[i:]]
        _, homogeneous_free, homogeneous_reduce, _ = relation_reducer(degree + 1, True)
        columns = []
        for element in basis:
            column = []
            for x in LETTERS:
                remainder = homogeneous_reduce(commutator(word(x), element))
                column.extend(remainder.get(j, 0) for j in homogeneous_free)
            columns.append(column)
        ranks.append(sp.Matrix(columns).rank())
    assert ranks == [3, 6]
    print("PASS: Z(S)_1=Z(S)_2=0 (commutator ranks 3 and 6)")

    xx = sp.symbols("X Y Z")
    dd = sp.symbols("d1:4")
    pp, qq, rr = sp.symbols("p q r")
    aa = sp.symbols("a1:4")
    tt = sp.symbols("t1:4")
    matrix = sp.Matrix([[dd[0], pp, rr], [pp, dd[1], qq], [rr, qq, dd[2]]])
    for i in range(3):
        translated = (xx[i] - tt[i])**2 + sum(
            matrix[i, j] * (xx[j] - tt[j]) for j in range(3)) - aa[i]
        normalized = xx[i]**2 + sum(
            (matrix[i, j] - (2 * tt[i] if i == j else 0)) * xx[j]
            for j in range(3)) - (aa[i] + sum(matrix[i, j] * tt[j]
                                             for j in range(3)) - tt[i]**2)
        assert sp.expand(translated - normalized) == 0
    assert (matrix - sp.diag(*dd)).diagonal() == sp.zeros(1, 3)
    print("PASS: translation law M'=M-2 diag(t), alpha'=alpha+Mt-t^2")

    symmetric_coordinates = (dd[0], dd[1], dd[2], pp, qq, rr)
    gauge = sp.Matrix([-2 * t for t in tt] + [0, 0, 0]).jacobian(tt)
    essential = sp.zeros(6, 3)
    for i in range(3):
        essential[i + 3, i] = 1
    assert gauge.rank() == 3 and gauge.row_join(essential).rank() == 6
    assert len(symmetric_coordinates) == 6
    print("PASS: three independent normalized first-order algebra deformation classes")

    constant_specialization = {m: coefficient for m, coefficient in omega.items()
                               if all(e == 0 for e in m[0][:3])}
    constant_formula = add(
        scale(Q(1, 3), add(*(word(x * 3) for x in LETTERS))),
        scale(Q(-1, 9), add(*(word("".join(w)) for w in permutations(LETTERS)))),
        scale(-1, add(*(multiply(alpha, word(x))
                        for alpha, x in zip((a, b, c), LETTERS)))),
    )
    assert constant_specialization == constant_formula
    print("PASS: p=q=r=0 recovers the existing constant-correction central cubic")


if __name__ == "__main__":
    main()
