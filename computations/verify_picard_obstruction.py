#!/usr/bin/env python3
"""Exact identities for the point-shift Picard obstruction and third division.

Run with Python 3 and SymPy. The valuation, descent, connectedness, and
derived-category arguments are proofs in the paper; these identities do
not replace them. Hesse arithmetic is shared with verify_active_sign.py.
"""

import sympy as sp

from verify_active_sign import (
    invariants as hesse_invariants,
    p as hesse_p,
    q as hesse_q,
    reduce_coefficient as hesse_reduce,
    reduce_matrix as hesse_reduce_matrix,
    zeta as hesse_zeta,
)


def check(name, expression):
    if sp.cancel(sp.expand(expression)) != 0:
        raise AssertionError(name)
    print(f"PASS {name}")


x, y, z, t, b, lam, zeta = sp.symbols("x y z t b lam zeta")
cubic = x**3 - t**3 * y**3 - b * z**3 + lam * x * y * z
b_lam = b + lam**3 / (27 * t**3)
check(
    "Hesse tangent has triple contact",
    cubic.subs(x, t * y - lam * z / (3 * t)) + b_lam * z**3,
)

conjugate_product = sp.prod(
    x - zeta**i * t * y + zeta ** ((3 - i) % 3) * lam * z / (3 * t)
    for i in range(3)
)
expected_norm = cubic + b_lam * z**3
numerator = sp.together(conjugate_product - expected_norm).as_numer_denom()[0]
check(
    "three tangent ratios have norm b_lambda",
    sp.rem(numerator, zeta**2 + zeta + 1, zeta),
)

A, B, C, mu, P, Q = sp.symbols("A B C mu P Q")
g = -2 / (A - B) * (C * (x**3 + y**3 + z**3) / 3 + (A + B) * x * y * z)
point_cubic = A * B * C * (x**3 + y**3 + z**3) - (A**3 + B**3 + C**3) * x * y * z
check(
    "normalized potential has the prescribed point cubic",
    g + sp.det(sp.hessian(g, (x, y, z))) / 24 - 8 * point_cubic / (3 * (A - B)**3),
)

inverse = {A: (2 - Q) / 4, B: -(Q + 2) / 4, C: -P / 2}
check(
    "Hesse parameter chart has a rational inverse",
    g.subs(inverse) - (P * (x**3 + y**3 + z**3) / 3 + Q * x * y * z),
)
check(
    "singular symmetric cubic would force singular Hesse curve",
    (A**3 + B**3 + C**3 - 3 * mu * A * B * C)
    - (C**3 + (A + B)**3)
    + 3 * A * B * (A + B + mu * C),
)

a, beta = sp.symbols("a beta", integer=True)
rotation = sp.Matrix([[-2, -1], [3, 1]])
centralizer = sp.Matrix([[a, beta], [-3 * beta, a - 3 * beta]])
assert centralizer * rotation == rotation * centralizer
assert sp.expand(centralizer.det()) == a**2 - 3 * a * beta + 3 * beta**2
# The paper's completed-square bound gives |beta| <= 1, hence |a| <= 2.
solutions = {
    tuple(centralizer.subs({a: av, beta: bv}))
    for av in range(-2, 3)
    for bv in range(-1, 2)
    if av**2 - 3 * av * bv + 3 * bv**2 == 1
}
expected = {tuple(sign * rotation**power) for sign in (-1, 1) for power in range(3)}
assert solutions == expected and len(solutions) == 6
print("PASS all six integral numerical rotation centralizers")

# The cyclic plane twist and its Picard-symbol coefficients. These exact
# polynomial checks do not prove the residue or the torsor-descent arguments.
aa, dd, ss = sp.symbols("aa dd ss", nonzero=True)
original = x**3 - aa * y**3 - b * z**3 + lam * x * y * z
twisted = x**3 - aa * dd * y**3 - b * dd**2 * z**3 + lam * dd * x * y * z
check(
    "cyclic plane twist becomes the original cubic after a cube root",
    twisted.subs({dd: ss**3, y: y / ss, z: z / ss**2}, simultaneous=True)
    - original,
)
check(
    "cyclic twist changes the tangent norm by d squared",
    b * dd**2 + (lam * dd)**3 / (27 * aa * dd)
    - dd**2 * (b + lam**3 / (27 * aa)),
)

# Alternating symbols in the ordered classes (a, d, B), modulo 3.
def exterior(left, right):
    return sp.Matrix([
        left[i] * right[j] - left[j] * right[i]
        for i, j in ((0, 1), (0, 2), (1, 2))
    ])


