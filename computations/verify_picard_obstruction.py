#!/usr/bin/env python3
"""Exact finite identities used in the point-shift Picard obstruction.

Run with Python 3 and SymPy. The valuation, descent, and derived-category
arguments are proofs in the paper; these identities do not replace them.
"""

import sympy as sp


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
