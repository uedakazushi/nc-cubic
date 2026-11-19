"""Exact nonzero-minor certificates for generic cubic Poisson schemes.

Use --generate FILE to generate the N=5,...,10 certificates, or --verify FILE
for an independent determinant check of the stored minors. Integer tensor T
means F=(1/6) sum_{i,j,k} T_ijk z_i z_j z_k. Coordinates are zero-based.
Only integer arithmetic modulo the prime 32003 is used; no numerical ranks.
"""
from __future__ import annotations
import argparse
from itertools import combinations, combinations_with_replacement
from math import comb, isqrt
from pathlib import Path
import json
import random
import numpy as np


def plucker_quadrics(n: int) -> int:
    return 5 * comb(n + 1, 6)


def jacobi_rank_bound(n: int) -> int:
    """Plucker bound and the independent universal exterior relations."""
    return min(plucker_quadrics(n), n * comb(n, 4) - comb(n, 3))


def nonstandard_columns(n: int):
    """Coordinates complementary to degree-two standard Plucker monomials."""
    triples = list(combinations(range(n), 3))
    pairs = combinations_with_replacement(range(len(triples)), 2)
    return [i for i, (a, b) in enumerate(pairs)
            if not all(x <= y for x, y in zip(triples[a], triples[b]))]


def jacobi_matrix(n: int, tensor: dict, prime: int) -> np.ndarray:
    triples = list(combinations(range(n), 3))
    triple_index = {t: i for i, t in enumerate(triples)}
    pairs = list(combinations_with_replacement(range(len(triples)), 2))
    pair_index = {t: i for i, t in enumerate(pairs)}

    def component(a, b, i):
        if i == a or i == b:
            return None
        t = (a, b, i)
        sign = (-1) ** sum(t[j] > t[k] for j in range(3) for k in range(j + 1, 3))
        return triple_index[tuple(sorted(t))], sign

    rows = []
    for r in range(n):
        for a, b, c, d in combinations(range(n), 4):
            row = np.zeros(len(pairs), dtype=np.int64)
            for aa, bb, cc, dd in [(a, b, c, d), (b, c, a, d), (c, a, b, d)]:
                for i in range(n):
                    x = component(aa, bb, i)
                    if x is None:
                        continue
                    for j in range(n):
                        y = component(cc, dd, j)
                        if y is None:
                            continue
                        column = pair_index[tuple(sorted((x[0], y[0])))]
                        row[column] += x[1] * y[1] * tensor[tuple(sorted((i, j, r)))]
            rows.append(row % prime)
    return np.array(rows, dtype=np.int64)


def nonzero_minor(matrix: np.ndarray, prime: int):
    a = matrix.copy()
    origin = list(range(len(a)))
    row_ids, column_ids = [], []
    determinant = 1
    rank = 0
    for j in range(a.shape[1]):
        candidates = np.flatnonzero(a[rank:, j])
        if not len(candidates):
            continue
        k = rank + int(candidates[0])
        a[[rank, k]] = a[[k, rank]]
        origin[rank], origin[k] = origin[k], origin[rank]
        row_ids.append(origin[rank])
        column_ids.append(j)
        determinant = determinant * int(a[rank, j]) % prime
        a[rank] = a[rank] * pow(int(a[rank, j]), -1, prime) % prime
        ids = np.flatnonzero(a[rank + 1:, j]) + rank + 1
        for start in range(0, len(ids), 64):
            ii = ids[start:start + 64]
            a[ii] = (a[ii] - a[ii, j, None] * a[rank]) % prime
        rank += 1
        if rank == len(a):
            break
    return row_ids, column_ids, determinant


def determinant_mod(matrix: np.ndarray, prime: int) -> int:
    """Direct determinant check on the stored square minor, without rank search."""
    a = matrix.copy()
    n = len(a)
    assert a.shape == (n, n)
    det = 1
    for j in range(n):
        candidates = np.flatnonzero(a[j:, j])
        if not len(candidates):
            return 0
        k = j + int(candidates[0])
        if k != j:
            a[[j, k]] = a[[k, j]]
            det = -det
        pivot = int(a[j, j])
        det = det * pivot % prime
        factors = a[j + 1:, j] * pow(pivot, -1, prime) % prime
        for start in range(0, len(factors), 64):
            stop = min(start + 64, len(factors))
            a[j + 1 + start:j + 1 + stop, j:] = (
                a[j + 1 + start:j + 1 + stop, j:]
                - factors[start:stop, None] * a[j, j:]
            ) % prime
    return int(det % prime)


def generate(n: int, seed: int = 901, prime: int = 32003):
    rng = random.Random(seed)
    tensor = {t: rng.randrange(prime) for t in combinations_with_replacement(range(n), 3)}
    a = jacobi_matrix(n, tensor, prime)
    # Restricting to nonstandard columns speeds up N=10. The resulting minor
    # still has its original column indices in the full integer matrix.
    selected = nonstandard_columns(n) if n >= 10 else list(range(a.shape[1]))
    rows, reduced_columns, determinant = nonzero_minor(a[:, selected], prime)
    columns = [selected[i] for i in reduced_columns]
    target = jacobi_rank_bound(n)
    assert len(rows) == target
    assert determinant != 0
    return {
        "N": n, "n": n - 2, "prime": prime, "generation_seed": seed,
        "hessian_tensor": [list(t) + [value] for t, value in tensor.items()],
        "matrix_rows": n * comb(n, 4), "matrix_columns": comb(comb(n, 3) + 1, 2),
        "plucker_quadrics": plucker_quadrics(n), "rank_upper_bound": target,
        "minor_rows_in_order": rows, "minor_columns": columns,
        "minor_determinant_mod_prime": determinant,
    }


def verify(case):
    n, prime = case["N"], case["prime"]
    assert all(prime % d for d in range(2, isqrt(prime) + 1))
    tensor = {tuple(t[:3]): t[3] for t in case["hessian_tensor"]}
    assert set(tensor) == set(combinations_with_replacement(range(n), 3))
    a = jacobi_matrix(n, tensor, prime)
    assert a.shape == (case["matrix_rows"], case["matrix_columns"])
    rows, columns = case["minor_rows_in_order"], case["minor_columns"]
    target = jacobi_rank_bound(n)
    assert case["plucker_quadrics"] == plucker_quadrics(n)
    assert case["rank_upper_bound"] == target
    assert len(rows) == len(set(rows)) == target
    assert len(columns) == len(set(columns)) == target
    value = determinant_mod(a[np.ix_(rows, columns)], prime)
    assert value == case["minor_determinant_mod_prime"] != 0
    return {"N": n, "minor_order": len(rows), "prime": prime, "determinant": value}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--generate", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    if args.generate:
        cases = []
        for n in range(5, 11):
            case = generate(n)
            cases.append(case)
            print(json.dumps({"N": n, "minor_order": case["rank_upper_bound"], "determinant": case["minor_determinant_mod_prime"]}), flush=True)
        payload = {"schema": 2, "date": "2026-11-20", "version": "v2", "interpretation": "Nonzero integer minors modulo 32003 attain the minimum of the Plucker bound and N*binom(N,4)-binom(N,3). Nonzero integer minors modulo a prime are nonzero in characteristic zero; no modular vanishing proves an identity.", "cases": cases}
        args.generate.parent.mkdir(parents=True, exist_ok=True)
        args.generate.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
    else:
        payload = json.loads(args.verify.read_text())
        for case in payload["cases"]:
            print(json.dumps(verify(case)), flush=True)


if __name__ == "__main__":
    main()
