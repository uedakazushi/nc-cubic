#!/usr/bin/env python3
"""Compute the one-way J: P3 -> P4 at tau1=tau2=2, a1=a2=1 over Q[Lambda].

Run directly in the computations directory or by path. --certificate FILE writes
the ordered pivot indices, determinants and rational PBW coefficients of J.
The preceding universal verifier supplies G and its documented basis conventions.
"""
import argparse
import json
import runpy
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement, product
from pathlib import Path

import sympy as sp


def triple_trace(word):
    """Coefficient of u1*u2*u3 in a separated dual cubic monomial."""
    distinct = len(set(word))
    return {1: 2, 2: 0, 3: 1}[distinct]


def fifth_moments():
    """Solve all 30 degree-five dual relations for three independent forces."""
    labels = list(combinations_with_replacement(range(3), 5))
    triples = list(combinations_with_replacement(range(3), 3))
    matrix = sp.zeros(30, 21)
    rhs = sp.zeros(30, 3)
    for row, (i, triple) in enumerate(product(range(3), triples)):
        pair = tuple(j for j in range(3) if j != i)
        matrix[row, labels.index(tuple(sorted((i, i) + triple)))] += 1
        matrix[row, labels.index(tuple(sorted(pair + triple)))] -= 2
        rhs[row, i] = -triple_trace(triple)
    pivots = list(matrix.T.rref()[1])
    assert len(pivots) == 21
    values = matrix[pivots, :].inv() * rhs[pivots, :]
    assert matrix * values == rhs
    return dict(zip(labels, values.tolist()))


def d4_coefficients():
    moments = fifth_moments()
    x = list(range(3))
    y = list(range(3, 6))
    qx = [tuple(j for j in x if j != i) for i in x]
    qy = [tuple(j for j in y if j != i) for i in y]
    e2 = qx + qy + list(product(x, y))
    e3 = [tuple(x), tuple(y)] + [q + (j,) for q in qx for j in y]
    e3 += [q + (i,) for q in qy for i in x]
    # The y*y*x basis elements carry two crossings, hence positive sign.
    entries = []
    for row, left in enumerate(e3):
        for j, (col, right) in product(range(6), enumerate(e2)):
            word = left + (j,) + right
            swaps = sum(a >= 3 and b < 3 for k, a in enumerate(word) for b in word[k + 1:])
            factor = Fraction((-1) ** swaps, 49)
            u = tuple(k for k in word if k < 3)
            v = tuple(sorted(k - 3 for k in word if k >= 3))
            if len(u) == 3:
                value = factor * triple_trace(u) * triple_trace(v)
                if value:
                    entries.append(((), row, col, j, value))
            if len(u) == 1:
                for a, b in product(x, repeat=2):
                    value = factor * triple_trace(u + qx[a]) * moments[v][b]
                    if value:
                        entries.append(((3*a+b,), row, col, j, Fraction(value)))
    return entries, [3 - sum(i < 3 for i in q) for q in e2]


def poly_key(*parts):
    return tuple(sorted(i for part in parts for i in part))


def linear_parts(get, origin, directions):
    """Extract coefficients of an affine-linear PBW expression in nine directions."""
    base = get(origin)
    assert all(degree == 0 for degree, *_ in base)
    ans = [((), (center, word), value) for (_, center, word), value in base.items()]
    for a, c in enumerate(directions):
        expr = get(c)
        assert all(0 <= degree <= 1 for degree, *_ in expr)
        assert {k: v for k, v in expr.items() if k[0] == 0} == base
        ans.extend(((a,), tuple(k[1:]), v) for k, v in expr.items() if k[0] == 1)
    return ans


