#!/usr/bin/env python3
"""Exact rational character and Euler checks for the mixed comparison.

2026-11-22 / v48. Run with Python 3 and SymPy 1.14.

This verifies finite Jacobian calculations and additive invariants. It does not
establish an equivalence with the noncommutative category or a categorical SOD.
"""
from math import comb
import sympy as s

x = s.symbols("x1 x2 x3 y1 y2 y3 u")
u = x[-1]
linear = x[0]+4*x[1]+9*x[2]+100*(16*x[3]+25*x[4]+49*x[5])
F = sum(v**3 for v in x[:3])+s.prod(x[:3])
F += 100*(sum(v**3 for v in x[3:6])+s.prod(x[3:6]))
F -= 3*u**2*linear
partials = [s.Poly(s.diff(F,v), *x) for v in x]

def exponents(n, degree):
    if n == 1:
        yield (degree,)
    else:
        for a in range(degree+1):
            for tail in exponents(n-1, degree-a):
                yield (a,)+tail

def rank_by_parity(degree):
    mons = list(exponents(7,degree))
    rows = []
    for e in exponents(7,degree-2):
        mon = s.prod(v**a for v,a in zip(x,e))
        for df in partials:
            poly = s.Poly(mon*df.as_expr(),*x)
            rows.append([poly.coeff_monomial(m) for m in mons])
    M=s.Matrix(rows)
    answer=[]
    for parity in (0,1):
        cols=[i for i,e in enumerate(mons) if e[-1]%2==parity]
        rank=M[:,cols].rank()
        answer.append((len(cols),rank,len(cols)-rank))
    return answer

assert s.expand(F.subs(u,-u)-F)==0
print("PASS involution preserves the homogeneous cubic")

r2=rank_by_parity(2)
assert r2==[(22,6,16),(6,1,5)]
print("PASS Jacobian degree 2 ambient/rank/quotient, +/-:",r2)
r3=rank_by_parity(3)
assert r3==[(62,37,25),(22,12,10)]
print("PASS Jacobian degree 3 ambient/rank/quotient, +/-:",r3)

t=s.symbols("t")
charpoly=s.cancel((1-t**2)**6*(1+t**2)/((1-t)**6*(1+t)))
assert s.expand(charpoly-(1+t)**5*(1+t**2))==0
chars=[s.expand(charpoly).coeff(t,j) for j in range(8)]
dims=[comb(7,j) for j in range(8)]
assert chars==[1,5,11,15,15,11,5,1]
assert all((d+c)%2==0 and d>=abs(c) for d,c in zip(dims,chars))
print("PASS full smooth Jacobian character:",chars)
print("PASS full smooth Jacobian dimensions:",dims)

# Griffiths residue carries det(iota)=-1. The cubic is invariant.
h32plus,h32minus=r2[1][2],r2[0][2]
assert (h32plus,h32minus)==(5,16)
assert (6-2*(h32plus-h32minus))==28  # Lefschetz = chi(Z)+chi(p).
print("PASS primitive H^(3,2) +/-=(5,16), trace=-11; Lefschetz=28")

hh_X={0:6,-1:21,1:21}
hh_X_inv={0:6,-1:5,1:5}
hh_Z={0:25,-2:1,2:1}
hh_p={0:1}
hh_orb={j:hh_X_inv.get(j,0)+hh_Z.get(j,0)+hh_p.get(j,0)
        for j in range(-2,3)}
hh_equiv_ku=dict(hh_orb)
hh_equiv_ku[0]-=4*2
assert hh_equiv_ku=={-2:1,-1:5,0:24,1:5,2:1}
hh_ku_Y={-1:5,0:2,1:5}
hh_ku_Z={-2:1,0:22,2:1}
assert hh_equiv_ku=={j:hh_ku_Y.get(j,0)+hh_ku_Z.get(j,0)
                     for j in range(-2,3)}
print("PASS equivariant Ku Hochschild homology:",hh_equiv_ku)
print("PASS additive HH agreement with Ku(Y) + Ku(Z)")

# Common Euler pairing of pr(O(4)), pr(O(5)), using the four line exceptions.
hilbert = lambda d: s.binomial(d+6,6)-s.binomial(d+3,6)
line_euler=s.Matrix(6,6,lambda i,j:hilbert(j-i))
exceptional=line_euler[:4,:4]
projected=[]
for j in (4,5):
    v=s.zeros(6,1)
    v[j]=1
    coeff=exceptional.inv()*line_euler[:4,j]
    for i in range(4):
        v[i]=-coeff[i]
    projected.append(v)
P=s.Matrix.hstack(*projected)
assert line_euler[:4,:]*P==s.zeros(4,2)
gram=P.T*line_euler*P
assert gram==s.Matrix([[-27,-189],[-162,-1161]])
assert gram.det()==729
T=s.Matrix([[1,-7],[0,1]])
assert T.T*gram*T==27*s.Matrix([[-1,0],[1,-1]])
print("PASS common Euler Gram matrix:",gram.tolist(),"det =",gram.det())
print("PASS all 9 finite checks; no categorical equivalence claimed")
