"""Exact fifth inverse-tensor coefficient in the fixed harmonic Kontsevich model.

2026-11-20. Python + SymPy. The 73 numerical graph records are extracted from
Buring's public research data; provenance, hashes and conventions are in JSON.
This evaluates finite rational contractions, not the graph integrals themselves.
Optional --source-directory audits the extraction against downloaded originals.
"""
from ast import literal_eval
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path
import argparse
import hashlib
import json
import sympy as s
from verify_cubic_covariants import contraction, SE, IE, JE

X = s.symbols('x y z')
PAIRS = tuple((i, j) for i in range(3) for j in range(3) if i != j)
DATA = json.loads((Path(__file__).parent / 'data/harmonic_linear_products.json').read_text())
GRAPHS = {n: [] for n in range(1, 6)}
for row in DATA['graphs']:
    n, targets = row['order'], tuple(row['targets'])
    ind = Counter(targets)
    assert len(targets) == 2*n and ind[0] == ind[1] == 1
    assert all(ind[v] <= 2 for v in range(2, n+2))
    assert Q(row['coefficient']) == Q(row['weight']) / row['automorphisms']
    GRAPHS[n].append((targets, Q(row['coefficient'])))
assert [len(GRAPHS[n]) for n in range(1, 6)] == [1, 1, 1, 19, 51]


def tensor_jets(F, point=(0, 0, 0), components=None):
    """All nonzero jets of order <=2 of Pi_F at the given active point."""
    subs, data = dict(zip(X, point)), {}
    for a, b in PAIRS:
        c = 3-a-b
        sign = 1 if (a,b,c) in [(0,1,2),(1,2,0),(2,0,1)] else -1
        p = sign*s.diff(F, X[c]) if components is None else components.get((a,b), s.Integer(0))
        for n in range(3):
            for ds in product(range(3), repeat=n):
                val = (s.diff(p, *[X[d] for d in ds]) if ds else p).subs(subs)
                if val:
                    data[a, b, tuple(sorted(ds))] = Q(val)
    return data


def graph_value(targets, jets, i, j):
    """Einstein contraction; each sink fixes one edge index to i or j."""
    n = len(jets)
    incoming = [[] for _ in range(n+2)]
    for e, target in enumerate(targets):
        incoming[target].append(e)
    fixed = {incoming[0][0]: i, incoming[1][0]: j}
    free = [e for e in range(2*n) if e not in fixed]
    indices = [0]*(2*n)
    for e, index in fixed.items():
        indices[e] = index
    total = Q(0)
    for values in product(range(3), repeat=len(free)):
        for e, index in zip(free, values):
            indices[e] = index
        value = Q(1)
        for v in range(n):
            key = (indices[2*v], indices[2*v+1],
                   tuple(sorted(indices[e] for e in incoming[v+2])))
            factor = jets[v].get(key, 0)
            if not factor:
                break
            value *= factor
        else:
            total += value
    return total


def B(n, P, i, j, replacement=None):
    """B_n(P^n), or its polarization with one slot replaced by replacement."""
    total = Q(0)
    choices = [None] if replacement is None else range(n)
    for targets, coefficient in GRAPHS[n]:
        for slot in choices:
            jets = [P]*n
            if slot is not None:
                jets[slot] = replacement
            total += coefficient*graph_value(targets, jets, i, j)
    return total


def inverse_at(F, point):
    P = tensor_jets(F, point)
    R = tensor_jets(s.det(s.hessian(F, X))/24, point)
    B2 = {(i,j): B(2,P,i,j) for i,j in product(range(3), repeat=2)}
    B4 = {(i,j): B(4,P,i,j)+B(2,P,i,j,replacement=R)
          for i,j in product(range(3), repeat=2)}
    answers, details = {}, {}
    for i,j in [(0,1),(1,2),(2,0)]:
        low = -2*B(3,P,i,j) + sum(P.get((i,j,tuple(sorted((a,b)))),0)*B2[a,b]/2
                                 for a,b in product(range(3),repeat=2))
        assert low == R.get((i,j,()),0), ('third coefficient', i,j,low)
        pure = B(5,P,i,j)
        polarized = B(3,P,i,j,replacement=R)
        weyl = sum(P.get((i,j,tuple(sorted((a,b)))),0)*B4[a,b]/2
                   for a,b in product(range(3),repeat=2))
        answers[i,j] = -2*(pure+polarized)+weyl
        details[i,j] = (pure, polarized, weyl)
    return answers, details


