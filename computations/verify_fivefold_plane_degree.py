#!/usr/bin/env python3
"""Verify the odd Pluecker degree of the plane surface of a cubic fivefold.

On Gr(3,7), F_2(Y) is the regular zero locus of Sym^3(S^*), of rank 10.
For Chern roots x,y,z of S^*, its Pluecker degree is

 [x^6 y^5 z^4] prod_{a+b+c=3}(a*x+b*y+c*z)
                  * (x+y+z)^2 * (x-y)*(x-z)*(y-z).

The coefficient formula is the Grassmannian integration formula, and the
expected value 2835 is Ciliberto--Zaidenberg, arXiv:1903.11294v2, Example 4.4.
https://arxiv.org/html/1903.11294v2

Only integer polynomial arithmetic is used; there are no external packages.
This verifies the numerical intersection calculation, not the categorical
descent or the existence of a coherent order-two action.
"""

from collections import defaultdict
from math import gcd


def multiply_linear(poly, weights):
    """Multiply a sparse three-variable integer polynomial by a linear form."""
    result = defaultdict(int)
    for monomial, coefficient in poly.items():
        for variable, weight in enumerate(weights):
            if weight:
                exponent = list(monomial)
                exponent[variable] += 1
                result[tuple(exponent)] += coefficient * weight
    return {monomial: coefficient for monomial, coefficient in result.items()
            if coefficient}


def plane_surface_degree():
    poly = {(0, 0, 0): 1}
    for a in range(4):
        for b in range(4 - a):
            poly = multiply_linear(poly, (a, b, 3 - a - b))
    for weights in ((1, 1, 1), (1, 1, 1),
                    (1, -1, 0), (1, 0, -1), (0, 1, -1)):
        poly = multiply_linear(poly, weights)
    return poly.get((6, 5, 4), 0)


def main():
    degree = plane_surface_degree()
    if degree != 2835:
        raise AssertionError(f"Expected published degree 2835, obtained {degree}")
    print(f"PASS: degree(F_2(Y)) = {degree}; gcd(degree, 2) = {gcd(degree, 2)}")


if __name__ == "__main__":
    main()
