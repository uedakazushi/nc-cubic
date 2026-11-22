#!/usr/bin/env python3
"""Exact finite BG certificates for two fixed Sklyanin factors.

2026-11-22 / v61.

Default: S(1,-1,-1) tensor S(1,-1,-1).
With --clifford: S(1,1,2) tensor S(1,1,2).

For V = span(x,y,z,X,Y,Z), take the six cyclic Sklyanin relations
  a*y*z + b*z*y + c*x*x
and their cyclic permutations, and the nine cross commutators.
Allow every correction
  r - u*ell(r) - u**2*beta(r),
where u is fixed central, ell:R->V has 90 coefficients, and beta:R->QQ
has 15 coefficients. No cross or foreign-output coefficient is set to
zero when constructing the linear conditions.

The script reconstructs W=(R tensor V) intersect (V tensor R) in V**3
from the original relations. It verifies:
  * ker of the first BG condition is Sym_3 direct sum Sym_3;
  * the infinitesimal coordinate translations have rank six;
  * the constant cocycles are exactly the six pure-factor constants;
  * all remaining BG identities vanish universally on these spaces.

Every matrix is computed over QQ. The final two checks are coefficient
identities in all 12 linear and 6 constant parameters, not interpolation.
The all-degree PBW conclusion additionally uses the known Koszul property
of the fixed tensor-product algebra and the Braverman--Gaitsgory theorem.
This script does not prove the general-factor theorem, construct a central
cubic lift (especially in the Clifford case), or prove a Ku comparison.

Requires Python 3 and SymPy. From the repository root:
  python3 computations/verify_interfactor_pbw.py
  python3 computations/verify_interfactor_pbw.py --clifford
"""

import argparse

import sympy as sp


N = 6
NR = 15
CYCLIC = ((0, 1, 2), (1, 2, 0), (2, 0, 1))


def relation_list(parameters):
    """Word dictionaries, pure factor relations first, then cross ones."""
    a, b, c = map(sp.Rational, parameters)
    relations = []
    for offset in (0, 3):
        for i, j, k in CYCLIC:
            relations.append({
                (offset + j, offset + k): a,
                (offset + k, offset + j): b,
                (offset + i, offset + i): c,
            })
    for i in range(3):
        for j in range(3, N):
            relations.append({(i, j): sp.Integer(1),
                              (j, i): sp.Integer(-1)})
    return relations


def relation_and_overlap_maps(relations):
    """Columns of R, R tensor V, and V tensor R in the word bases."""
    relation = sp.zeros(N * N, NR)
    left = sp.zeros(N**3, NR * N)
    right = sp.zeros(N**3, N * NR)
    for r, polynomial in enumerate(relations):
        for (i, j), coefficient in polynomial.items():
            relation[i * N + j, r] = coefficient
            for k in range(N):
                left[(i * N + j) * N + k, r * N + k] = coefficient
                right[(k * N + i) * N + j, k * NR + r] = coefficient
    return relation, left, right


def correction_maps(overlap):
    """Coefficient matrices of D_ell and D_beta on one overlap.

Write overlap=(a,b), where sum a[r,i] r tensor v_i equals
sum b[i,r] v_i tensor r. Then
  D_ell = (ell tensor 1 - 1 tensor ell)(overlap) in V tensor V,
  D_beta = (beta tensor 1 - 1 tensor beta)(overlap) in V.
The ell coefficient order is (relation r, output generator j).
"""
    a, b = overlap[:NR * N], overlap[NR * N:]
    linear = sp.zeros(N * N, NR * N)
    constant = sp.zeros(N, NR)
    for r in range(NR):
        for i in range(N):
            ca, cb = a[r * N + i], b[i * NR + r]
            if ca:
                constant[i, r] += ca
                for j in range(N):
                    linear[j * N + i, r * N + j] += ca
            if cb:
                constant[i, r] -= cb
                for j in range(N):
                    linear[i * N + j, r * N + j] -= cb
    return linear, constant


def pure_linear_basis():
    """Twelve columns: the full symmetric matrix in each factor."""
    basis = sp.zeros(NR * N, 12)
    column = 0
    for offset in (0, 3):
        for i in range(3):
            for j in range(i, 3):
                basis[(offset + i) * N + offset + j, column] = 1
                basis[(offset + j) * N + offset + i, column] = 1
                column += 1
    return basis


def translation_matrix(relations):
    """The coefficient of u in r(v+u*t), before quotienting by gauge."""
    gauge = sp.zeros(NR * N, N)
    for r, polynomial in enumerate(relations):
        for (i, j), coefficient in polynomial.items():
            gauge[r * N + j, i] += coefficient
            gauge[r * N + i, j] += coefficient
    return gauge


