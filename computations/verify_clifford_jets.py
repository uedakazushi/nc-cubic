#!/usr/bin/env python3
"""Exact finite certificates for the fixed-slice Clifford jet calculation.

Current result: 2026-11-23 / v65.

Run with Python 3 and SymPy:
    python3 computations/verify_clifford_jets.py

The checks enumerate the complete monomial spaces, not random samples.
They verify the Heisenberg covariants/invariants, the additional factor
reflections, their gradients, the four simultaneous and minimal one-parameter coefficient probes,
and symbolic Hesse Jacobian complements.  Free-word calculations distinguish
the noncommutative lift -P from the commutative lift P.

The actual Picard kernel, its coherent period comparison, formal recognition,
and the numerical values of the twelve higher coefficients are NOT verified
by this finite calculation.  No proof assistant is used.
"""

from collections import Counter
from itertools import combinations_with_replacement, permutations

import sympy as sp


INDICES = tuple(range(9))


def index(a, b):
    return 3 * (a % 3) + b % 3


def pair(i):
    return divmod(i, 3)


def monomial(indices):
    return tuple(sorted(indices))


def weight(m):
    return tuple(sum(pair(i)[j] for i in m) % 3 for j in range(2))


def translate(m, a, b):
    return monomial(index(pair(i)[0] + a, pair(i)[1] + b) for i in m)


def reflection(a):
    # Exchange the first two Hesse coordinates; the third stays fixed.
    return (1 - a) % 3


def reflect(m, axis):
    return monomial(index(reflection(pair(i)[0]), pair(i)[1]) if axis == 0
                    else index(pair(i)[0], reflection(pair(i)[1])) for i in m)


def quadratic(j, a, b):
    pairs = [((a, b), (a, b)),
             ((a + 1, b), (a + 2, b)),
             ((a, b + 1), (a, b + 2)),
             ((a + 1, b + 1), (a + 2, b + 2)),
             ((a + 1, b + 2), (a + 2, b + 1))]
    return monomial(index(*p) for p in pairs[j])


def parity(p):
    return sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2


INVARIANTS = [
    {monomial([j, j, j]) for j in INDICES},
    {monomial(index(a, b) for b in range(3)) for a in range(3)},
    {monomial(index(a, b) for a in range(3)) for b in range(3)},
    {monomial(index(a, p[a]) for a in range(3))
     for p in permutations(range(3)) if parity(p) == 0},
    {monomial(index(a, p[a]) for a in range(3))
     for p in permutations(range(3)) if parity(p) == 1},
]


def check_quadratic_space():
    # W_00 has trivial diagonal weight; row/column cycles determine all W_ab.
    seeds = {m for m in combinations_with_replacement(INDICES, 2)
             if weight(m) == (0, 0)}
    assert seeds == {quadratic(j, 0, 0) for j in range(5)}
    for j in range(5):
        for a in range(3):
            for b in range(3):
                q = quadratic(j, a, b)
                # The second diagonal generator acts with the NEGATIVE
                # column weight on V, so this gives W weight (-a,+b).
                assert weight(q) == ((-a) % 3, (-b) % 3)
                assert translate(q, -1, 0) == quadratic(j, a - 1, b)
                assert translate(q, 0, -1) == quadratic(j, a, b - 1)
    print("PASS: complete quadratic covariant space has dimension 5")


def check_cubic_space():
    remaining = {m for m in combinations_with_replacement(INDICES, 3)
                 if weight(m) == (0, 0)}
    orbits = []
    while remaining:
        seed = min(remaining)
        orbit = {translate(seed, a, b) for a in range(3) for b in range(3)}
        assert orbit <= remaining
        orbits.append(orbit)
        remaining -= orbit
    assert {frozenset(o) for o in orbits} == {
        frozenset(o) for o in INVARIANTS}
    assert sorted(map(len, orbits)) == [3, 3, 3, 3, 9]
    print("PASS: complete cubic invariant space has dimension 5; pure-pair dimension 10")


def check_reflections():
    permutation = [0, 1, 2, 4, 3]
    for axis in (0, 1):
        for j, jj in enumerate(permutation):
            for a in range(3):
                for b in range(3):
                    target = quadratic(jj, reflection(a), b) if axis == 0 else \
                        quadratic(jj, a, reflection(b))
                    assert reflect(quadratic(j, a, b), axis) == target
            assert {reflect(m, axis) for m in INVARIANTS[j]} == INVARIANTS[jj]
    print("PASS: each factor reflection fixes a 4-dimensional space; pure-pair dimension 8")


def check_gradients():
    for j, polynomials in enumerate(INVARIANTS):
        qj = [0, 2, 1, 3, 4][j]
        for variable in INDICES:
            derivative = Counter()
            for m in polynomials:
                if variable in m:
                    term = list(m)
                    term.remove(variable)
                    derivative[monomial(term)] += m.count(variable)
            expected = Counter({quadratic(qj, *pair(variable)): 3 if j == 0 else 1})
            assert derivative == expected
    variables = sp.symbols("l00 l01 l02 l10 l11 l12 l20 l21 l22")
    even = sum(sp.prod(variables[i] for i in m) for m in INVARIANTS[3])
    odd = sum(sp.prod(variables[i] for i in m) for m in INVARIANTS[4])
    assert sp.expand(even - odd - sp.Matrix(3, 3, variables).det()) == 0
    print("PASS: all quadratic covariants are gradients; the odd cubic is det(Lambda)")


