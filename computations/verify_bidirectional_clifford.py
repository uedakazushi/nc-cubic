#!/usr/bin/env python3
"""Exact finite certificates for the bidirectional Clifford family.

Current result: 2026-11-23 / v64.
Run: python3 computations/verify_bidirectional_clifford.py
Requires Python 3 and SymPy.  All parameter identities are symbolic over Q;
Heisenberg calculations use Q[omega]/(omega^2+omega+1), without floating point.

Checks: the full quadratic annihilator, cocycle and trace signs, origin
complete-intersection identities, the monic central-norm coefficient, an
actual bad parameter point, the finite Heisenberg representation data, and
the pure Hesse derivative with the first-order central normalization ratio.
These are algebraic inputs to the paper.  They do NOT prove Koszulness,
Calabi--Yau duality, the relative category, a comparison kernel, or its
Heisenberg linearization.  No random samples or proof assistant are used.
"""

from itertools import combinations, permutations, product

import sympy as sp


def zero(expression):
    return sp.expand(expression) == 0


def main():
    tau1, tau2, tau = sp.symbols("tau1 tau2 tau")
    lam = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"L{i+1}{j+1}"))
    mix = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"M{i+1}{j+1}"))
    u, v = sp.symbols("u1:4"), sp.symbols("v1:4")
    z = u + v

    # Words are ordered tensors, not commutative degree-two monomials.
    def word(i, j):
        row = sp.zeros(1, 36)
        row[0, 6*i+j] = 1
        return row

    primal, primal_pivots = [], []
    for block, parameter, matrix in ((0, tau1, lam), (3, tau2, mix)):
        other = 3 - block
        for i in range(3):
            j, k = (i+1) % 3, (i+2) % 3
            row = word(block+j, block+k) + word(block+k, block+j)
            row += parameter * word(block+i, block+i)
            for b in range(3):
                row -= matrix[i, b] * word(other+b, other+b)
            primal.append(row)
            primal_pivots.append(6*(block+j)+block+k)
    for i, j in product(range(3), repeat=2):
        primal.append(word(i, 3+j) - word(3+j, i))
        primal_pivots.append(6*i+3+j)
    primal = sp.Matrix.vstack(*primal)

    # All 15 skew-polynomial relations, then the six displayed quadrics.
    pairs = list(combinations(range(6), 2))
    dual = [word(i, j) + (1 if i < 3 <= j else -1) * word(j, i)
            for i, j in pairs]
    for block, parameter, matrix in ((0, tau1, mix), (3, tau2, lam)):
        other = 3 - block
        for i in range(3):
            row = word(block+i, block+i)
            row -= parameter * word(block+(i+1) % 3, block+(i+2) % 3)
            for b in range(3):
                row += matrix[b, i] * word(other+(b+1) % 3,
                                          other+(b+2) % 3)
            dual.append(row)
    dual = sp.Matrix.vstack(*dual)
    assert primal.shape == (15, 36) and dual.shape == (21, 36)
    assert primal[:, primal_pivots] == sp.eye(15)
    dual_minor = dual[:, [6*i+j for i, j in pairs] + [7*i for i in range(6)]]
    assert dual_minor[:15, :15] == sp.eye(15)
    assert dual_minor[:15, 15:] == sp.zeros(15, 6)
    assert dual_minor[15:, 15:] == sp.eye(6)
    assert all(zero(value) for value in primal * dual.T)
    print("PASS all 15 primal and 21 dual relations: unit minors and zero pairing")

    # Extract exactly the same quadrics in the commutative polynomial ring.
    quadrics = [sp.expand(sum(row[6*i+j] * z[i] * z[j]
                             for i, j in product(range(6), repeat=2)))
                for row in dual.tolist()[15:]]
    group = list(product(range(2), repeat=2))

    def add(g, h):
        return tuple((a+b) % 2 for a, b in zip(g, h))

    def chi(g, h):
        return (-1) ** (g[1]*h[0])

    for g, h, k in product(group, repeat=3):
        assert chi(g, h) * chi(add(g, h), k) == chi(h, k) * chi(g, add(h, k))
    for g in group:
        assert chi((0, 0), g) == chi(g, (0, 0)) == 1
    for expression in quadrics:
        for powers, coefficient in sp.Poly(expression, *z).terms():
            assert sum(powers) == 2
            parity = (sum(powers[:3]) % 2, sum(powers[3:]) % 2)
            assert parity == (0, 0)
            assert all(chi(parity, g) == chi(g, parity) for g in group)
    print("PASS all cocycle triples and central parity of every dual-quadric term")

    socle = (1, 1)
    for g in group:
        complement = add(socle, g)
        sign = (-1) ** (g[0]+g[1])
        assert chi(g, complement) == sign * chi(complement, g)
    for degree in range(7):
        assert (-1) ** (degree*(6-degree)) == (-1) ** degree
    assert (-1) ** 7 * (-1) == 1
    print("PASS socle-(1,1) Frobenius ratio and the dimension-six Nakayama sign")

    x = sp.symbols("x y z")
    origin = [x[i]**2 - tau*x[(i+1) % 3]*x[(i+2) % 3] for i in range(3)]
    for i, j, k in permutations(range(3)):
        rhs = x[j]*origin[i] + tau*x[k]*origin[j] + tau**2*x[i]*origin[k]
        assert zero((1-tau**3)*x[i]**2*x[j] - rhs)
    for i in range(3):
        assert zero(x[i]**3 - tau*sp.prod(x) - x[i]*origin[i])
    assert all(expression.subs(dict(zip(x, (1, 1, 1)))).subs(tau, 1) == 0
               for expression in origin)
    print("PASS six universal origin cubic identities, cube reductions, and tau^3=1 example")

    jacobian = sp.Matrix(origin).jacobian(x).det()
    correction = -2*tau**2 * sum(x[i]*origin[i] for i in range(3))
    assert zero(jacobian - 8*(1-tau**3)*sp.prod(x) - correction)
    print("PASS actual origin Jacobian determinant modulo the three cube relations")

    X, Y = sp.symbols("X1:4"), sp.symbols("Y1:4")
    a1, a2 = sp.symbols("a1 a2")
    alpha1, alpha2 = 2*a1*(1-tau1**3), 2*a2*(1-tau2**3)
    px = list(lam*sp.Matrix(Y) - tau1*sp.Matrix(X))
    py = list(mix*sp.Matrix(X) - tau2*sp.Matrix(Y))

    def clifford_matrix(diagonal, cross):
        return sp.Matrix(((diagonal[0], cross[2]/2, cross[1]/2),
                          (cross[2]/2, diagonal[1], cross[0]/2),
                          (cross[1]/2, cross[0]/2, diagonal[2])))

    detx = clifford_matrix(X, px).det(method="berkowitz")
    dety = clifford_matrix(Y, py).det(method="berkowitz")
    cx = sp.Poly(detx, X[0]).coeff_monomial(X[0]**3)
    cy = sp.Poly(dety, X[0]).coeff_monomial(X[0]**3)
    assert zero(cx + tau1**2/4)
    assert zero(cy - mix[0, 0]*mix[1, 0]*mix[2, 0]/4)
    coefficient = sp.expand(-alpha1**2*cx + alpha2**2*cy)
    expected = (alpha1**2*tau1**2 + alpha2**2*sp.prod(mix[:, 0]))/4
    assert zero(coefficient - expected)
    assert max(sp.Poly(detx, X[0]).degree(), sp.Poly(dety, X[0]).degree()) == 3
    at_origin = {parameter: 0 for parameter in list(lam)+list(mix)}
    assert zero(coefficient.subs(at_origin) - a1**2*tau1**2*(1-tau1**3)**2)
    print("PASS universal X1^3 coefficient of the central norm and its origin value")

    bad = {tau1: 2, tau2: 2, a1: 1, a2: 1}
    bad.update({lam[i, j]: int(i == j) for i, j in product(range(3), repeat=2)})
    bad.update({mix[i, j]: int(i == j) for i, j in product(range(3), repeat=2)})
    point = dict.fromkeys(z, 1)
    assert all(expression.subs(bad).subs(point) == 0 for expression in quadrics)
    assert coefficient.subs(bad) == 196
    assert alpha1.subs(bad) == alpha2.subs(bad) == -14
    print("PASS actual bad point tau1=tau2=2, Lambda=M=I: common zero and c=196")

    omega = sp.Symbol("omega")

    def cyclotomic(expression):
        return sp.rem(sp.expand(expression), omega**2+omega+1, omega)

    def equal(left, right):
        return all(cyclotomic(value) == 0 for value in left-right)

    cyclic = sp.Matrix(((0, 0, 1), (1, 0, 0), (0, 1, 0)))
    diagonal = sp.diag(1, omega, omega**2)
    relation_diagonal = sp.diag(1, omega**2, omega)
    aa, bb, cc = sp.symbols("a b c")
    relations = sp.zeros(9, 3)
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        relations[3*j+k, i] += aa
        relations[3*k+j, i] += bb
        relations[4*i, i] += cc
    assert equal(sp.kronecker_product(cyclic, cyclic)*relations, relations*cyclic)
    assert equal(sp.kronecker_product(diagonal, diagonal)*relations,
                 relations*relation_diagonal)
    # The parameter-point action is the inverse transpose of relation action.
    assert cyclic.T*cyclic == sp.eye(3)
    assert equal(relation_diagonal.T*diagonal, sp.eye(3))
    assert equal(cyclic*diagonal, omega**2*diagonal*cyclic)
    assert cyclotomic(diagonal.det()) == cyclic.det() == 1
    square_weights = [omega**(2*i) for i in range(3)]
    cross_weights = [omega**(((i+1) % 3)+((i+2) % 3)) for i in range(3)]
    assert all(cyclotomic(a-b) == 0 for a, b in zip(square_weights, cross_weights))
    # Cyclic permutation carries each square and each opposite product forward.
    cycle_substitution = {x[i]: x[(i+1) % 3] for i in range(3)}
    for basis in ([value**2 for value in x],
                  [x[(i+1) % 3]*x[(i+2) % 3] for i in range(3)]):
        assert all(basis[i].xreplace(cycle_substitution) == basis[(i+1) % 3]
                   for i in range(3))
    three_torsion = list(product(range(3), repeat=2))
    characters = {q: tuple((q[0]*h[1]-q[1]*h[0]) % 3 for h in three_torsion)
                  for q in three_torsion}
    assert len(set(characters.values())) == 9
    for q in three_torsion:
        inverse = tuple((-value) % 3 for value in q)
        assert all((a+b) % 3 == 0 for a, b in zip(characters[q], characters[inverse]))
    print("PASS exact H3 source/target actions, square/cross weights, and character pairing")

    # The center ratio uses fixed Omega_tau in the tau-epsilon relations.
    # This checks its scalar expansion, not its transport by a categorical kernel.
    epsilon = sp.Symbol("epsilon")
    f_tau = tau*sum(value**3 for value in x) - (2+tau**3)*sp.prod(x)
    assert zero(tau*sp.diff(f_tau, tau) - f_tau - 2*(1-tau**3)*sp.prod(x))
    assert zero(sum(value*sp.diff(f_tau, value) for value in x) - 3*f_tau)
    center_ratio = (1-tau**3)/(1-(tau-epsilon)**3)
    expected_ratio = 1 - 3*tau**2*epsilon/(1-tau**3)
    assert sp.cancel(sp.series(center_ratio, epsilon, 0, 2).removeO()
                     - expected_ratio) == 0
    # Independently clear the denominator and check divisibility by epsilon^2.
    numerator = sp.together(center_ratio-expected_ratio).as_numer_denom()[0]
    assert sp.Poly(numerator, epsilon).coeff_monomial(1) == 0
    assert sp.Poly(numerator, epsilon).coeff_monomial(epsilon) == 0
    print("PASS pure Hesse derivative, Euler identity, and normalized center ratio mod epsilon^2")


if __name__ == "__main__":
    main()
