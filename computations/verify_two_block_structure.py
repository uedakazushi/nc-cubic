#!/usr/bin/env python3
"""Exact finite checks for the two-block cubic presentation.

Run from the repository root with Python 3 and SymPy.  All linear algebra is
over QQ, starting from the defining quadratic relations, without inserting a
precomputed central cubic.  This checks two explicit factors through degree 4,
the low-degree centers of their tensor product and central quotient, and the
finite Heisenberg central product.  It does not prove the general statements,
the scheme-theoretic point-module calculation, or categorical equivalences.
"""

from itertools import product
from math import comb
import json

import sympy as sp


def quotient_map(rows, width):
    """Return reduction to a quotient basis, and the basis column indices."""
    if not rows:
        return sp.eye(width), list(range(width))
    echelon, pivots = sp.Matrix(rows).rref()
    free = [j for j in range(width) if j not in pivots]
    reduction = sp.zeros(len(free), width)
    for j, col in enumerate(free):
        reduction[j, col] = 1
    for row, pivot in enumerate(pivots):
        for j, col in enumerate(free):
            reduction[j, pivot] = -echelon[row, col]
    return reduction, free


class Sklyanin:
    def __init__(self, parameters):
        self.parameters = tuple(parameters)
        a, b, c = self.parameters
        # These are precisely the smoothness conditions for the Hesse point
        # cubic abc*(x^3+y^3+z^3)-(a^3+b^3+c^3)*xyz.
        assert a * b * c != 0
        assert (a**3 + b**3 + c**3)**3 != 27 * (a*b*c)**3
        self.words, self.index, self.reduce, self.basis = {}, {}, {}, {}
        for degree in range(5):
            words = list(product(range(3), repeat=degree))
            index = {word: i for i, word in enumerate(words)}
            rows = []
            for position in range(degree - 1):
                for before in product(range(3), repeat=position):
                    for after in product(range(3), repeat=degree-position-2):
                        for i in range(3):
                            j, k = (i+1) % 3, (i+2) % 3
                            row = [0] * len(words)
                            for coefficient, middle in ((a, (j, k)), (b, (k, j)), (c, (i, i))):
                                row[index[before+middle+after]] += coefficient
                            rows.append(row)
            reduction, free = quotient_map(rows, len(words))
            self.words[degree], self.index[degree] = words, index
            self.reduce[degree] = reduction
            self.basis[degree] = [words[i] for i in free]
            assert len(free) == comb(degree+2, 2)
        self.left, self.right = {}, {}
        for degree in range(4):
            for generator in range(3):
                for side, table in (("left", self.left), ("right", self.right)):
                    columns = []
                    for word in self.basis[degree]:
                        new = (generator,)+word if side == "left" else word+(generator,)
                        columns.append(self.reduce[degree+1][:, self.index[degree+1][new]])
                    table[degree, generator] = sp.Matrix.hstack(*columns)
        commutators = sp.Matrix.vstack(*(self.left[3, i]-self.right[3, i] for i in range(3)))
        kernel = commutators.nullspace()
        assert len(kernel) == 1
        central = kernel[0]
        scale = sp.ilcm(*(v.q for v in central))
        central = central * scale
        divisor = sp.igcd(*(int(v) for v in central))
        self.omega = central / divisor
        # Check the standard H_3 generators on this computed central element.
        cycle = sp.zeros(len(self.basis[3]), 1)
        for col, word in enumerate(self.basis[3]):
            new = tuple((i+1) % 3 for i in word)
            cycle += self.omega[col] * self.reduce[3][:, self.index[3][new]]
        assert cycle == self.omega
        for col, word in enumerate(self.basis[3]):
            if self.omega[col]:
                assert sum(word) % 3 == 0  # diag(1,zeta,zeta^2)


