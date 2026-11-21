#!/usr/bin/env python3
"""Exact finite certificates for point/Poisson comparison obstructions.

Checks the 24-variable integrability matrix in dimension N=8 and the
polynomial identities used to classify the Hessian-rank-two points of a
split Hesse cubic threefold.  Also checks their kernel cubic forms and the
nonzero j-invariant difference used to distinguish local Artin algebras.
Also verifies the fixed h=1 Sklyanin center and exact j-values, two mixed
four-generator centers by complete degree-four word reduction, and the
64 distinct rational roots of the mixed two-block stationary norm.

The complete geometric case split, the local associated-graded argument,
all-degree PBW assertions, and categorical comparison/Torelli theorems
are not proved by this script.

Run: python3 computations/verify_point_poisson_obstruction.py
Requires: SymPy.
"""

from itertools import permutations, product

import sympy as sp


def verify_quadratic_net():
    x, y, z = sp.symbols("x y z")
    central = sp.symbols("u1:6")
    coords = (x, y, z, *central)
    g = (x**3 + y**3 + z**3) / 3 + x*y*z
    Q1 = sum(u**2 for u in central)
    Q2 = sum(i*u**2 for i, u in enumerate(central, 1))
    Q3 = 2*central[0]*central[1] + 2*central[2]*central[3]
    F = g + x*Q1 + y*Q2 + z*Q3
    quadrics = tuple(sp.diff(F, a) for a in (x, y, z))
    matrices = tuple(sp.hessian(q, coords) / 2 for q in quadrics)
    A1, A2, A3 = matrices
    assert all(A == A.T for A in matrices)
    assert A1.det() != 0

    skew = A3*A1.inv()*A2 - A2*A1.inv()*A3
    assert skew.T == -skew
    expected_active = sp.Matrix([
        [0, 0, 0],
        [0, 0, -sp.Rational(7, 4)],
        [0, sp.Rational(7, 4), 0],
    ])
    block = sp.Matrix([[0, 1], [-1, 0]])
    expected = sp.diag(expected_active, block, block, sp.zeros(1))
    assert skew == expected
    assert skew.rank() == 6
    print("PASS: exact 8-by-8 skew matrix has rank 6 and nullity 2")

    zero = sp.zeros(8)
    full = sp.BlockMatrix([
        [A2, -A1, zero],
        [A3, zero, -A1],
        [zero, A3, -A2],
    ]).as_explicit()
    assert full.shape == (24, 24)
    assert full.rank() == 22
    lifted = []
    for v1 in skew.nullspace():
        triple = sp.Matrix.vstack(v1, A1.inv()*A2*v1, A1.inv()*A3*v1)
        assert full*triple == sp.zeros(24, 1)
        lifted.append(triple)
    assert sp.Matrix.hstack(*lifted).rank() == 2
    print("PASS: the full integrability matrix has rank 22 and the same kernel")

    standard = sp.Matrix.vstack(*[sp.eye(8)[:, i] for i in range(3)])
    assert full*standard == sp.zeros(24, 1)
    assert 8 - skew.rank() >= 2
    print("PASS: the original active support is one nonzero integrable solution")