symbol_difference = (
    exterior((1, 1, 0), (0, 2, 1))  # (ad, d^2 B)
    - exterior((1, 0, 0), (0, 0, 1))  # (a, B)
    - exterior((0, 1, 0), (1, 0, 1))  # (d, aB)
)
assert all(coefficient % 3 == 0 for coefficient in symbol_difference)
print("PASS cyclic Picard correction is the symbol (d,aB) modulo 3")

# The universal Jacobian's full three-torsion field. All arithmetic stays
# in QQ(zeta)[p,q], with zeta^2 + zeta + 1 = 0.
hesse_s, hesse_t = hesse_invariants(hesse_p, hesse_q)
sqrt_minus_three = 1 + 2 * hesse_zeta
torsion_x = -9 * hesse_q**2
torsion_y = 12 * sqrt_minus_three * (hesse_p**3 + hesse_q**3)
assert hesse_reduce(
    torsion_y**2 - (torsion_x**3 - 27 * hesse_s * torsion_x + 54 * hesse_t)
) == 0
assert hesse_reduce(
    3 * torsion_x**4 - 162 * hesse_s * torsion_x**2
    + 648 * hesse_t * torsion_x - 729 * hesse_s**2
) == 0
print("PASS explicit Hesse point lies on the universal Jacobian and has order three")

hesse_a = sp.diag(hesse_zeta, 1)
hesse_a_inverse = sp.diag(hesse_zeta**2, 1)
hesse_b = sqrt_minus_three / 3 * sp.Matrix([[1, 1], [2, -1]])
hesse_c = hesse_reduce_matrix(hesse_a * hesse_b * hesse_a_inverse)
hesse_d = hesse_reduce_matrix(hesse_a_inverse * hesse_b * hesse_a)
hesse_identity = sp.eye(2)
quaternion = [
    hesse_identity, -hesse_identity, hesse_b, -hesse_b,
    hesse_c, -hesse_c, hesse_d, -hesse_d,
]
hesse_group = [
    hesse_reduce_matrix(element * hesse_a**j)
    for element in quaternion for j in range(3)
]
assert len({tuple(element) for element in hesse_group}) == 24
torsion_point = (hesse_reduce(torsion_x), hesse_reduce(torsion_y))
torsion_orbit = set()
torsion_stabilizer = set()
for matrix in hesse_group:
    transformed_p, transformed_q = matrix * sp.Matrix([hesse_p, hesse_q])
    image = (
        hesse_reduce(-9 * transformed_q**2),
        hesse_reduce(12 * sqrt_minus_three * (transformed_p**3 + transformed_q**3)),
    )
    torsion_orbit.add(image)
    if image == torsion_point:
        torsion_stabilizer.add(tuple(matrix))
assert len(torsion_orbit) == 8
assert torsion_stabilizer == {
    tuple(hesse_reduce_matrix(hesse_a**j)) for j in range(3)
}
print("PASS Hesse orbit has all eight nonzero three-torsion points and stabilizer C3")

stabilizer_core = set(torsion_stabilizer)
for matrix in hesse_group:
    inverse_matrix = next(
        candidate for candidate in hesse_group
        if hesse_reduce_matrix(matrix * candidate) == hesse_identity
    )
    conjugate = {
        tuple(hesse_reduce_matrix(matrix * sp.Matrix(2, 2, element) * inverse_matrix))
        for element in torsion_stabilizer
    }
    stabilizer_core &= conjugate
assert stabilizer_core == {tuple(hesse_identity)}
print("PASS the order-three stabilizer has trivial normal core in the Hesse group")

# Check the orientation of the actual right point correspondence: its
# three multilinear relations vanish at (o,p), o=(1:-1:0), p=(A:B:C).
left_point = (sp.Integer(1), sp.Integer(-1), sp.Integer(0))
right_point = (A, B, C)
point_relations = (
    A * left_point[1] * right_point[2]
    + B * left_point[2] * right_point[1]
    + C * left_point[0] * right_point[0],
    A * left_point[2] * right_point[0]
    + B * left_point[0] * right_point[2]
    + C * left_point[1] * right_point[1],
    A * left_point[0] * right_point[1]
    + B * left_point[1] * right_point[0]
    + C * left_point[2] * right_point[2],
)
assert all(sp.expand(relation) == 0 for relation in point_relations)
print("PASS the right point correspondence sends the Hesse origin to (A:B:C)")
