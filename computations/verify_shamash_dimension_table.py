#!/usr/bin/env python3
"""Exact bidegree dimensions forced by the split Koszul resolution.

This checks ONLY combinatorial dimension/rank formulas at s=0; it does
not construct any pivot minor, perturbed Shamash map or comparison kernel.
"""
from math import comb


def b(d, x):
    return comb(x + 2, 2) * comb(d - x + 2, 2) if 0 <= x <= d else 0


def k(i, p):
    return comb(3, p) * comb(3, i - p) if 0 <= p <= 3 and 0 <= i - p <= 3 else 0


def c(i, n, q):
    return sum(k(i, p) * b(n - i, q - p) for p in range(4)) if n >= i else 0


def rank(i, n, q):
    return sum((-1)**(j - i) * c(j, n, q) for j in range(i, 7))


def main():
    actual = [(q, c(4, 6, q), c(3, 6, q), rank(4, 6, q))
              for q in range(7)]
    expected = [(0, 0, 10, 0), (1, 18, 108, 18),
                (2, 81, 270, 72), (3, 117, 344, 100),
                (4, 81, 270, 72), (5, 18, 108, 18),
                (6, 0, 10, 0)]
    assert actual == expected, (actual, expected)
    print("PASS: d4 split bidegree dimensions and ranks", actual)
    for n, i, expected_dims in [(6, 4, (315, 1120, 280)),
                                (7, 5, (126, 840, 120)),
                                (8, 6, (21, 336, 21))]:
        dims = (sum(c(i, n, q) for q in range(n + 1)),
                sum(c(i - 1, n, q) for q in range(n + 1)),
                sum(rank(i, n, q) for q in range(n + 1)))
        assert dims == expected_dims, (n, i, dims)
        print(f"PASS: N={n}, d{i}: {dims}")
    print("PASS: exactness-based dimensions only; no PBW matrix evaluated")


if __name__ == "__main__":
    main()