class TensorProduct:
    def __init__(self, first, second):
        self.factors = (first, second)
        self.basis, self.index = {}, {}
        for degree in range(5):
            basis = [(p, i, j) for p in range(degree+1)
                     for i in range(len(first.basis[p]))
                     for j in range(len(second.basis[degree-p]))]
            self.basis[degree] = basis
            self.index[degree] = {v: i for i, v in enumerate(basis)}
            assert len(basis) == comb(degree+5, 5)
        self.left, self.right = {}, {}
        for degree in range(4):
            for generator in range(6):
                factor, local_generator = divmod(generator, 3)
                for side, table in (("left", self.left), ("right", self.right)):
                    matrix = sp.zeros(len(self.basis[degree+1]), len(self.basis[degree]))
                    for col, (p, i, j) in enumerate(self.basis[degree]):
                        local_degree = p if factor == 0 else degree-p
                        multiplication = getattr(self.factors[factor], side)[local_degree, local_generator]
                        local_index = i if factor == 0 else j
                        for row in range(multiplication.rows):
                            value = multiplication[row, local_index]
                            if value:
                                target = (p+1, row, j) if factor == 0 else (p, i, row)
                                matrix[self.index[degree+1][target], col] = value
                    table[degree, generator] = matrix
        self.centers = []
        for factor in range(2):
            vector = sp.zeros(len(self.basis[3]), 1)
            for i, value in enumerate(self.factors[factor].omega):
                target = (3, i, 0) if factor == 0 else (0, 0, i)
                vector[self.index[3][target]] = value
            self.centers.append(vector)

    def commutator(self, degree, reduction=None):
        reduction = sp.eye(len(self.basis[degree+1])) if reduction is None else reduction
        return sp.Matrix.vstack(*(reduction*(self.left[degree, g]-self.right[degree, g])
                                  for g in range(6)))


def heisenberg_check():
    # H_3 x H_3 / diagonal central F_3.  Representatives have last central
    # coordinate 0; c is the difference of the two original central entries.
    elements = list(product(range(3), repeat=5))

    def multiply(x, y):
        a, b, u, v, c = x
        A, B, U, V, C = y
        return ((a+A) % 3, (b+B) % 3, (u+U) % 3, (v+V) % 3,
                (c+C+a*B-u*V) % 3)

    zero = (0, 0, 0, 0, 0)
    generators = [(1, 0, 0, 0, 0), (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 0), (0, 0, 0, 1, 0)]
    reached, frontier = {zero}, [zero]
    while frontier:
        x = frontier.pop()
        for g in generators:
            y = multiply(x, g)
            if y not in reached:
                reached.add(y)
                frontier.append(y)
    assert len(reached) == 243
    center = [x for x in elements if all(multiply(x, g) == multiply(g, x) for g in generators)]
    assert len(center) == 3
    assert all(multiply(multiply(x, x), x) == zero for x in elements)
    return {"order": len(reached), "center_order": len(center), "exponent": 3}


def main():
    factors = [Sklyanin((1, 2, 3)), Sklyanin((1, 3, 4))]
    tensor = TensorProduct(*factors)
    ambient_centers = {}
    for degree in (1, 2, 3):
        matrix = tensor.commutator(degree)
        ambient_centers[str(degree)] = matrix.cols - matrix.rank()
    assert ambient_centers == {"1": 0, "2": 0, "3": 2}
    w = tensor.centers[0] + tensor.centers[1]
    assert tensor.commutator(3)*w == sp.zeros(6*len(tensor.basis[4]), 1)
    ideal = {0: [], 1: [], 2: [], 3: [list(w)],
             4: [list(tensor.right[3, g]*w) for g in range(6)]}
    reductions = {d: quotient_map(rows, len(tensor.basis[d]))[0] for d, rows in ideal.items()}
    quotient_centers, quotient_hilbert = {}, []
    for degree in range(5):
        quotient_hilbert.append(reductions[degree].rows)
    assert quotient_hilbert == [1, 6, 21, 55, 120]
    for degree in (1, 2, 3):
        matrix = tensor.commutator(degree, reductions[degree+1])
        quotient_centers[str(degree)] = reductions[degree].rows - matrix.rank()
    assert quotient_centers == {"1": 0, "2": 0, "3": 1}
    # μ_3 invariant cubic monomials: exactly the two pure cubic blocks.
    exponents = [e for e in product(range(4), repeat=6) if sum(e) == 3]
    invariants = [e for e in exponents if sum(e[3:]) % 3 == 0]
    assert len(invariants) == 20
    assert all(sum(e[:3]) == 0 or sum(e[3:]) == 0 for e in invariants)
    print(json.dumps({
        "field": "QQ", "parameters": [s.parameters for s in factors],
        "factor_hilbert_through_4": [len(factors[0].basis[d]) for d in range(5)],
        "ambient_center_dimensions": ambient_centers,
        "quotient_hilbert_through_4": quotient_hilbert,
        "quotient_center_dimensions": quotient_centers,
        "central_product": heisenberg_check(),
        "invariant_cubic_dimension": len(invariants),
        "scope": "exact finite checks only; general theorems require the written proofs"
    }, indent=2))


if __name__ == "__main__":
    main()