def run(data, certificate):
    B2, B3 = data['B2'], data['B3I']
    origin, dirs = data['cl0'], data['cldirs']
    left_mul = {}
    right_mul = {}
    for j, bb in product(range(6), range(21)):
        for table, left in [(left_mul, True), (right_mul, False)]:
            def mult(c):
                return c.mul(c.z[j], B2[bb]) if left else c.mul(B2[bb], c.z[j])
            table[j, bb] = [(m, B3[k], v) for m, k, v in linear_parts(mult, origin, dirs)]

    # D4 on all B2 columns, including any mixed coefficients from PBW multiplication.
    d4, k4deg = d4_coefficients()
    action = defaultdict(lambda: defaultdict(lambda: defaultdict(Fraction)))
    for m, row, col, j, coeff in d4:
        for bb in range(21):
            for t, out, v in left_mul[j, bb]:
                action[poly_key(m,t)][col*21+bb][row*56+out] += coeff*v
    action = {m: {col: {r:v for r,v in xs.items() if v} for col,xs in cols.items()}
              for m,cols in action.items()}
    k3deg = data['K3p']
    xdeg = data['xdeg']
    rowdeg = [p+xdeg(b) for p in k3deg for b in data['B3keys']]
    coldeg = [p+xdeg(b) for p in k4deg for b in data['B2keys']]
    assert all(coldeg[c] == rowdeg[r] + 2*len(m)
               for m, cols in action.items() for c, xs in cols.items() for r in xs)

    blocks = []
    for q in range(7):
        rows = [r for r,p in enumerate(rowdeg) if p == q]
        cols = [c for c,p in enumerate(coldeg) if p == q]
        if not cols:
            continue
        loc = {r:i for i,r in enumerate(rows)}
        mat = sp.SparseMatrix(len(rows),len(cols),
                {(loc[r],j): v for j,c in enumerate(cols) for r,v in action[()][c].items()})
        pc = list(mat.rref()[1])
        pr = list(mat[:,pc].T.rref()[1])
        minor = mat[pr,pc]
        inv = minor.inv().todok()
        det = minor.det(method='domain-ge')
        assert det != 0
        blocks.append(([rows[i] for i in pr], [cols[i] for i in pc],
                       {k:Fraction(v) for k,v in inv.items()}, str(det)))
    ranks = [len(rows) for rows, *_ in blocks]
    assert ranks == [18,72,100,72,18]
    print('Exact D4 origin pivot ranks:', ranks, flush=True)

    # Store a column of w*I - G*d3 in the 1120-row PBW basis.
    def empty_columns():
        return [defaultdict(Fraction) for _ in range(20)]
    rhs = defaultdict(empty_columns)
    for m,key,v in linear_parts(lambda c:c.get_u_w()[1], origin, dirs):
        for i in range(20):
            rhs[m][i][56*i+B3[key]] += v
    syz = data['syzygies']
    origin_syzygies = syz(data['ZERO'],origin)
    dir_syzygies = [syz(data['cU'](a),c) for a,c in enumerate(dirs)]
    d3 = defaultdict(list)
    for i, h in enumerate([origin_syzygies] + dir_syzygies):
        for col, entries in enumerate(h):
            for label, poly in entries.items():
                for (degree,cent,word),v in poly.items():
                    assert degree <= 1 and not cent and len(word)==1
                    if i==0 or degree==1:
                        m = () if i==0 else (i-1,)
                        d3[data['rindex'][label]].append((m,col,word[0],v))
    g_coeffs = {():data['G0'], **{(a,):val for a,val in data['G1'].items()}, **data['G2']}
    for m, gcols in g_coeffs.items():
        for mid,gcol in enumerate(gcols):
            for idx,v in gcol.items():
                row,bb = divmod(idx,21)
                for t,col,j,z in d3[mid]:
                    for n,out,w in right_mul[j,bb]:
                        rhs[poly_key(m,t,n)][col][56*row+out] -= v*z*w

    # Solve with one fixed right inverse at the origin and coefficient recursion.
    # Checking the residual on every row also tests all equations outside the minor.
    solutions = {}
    for degree in range(5):
        for m in combinations_with_replacement(range(9),degree):
            res = rhs.pop(m,empty_columns())
            for n,operator in action.items():
                if not n:
                    continue
                diff = list(m)
                for a in n:
                    if a not in diff:
                        break
                    diff.remove(a)
                else:
                    for col,vec in enumerate(solutions.get(tuple(diff), [])):
                        for c,value in vec.items():
                            for row,v in operator.get(c,{}).items():
                                res[col][row] -= v*value
            if degree <= 2:
                coeffs = empty_columns()
                for rows,cols,inv,_ in blocks:
                    for (j,i),v in inv.items():
                        for col,vec in enumerate(res):
                            value = vec.get(rows[i],0)
                            if value:
                                coeffs[col][cols[j]] += v*value
                coeffs = [{c:v for c,v in xs.items() if v} for xs in coeffs]
                solutions[m] = coeffs
                for col,vec in enumerate(coeffs):
                    for c,value in vec.items():
                        for row,v in action[()][c].items():
                            res[col][row] -= v*value
            assert not any(any(vec.values()) for vec in res), ('identity',m)
    assert all(not any(any(vec.values()) for vec in vals) for vals in rhs.values())
    counts = [sum(len(vec) for m,cs in solutions.items() if len(m)==i for vec in cs)
              for i in range(3)]
    print('All 20 columns checked over Q[Lambda]; nonzero J coefficients:', counts)
    if certificate:
        out = {'indexing':'zero-based: row=56*K3+B3, column=21*K4+B2',
               'blocks':[{'rows':r,'columns':c,'determinant':d} for r,c,_,d in blocks],
               'J':[[list(m),j,c,str(v)] for m,cols in solutions.items()
                    for j,vec in enumerate(cols) for c,v in sorted(vec.items())]}
        certificate.write_text(json.dumps(out, separators=(',',':'))+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path)
    args = parser.parse_args()
    previous = Path(__file__).with_name('verify_clifford_mixed_shamash_second_middle.py')
    run(runpy.run_path(str(previous)), args.certificate)
