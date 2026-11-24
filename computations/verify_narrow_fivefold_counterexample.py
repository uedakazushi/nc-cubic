#!/usr/bin/env python3
"""Exact checks for the deformation-connected fivefold and its rotation products."""
from collections import Counter
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb

import sympy as sy


def equal(left, right):
    return (left - right).applyfunc(sy.expand).is_zero_matrix


def verify_clifford_products():
    dimension = 8
    eye = sy.eye(dimension)
    zero = sy.zeros(dimension)
    period = sy.symbols("t", nonzero=True)
    x = sy.symbols("x1:4")
    u = sy.symbols("u1:4")
    wedges = []
    for index in range(3):
        bit = 1 << index
        matrix = sy.zeros(dimension)
        for mask in range(dimension):
            if not mask & bit:
                matrix[mask | bit, mask] = (-1)**((mask & (bit-1)).bit_count())
        wedges.append(matrix)
    contractions = [matrix.T for matrix in wedges]
    differential = sum((v*i + period*h*v*e for v,h,i,e in
                        zip(x, u, contractions, wedges)), sy.zeros(dimension))
    assert equal(differential**2, period*sum(h*v*v for v,h in zip(x,u))*eye)
    theta = [i-period*h*e for i,h,e in zip(contractions,u,wedges)]
    assert all(equal(differential*a+a*differential, zero) for a in theta)
    j = sy.diag(1,-1)
    k = sy.Matrix([[0,1],[1,0]])
    eta = [sy.kronecker_product(a,p) for a,p in zip(theta,(j,k,sy.I*j*k))]
    pairs = list(combinations(range(3), 2))
    for a in range(3):
        assert equal(eta[a]**2, -period*u[a]*sy.eye(16))
    for a,b in pairs:
        assert equal(eta[a]*eta[b], eta[b]*eta[a])
    z = {(a,b): -eta[a]*eta[b]/period for a,b in pairs}
    def entry(a,b):
        return z[tuple(sorted((a,b)))]
    for a,b in pairs:
        assert equal(entry(a,b)**2, u[a]*u[b]*sy.eye(16))
    for a in range(3):
        b,c = [i for i in range(3) if i != a]
        assert equal(entry(a,b)*entry(a,c), u[a]*entry(b,c))
    # Conjugation on End(V) transports the character twist on the generator.
    # Recover the graph label of each z_ab from all four twist eigenvalues.
    lifts = (sy.eye(2), j, k, sy.I*j*k)
    for a, b in pairs:
        factor = lifts[a+1]*lifts[b+1]
        remaining_coordinate = 3 - a - b
        label = lifts[remaining_coordinate + 1]
        for index, coordinate in enumerate(lifts[1:]):
            assert (label*coordinate == coordinate*label) == (index == remaining_coordinate)
        for lift in lifts:
            sign = 1 if lift*label == label*lift else -1
            assert lift*factor*lift.inv() == sign*factor
    print("All four dual twists match the three nonidentity graph labels.")
    origin = {h:0 for h in u} | {period:1}
    evaluations = [matrix.subs(origin).reshape(256,1) for matrix in z.values()]
    assert sy.Matrix.hstack(*evaluations).rank() == 3
    print("Closed Clifford operators, six product identities, origin evaluation rank three.")


def verify_quadrics():
    u,v,w,a,b,c = variables = sy.symbols("u v w a b c")
    quadrics = [a*a-u*v, b*b-u*w, c*c-v*w,
               a*b-u*c, a*c-v*b, b*c-w*a]
    monomials = [x*y for i,x in enumerate(variables) for y in variables[i:]]
    polys = [sy.Poly(q,*variables) for q in quadrics]
    assert sy.Matrix([[p.coeff_monomial(m) for m in monomials] for p in polys]).rank() == 6
    s,t,h = sy.symbols("s t h")
    cover = dict(zip(variables,(s*s,t*t,h*h,s*t,s*h,t*h)))
    assert all(sy.expand(q.xreplace(cover)) == 0 for q in quadrics)
    jac = sy.Matrix(list(cover.values())).jacobian((s,t,h))
    assert jac.subs({s:1,t:1,h:1}).rank() == 3
    print("Six independent quadrics vanish on a three-dimensional affine Veronese cone.")