def expected_translation(parameters):
    """Cyclic formula: diagonal 2*c*t_i, off-diagonal (a+b)*t_k."""
    a, b, c = map(sp.Rational, parameters)
    result = sp.zeros(NR * N, N)
    for offset in (0, 3):
        for i, j, k in CYCLIC:
            result[(offset + i) * N + offset + i, offset + i] = 2 * c
            result[(offset + i) * N + offset + j, offset + k] = a + b
            result[(offset + i) * N + offset + k, offset + j] = a + b
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--clifford", action="store_true",
                        help="use S(1,1,2) for both factors")
    args = parser.parse_args()
    parameters = (1, 1, 2) if args.clifford else (1, -1, -1)
    print(f"Fixed factors: S{parameters} tensor S{parameters}")

    relations = relation_list(parameters)
    relation, left, right = relation_and_overlap_maps(relations)
    assert relation.shape == (36, 15) and relation.rank() == 15
    assert left.rank() == right.rank() == 90
    comparison = left.row_join(-right)
    overlaps = comparison.nullspace()
    assert len(overlaps) == 20
    overlap_columns = sp.Matrix.hstack(*overlaps)
    assert comparison * overlap_columns == sp.zeros(216, 20)
    assert overlap_columns.rank() == 20
    assert (left * overlap_columns[:90, :]).rank() == 20
    assert 216 - (180 - len(overlaps)) == 56
    print("PASS: R rank 15; overlap comparison 216x180 rank 160;"
          " W dimension 20; degree-three quotient dimension 56")

    # An exact annihilator realizes the quotient (V tensor V)/R.
    annihilator = sp.Matrix.hstack(*relation.T.nullspace()).T
    assert annihilator.shape == (21, 36) and annihilator.rank() == 21
    assert annihilator * relation == sp.zeros(21, 15)
    maps = [correction_maps(w) for w in overlaps]
    linear_maps = [pair[0] for pair in maps]
    first = sp.Matrix.vstack(*(annihilator * d for d in linear_maps))
    assert first.shape == (420, 90)
    first_rank = first.rank()
    pure = pure_linear_basis()
    assert first_rank == 78 and pure.rank() == 12
    assert first * pure == sp.zeros(420, 12)
    # Rank plus containment proves equality of the entire kernel.
    assert first.cols - first_rank == pure.cols
    forbidden = [
        r * N + j for r in range(NR) for j in range(N)
        if r >= 6 or (r < 3) != (j < 3)
    ]
    assert len(forbidden) == 72
    assert pure.extract(forbidden, range(12)) == sp.zeros(72, 12)
    print("PASS: first BG matrix 420x90 rank 78; kernel dimension 12"
          " = Sym3+Sym3; all 72 mixed/foreign-output coefficients zero")

    gauge = translation_matrix(relations)
    assert gauge == expected_translation(parameters)
    assert gauge.rank() == 6
    assert first * gauge == sp.zeros(420, 6)
    assert pure.row_join(gauge).rank() == 12
    if not args.clifford:
        expected = sp.zeros(90, 6)
        for i in range(N):
            expected[i * N + i, i] = -2
        assert gauge == expected
    print("PASS: translation gauge 90x6 rank 6;"
          " first-order quotient dimension 12-6=6")

    constants = sp.Matrix.vstack(*(pair[1] for pair in maps))
    pure_constants = sp.zeros(NR, 6)
    for i in range(6):
        pure_constants[i, i] = 1
    assert constants.shape == (120, 15)
    assert constants.rank() == 9
    assert pure_constants.rank() == 6
    assert constants * pure_constants == sp.zeros(120, 6)
    print("PASS: constant BG matrix 120x15 rank 9;"
          " kernel dimension 6 = pure-factor constants; cross constants zero")

    # Compute D_ell(W) in the ORIGINAL relation basis, over all twelve
    # parameters simultaneously. Only the nine cross relations occur.
    pivot_rows = relation.T.rref()[1]
    assert len(pivot_rows) == NR
    inverse = relation.extract(pivot_rows, range(NR)).inv()
    relation_coordinates = []
    for d in linear_maps:
        image = d * pure
        coordinates = inverse * image.extract(pivot_rows, range(12))
        assert relation * coordinates == image
        assert coordinates[:6, :] == sp.zeros(6, 12)
        relation_coordinates.append(coordinates)
    print("PASS: universal D_ell(W) lies in the cross-relation span;"
          " no pure-relation component")

    # Each column is one ell basis vector. The following products check
    # all ordered pairs of linear parameters and all beta/ell pairs.
    ell_maps = [
        sp.Matrix(NR, N, list(pure[:, column])).T
        for column in range(pure.cols)
    ]
    for coordinates in relation_coordinates:
        for ell in ell_maps:
            assert ell * coordinates == sp.zeros(N, 12)
        assert pure_constants.T * coordinates == sp.zeros(6, 12)
    # D_beta=0 was checked above. Thus ell(D_ell)=-D_beta and
    # beta(D_ell)=0 hold as polynomial identities in all 18 parameters.
    print("PASS: remaining BG identities hold universally in all"
          " 12 linear and 6 constant parameters")
    print("Finite exact certificate complete;"
          " all-degree PBW uses the separate Koszul/BG theorem.")


if __name__ == "__main__":
    main()
