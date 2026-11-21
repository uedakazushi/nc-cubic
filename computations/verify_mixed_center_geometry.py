#!/usr/bin/env python3
"""Exact centres and critical fibres for two mixed Sklyanin factors.

Requires Python 3 + SymPy and the sibling verify_mixed_pi_center.py.
All noncommutative calculations use Fraction over QQ.  No free-word space
of length 18 is enumerated: at stage n the temporary highest-degree space
has 3*binomial(n+1,2) columns.  At n=18 this is 513, not 3**18.

The established PBW theorem supplies dim gr(D)_n=binomial(n+2,2).
Each stage imposes actual relation multiples and checks precisely this
dimension, so its quotient map is an isomorphism in the required degrees.
This is an exact finite calculation, not a formal-proof-assistant proof.

Default: verify both examples.  To locate the existing centre formulae:
  python3 verify_mixed_center_geometry.py --source /path/verify_mixed_pi_center.py
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import permutations, product
from pathlib import Path
from time import monotonic
import sympy as sp


class FilteredQuotient:
    """Word representatives and exact right multiplication through a bound."""
    def __init__(self, alpha):
        self.alpha = tuple(map(Q, alpha))
        self.words = [(), (0,), (1,), (2,)]
        self.degrees = [0, 1, 1, 1]
        self.front = {0: [0], 1: [1, 2, 3]}
        self.mul = {(0, i): {1+i: Q(1)} for i in range(3)}

    def build(self, bound):
        for n in range(2, bound+1):
            previous = self.front[n-1]
            columns = 3*len(previous)
            positions = {w: i for i, w in enumerate(previous)}
            echelon = {}

            def reduce(row):
                row = {j: Q(c) for j, c in row.items() if c}
                while row:
                    pivot = next((j for j in sorted(row) if j in echelon), None)
                    if pivot is None:
                        break
                    coefficient = row.pop(pivot)
                    for j, value in echelon[pivot].items():
                        if j == pivot:
                            continue
                        value = row.get(j, 0)-coefficient*value
                        if value:
                            row[j] = value
                        else:
                            row.pop(j, None)
                return row

            def append_temporary(vector, letter):
                result = {}
                for j, c in vector.items():
                    if self.degrees[j] == n-1:
                        index = 3*positions[j]+letter
                        result[index] = result.get(index, 0)+c
                    else:
                        for k, value in self.mul[j, letter].items():
                            index = columns+k
                            result[index] = result.get(index, 0)+c*value
                return result

            for w in self.front[n-2]:
                for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
                    row = {columns+w: self.alpha[i]}
                    for a, b, sign in ((j, k, 1), (k, j, -1), (i, i, -1)):
                        for index, c in append_temporary(self.mul[w, a], b).items():
                            row[index] = row.get(index, 0)+sign*c
                    row = reduce(row)
                    if row:
                        pivot = min(row)
                        assert pivot < columns, "Unexpected relation of lower degree"
                        coefficient = row[pivot]
                        echelon[pivot] = {j: c/coefficient for j, c in row.items()}
            free = [j for j in range(columns) if j not in echelon]
            assert len(free) == (n+1)*(n+2)//2
            remap = {j: len(self.words)+k for k, j in enumerate(free)}
            self.front[n] = list(remap.values())
            self.words.extend(self.words[previous[j//3]]+(j % 3,) for j in free)
            self.degrees.extend([n]*len(free))
            for j in range(columns):
                vector = reduce({j: Q(1)})
                self.mul[previous[j//3], j % 3] = {
                    remap[k] if k < columns else k-columns: c
                    for k, c in vector.items()}
        assert len(self.words) == (bound+1)*(bound+2)*(bound+3)//6

    def append(self, vector, letter):
        result = {}
        for i, c in vector.items():
            for j, value in self.mul[i, letter].items():
                result[j] = result.get(j, 0)+c*value
        return {j: c for j, c in result.items() if c}

    def specialize(self, polynomial):
        terms = {}
        for (powers, word), c in polynomial.items():
            c *= product_scalar(a**e for a, e in zip(self.alpha, powers))
            terms[word] = terms.get(word, 0)+c
        return {w: c for w, c in terms.items() if c}

    def act(self, vector, terms):
        """Evaluate a right polynomial, reusing every common word prefix."""
        prefixes = {w[:length] for w in terms for length in range(len(w)+1)}
        cache = {(): vector}
        result = {}
        for word in sorted(prefixes, key=lambda w: (len(w), w)):
            if word:
                cache[word] = self.append(cache[word[:-1]], word[-1])
            if word in terms:
                for j, c in cache[word].items():
                    result[j] = result.get(j, 0)+terms[word]*c
        return {j: c for j, c in result.items() if c}


def product_scalar(values):
    result = 1
    for value in values:
        result *= value
    return result


def exponents(total, length):
    if length == 1:
        yield (total,)
    else:
        for a in range(total+1):
            for tail in exponents(total-a, length-1):
                yield (a,)+tail


TOP = {(2, 1, 0, 0): 81, (1, 2, 0, 0): 468,
       (0, 3, 0, 0): 784, (1, 0, 1, 1): -36,
       (0, 1, 1, 1): -176, (0, 0, 3, 0): 16, (0, 0, 0, 3): 16}
LOWER_MONOMIALS = [
    (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1),
    (0, 2, 0, 0), (0, 1, 1, 0), (0, 1, 0, 1),
    (0, 0, 2, 0), (0, 0, 1, 1), (0, 0, 0, 2),
    (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0),
    (0, 0, 0, 1), (0, 0, 0, 0)]
EXAMPLES = [
    ((1, 4, 9),
     [-59760, 144, 324, -193984, -13952, -20752,
      5152, 13856, 3472, -47952, 7099264, -152048, -153248, 997056],
     [(1, 784), (1, 256), (9, 3136), (9, 784), (343, 73728)],
     [129140163, -188108856360, 92316693932208,
      -16917496764590592, 875501309973348352]),
    ((16, 25, 49),
     [-11301840, 230400, 451584, -39551680, -3701824, -3076672,
      718992, 2825120, 899856, -16719897600, 180425753600,
      -43671732224, -48922542080, 448348972646400],
     [(1, 200704), (1, 38416), (1, 30976), (9, 80656),
      (748505944125, 37623589339922432)],
     [129140163, -34079674491720, 2934863745734897712,
      -83555308663913970224640, 165916680996850221150748672])
]


def central_relation(quotient, source):
    omega, c0, cp, cm = source.central_elements()
    raw_forms = [source.power(omega, 2), c0, cp, cm]
    forms = []
    for raw in raw_forms:
        normal = quotient.act({0: Q(1)}, quotient.specialize(raw))
        forms.append({quotient.words[j]: c for j, c in normal.items()})
    vectors = {(0, 0, 0, 0): {0: Q(1)}}
    for degree in range(1, 4):
        for powers in exponents(degree, 4):
            j = next(j for j in range(4) if powers[j])
            previous = list(powers)
            previous[j] -= 1
            vectors[powers] = quotient.act(vectors[tuple(previous)], forms[j])
    echelon, relations = {}, []
    keys = list(vectors)
    for index, powers in enumerate(keys):
        row, coefficients = vectors[powers].copy(), {index: Q(1)}
        while row:
            pivot = max(row)
            if pivot not in echelon:
                break
            old, old_coefficients = echelon[pivot]
            coefficient = row[pivot]
            for target, vector in ((row, old), (coefficients, old_coefficients)):
                for j, c in vector.items():
                    value = target.get(j, 0)-coefficient*c
                    if value:
                        target[j] = value
                    else:
                        target.pop(j, None)
        if row:
            coefficient = row[max(row)]
            echelon[max(row)] = ({j: c/coefficient for j, c in row.items()},
                                 {j: c/coefficient for j, c in coefficients.items()})
        else:
            relations.append({keys[j]: c for j, c in coefficients.items()})
    assert len(keys) == 35 and len(echelon) == 34 and len(relations) == 1
    relation = relations[0]
    scale = Q(81)/relation[(2, 1, 0, 0)]
    return {powers: scale*c for powers, c in relation.items()}


def length_of_quotient(groebner):
    """Count standard monomials of a zero-dimensional monomial ideal."""
    leading = [p.LM(order=groebner.order).exponents for p in groebner.polys]
    bounds = []
    for i in range(len(groebner.gens)):
        bounds.append(min(e[i] for e in leading
                          if e[i] and all(not e[j] for j in range(len(e)) if j != i)))
    return sum(not any(all(a >= b for a, b in zip(e, leading_term))
                       for leading_term in leading)
               for e in product(*(range(n) for n in bounds)))


def determinant(matrix):
    """Small determinant expanded directly; avoid costly rational simplification."""
    n = matrix.rows
    return sp.expand(sum(
        (-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        *sp.prod(matrix[i, p[i]] for i in range(n))
        for p in permutations(range(n))))


def verify_geometry(relation, linear_factors, quartic_coefficients):
    w, u, v, t = sp.symbols("W U V T")
    variables = (u, v, t, w)
    polynomial = sp.expand(sum(
        sp.Rational(c)*sp.prod(x**e for x, e in zip((w, u, v, t), powers))
        for powers, c in relation.items()))
    h = sp.prod(a*w-b for a, b in linear_factors)
    q = sp.Poly.from_list(quartic_coefficients, w).as_expr()
    delta = sp.Poly(w*h**2*q, w).monic()
    assert sp.Poly(q, w).is_irreducible
    assert sp.gcd(w*h, q) == 1 and sp.gcd(h, sp.diff(h, w)) == 1

    equations = [polynomial]+[sp.diff(polynomial, x) for x in (u, v, t)]
    critical = sp.groebner(equations, *variables, order="grevlex")
    assert critical.is_zero_dimensional
    critical = critical.fglm("lex")
    univariate = [p.as_expr() for p in critical.polys
                  if p.as_expr().free_symbols <= {w}]
    assert len(univariate) == 1 and sp.Poly(univariate[0], w).monic() == delta
    assert length_of_quotient(critical) == 18

    derivative = sp.diff(polynomial, w)
    singular = sp.groebner(equations+[derivative], *variables, order="grevlex").fglm("lex")
    assert length_of_quotient(singular) == 5
    assert sp.Poly(singular.polys[-1].as_expr(), w).monic() == sp.Poly(h, w).monic()
    at_zero = sp.groebner([f.subs(w, 0) for f in equations], u, v, t, order="lex")
    assert length_of_quotient(at_zero) == 4
    zero_quartic = at_zero.polys[-1].as_expr()
    assert sp.degree(zero_quartic, t) == 4
    assert sp.gcd(zero_quartic, sp.diff(zero_quartic, t)) == 1
    at_quartic = sp.groebner(equations+[q], *variables, order="grevlex").fglm("lex")
    assert length_of_quotient(at_quartic) == 4

    def is_unit_on(basis, value):
        remainder = basis.reduce(value)[1]
        return list(sp.groebner(list(basis)+[remainder], *basis.gens)) == [1]

    hessian3 = determinant(sp.hessian(polynomial, (u, v, t)))
    hessian4 = determinant(sp.hessian(polynomial, (w, u, v, t)))
    assert is_unit_on(at_quartic, derivative)
    assert is_unit_on(at_quartic, hessian3)
    assert is_unit_on(at_zero, derivative.subs(w, 0))
    assert is_unit_on(at_zero, hessian3.subs(w, 0))
    assert is_unit_on(singular, hessian4)
    print("  PASS: critical scheme length 18; eliminant W*H(W)^2*Q(W)")
    print("  H =", sp.factor(h))
    print("  Q =", q)
    print("  PASS: centre has 14 ordinary double points; 19 singular Omega fibres")
    print("  PASS: Q(Omega^2)=0 gives 8 Morse critical points on the smooth centre")


def verify_mixed_morse_resultant():
    """The 8-by-8 sums of the two new Morse critical spectra."""
    c, z, w = sp.symbols("c z W")
    q1, q2 = (sp.Poly.from_list(example[3], w).as_expr() for example in EXAMPLES)
    resultant = sp.resultant(q1.subs(w, (-c-100*z)**2), q2.subs(w, z**2), z)
    polynomial = sp.Poly(resultant, c).primitive()[1]
    if polynomial.LC() < 0:
        polynomial = -polynomial
    assert polynomial.degree() == 64
    assert all(exponent[0] % 2 == 0 for exponent, _ in polynomial.terms())
    assert sp.gcd(polynomial, polynomial.diff()).degree() == 0
    assert polynomial.eval(0) != 0
    scalar1 = [sign*a for sign in (-1, 1)
               for a in (28, 16, sp.Rational(56, 3), sp.Rational(28, 3))]
    scalar2 = [sign*a for sign in (-1, 1)
               for a in (448, 196, 176, sp.Rational(284, 3))]
    scalar_norm = sp.Poly(sp.prod(c+a+100*b for a in scalar1 for b in scalar2), c)
    assert scalar_norm.degree() == 64
    assert sp.gcd(polynomial, scalar_norm).degree() == 0
    canonical = ",".join(map(str, polynomial.all_coeffs())).encode("ascii")
    digest = sha256(canonical).hexdigest()
    assert len(canonical) == 6910
    assert digest == "20923491b92e21c3fceb0b30b0f331e500d83f898f756d0cb853ace75de42dbb"
    print("PASS: mixed Morse resultant is primitive, even, degree 64, squarefree")
    print("PASS: nonzero at c=0 and coprime to the earlier 64-character norm")
    print("  SHA256 of comma-joined descending coefficients:", digest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path,
                        default=Path(__file__).with_name("verify_mixed_pi_center.py"))
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("mixed_centre", args.source)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    for alpha, lower, linear_factors, quartic_coefficients in EXAMPLES:
        start = monotonic()
        print("alpha =", alpha, flush=True)
        quotient = FilteredQuotient(alpha)
        quotient.build(18)
        print("  PASS: PBW dimensions through 18; 1330 word representatives", flush=True)
        relation = central_relation(quotient, source)
        expected = TOP | dict(zip(LOWER_MONOMIALS, lower))
        assert relation == expected
        print("  PASS: the displayed 21-term relation spans the 35-column kernel", flush=True)
        verify_geometry(relation, linear_factors, quartic_coefficients)
        print("  seconds:", round(monotonic()-start, 2), flush=True)
    verify_mixed_morse_resultant()


if __name__ == "__main__":
    main()