def verify_integrable_cubics():
    # Columns are cubics; each row is one coefficient of one restricted
    # partial derivative on the Veronese cone with a square-zero coordinate.
    a, b, c, w = sy.symbols("a b c w")
    coords = sy.symbols("d1 d2 d3 z12 z13 z23 w")
    restriction = dict(zip(coords, (a*a, b*b, c*c, a*b, a*c, b*c, w)))
    monomials = [sy.prod(m) for m in combinations_with_replacement(coords, 3)]
    def constraints_mod(w_squared):
        rows = {}
        for column, monomial in enumerate(monomials):
            for i, x in enumerate(coords):
                restricted = monomial.diff(x).xreplace(restriction)
                derivative = sy.Poly(restricted.subs(w**2, w_squared), a,b,c,w)
                for powers, coefficient in derivative.terms():
                    if coefficient:
                        rows.setdefault((i, powers), {})[column] = coefficient
        constraints = sy.zeros(len(rows), len(monomials))
        for row, entries in enumerate(rows.values()):
            for col, value in entries.items():
                constraints[row, col] = value
        return constraints

    constraints = constraints_mod(0)
    assert constraints.shape[1] == 84 and constraints.rank() == 82
    rank_two = constraints_mod(-a**4 / 3)  # q = 3w^2 + u1^2
    assert rank_two.rank() == 83
    d1,d2,d3,z12,z13,z23,_ = coords
    det = sy.Matrix([[d1,z12,z13],[z12,d2,z23],[z13,z23,d3]]).det()
    for solution in (det, w**3):
        poly = sy.Poly(solution, *coords)
        assert (constraints * sy.Matrix([poly.coeff_monomial(m) for m in monomials])).is_zero_matrix
    print("Cubic integration on 84 coefficients: constraint ranks 82 (rank-one q) and 83 (rank-two q).")


def verify_smooth_fibers():
    x,y,z,u,v,h,w = variables = sy.symbols("x y z u v h w")
    g = u**3+v**3+h**3+w**3
    f0 = u*x*x+v*y*y+h*z*z+g
    f2 = f0+2*x*y*z
    dual = u*x*x+v*y*y-h*z*z+2*x*y*z+g+u*v*h
    lam = sy.symbols("lambda", nonzero=True)
    a,b,c = sy.symbols("a b c")  # entries (12), (13), (23)
    transformed = u*x*x+v*y*y-h*z*z+lam*x*y*z+g+4*u*v*h/lam**2
    change = {x:2*sy.I*c/lam, y:-2*sy.I*b/lam, z:2*a/lam}
    determinant = sy.Matrix([[u,a,b], [a,v,c], [b,c,h]]).det()
    assert sy.expand(lam**2*transformed.xreplace(change)/4 -
                     determinant-lam**2*g/4) == 0
    for polynomial in (f0,f2,dual):
        ideal = sy.groebner([polynomial.diff(i) for i in variables],
                            *variables, order="grevlex", domain=sy.QQ)
        assert ideal.is_zero_dimensional
    print("The three endpoint equations have zero-dimensional affine gradient scheme over Q.")


def invariant_jacobian_piece(polynomial, variables, signs, active_count, degree):
    """Ranks of the invariant quotient, central products, and odd active part."""
    def products(size):
        return list(combinations_with_replacement(range(len(variables)), size))

    indices = []
    for factors in products(degree):
        character = 0
        for index in factors:
            character ^= signs[index]
        if character == 0:
            indices.append(factors)
    monomials = [sy.prod(variables[i] for i in factors) for factors in indices]
    relations = []
    if degree >= 2:
        for i, variable in enumerate(variables):
            for factors in products(degree-2):
                character = signs[i]
                for j in factors:
                    character ^= signs[j]
                if character == 0:
                    poly = sy.Poly(polynomial.diff(variable) *
                                   sy.prod(variables[j] for j in factors), *variables)
                    relations.append([poly.coeff_monomial(m) for m in monomials])
    ideal = sy.Matrix(relations) if relations else sy.zeros(0, len(indices))
    standard = sy.eye(len(indices))
    central = [j for j, factors in enumerate(indices)
               if all(i >= active_count for i in factors)]
    odd = [j for j, factors in enumerate(indices)
           if sum(i < active_count for i in factors) % 2]

    def image_dimension(rows):
        return ideal.col_join(standard[rows, :]).rank() - ideal.rank()

    return len(indices)-ideal.rank(), image_dimension(central), image_dimension(odd)


