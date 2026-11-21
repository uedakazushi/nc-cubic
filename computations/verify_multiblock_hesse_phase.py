#!/usr/bin/env python3
"""Exact polynomial checks for the natural multiblock period formula.

2026-11-21 / v39.  Requires Python 3 and SymPy.

These checks verify finite algebraic identities used in mbhp and mbfc.
They do not verify the categorical period comparison, descent of kernels,
Orlov's theorem, or the minimal-degree proofs.
Run from the repository root:
    python3 computations/verify_multiblock_hesse_phase.py
"""

import sympy as s


def zero(expr):
    assert s.cancel(expr) == 0, s.factor(expr)


a, b, c, mu, C, U = s.symbols("a b c mu C U")
F = a**3 + b**3 + c**3 - 3 * mu * a * b * c
V_word = (-c * C - a * U) / b
Omega = c * (a**3 - b**3) * C + a * (b**3 - c**3) * U + b * (c**3 - a**3) * V_word
regular = 3 * a * c * ((a**2 - mu * b * c) * C + (mu * a * b - c**2) * U)
zero(Omega - regular - (-c * C + a * U) * F)
regular_center = 3 / b * ((a**2 - mu * b * c) * C + (mu * a * b - c**2) * U)
W = s.symbols("V_word")
Omega_a = c * (a**3 - b**3) * C + a * (b**3 - c**3) * ((-c * C - b * W) / a) + b * (c**3 - a**3) * W
regular_a = -3 / a * ((b**2 - mu * a * c) * C + (mu * a * b - c**2) * W)
zero(s.rem(s.fraction(s.cancel(Omega_a - a * b * c * regular_a))[0], F, a))
zero(regular_center.subs({a: 1, b: -1, c: 0}) + 3 * (C - mu * U))
print("PASS: both regularized center charts and origin specialization")

# The branch through (1:-1:0), to the order used for the period calibration.
b_jet = -1 - mu * c + (mu**3 - 1) * c**3 / 3
jet_residual = s.Poly(s.expand(F.subs({a: 1, b: b_jet})), c)
for degree in range(4):
    zero(jet_residual.nth(degree))
print("PASS: Hesse branch at the origin through cubic order")

# Weierstrass coordinates with the explicitly specified Hodge frame.
Fa = F.subs(a, 1)
ell = 1 + b + mu * c
X = 3 * (mu**3 - 1) * c / ell
V = 9 * (1 - mu**3) * (1 - b) / ell
db_dc = -(c**2 - mu * b) / (b**2 - mu * c)
dX_omega = (s.diff(X, c) + s.diff(X, b) * db_dc) * (3 * b**2 - 3 * mu * c)


def zero_on_hesse(expr):
    numerator = s.fraction(s.cancel(expr))[0]
    # Treat b as the elimination variable; coefficients are rational in mu,c.
    remainder = s.rem(numerator, Fa, b)
    zero(remainder)


zero_on_hesse(dX_omega - V)
weierstrass = 4 * X**3 - 27 * mu**2 * X**2 + 54 * mu * (mu**3 - 1) * X - 27 * (mu**3 - 1)**2
zero_on_hesse(V**2 - weierstrass)
zero(s.limit(c**3 * V.subs(b, b_jet), c, 0) + 54)
q = ell / (9 * (mu**3 - 1) * (1 - b))
zero(q * V + 1)
zero(s.limit(q.subs(b, b_jet) / c**3, c, 0) - s.Rational(1, 54))
print("PASS: dX/omega=V, Weierstrass equation, qV=-1, origin coefficients")

# Fixed Hesse-level automorphisms preserve the equation, including its scale.
x, y, z, zeta, u, v = s.symbols("x y z zeta u v")
hesse = u * (x**3 + y**3 + z**3) + v * x * y * z
for change in (
    {x: x, y: zeta * y, z: zeta**2 * z},
    {x: y, y: z, z: x},
    {x: y, y: x, z: z},
):
    difference = s.expand(hesse.subs(change, simultaneous=True) - hesse)
    zero(s.rem(difference, zeta**2 + zeta + 1, zeta))
print("PASS: fixed Hesse-level generators preserve both cubic terms")

# Over C(a), a projective order-three automorphism can have nonzero multiplier.
twisted = x**3 + a * y**3 + a**2 * z**3 - 3 * mu * a * x * y * z
g = {x: a * z, y: x, z: y}
zero(twisted.subs(g, simultaneous=True) - a * twisted)
for variable in (x, y, z):
    moved = variable
    for _ in range(3):
        moved = moved.subs(g, simultaneous=True)
    zero(moved - a * variable)
print("PASS: twisted example g(f)=a*f and g^3=a*I")
print(f"All exact identities passed (SymPy {s.__version__}).")
