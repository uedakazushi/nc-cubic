#!/usr/bin/env python3
"""Exact finite identities for the mixed family's formal comparison kernel.

Requires SymPy.  Run from the repository root with
    python3 computations/verify_mixed_formal_kernel.py

The six alpha coefficients remain independent symbols.  This checks the PBW
overlap, the first curved bar homotopy, and the second potential jet.  It does
not verify all-degree PBW, formality, the whole A-infinity functor, or a kernel
at h=1; those are distinct assertions in the accompanying manuscript.
"""

from itertools import combinations, permutations

import sympy as sp


def main():
    xs = sp.symbols("x1 y1 z1 x2 y2 z2 u")
    x1, y1, z1, x2, y2, z2, u = xs
    alpha = sp.symbols("a1:7")
    h = sp.Symbol("h")
    weights = (sp.Integer(1), sp.Integer(100))
    P = x1 * y1 * z1 + 100 * x2 * y2 * z2
    F = sp.expand(
        sum(
            weights[block]
            * sum(xs[i] ** 3 / 3 - alpha[i] * u**2 * xs[i]
                  for i in range(3 * block, 3 * block + 3))
            for block in range(2)
        )
    )
    poisson = sp.zeros(7)
    for offset in (0, 3):
        for row, col, variable in ((1, 2, 0), (2, 0, 1), (0, 1, 2)):
            value = xs[offset + variable] ** 2 - alpha[offset + variable] * u**2
            poisson[offset + row, offset + col] = value
            poisson[offset + col, offset + row] = -value

    def equal(a, b=0):
        assert sp.expand(a - b) == 0, (a, b)

    # The relation space has a cyclic degree-three overlap for every h.
    relations = (
        {"yz": 1, "zy": -1, "xx": -h},
        {"zx": 1, "xz": -1, "yy": -h},
        {"xy": 1, "yx": -1, "zz": -h},
    )
    overlap = {}
    for variable, relation in zip("xyz", relations):
        for word, coefficient in relation.items():
            overlap[variable + word] = overlap.get(variable + word, 0) + coefficient
            overlap[word + variable] = overlap.get(word + variable, 0) - coefficient
    for coefficient in overlap.values():
        equal(coefficient)
    print("PASS: universal cyclic PBW overlap")

    # The displayed constant trivector contracts F to the input Poisson tensor.
    for block, weight in enumerate(weights):
        offset = 3 * block
        for row, col, variable in ((1, 2, 0), (2, 0, 1), (0, 1, 2)):
            equal(sp.diff(F, xs[offset + variable]) / weight,
                  poisson[offset + row, offset + col])
    for entry in poisson * sp.Matrix([sp.diff(F, x) for x in xs]):
        equal(entry)
    for i, j, k in combinations(range(7), 3):
        jacobi = sum(
            poisson[i, ell] * sp.diff(poisson[j, k], xs[ell])
            + poisson[j, ell] * sp.diff(poisson[k, i], xs[ell])
            + poisson[k, ell] * sp.diff(poisson[i, j], xs[ell])
            for ell in range(7)
        )
        equal(jacobi)
    print("PASS: Poisson Jacobi identity, Casimir, and constant-trivector primitive")

    def sign(permutation):
        return (-1) ** sum(
            permutation[i] > permutation[j]
            for i in range(3) for j in range(i + 1, 3)
        )

    def hkr_trivector(a, b, c):
        value = 0
        for block, weight in enumerate(weights):
            coordinates = xs[3 * block:3 * block + 3]
            for permutation in permutations(range(3)):
                value += (
                    sign(permutation)
                    * sp.diff(a, coordinates[permutation[0]])
                    * sp.diff(b, coordinates[permutation[1]])
                    * sp.diff(c, coordinates[permutation[2]])
                    / (6 * weight)
                )
        return sp.expand(value)

    # [HKR(Xi)/t,-tF] is -one-half of the Poisson biderivation.
    for i, a in enumerate(xs):
        for j, b in enumerate(xs):
            insertion = (
                hkr_trivector(F, a, b)
                - hkr_trivector(a, F, b)
                + hkr_trivector(a, b, F)
            )
            equal(insertion, poisson[i, j] / 2)
    print("PASS: normalized first curved bar homotopy on all coordinate pairs")

    theta = sp.Matrix(7, 7, lambda i, k: sp.expand(sum(
        sp.diff(poisson[i, j], xs[ell]) * sp.diff(poisson[k, ell], xs[j])
        for j in range(7) for ell in range(7)
    )))
    expected_theta = -8 * sp.diag(
        y1 * z1, z1 * x1, x1 * y1,
        y2 * z2, z2 * x2, x2 * y2, 0,
    )
    assert theta == expected_theta
    print("PASS: universal seven-variable eye-contraction matrix")

    rho_F = sp.expand(-sum(
        theta[i, k] * sp.diff(F, xs[i], xs[k])
        for i in range(7) for k in range(7)
    ) / 48)
    equal(rho_F, P)
    equal(rho_F - sp.Rational(2, 3) * P, P / 3)
    print("PASS: Weyl eye correction and recovered quadratic potential coefficient")

    candidate = F + h**2 * P / 3
    equal(candidate.subs(u, -u), candidate)
    equal(sp.diff(candidate, h).subs(h, 0))
    equal(sp.diff(candidate, h, 2).subs(h, 0) / 2, P / 3)
    print("PASS: commutative candidate jet and reflection invariance")

    def witness(polynomial):
        return sp.Poly(polynomial, *xs).coeff_monomial(x1 * y1 * z1)

    for a in xs:
        for b in xs:
            equal(witness(a * sp.diff(F, b)))
    equal(witness(P), 1)
    print("PASS: nonzero Jacobian class witnessed against all 49 cubic generators")
    # Auxiliary weight forces either a pure active cubic, or u^2 alpha_i x_j.
    def degree_three_triples():
        return [(i, j, 3 - i - j) for i in range(4) for j in range(4 - i)]

    allowed = [(xyz + (0, 0, 0)) for xyz in degree_three_triples()]
    for i in range(3):
        for j in range(3):
            xyz = tuple(int(k == i) for k in range(3))
            a_exponents = tuple(int(k == j) for k in range(3))
            allowed.append(xyz + a_exponents)
    diagonal_weights = (0, 1, 2, 0, 2, 1)
    diagonal_invariants = {
        exponent for exponent in allowed
        if sum(a * b for a, b in zip(exponent, diagonal_weights)) % 3 == 0
    }

    def cycle(exponent):
        x, y, z, a, b, c = exponent
        return z, x, y, c, a, b

    orbits = []
    while diagonal_invariants:
        exponent = next(iter(diagonal_invariants))
        orbit = frozenset((exponent, cycle(exponent), cycle(cycle(exponent))))
        assert orbit <= diagonal_invariants
        orbits.append(orbit)
        diagonal_invariants.difference_update(orbit)
    assert sorted(len(orbit) for orbit in orbits) == [1, 3, 3]
    assert frozenset(((1, 1, 1, 0, 0, 0),)) in orbits
    print("PASS: universal auxiliary-weight and Heisenberg invariant space has dimension three")

    s = sp.Symbol("s")
    j_function = 27 * s * (8 - s) ** 3 / (1 + s) ** 3
    equal(sp.diff(j_function, s).subs(s, 0), 13824)
    assert sp.cancel(j_function.subs(s, h**6 / 27)
                     - h**6 * (216 - h**6) ** 3 / (27 + h**6) ** 3) == 0
    A, C = sp.symbols("A C", nonzero=True)
    L = sum(weights[block] * sum(alpha[i] * xs[i]
            for i in range(3 * block, 3 * block + 3)) for block in range(2))
    G = sp.expand(F + u**2 * L)
    universal_target = A**3 * G + A**3 * h**2 * P / 3 - A * C**2 * u**2 * L
    change = {x: x / A for x in xs[:6]}
    change[u] = u / C
    equal(universal_target.subs(change, simultaneous=True), candidate)
    print("PASS: Hesse-j local inverse and common-coordinate normalization")
    print("LIMIT: finite identities only; all-order functor and descent require the manuscript proofs")
    print("LIMIT: no h=1 kernel specialization is verified")


if __name__ == "__main__":
    main()