def verify_sector_triple_products():
    active = sy.symbols("x1:4")
    central = sy.symbols("u1:4") + (sy.Symbol("w"),)
    cubic = sum(v**3 for v in central)
    products = sum(u*x**2 for u,x in zip(central, active))
    for parameter, expected_rank in ((0, 34), (2, 35)):
        polynomial = cubic + products + parameter*sy.prod(active)
        ranks = {}
        for degree in (1,2,3):
            ranks[degree] = [
                invariant_jacobian_piece(polynomial, active+central,
                                         (1,2,3,0,0,0,0), 3, degree)]
            for i, x in enumerate(active):
                fixed = cubic + central[i]*x**2
                # After the determinant and multiplier characters cancel,
                # each moving pair contributes fixed degree degree-1.
                ranks[degree].append(invariant_jacobian_piece(
                    fixed, (x,)+central, (i+1,0,0,0,0), 1, degree-1))
        assert sum(dim for dim, _, _ in ranks[1]) == 7
        assert [(dim, span) for dim, span, _ in ranks[2]] == [(9,9)] + [(4,4)]*3
        assert sum(dim for dim, _, _ in ranks[3]) == 35
        assert sum(span for _, span, _ in ranks[3]) == expected_rank
        if parameter == 0:
            assert all(odd == 0 for _, _, odd in ranks[1])
            assert [odd for _, _, odd in ranks[3]] == [1, 0, 0, 0]
        print(f"b={parameter}: four Jacobian sectors, triple product rank {expected_rank}/35.")


def verify_sector_hilbert_series():
    """Average traces of the gradient Koszul resolution on each fixed space."""
    z = sy.symbols("z")
    total = 0
    for sector in range(4):
        # Nonzero characters label the three active coordinates.
        fixed = [0] * 4 + [c for c in range(1, 4)
                            if (c & sector).bit_count() % 2 == 0]
        for element in range(4):
            signs = [(-1) ** ((c & element).bit_count() % 2) for c in fixed]
            trace = sy.prod((1 - sign*z**2)/(1 - sign*z) for sign in signs)
            total += trace * (z if sector else 1) / 4
    assert sy.cancel(total - (1 + z)**7) == 0
    print("All four averaged sector series sum to (1+z)^7.")


def standard_monomials(basis):
    leading = [p.LM(order=basis.order).exponents for p in basis.polys]
    assert basis.is_zero_dimensional
    bounds = [min(m[i] for m in leading if m[i] and sum(m) == m[i])
              for i in range(len(basis.gens))]
    return [m for m in product(*(range(bound) for bound in bounds))
            if not any(all(a >= b for a, b in zip(m, term)) for term in leading)]


def verify_odd_invariant_generators():
    active = sy.symbols("x1:4")
    central = sy.symbols("u1:4") + (sy.Symbol("w"),)
    variables = active + central
    w = central[-1]
    primitive = sy.prod(active)
    for extra in (0, central[0]**2*w):
        g = sum(v**3 for v in central) + extra
        cubic = g + sum(u*x**2 for u, x in zip(central, active))
        gb = sy.groebner([cubic.diff(v) for v in variables], *variables,
                         order="lex", domain=sy.QQ)
        identity_even = 0
        odd_words = []
        for powers in standard_monomials(gb):
            parity = [v % 2 for v in powers[:3]]
            if parity == [0, 0, 0]:
                identity_even += 1
            if parity == [1, 1, 1]:
                odd_words.append(sy.prod(x**n for x, n in zip(variables, powers)))
        assert identity_even == 54 and set(odd_words) == {primitive, primitive*w}
        assert gb.reduce(primitive**2 + sy.prod(g.diff(u) for u in central[:3]))[1] == 0
    print("Two full gradient algebras: the two missing invariant monomials are P and wP.")


