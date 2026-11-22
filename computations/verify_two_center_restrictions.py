#!/usr/bin/env python3
"""Exact finite checks for the two-center restriction section.

Run with Python 3 and SymPy:
    python computations/verify_two_center_restrictions.py

The rank-four Koszul factorization uses the ordered exterior basis
(1, e_u, e_v, e_u wedge e_v).  Coefficients are algebraically independent;
all matrix equalities are checked over a rational polynomial ring.

These checks cover the normal factorization, its product homotopy and
polarized cubic transfer, and the binary part of the identical-axis
counterexample.  They do not verify residual mutations, Beck--Chevalley
coherence, a full A-infinity comparison, or categorical smoothness.
Those statements are proved in two_center_restrictions.tex.
"""

import sympy as sp


def require_zero(expression, label):
    entries = expression if isinstance(expression, sp.MatrixBase) else [expression]
    for entry in entries:
        remainder = sp.expand(entry)
        if remainder != 0:
            raise AssertionError(f"{label}: nonzero remainder {remainder}")


def main():
    u, v, t, a2, b2, c2, d, e, f, h, r, s = sp.symbols(
        "u v t A_2 B_2 C_2 d e f h r s"
    )
    identity = sp.eye(4)
    wedge_u = sp.zeros(4)
    wedge_v = sp.zeros(4)
    contract_u = sp.zeros(4)
    contract_v = sp.zeros(4)
    wedge_u[1, 0] = wedge_u[3, 2] = 1
    wedge_v[2, 0] = 1
    wedge_v[3, 1] = -1
    contract_u[0, 1] = contract_u[2, 3] = 1
    contract_v[0, 2] = 1
    contract_v[1, 3] = -1

    for i, left in enumerate((contract_u, contract_v)):
        for j, right in enumerate((wedge_u, wedge_v)):
            require_zero(
                left * right + right * left - int(i == j) * identity,
                "exterior contraction relation",
            )
    for first, second in ((wedge_u, wedge_v), (contract_u, contract_v)):
        require_zero(first * first, "square-zero operator")
        require_zero(second * second, "square-zero operator")
        require_zero(first * second + second * first, "anticommuting operators")

    huu = a2 + d * u + e * v / 3
    huv = b2 / 2 + e * u / 3 + f * v / 3
    hvv = c2 + f * u / 3 + h * v
    a = u * huu + v * huv
    b = u * huv + v * hvv
    q = a2 * u**2 + b2 * u * v + c2 * v**2
    q += d * u**3 + e * u**2 * v + f * u * v**2 + h * v**3
    differential = u * contract_u + v * contract_v
    differential += t * (a * wedge_u + b * wedge_v)
    theta_u = contract_u - t * (huu * wedge_u + huv * wedge_v)
    theta_v = contract_v - t * (huv * wedge_u + hvv * wedge_v)

    require_zero(differential**2 - t * q * identity, "Koszul curvature")
    print("PASS 1/6: exterior operators and Koszul curvature D^2 = t q")

    for theta in (theta_u, theta_v):
        require_zero(differential * theta + theta * differential, "closed generator")
    require_zero(differential * wedge_u + wedge_u * differential - u * identity,
                 "u nullhomotopy")
    require_zero(differential * wedge_v + wedge_v * differential - v * identity,
                 "v nullhomotopy")
    print("PASS 2/6: closed normal generators and coordinate nullhomotopies")

    require_zero(theta_u**2 + t * huu * identity, "u square")
    require_zero(theta_v**2 + t * hvv * identity, "v square")
    require_zero(theta_u * theta_v + theta_v * theta_u + 2 * t * huv * identity,
                 "mixed quadratic product")
    print("PASS 3/6: exact quadratic products and mixed anticommutator")

    theta = r * theta_u + s * theta_v
    homotopy = -t * (
        (d * r**2 + 2 * e * r * s / 3 + f * s**2 / 3) * wedge_u
        + (e * r**2 / 3 + 2 * f * r * s / 3 + h * s**2) * wedge_v
    )
    cohomology_square = -t * (a2 * r**2 + b2 * r * s + c2 * s**2) * identity
    require_zero(
        differential * homotopy + homotopy * differential
        - (theta**2 - cohomology_square),
        "product homotopy",
    )
    print("PASS 4/6: explicit homogeneous product homotopy")

    cubic = d * r**3 + e * r**2 * s + f * r * s**2 + h * s**3
    require_zero(theta * homotopy + homotopy * theta + t * cubic * identity,
                 "polarized cubic transfer")
    print("PASS 5/6: polarized cubic transfer including both mixed coefficients")

    g0 = u**3 + v**3
    g1 = (u + v) * (u - v)**2
    require_zero(g1 - (g0 - u**2 * v - u * v**2), "binary factorization")
    require_zero((g1 - g0).subs(u, 0), "common u=0 axis")
    require_zero((g1 - g0).subs(v, 0), "common v=0 axis")
    require_zero(sp.diff(g0, u) - 3 * u**2, "smooth binary cubic u gradient")
    require_zero(sp.diff(g0, v) - 3 * v**2, "smooth binary cubic v gradient")
    require_zero(sp.diff(g1, u) - (u - v) * (3 * u + v), "singular u gradient")
    require_zero(sp.diff(g1, v) + (u - v) * (u + 3 * v), "singular v gradient")
    for expression in (g1, sp.diff(g1, u), sp.diff(g1, v)):
        require_zero(expression.subs({u: 1, v: 1}), "singular projective point")
    require_zero(g1.subs({u: 1 + s, v: 1}) - (2 + s) * s**2,
                 "singular local equation")
    print("PASS 6/6: identical axes, binary gradients, and singular local equation")


if __name__ == "__main__":
    main()
