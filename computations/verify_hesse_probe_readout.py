#!/usr/bin/env python3
"""Exact 12-coefficient readout from four Clifford Hesse one-way probes.

Input: F+sG1+s²G2+s³G3 with G1=κΣ A_ab X_a Y_{b+1}Y_{b+2}.
G2,G3 are arbitrary cubic forms. This verifies polynomial coordinate
normalization, NOT an actual comparison kernel or its higher coefficients.
Depends on SymPy and verify_hesse_slice_transfer.py in the same directory.
"""
import sympy as S
import verify_hesse_slice_transfer as src

z = src.z
x0, x1, x2, y0, y1, y2 = z
xs, ys = z[:3], z[3:]
h1, h2 = src.h
t1, _ = src.t
kappa = S.symbols("kappa")
probes = {
    "E00": {(0, 0): 1},
    "R0": {(0, 0): 1, (0, 1): 1, (0, 2): 1},
    "C0": {(0, 0): 1, (1, 0): 1, (2, 0): 1},
    "I3": {(0, 0): 1, (1, 1): 1, (2, 2): 1},
}
PX, PY = x0 * x1 * x2, y0 * y1 * y2

def first_jet(A):
    return kappa * sum(
        value * xs[a] * ys[(b + 1) % 3] * ys[(b + 2) % 3]
        for (a, b), value in A.items()
    )

def observables(A, G2, G3):
    P2, P3 = S.Poly(G2, *z), S.Poly(G3, *z)
    B = P2.coeff_monomial(x1*x2*y0) + h1*P2.coeff_monomial(x0**2*y0)
    U = P3.coeff_monomial(PX) + h1*sum(P3.coeff_monomial(x**3) for x in xs)
    V = P3.coeff_monomial(PY) + h2*sum(P3.coeff_monomial(y**3) for y in ys)
    V -= kappa/t1*sum(
        value*P2.coeff_monomial(xs[a]**2*ys[b])
        for (a,b),value in A.items()
    )
    return [S.expand(q) for q in (B,U,V)]

def projected(A, G2, G3):
    G1 = first_jet(A)
    P2, J2 = src.project_and_J(G2)
    V = J2 * S.Matrix(z)
    D = sum(V[i]*S.diff(G1, z[i]) for i in range(6))
    H3 = src.project_and_J(S.expand(G3-D))[0]
    Q2,Q3 = S.Poly(P2,*z),S.Poly(H3,*z)
    return [Q2.coeff_monomial(x1*x2*y0),
            Q3.coeff_monomial(PX),Q3.coeff_monomial(PY)]

for label,A in probes.items():
    for m in src.basis:
        for G2,G3 in [(m,0),(0,m)]:
            a,b = observables(A,G2,G3),projected(A,G2,G3)
            assert all(S.cancel(u-v)==0 for u,v in zip(a,b)),(label,m,a,b)
print("PASS 1: all 56 G2 and 56 G3 monomials on each of four probes")

M = S.Matrix([[1,0,0,0],[1,0,1,0],[1,1,0,0],[1,0,0,1]])
N = S.Matrix([[1,0,0,0],[3,1,0,0],[3,0,1,0],[3,0,0,1]])
assert M.det() == -1 and N.det() == 1
b = S.symbols("b0 bR bC bI")
x = S.symbols("x0 xR xC xI")
y = S.symbols("y0 yR yC yI")
assert M.inv()*S.Matrix(b)==S.Matrix([b[0],b[2]-b[0],b[1]-b[0],b[3]-b[0]])
for values in [x,y]:
    assert N.inv()*S.Matrix(values)==S.Matrix(
        [values[0],values[1]-3*values[0],values[2]-3*values[0],values[3]-3*values[0]])
print("PASS 2: inverse matrices reconstruct all 4+8 scalar coefficients")

g = S.symbols("g00 g01 g02 g10 g11 g12 g20 g21 g22")
for label,A in probes.items():
    result = sum(value*g[3*a+b] for (a,b),value in A.items())
    expected = {"E00":g[0],"R0":sum(g[:3]),"C0":g[0]+g[3]+g[6],
                "I3":g[0]+g[4]+g[8]}[label]
    assert S.expand(result-expected)==0
assert 4 + sum(len(A) for A in probes.values()) == 14
assert 4*8 == 32
print("PASS 3: exact quadratic correction and 14+32=46 raw coefficient slots")

toy = observables(probes["E00"], x0**2*y0, 0)
assert toy == [h1,S.Integer(0),-kappa/t1]
assert projected(probes["E00"],x0**2*y0,0) == toy
print("PASS 4: pure-X third jet gauge-free, pure-Y receives a nonzero term")
print("4 PASS; no comparison kernel or numerical beta/gamma values verified.")
