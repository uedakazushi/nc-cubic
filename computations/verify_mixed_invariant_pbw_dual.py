#!/usr/bin/env python3
"""Exact finite checks for the PBW dual of D = B^(u -> -u).

Requires Python 3 and SymPy.  The auxiliary PBW filtration assigns degree one
to all six active generators and v; the original internal weights are 1 and 2.
This checks the 128-dimensional uncurved quadratic-linear dual, its differential,
and its 80-dimensional cohomology.  It does not construct the curved model for
(D, w), a Knorrer kernel, Hochschild homology, or a Kuznetsov equivalence.
"""

from collections import defaultdict
from itertools import product

import sympy as sp


ALPHAS = ((1, 4, 9), (16, 25, 49))
LETTERS = "abc"


def clean(vector):
    return {key: value for key, value in vector.items() if value}


def add(*vectors):
    result = defaultdict(lambda: sp.S.Zero)
    for vector in vectors:
        for key, value in vector.items():
            result[key] += value
    return clean(result)


def scale(vector, scalar):
    return clean({key: scalar * value for key, value in vector.items()})


def word_quotients():
    """Build S! directly from the orthogonal complement of the S relations."""
    words2 = ["".join(w) for w in product(LETTERS, repeat=2)]
    positions2 = {word: i for i, word in enumerate(words2)}
    original_relations = (
        {"bc": 1, "cb": -1, "aa": -1},
        {"ca": 1, "ac": -1, "bb": -1},
        {"ab": 1, "ba": -1, "cc": -1},
    )
    original = sp.zeros(3, 9)
    for i, relation in enumerate(original_relations):
        for word, coefficient in relation.items():
            original[i, positions2[word]] = coefficient
    dual_relations = [
        {words2[i]: vector[i] for i in range(9) if vector[i]}
        for vector in original.nullspace()
    ]
    assert len(dual_relations) == 6

    basis_by_degree = {}
    normal = {}
    for degree in range(5):
        words = ["".join(w) for w in product(LETTERS, repeat=degree)]
        position = {word: i for i, word in enumerate(words)}
        rows = []
        for left_degree in range(max(0, degree - 1)):
            right_degree = degree - left_degree - 2
            for left in product(LETTERS, repeat=left_degree):
                for right in product(LETTERS, repeat=right_degree):
                    for relation in dual_relations:
                        row = [sp.S.Zero] * len(words)
                        for word, coefficient in relation.items():
                            row[position["".join(left) + word + "".join(right)]] += coefficient
                        rows.append(row)
        matrix = sp.Matrix(rows) if rows else sp.zeros(0, len(words))
        reduced, pivots = matrix.rref()
        free = [j for j in range(len(words)) if j not in pivots]
        basis_by_degree[degree] = [words[j] for j in free]
        pivot_rows = {pivot: i for i, pivot in enumerate(pivots)}
        for j, word in enumerate(words):
            if j in free:
                normal[word] = {word: sp.S.One}
            else:
                row = pivot_rows[j]
                normal[word] = {
                    words[k]: -reduced[row, k] for k in free if reduced[row, k]
                }
    return basis_by_degree, normal


BASIS_BY_DEGREE, NORMAL = word_quotients()
ONE_BASIS = [word for degree in range(4) for word in BASIS_BY_DEGREE[degree]]


def one_multiply(left, right):
    result = defaultdict(lambda: sp.S.Zero)
    for a, ca in left.items():
        for b, cb in right.items():
            if len(a) + len(b) >= 4:
                continue
            for word, coefficient in NORMAL[a + b].items():
                result[word] += ca * cb * coefficient
    return clean(result)


F_BASIS = list(product(ONE_BASIS, repeat=2))


def f_degree(basis_element):
    return len(basis_element[0]) + len(basis_element[1])


def f_multiply(left, right):
    result = defaultdict(lambda: sp.S.Zero)
    for (a, b), left_coefficient in left.items():
        for (c, d), right_coefficient in right.items():
            sign = (-1) ** (len(b) * len(c))
            for ac, first_coefficient in one_multiply({a: 1}, {c: 1}).items():
                for bd, second_coefficient in one_multiply({b: 1}, {d: 1}).items():
                    result[(ac, bd)] += (
                        sign * left_coefficient * right_coefficient
                        * first_coefficient * second_coefficient
                    )
    return clean(result)


def q_element():
    result = {}
    for block, alpha in enumerate(ALPHAS):
        for letter, coefficient in zip(LETTERS, alpha):
            for word, scalar in NORMAL[letter + letter].items():
                key = (word, "") if block == 0 else ("", word)
                result = add(result, {key: -coefficient * scalar})
    return result