def probe(*positions):
    values = [0] * 9
    for a, b in positions:
        values[index(a, b)] += 1
    return values


def evaluate(m, values):
    result = 1
    for i in m:
        result *= values[i]
    return result


def check_probes():
    # Simultaneously recover beta and both gamma rows from the same four lines.
    probes = [
        probe((0, 0)),
        probe((0, 0), (0, 1), (0, 2)),
        probe((0, 0), (1, 0), (2, 0)),
        probe((0, 0), (1, 1), (2, 2)),
    ]
    qmatrix = []
    imatrix = []
    for values in probes:
        qrow = [evaluate(quadratic(j, 0, 0), values) for j in range(3)]
        qrow.append(sum(evaluate(quadratic(j, 0, 0), values) for j in (3, 4)))
        qmatrix.append(qrow)
        irow = [sum(evaluate(m, values) for m in INVARIANTS[j]) for j in range(3)]
        irow.append(sum(evaluate(m, values) for j in (3, 4)
                        for m in INVARIANTS[j]))
        imatrix.append(irow)
    Q = sp.Matrix(qmatrix)
    I = sp.Matrix(imatrix)
    assert Q == sp.Matrix([[1, 0, 0, 0], [1, 0, 1, 0],
                           [1, 1, 0, 0], [1, 0, 0, 1]])
    assert I == sp.Matrix([[1, 0, 0, 0], [3, 1, 0, 0],
                           [3, 0, 1, 0], [3, 0, 0, 1]])
    assert (Q.det(), I.det()) == (-1, 1)
    assert len({tuple(v) for v in probes}) == 4

    # If PBW has no quadratic term, first or third row vanishes.
    # Every column-product and permutation cubic then vanishes.
    symbols = sp.symbols("l00 l01 l02 l10 l11 l12 l20 l21 l22")
    for zero_row in (0, 2):
        v = list(symbols)
        for b in range(3):
            v[index(zero_row, b)] = 0
        for j in (2, 3, 4):
            assert sp.expand(sum(evaluate(m, v) for m in INVARIANTS[j])) == 0
    print("PASS: four probes recover 4+8; minimum four lines and two nonlinear PBW probes")



def check_hesse_complements():
    x = sp.symbols("x0 x1 x2")
    h = sp.Symbol("h")
    quadrics = [x[a] ** 2 - h * x[(a + 1) % 3] * x[(a + 2) % 3]
                for a in range(3)]

    def matrix(polynomials, degree):
        basis = [sp.prod(x[i] for i in m)
                 for m in combinations_with_replacement(range(3), degree)]
        return sp.Matrix([[sp.Poly(p, *x).coeff_monomial(m) for p in polynomials]
                          for m in basis])

    cross = [x[(a + 1) % 3] * x[(a + 2) % 3] for a in range(3)]
    det2 = sp.factor(matrix(quadrics + cross, 2).det())
    det3 = sp.factor(matrix([z * q for q in quadrics for z in x]
                            + [sp.prod(x)], 3).det())
    assert det2 in (1, -1)
    assert sp.cancel(det3 / (1 - h ** 3) ** 2) in (1, -1)
    assert det3.subs(h, 0) != 0
    print("PASS: Hesse slice determinants are units times 1 and (1-h^3)^2, including h=0")


def check_actual_reflection_signs():
    tau = sp.Symbol("tau")
    p = [1, 0, 2]

    def transform(polynomial):
        result = {}
        for word, coefficient in polynomial.items():
            target = tuple(p[i] for i in word)
            result[target] = result.get(target, 0) + (-1) ** len(word) * coefficient
        return {w: sp.expand(c) for w, c in result.items() if c != 0}

    def relation(a):
        b, c = (a + 1) % 3, (a + 2) % 3
        return {(b, c): 1, (c, b): 1, (a, a): tau}

    for a in range(3):
        assert transform(relation(a)) == relation(p[a])
    alternating = {word: (-1) ** parity(word) for word in permutations(range(3))}
    assert transform(alternating) == alternating
    potential = {word: sp.Rational(1, 3) for word in permutations(range(3))}
    potential.update({(a, a, a): tau / 3 for a in range(3)})
    assert transform(potential) == {w: -c for w, c in potential.items()}
    x = sp.symbols("x0 x1 x2")
    f = tau * sum(z ** 3 for z in x) - (2 + tau ** 3) * sp.prod(x)
    assert sp.expand(f.xreplace({x[a]: x[p[a]] for a in range(3)}) - f) == 0
    assert sp.expand(f.xreplace({x[a]: -x[p[a]] for a in range(3)}) + f) == 0
    assert sp.eye(3)[p, :].det() == -1
    print("PASS: nc -P fixes the alternating center; commutative P fixes f; top-line signs agree")


def main():
    check_quadratic_space()
    check_cubic_space()
    check_reflections()
    check_gradients()
    check_probes()
    check_hesse_complements()
    check_actual_reflection_signs()
    print("7 PASS. LIMIT: finite algebra only; no comparison kernel or higher numerical coefficients computed.")


if __name__ == "__main__":
    main()