def verify_hesse_hessian():
    x, y, z, u, v, t, e, s, h = sp.symbols("x y z u v t e s h")
    active = (x, y, z)
    coords = (*active, u, v)
    g = (x**3 + y**3 + z**3) / 3 + t*x*y*z
    F = g + (u**3 + v**3) / 3
    H = sp.hessian(g, active)
    HF = sp.hessian(F, coords)
    assert HF == sp.diag(H, 2*u, 2*v)

    # If all 2-by-2 minors vanish and t*(t^3-8) is invertible,
    # these three identities force x=y=z=0 over a field.
    for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        mixed = H.extract([a, b], [a, c]).det()
        principal = H.extract([b, c], [b, c]).det()
        q = 2*active[a]**2 - t*active[b]*active[c]
        assert sp.expand(mixed - t*q) == 0
        assert sp.expand(t*principal + 4*q - (8-t**3)*active[a]**2) == 0
    assert sp.expand(H.det() + 6*t**2*g - 8*(1+t**3)*x*y*z) == 0
    print("PASS: exact minor identities exclude active Hessian rank <= 1")
    print("PASS: the active Hessian determinant on the cubic is 8*(1+t^3)*xyz")

    def cube_reduce(expr):
        return sp.expand(sp.rem(sp.expand(expr), e**3-1, e))

    # The variable e represents all three roots of unity at once.
    center = {x: 0, y: 0, z: 0, u: 1, v: -e}
    center_hessian = HF.subs(center)
    center_kernel = sp.Matrix.hstack(*(sp.eye(5)[:, i] for i in range(3)))
    assert cube_reduce(F.subs(center)) == 0
    assert center_hessian*center_kernel == sp.zeros(5, 3)
    assert cube_reduce(center_hessian.extract([3, 4], [3, 4]).det() * (-e**2/4)) == 1
    assert sp.expand(F.subs({u: 0, v: 0}) - g) == 0

    for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        p = [sp.Integer(0)]*5
        p[a], p[b] = sp.Integer(1), -e
        r = [sp.Integer(0)]*5
        r[a], r[b], r[c] = t*e/2, t*e**2/2, sp.Integer(1)
        point = dict(zip(coords, p))
        tangent_kernel = sp.Matrix.hstack(sp.Matrix(r), sp.eye(5)[:, 3], sp.eye(5)[:, 4])
        hessian_at_point = HF.subs(point)
        assert cube_reduce(F.subs(point)) == 0
        assert (hessian_at_point*tangent_kernel).applyfunc(cube_reduce) == sp.zeros(5, 3)
        minor = hessian_at_point.extract([a, b], [a, b]).det()
        assert cube_reduce(minor*(-e**2/4)) == 1
        substitution = {active[i]: s*r[i] for i in range(3)}
        kernel_cubic = F.subs(substitution, simultaneous=True)
        expected = ((1+t**3)*s**3 + u**3 + v**3) / 3
        assert cube_reduce(kernel_cubic - expected) == 0
    print("PASS: all three central and nine flex points have the stated rank-two kernels")
    print("PASS: kernel cubics are Hesse at central points and Fermat at flex points")

    def j(value):
        value = sp.sympify(value)
        return 27*value**3*(8-value**3)**3/(1+value**3)**3

    lam = (h + h**2/3 + h**5/12)/(1-h**4/4)
    difference = sp.cancel(j(lam)-j(h))
    numerator, denominator = sp.fraction(difference)
    valuation = min(monomial[0] for monomial, coefficient in sp.Poly(numerator, h).terms())
    assert valuation == 4 and denominator.subs(h, 0) != 0
    assert sp.cancel(numerator/h**4).subs(h, 0) / denominator.subs(h, 0) == 13824
    assert sp.cancel(j(h)) != 0 and j(0) == 0
    for forbidden in (lam, 1+lam**3, 8-lam**3):
        assert sp.cancel(forbidden) != 0
    print("PASS: j(lambda)-j(h) has exact leading term 13824*h^4, and j(h) != 0")

    # A fixed complex parameter; the categorical comparison at this point
    # is a separate theorem, not a consequence of these rational identities.
    fixed_h = sp.Integer(1)
    fixed_lam = sp.cancel(lam.subs(h, fixed_h))
    source_a = 1 + h**4/2 + h**5/6 - h**8/48
    source_b = (4-h**4)*(12*h+h**5-8*h**2)/48
    assert fixed_lam == sp.Rational(17, 9)
    assert source_a.subs(h, fixed_h) == sp.Rational(79, 48)
    assert source_b.subs(h, fixed_h) == sp.Rational(5, 16)
    assert (source_b-h*source_a).subs(h, fixed_h) == -sp.Rational(4, 3)
    assert j(fixed_h) == sp.Rational(9261, 8)
    assert j(fixed_lam) == sp.Rational(3813232609367, 4849120870776)
    assert j(fixed_lam)-j(fixed_h) == -sp.Rational(1402412578855675, 1212280217694)
    assert fixed_lam**3-8 == -sp.Rational(919, 729)
    assert fixed_lam**3+1 == sp.Rational(5642, 729)
    print("PASS: h=1 gives lambda=17/9, nonzero j difference, and central socle -4*xyz/3")


def word_quotient_reducer(letter_count, relations, degree):
    """Exact quotient by all relation multiples in one specified degree."""
    letters = range(letter_count)
    words = tuple(product(letters, repeat=degree))
    positions = {word: index for index, word in enumerate(words)}
    rows = []
    for left_degree in range(degree-1):
        right_degree = degree-2-left_degree
        for left in product(letters, repeat=left_degree):
            for right in product(letters, repeat=right_degree):
                for quadratic in relations:
                    row = [sp.Integer(0)]*len(words)
                    for word, coefficient in quadratic.items():
                        row[positions[left+word+right]] += coefficient
                    rows.append(row)
    matrix = sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix(rows)).convert_to(sp.QQ)
    echelon, pivots = matrix.rref()
    reduced = echelon.to_Matrix()

    def reduce(polynomial):
        vector = sp.zeros(1, len(words))
        for word, coefficient in polynomial.items():
            vector[0, positions[word]] += coefficient
        for row, pivot in enumerate(pivots):
            if vector[0, pivot]:
                vector -= vector[0, pivot]*reduced[row, :]
        return vector

    return len(words)-len(pivots), reduce


def word_commutator(letter, polynomial):
    result = {}
    for word, coefficient in polynomial.items():
        left, right = (letter,)+word, word+(letter,)
        result[left] = result.get(left, 0)+coefficient
        result[right] = result.get(right, 0)-coefficient
    return result