Q = q_element()
E_BASIS = [(a, b, epsilon) for a, b in F_BASIS for epsilon in (0, 1)]


def cohomological_degree(element):
    a, b, epsilon = element
    return len(a) + len(b) + epsilon


def internal_weight(element):
    a, b, epsilon = element
    return len(a) + len(b) + 2 * epsilon


def differential(element):
    a, b, epsilon = element
    if not epsilon:
        return {}
    sign = (-1) ** (len(a) + len(b))
    return {
        (c, d, 0): sign * coefficient
        for (c, d), coefficient in f_multiply({(a, b): 1}, Q).items()
    }


def exact_matrix(source, target, function):
    positions = {element: i for i, element in enumerate(target)}
    matrix = sp.zeros(len(target), len(source))
    for column, element in enumerate(source):
        for image, coefficient in function(element).items():
            assert image in positions
            matrix[positions[image], column] += coefficient
    return matrix


def main():
    assert [len(BASIS_BY_DEGREE[d]) for d in range(5)] == [1, 3, 3, 1, 0]
    for a, b, c in product(ONE_BASIS, repeat=3):
        assert one_multiply(one_multiply({a: 1}, {b: 1}), {c: 1}) == one_multiply(
            {a: 1}, one_multiply({b: 1}, {c: 1})
        )
    print("PASS: one-block quadratic dual derived from relation orthogonals; dimensions 1,3,3,1")

    assert len(F_BASIS) == 64 and len(E_BASIS) == 128
    for element in F_BASIS:
        assert f_multiply(Q, {element: 1}) == f_multiply({element: 1}, Q)
    for element in E_BASIS:
        image = differential(element)
        assert all(cohomological_degree(x) == cohomological_degree(element) + 1 for x in image)
        assert all(internal_weight(x) == internal_weight(element) for x in image)
        assert not add(*(scale(differential(x), coefficient) for x, coefficient in image.items()))
    print("PASS: d(epsilon_v)=-sum alpha_j xi_j^2 is central, has bidegree (1,0), and d^2=0")

    ranks = []
    for degree in range(5):
        source = [element for element in F_BASIS if f_degree(element) == degree]
        target = [element for element in F_BASIS if f_degree(element) == degree + 2]
        matrix = exact_matrix(source, target, lambda element: f_multiply({element: 1}, Q))
        ranks.append(matrix.rank())
    assert ranks == [1, 6, 10, 6, 1]
    print("PASS: multiplication by q has degreewise ranks (1,6,10,6,1), total 24")

    dimensions = defaultdict(int)
    differential_ranks = defaultdict(int)
    for degree in range(8):
        for weight in range(9):
            source = [e for e in E_BASIS if (cohomological_degree(e), internal_weight(e)) == (degree, weight)]
            target = [e for e in E_BASIS if (cohomological_degree(e), internal_weight(e)) == (degree + 1, weight)]
            dimensions[(degree, weight)] = len(source)
            differential_ranks[(degree, weight)] = exact_matrix(source, target, differential).rank()
    cohomology = {
        (degree, weight): dimensions[(degree, weight)]
        - differential_ranks[(degree, weight)] - differential_ranks[(degree - 1, weight)]
        for degree in range(8) for weight in range(9)
    }
    cohomology = {key: value for key, value in cohomology.items() if value}
    expected = {
        (0, 0): 1, (1, 1): 6, (2, 2): 14, (3, 3): 14, (3, 4): 5,
        (4, 4): 5, (4, 5): 14, (5, 6): 14, (6, 7): 6, (7, 8): 1,
    }
    assert cohomology == expected
    betti = [sum(value for (d, _), value in cohomology.items() if d == degree) for degree in range(8)]
    assert betti == [1, 6, 14, 19, 19, 14, 6, 1] and sum(betti) == 80
    print("PASS: cohomology has dimension 80 and Betti numbers (1,6,14,19,19,14,6,1)")

    t = sp.Symbol("t")
    euler = sum((-1) ** degree * dimension * t ** weight for (degree, weight), dimension in cohomology.items())
    assert sp.expand(euler - (1 - t) ** 6 * (1 - t ** 2)) == 0
    print("PASS: internally graded Euler polynomial equals (1-t)^6(1-t^2)")
    print("Bigraded cohomology (cohomological degree, internal weight):")
    for key, value in sorted(cohomology.items()):
        print(f"  {key}: {value}")
    print("Scope: uncurved ambient PBW dual only; curved w-model and comparison kernel remain unconstructed.")


if __name__ == "__main__":
    main()