def normalized_graph(targets, n):
    """Canonical aerial relabeling, outgoing-order sign and stabilizer size."""
    forms = []
    for p in permutations(range(2,n+2)):
        relabel = {0:0,1:1,**{v+2:p[v] for v in range(n)}}
        outgoing = [[] for _ in range(n)]
        for edge, target in enumerate(targets):
            outgoing[relabel[2+edge//2]-2].append(relabel[target])
        sign = 1
        for pair in outgoing:
            if pair[0] > pair[1]:
                pair.reverse()
                sign = -sign
        forms.append((tuple(t for pair in outgoing for t in pair), sign))
    key = min(key for key, sign in forms)
    signs = [sign for candidate,sign in forms if candidate == key]
    assert len(set(signs)) == 1
    return key, signs[0], len(signs)


def audit_source(directory):
    for name, digest in DATA['input_sha256'].items():
        assert hashlib.sha256((directory/name).read_bytes()).hexdigest() == digest, name
    extracted = {n:{} for n in range(1,6)}
    for line in (directory/'star5.txt').read_text().splitlines():
        fields = line.split()
        if not fields or fields[0] != '2' or fields[1] == '0':
            continue
        n = int(fields[1]); targets = tuple(map(int,fields[3:-1])); ind = Counter(targets)
        if ind[0] != 1 or ind[1] != 1 or any(ind[v]>2 for v in range(2,n+2)):
            continue
        key, sign, aut = normalized_graph(targets,n)
        extracted[n][key] = extracted[n].get(key,Q(0))+sign*Q(fields[2])*Q(fields[-1])/2**n
    for n in range(1,6):
        raw = {}
        gs = (directory/f'kontsevich_2_{n}.txt').read_text().splitlines()
        ws = (directory/f'weights_kontsevich_2_{n}.txt').read_text().splitlines()
        assert len(gs) == len(ws)
        for graph,weight in zip(gs,ws):
            weight = Q(weight)
            if not weight:
                continue
            edges = literal_eval(graph); ind = Counter(target for vertex,target in edges)
            if ind[0] != 1 or ind[1] != 1 or any(ind[v]>2 for v in range(2,n+2)):
                continue
            assert [vertex for vertex,target in edges] == [2+edge//2 for edge in range(2*n)]
            key,sign,aut = normalized_graph(tuple(target for vertex,target in edges),n)
            raw[key] = raw.get(key,Q(0))+sign*weight/aut
        assert raw == extracted[n] == dict(GRAPHS[n])
    print('PASS: source hashes and all 73 coefficients match both star5/2^n and raw weights/Aut.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-directory', type=Path)
    args = parser.parse_args()
    if args.source_directory:
        audit_source(args.source_directory)
    x,y,z = X
    # Independent published calibration: Banks--Panzer--Pym, arXiv v1, p.3.
    planar = tensor_jets(0,(1,1,1),{(0,1):x*y,(1,0):-x*y})
    assert [B(n,planar,0,1) for n in range(1,6)] == [Q(1,2),Q(1,24),Q(-1,48),Q(-1,1440),Q(1,480)]
    print('PASS: all five two-dimensional log-canonical coefficients match the published expansion.')
    results = []
    for name,F,point in [('log',x*y*z,(1,1,1)),
                         ('quadratic mixed',x*y*z+z*z/2,(0,0,1)),
                         ('linear mixed',x*y*z+z,(0,0,1))]:
        value,details = inverse_at(F,point)
        results.append(value[0,1])
        print(name, 'pi5 =', value, '(B5, polarized B3, Weyl) =', details[0,1])
    assert results == [Q(1,80),Q(-1,90),Q(-1,144)]
    a = 3*(Q(1,80)-results[1])  # 4 beta + gamma
    b = Q(1,80)-results[2]     # beta + 2 gamma/3
    beta = (2*a-3*b)/5
    gamma = a-4*beta
    alpha = Q(1,80)-beta-gamma
    assert (alpha,beta,gamma) == (Q(-1,120),Q(1,60),Q(1,240))
    print('PASS: alpha = -1/120; beta = 1/60; gamma = 1/240.')
    # The non-log-canonical mixed jet used to prove independence of the three covariants.
    F = (x**3+y**3+z**3)/3+x*y*z+x*x/2+x*y+x
    value,_ = inverse_at(F,(0,0,0))
    T = {ds:Q(s.diff(F,*[X[i] for i in ds])) for ds in product(range(3),repeat=3)}
    zero = dict(zip(X,[0,0,0]))
    M = {ds:Q(s.diff(F,*[X[i] for i in ds]).subs(zero)) for ds in product(range(3),repeat=2)}
    q = {(i,):Q(s.diff(F,X[i]).subs(zero)) for i in range(3)}
    S = contraction([T]*4,SE)
    expected = []
    for k in range(3):
        Tk = {(i,j):T[i,j,k] for i,j in product(range(3),repeat=2)}
        Mk = {(i,):M[i,k] for i in range(3)}
        dI = sum(contraction([T,T]+[Tk if v==slot else M for v in range(3)],IE) for slot in range(3))
        dJ = contraction([T,T,T,Tk,q],JE)+contraction([T,T,T,M,Mk],JE)
        expected.append(alpha*S*q[k,]+beta*dI+gamma*dJ)
    assert expected == [Q(1,30),Q(-11,720),Q(1,36)]
    assert [value[pair] for pair in [(1,2),(2,0),(0,1)]] == expected
    print('PASS: independent mixed jet agrees with the uniform three-covariant formula.')
    print('NOT CHECKED: graph integration, arbitrary-order tensor, MF equivalence, formal proof assistant.')


if __name__ == '__main__':
    main()