def verify_fixed_parameter_centrality():
    """Check the displayed cubic modulo the quadratic relations over QQ.

    This only computes the degree-three and degree-four relation spaces.
    It does not establish AS regularity, the domain property, or PBW in all
    degrees; those properties require the separate arguments in the paper.
    """
    letters = range(3)
    relation = {(1, 2): 1, (2, 1): -3, (0, 0): -2}
    relations = [
        {tuple((letter+shift) % 3 for letter in word): coefficient
         for word, coefficient in relation.items()}
        for shift in letters
    ]
    omega = {(letter,)*3: sp.Rational(79, 144) for letter in letters}
    omega.update({word: sp.Rational(5, 96) for word in permutations(letters)})

    dimension_three, reduce_three = word_quotient_reducer(3, relations, 3)
    dimension_four, reduce_four = word_quotient_reducer(3, relations, 4)
    assert dimension_three == 10 and dimension_four == 15
    assert reduce_three(omega) != sp.zeros(1, 27)
    for letter in letters:
        assert reduce_four(word_commutator(letter, omega)) == sp.zeros(1, 81)
    print("PASS: at h=1, quotient dimensions are 10 and 15, and the nonzero cubic is central")


def verify_mixed_central_norm():
    """Two explicit PBW presentations and their complete 64-point norm.

    Word reduction certifies centrality in these presentations.  The PBW
    theorem is used separately in the paper, as is every smoothness claim.
    The 64-point calculation is exhaustive exact diagonalization, not a
    numerical sample or interpolation.
    """
    spectral_data = []
    for roots in ((1, 2, 3), (4, 5, 7)):
        alpha = tuple(a*a for a in roots)
        relations = []
        for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
            relations.append({(j, k): 1, (k, j): -1, (i, i): -1, (3, 3): alpha[i]})
        relations += [{(i, 3): 1, (3, i): -1} for i in range(3)]
        omega = {(i,)*3: sp.Rational(1, 3) for i in range(3)}
        omega.update({p: -sp.Rational(1, 9) for p in permutations(range(3))})
        for i in range(3):
            omega[(i, 3, 3)] = -alpha[i]
        dim3, red3 = word_quotient_reducer(4, relations, 3)
        dim4, red4 = word_quotient_reducer(4, relations, 4)
        assert (dim3, dim4) == (20, 35)
        assert red3(omega) != sp.zeros(1, 64)
        assert all(red4(word_commutator(i, omega)) == sp.zeros(1, 256) for i in range(4))

        basis = tuple(product((0, 1), repeat=3))
        positions = {b: j for j, b in enumerate(basis)}
        multiplication = []
        for i in range(3):
            matrix = sp.zeros(8)
            for j, b in enumerate(basis):
                out = list(b)
                out[i] = 1-b[i]
                matrix[positions[tuple(out)], j] = alpha[i] if b[i] else 1
            multiplication.append(matrix)
        X, Y, Z = multiplication
        M = -sp.Rational(2, 3)*(sum((alpha[i]*multiplication[i] for i in range(3)), sp.zeros(8)) + X*Y*Z)
        points = [tuple(signs[i]*roots[i] for i in range(3)) for signs in product((-1, 1), repeat=3)]
        evaluation = sp.Matrix([[sp.prod(p[i]**b[i] for i in range(3)) for b in basis] for p in points])
        eigenvalues = [-sp.Rational(2, 3)*(sum(alpha[i]*p[i] for i in range(3)) + sp.prod(p)) for p in points]
        assert evaluation.det() != 0
        assert evaluation*M == sp.diag(*eigenvalues)*evaluation
        spectral_data.append(eigenvalues)
    assert set(spectral_data[0]) == {sign*a for sign in (-1, 1) for a in (28, 16, sp.Rational(56, 3), sp.Rational(28, 3))}
    assert set(spectral_data[1]) == {sign*a for sign in (-1, 1) for a in (448, 196, 176, sp.Rational(284, 3))}
    print("PASS: two mixed four-generator presentations have the stated nonzero central cubic and exact spectra")

    eigenvalues = [a+100*b for a in spectral_data[0] for b in spectral_data[1]]
    assert len(eigenvalues) == len(set(eigenvalues)) == 64
    assert all(a != 0 for a in eigenvalues)
    c = sp.symbols('c')
    norm = sp.Poly(sp.prod(c+a for a in eigenvalues), c)
    assert norm.degree() == 64 and norm.LC() == 1
    assert sp.gcd(norm, norm.diff()).degree() == 0
    assert norm.eval(0) != 0
    print("PASS: the mixed two-block norm is monic degree 64, squarefree, and nonzero at c=0")


def main():
    verify_quadratic_net()
    verify_hesse_hessian()
    verify_fixed_parameter_centrality()
    verify_mixed_central_norm()
    print("Scope: finite polynomial certificates; full geometric and categorical proofs are in the paper.")


if __name__ == "__main__":
    main()
