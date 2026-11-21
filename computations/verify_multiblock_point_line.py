#!/usr/bin/env python3
"""Exact checks for the centre-to-point-line comparison.

Run: python computations/verify_multiblock_point_line.py
Dependency: SymPy. Fermat linear algebra is over QQ(t), not at sample values;
the Hesse determinant and comparison certificate are polynomial identities.
This verifies finite-degree identities, not PBW, smoothness, or equivalences.
"""

from itertools import product

import sympy as sp
from sympy.polys.matrices import DomainMatrix


t = sp.Symbol("t")


def add(*polys):
    result = {}
    for poly in polys:
        for word, coefficient in poly.items():
            result[word] = sp.expand(result.get(word, 0) + coefficient)
    return {word: coefficient for word, coefficient in result.items() if coefficient != 0}


def scale(coefficient, poly):
    return {word: sp.expand(coefficient * value) for word, value in poly.items()}


def mul(left, right):
    result = {}
    for a, av in left.items():
        for b, bv in right.items():
            word = a + b
            result[word] = sp.expand(result.get(word, 0) + av * bv)
    return result


def comm(left, right):
    return add(mul(left, right), scale(-1, mul(right, left)))


letters = [{(i,): sp.Integer(1)} for i in range(3)]
cube_sum = {(i, i, i): sp.Integer(1) for i in range(3)}
cyclic_sum = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1}
omega = add(scale(3 + t**3, cube_sum), scale(-2 * t**2, cyclic_sum))
relations = []
for i in range(3):
    j, k = (i + 1) % 3, (i + 2) % 3
    relations.append(add(comm(letters[j], letters[k]), scale(-t, mul(letters[i], letters[i]))))

words = list(product(range(3), repeat=4))
word_index = {word: index for index, word in enumerate(words)}


def column(poly):
    result = [sp.Integer(0)] * len(words)
    for word, coefficient in poly.items():
        result[word_index[word]] = coefficient
    return sp.Matrix(result)


relation_columns = []
for relation in relations:
    for prefix_length in range(3):
        for prefix in product(range(3), repeat=prefix_length):
            for suffix in product(range(3), repeat=2 - prefix_length):
                relation_columns.append(column(mul(mul({prefix: 1}, relation), {suffix: 1})))

witnesses = []
for i in range(3):
    j, k = (i + 1) % 3, (i + 2) % 3
    yz_x2 = comm(mul(letters[j], letters[k]), mul(letters[i], letters[i]))
    witnesses.extend([
        comm(omega, letters[i]),
        add(comm(cube_sum, letters[i]), scale(-t**2, yz_x2)),
        add(scale(2, comm(cyclic_sum, letters[i])), scale(-(3 + t**3), yz_x2)),
    ])

matrix = sp.Matrix.hstack(*relation_columns)
augmented = sp.Matrix.hstack(matrix, *(column(w) for w in witnesses))
field = sp.QQ.frac_field(t)
rank = DomainMatrix.from_Matrix(matrix).convert_to(field).rank()
augmented_rank = DomainMatrix.from_Matrix(augmented).convert_to(field).rank()
assert rank == augmented_rank == 66, (rank, augmented_rank)

x, y, z = sp.symbols("x y z")
point = x**3 + y**3 + z**3 + t**2 * x * y * z
point_matrix = sp.Matrix([[-t * x, -z, y], [z, -t * y, -x], [-y, x, -t * z]])
assert sp.expand(point_matrix.det() + t * point) == 0

abelian_omega = (3 + t**3) * (x**3 + y**3 + z**3) - 6 * t**2 * x * y * z
jacobian_ideal = sp.groebner([x**2, y**2, z**2], x, y, z, domain=field)
omega_image = jacobian_ideal.reduce(abelian_omega)[1]
point_image = jacobian_ideal.reduce(point)[1]
assert omega_image == -6 * t**2 * x * y * z
assert point_image == t**2 * x * y * z
assert sp.expand(omega_image + 6 * point_image) == 0

# The Hesse comparison survives degeneration of the degree-three abelianization.
# This certificate has polynomial coefficients: no localization or rank test
# enters the equality. Centrality of this Hesse element is a separate, cited
# theorem and is not certified here by specialization or sampling.
a, b, c = sp.symbols("a b c")
commutative_cubes = x**3 + y**3 + z**3
hesse_point = a * b * c * commutative_cubes - (a**3 + b**3 + c**3) * x * y * z
hesse_matrix = sp.Matrix([[c*x, b*z, a*y], [a*z, c*y, b*x], [b*y, a*x, c*z]])
assert sp.expand(hesse_matrix.det() + hesse_point) == 0
hesse_omega_ab = (
    c * (a**3 - b**3) * commutative_cubes
    + 3 * (a * (b**3 - c**3) + b * (c**3 - a**3)) * x * y * z
)
commutative_relations = [c*x**2 + (a+b)*y*z,
                         c*y**2 + (a+b)*z*x,
                         c*z**2 + (a+b)*x*y]
relation_certificate = (a-b)**3 * sum(
    variable * relation
    for variable, relation in zip((x, y, z), commutative_relations)
)
assert sp.expand(hesse_omega_ab - 3*(a-b)*hesse_point - relation_certificate) == 0

print("OK QQ(t): degree-four relation rank 66; all 9 centre/commutator identities vanish.")
print("OK determinant: det(M) = -t * (x^3+y^3+z^3+t^2 xyz).")
print("OK maximal commutative quotient: Omega -> -6 t^2 xyz, point cubic -> t^2 xyz.")
print("OK Hesse determinant over QQ[a,b,c,x,y,z]: det(M_H) = -F_H.")
print("OK Hesse certificate: ab(Omega_H)-3(a-b)F_H = (a-b)^3 sum(x_i r_i^ab).")
print("LIMIT: finite-degree identities only; no PBW, smoothness, or categorical verification.")
