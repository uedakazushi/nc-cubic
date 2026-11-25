"""Verify the Massey sign and the obstruction degrees in cubic_orbit_generator.tex."""

from itertools import combinations_with_replacement, product

import sympy as sp


def exterior_product(left, right):
    """Return the coefficient and basis mask of a product of exterior monomials."""
    if left & right:
        return 0, 0
    swaps = sum((left >> (i + 1)).bit_count() for i in range(right.bit_length())
                if right & (1 << i))
    return (-1) ** swaps, left | right


def bar_basis(arity, degree):
    # For an input of total wedge length s, the output is T^(-degree)
    # times an exterior monomial of length s + 3*degree.
    return [(args, out) for args in product(range(1, 4), repeat=arity)
            for out in range(4)
            if out.bit_count() == sum(a.bit_count() for a in args) + 3 * degree]


def bar_rank(arity, degree):
    source = bar_basis(arity, degree)
    target = bar_basis(arity + 1, degree)
    columns = {entry: j for j, entry in enumerate(source)}
    entries = {}
    for row, (args, out) in enumerate(target):
        def add(key, coefficient):
            if key in columns and coefficient:
                pos = row, columns[key]
                entries[pos] = entries.get(pos, 0) + coefficient

        for middle in range(4):
            sign, value = exterior_product(args[0], middle)
            if value == out:
                sign *= (-1) ** ((degree * args[0].bit_count()) % 2)
                add((args[1:], middle), sign)
            sign, value = exterior_product(middle, args[-1])
            if value == out:
                add((args[:-1], middle), (-1) ** (arity + 1) * sign)
        for i in range(arity):
            sign, value = exterior_product(args[i], args[i + 1])
            if sign:
                merged = args[:i] + (value,) + args[i + 2:]
                add((merged, out), (-1) ** (i + 1) * sign)
    matrix = sp.SparseMatrix(len(target), len(source), entries)
    return matrix.to_DM().rank()


def check_bar_cohomology():
    for arity, expected in ((3, 4), (4, 0), (5, 0)):
        degree = 2 - arity
        dimension = (len(bar_basis(arity, degree)) - bar_rank(arity - 1, degree)
                     - bar_rank(arity, degree))
        assert dimension == expected, (arity, dimension)
        print(f"Two-generator normalized bar HH, arity {arity}: {dimension}")


def check_stabilization():
    x = sp.symbols("x:3")
    u = sp.symbols("u:3")
    period = sp.Symbol("T")
    identity = sp.eye(8)
    wedge = [sp.zeros(8) for _ in x]
    for i in range(3):
        for col in range(8):
            sign, row = exterior_product(1 << i, col)
            wedge[i][row, col] = sign
    contract = [operator.T for operator in wedge]
    for i, j in product(range(3), repeat=2):
        anticommutator = contract[i] * wedge[j] + wedge[j] * contract[i]
        assert anticommutator == (identity if i == j else sp.zeros(8))

    def zero(matrix):
        assert matrix.applyfunc(sp.expand) == sp.zeros(8)

    def direction(poly):
        return sum(v * poly.diff(t) for v, t in zip(u, x))

    # All degree-three monomials and a mixed polynomial check both the
    # polarizations and terms quadratic in the coefficients in d^2 and theta^2.
    basis = [x[i] * x[j] * x[k] for i, j, k in combinations_with_replacement(range(3), 3)]
    for cubic in [*basis, sum((i + 1) * f for i, f in enumerate(basis))]:
        differential, cycle, primitive = (sp.zeros(8) for _ in range(3))
        for i in range(3):
            first = cubic.diff(x[i]) / 3
            second = direction(first) / 2
            third = direction(second)
            differential += x[i] * contract[i] + period * first * wedge[i]
            cycle += u[i] * contract[i] - period * second * wedge[i]
            primitive -= period * third * wedge[i]
        zero(differential**2 - period * cubic * identity)
        zero(differential * cycle + cycle * differential)
        zero(differential * primitive + primitive * differential - cycle**2)
        zero(cycle * primitive + primitive * cycle
             + period * cubic.xreplace(dict(zip(x, u))) * identity)
    print("Koszul stabilization: ten cubic monomials and a mixed cubic, exact matrices")


if __name__ == "__main__":
    check_bar_cohomology()
    check_stabilization()
