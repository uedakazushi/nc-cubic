#!/usr/bin/env python3
"""Exhaustively check the finite groups used in multiblock_roots.tex.

Each H_27 is the group of unipotent upper-triangular 3x3 matrices over F_3,
with coordinates (a,b,c) and product
    (a,b,c)(a',b',c') = (a+a', b+b', c+c'+a*b').
We form H_27^ell / diagonal(center), choosing the last central coordinate 0.
Conjugacy orbits are computed by group multiplication, inverse, and conjugation
by the 2*ell standard noncentral generators. The closed formulas in the paper
are used only after the orbits have been computed.

This is a finite-group check. It does not verify the algebra-isomorphism or
categorical arguments that identify this groupoid with algebraic Zhang twists.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from itertools import product
from math import comb


class CentralProduct:
    def __init__(self, blocks: int):
        if blocks < 2:
            raise ValueError("at least two blocks are required")
        self.blocks = blocks
        self.width = 3 * blocks - 1
        self.one = (0,) * self.width

    def multiply(self, x: tuple[int, ...], y: tuple[int, ...]):
        ell = self.blocks
        a = tuple((x[i] + y[i]) % 3 for i in range(ell))
        b = tuple((x[ell + i] + y[ell + i]) % 3 for i in range(ell))
        last = x[ell - 1] * y[2 * ell - 1]
        c = tuple(
            (x[2 * ell + i] + y[2 * ell + i]
             + x[i] * y[ell + i] - last) % 3
            for i in range(ell - 1)
        )
        return a + b + c

    def inverse(self, x: tuple[int, ...]):
        ell = self.blocks
        a = tuple(-x[i] % 3 for i in range(ell))
        b = tuple(-x[ell + i] % 3 for i in range(ell))
        last = x[ell - 1] * x[2 * ell - 1]
        c = tuple(
            (-x[2 * ell + i] + x[i] * x[ell + i] - last) % 3
            for i in range(ell - 1)
        )
        return a + b + c

    def generators(self):
        result = []
        for i in range(2 * self.blocks):
            entry = [0] * self.width
            entry[i] = 1
            result.append(tuple(entry))
        return result

    def support(self, x: tuple[int, ...]):
        ell = self.blocks
        return sum(x[i] != 0 or x[ell + i] != 0 for i in range(ell))


def check(blocks: int):
    group = CentralProduct(blocks)
    elements = set(product(range(3), repeat=group.width))
    order = len(elements)
    generators = group.generators()
    inverse_generators = [(g, group.inverse(g)) for g in generators]

    # Every encoded tuple is checked, including the exponent-three assertion.
    for element in elements:
        inverse = group.inverse(element)
        assert group.multiply(element, inverse) == group.one
        assert group.multiply(inverse, element) == group.one
        assert group.multiply(group.multiply(element, element), element) == group.one

    remaining = set(elements)
    classes = []
    while remaining:
        representative = next(iter(remaining))
        orbit = {representative}
        queue = deque([representative])
        while queue:
            element = queue.popleft()
            for generator, inverse in inverse_generators:
                conjugate = group.multiply(
                    group.multiply(generator, element), inverse
                )
                assert conjugate in elements
                if conjugate not in orbit:
                    orbit.add(conjugate)
                    queue.append(conjugate)
        assert orbit <= remaining
        remaining.difference_update(orbit)
        classes.append((representative, orbit))

    by_support = Counter()
    sizes = Counter()
    for representative, orbit in classes:
        support = group.support(representative)
        by_support[support] += 1
        sizes[len(orbit)] += 1
        assert len(orbit) == 3 ** min(support, blocks - 1)
        assert all(group.support(element) == support for element in orbit)
        assert all(element[:2 * blocks] == representative[:2 * blocks]
                   for element in orbit)

    assert order == 3 ** (3 * blocks - 1)
    assert len(classes) == (11 ** blocks + 2 * 8 ** blocks) // 3
    for support in range(blocks + 1):
        predicted = comb(blocks, support) * 8 ** support * 3 ** max(
            blocks - 1 - support, 0
        )
        assert by_support[support] == predicted
    assert sizes[1] == 3 ** (blocks - 1)
    assert sum(size * number for size, number in sizes.items()) == order

    print(f"blocks={blocks}, order={order}, conjugacy_classes={len(classes)}")
    print("  classes_by_support=" + str(dict(sorted(by_support.items()))))
    print("  conjugacy_sizes=" + str(dict(sorted(sizes.items()))))
    print(f"  scalar_twist_classes={sizes[1]}; exact checks passed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blocks", type=int, nargs="+", default=[2, 3])
    args = parser.parse_args()
    for blocks in args.blocks:
        check(blocks)


if __name__ == "__main__":
    main()