def verify_weighted_presentation():
    u = sy.symbols("u1:4")
    w, p = sy.symbols("w p")
    z12, z13, z23 = sy.symbols("z12 z13 z23")
    d = sy.Matrix([[u[0], z12, z13], [z12, u[1], z23], [z13, z23, u[2]]])
    pairs = list(combinations(range(3), 2))
    minors = [d.extract(rows, cols).det() for i, rows in enumerate(pairs) for cols in pairs[i:]]
    variables = (p, z12, z13, z23) + u + (w,)
    v = sy.symbols("v1:4")
    pullback = dict(zip(u, [x**2 for x in v]))
    for extra in (0, u[0]**2*w):
        g = sum(x**3 for x in u) + w**3 + extra
        gradients = [g.diff(x) for x in u]
        cubic = [d[i,j]*gradients[i] for i in range(3) for j in range(3)]
        quartic = [p*d[i,j] for i in range(3) for j in range(i,3)]
        relations = minors + [g.diff(w)] + cubic + quartic + [p**2 + sy.prod(gradients)]
        gb = sy.groebner(relations, *variables, order="lex", domain=sy.QQ)
        monomials = standard_monomials(gb)
        degree = lambda m: 3*m[0] + sum(m[1:])
        full = Counter(degree(m) for m in monomials)
        assert full == {i: comb(7,i) for i in range(8)}
        assert gb.reduce(w*p**2)[1] != 0
        h = g.xreplace(pullback)
        weighted = sy.groebner([h.diff(x) for x in v + (w,)], *v, w, order="lex", domain=sy.QQ)
        weights = [sum(m[:3])+2*m[3] for m in standard_monomials(weighted)]
        even = Counter(n//2 for n in weights if n % 2 == 0)
        assert full == even + Counter({3: 1, 4: 1})
        # Read the product pairings from rational normal forms in the
        # presented algebra, independently of its sector decomposition.
        ring, *_ = sy.polys.rings.ring(variables, sy.QQ, order="lex")
        divisors = [ring.from_dict(poly.rep.to_dict()) for poly in gb.polys]
        socle, = [m for m in monomials if degree(m) == 7]

        @lru_cache(maxsize=None)
        def top_coefficient(exponents):
            remainder = ring.from_dict({exponents: sy.QQ.one}).rem(divisors)
            return remainder.get(socle, 0)

        for i in range(4):
            left = [m for m in monomials if degree(m) == i]
            right = [m for m in monomials if degree(m) == 7-i]
            pairing = sy.Matrix([[top_coefficient(tuple(a+b for a, b in zip(x, y)))
                                  for y in right] for x in left])
            assert pairing.to_DM().rank() == comb(7, i)
    print("Two sextic presentations: dimensions 126 and 128; pairing ranks 1, 7, 21, 35.")


def verify_hesse_nonrealizable_slice():
    v = sy.symbols("v1:4")
    direction = sy.symbols("b1:4")
    kappa, lam = sy.symbols("kappa lambda")
    h = sum(x**6 for x in v) + kappa*sy.prod(v)**2
    polar = h
    for _ in range(3):
        polar = sum(b*polar.diff(x) for b, x in zip(direction, v))
    coefficients = sy.Poly(polar, *v)
    for i, x in enumerate(v):
        assert coefficients.coeff_monomial(x**3) == 120*direction[i]**3
        for j, y in enumerate(v):
            if i != j:
                k = 3-i-j
                assert coefficients.coeff_monomial(x**2*y) == 12*kappa*direction[j]*direction[k]**2
    assert coefficients.coeff_monomial(sy.prod(v)) == 48*kappa*sy.prod(direction)

    # Direct gradient checks for the two excluded components at lambda = 2.
    u = sy.symbols("u1:4")
    w = sy.Symbol("w")
    cubic = (sum(c*x**2 + c**3 for c, x in zip(u, v)) + w**3
             + kappa*sy.prod(u) + lam*sy.prod(v))
    for parameter, x in ((-3, 0), (-4, -1)):
        point = dict.fromkeys(u, 1) | dict.fromkeys(v, x) | {w: 0, kappa: parameter, lam: 2}
        assert all(cubic.diff(y).subs(point) == 0 for y in u + v + (w,))
    print("Hesse slice: ten polar coefficients and singular points on both components verified.")


def verify_degree_one_kernel():
    # eta_I maps to (-T)^floor(|I|/2) v_I theta^(|I| mod 2).
    # Record the period, odd generator and three square exponents separately.
    def image(mask):
        size = mask.bit_count()
        return size//2, size % 2, tuple((mask >> i) & 1 for i in range(3))

    for left, right in product(range(8), repeat=2):
        lp, lt, lv = image(left)
        rp, rt, rv = image(right)
        n, h, v = image(left ^ right)
        overlap = left & right
        assert lp + rp + (lt+rt)//2 == n + overlap.bit_count()
        assert (lt+rt) % 2 == h
        assert tuple(a+b for a, b in zip(lv, rv)) == tuple(
            v[i]+2*((overlap >> i) & 1) for i in range(3))
        assert -6*lp - 3*lt + sum(lv) == -2*left.bit_count()

    # Removing the dual coefficient of a zero slot by exterior conjugation.
    x, t, a, c = sy.symbols("x T A C")
    wedges = []
    for i in range(2):
        wedge = sy.zeros(4)
        for mask in range(4):
            if not mask & (1 << i):
                wedge[mask | (1 << i), mask] = (-1)**((mask % (1 << i)).bit_count())
        wedges.append(wedge)
    e, f = wedges
    n = t*c*e*f
    simple = x*e.T + t*a*e
    original = simple + t*x*c*f
    assert n*n == sy.zeros(4)
    assert equal((sy.eye(4)+n)*original*(sy.eye(4)-n), simple)
    # The nonidentity scalar sectors have fixed w, fixed s, or only the origin.
    weights = (1, 1, 1, 2, 3)
    correction = {}
    for power in range(1, 6):
        moving = [wt for wt in weights if power*wt % 6]
        if len(moving) % 2 == 0:
            correction[power] = sum(moving)-6*(len(moving)//2)
    assert correction == {2: -7, 3: -6, 4: -7}
    assert [degree for degree in range(8) if 2*degree+correction[3] in (0,2)] == [3,4]
    print("Degree-one kernel: 64 Clifford products, Koszul conjugation and all five scalar sectors.")


def verify_fermat_sign_markings():
    # Represent a projective monomial matrix by sixth-root exponents with
    # last exponent zero and by the column of the nonzero entry in each row.
    identity = ((0, 0, 0), (0, 1, 2))
    group = [((a, b, 0), perm) for a, b in product(range(6), repeat=2)
             for perm in permutations(range(3))]

    def multiply(left, right):
        a, perm = left
        b, other = right
        exponents = [a[i] + b[perm[i]] for i in range(3)]
        return (tuple((e-exponents[2]) % 6 for e in exponents),
                tuple(other[i] for i in perm))

    involutions = [x for x in group if x != identity and multiply(x, x) == identity]
    klein = {frozenset((identity, x, y, multiply(x, y))) for x, y in combinations(involutions, 2)
             if multiply(x, y) == multiply(y, x)}
    inverses = {x: next(y for y in group if multiply(x, y) == identity) for x in group}
    sizes = []
    while klein:
        representative = next(iter(klein))
        orbit = {frozenset(multiply(multiply(x, h), inverses[x]) for h in representative)
                 for x in group}
        assert orbit <= klein
        sizes.append(len(orbit))
        klein.difference_update(orbit)
    assert sorted(sizes) == [1, 9]
    x, y = sy.symbols("x y")
    assert sy.expand((x+y)**6 + (x-y)**6) == 2*x**6 + 30*x**4*y**2 + 30*x**2*y**4 + 2*y**6
    print("Fermat sextic: ten Klein four subgroups in two orbits of sizes 1 and 9.")


def verify_exceptional_projection():
    # End(V) is the regular G-representation, so the invariant multiplicity
    # equals the ordinary section dimension. Use the cubic hypersurface sequence.
    def section_count(degree):
        if degree < 0:
            return 0
        return sy.binomial(6 + degree, 6)

    gram = sy.Matrix(4, 4, lambda i, j: section_count(j-i) - section_count(j-i-3))
    assert list(gram.row(0)) == [1, 7, 28, 83]
    # Act on the four relative Euler pairings with an arbitrary input object.
    projector = sy.eye(4)
    for j in reversed(range(4)):
        projector = (sy.eye(4) - gram.col(j) * sy.eye(4).row(j)) * projector
    assert projector == sy.zeros(4)
    print("Reverse-order mutations annihilate all four exceptional Euler pairings.")


if __name__ == "__main__":
    verify_clifford_products()
    verify_quadrics()
    verify_integrable_cubics()
    verify_smooth_fibers()
    verify_sector_triple_products()
    verify_sector_hilbert_series()
    verify_odd_invariant_generators()
    verify_weighted_presentation()
    verify_hesse_nonrealizable_slice()
    verify_fermat_sign_markings()
    verify_degree_one_kernel()
    verify_exceptional_projection()
