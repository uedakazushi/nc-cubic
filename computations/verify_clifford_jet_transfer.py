#!/usr/bin/env python3
"""Exact PBW affine/quadratic dependence for the one-way Clifford family.

Only symbolic Clifford algebra and formal perturbation identities are checked,
not the actual Picard/period comparison, higher KS jets, or Ku equivalence.
Requires SymPy.
"""
import sympy as s
from functools import lru_cache

Z1, Z2, Z3, q12, q13, q23 = s.symbols('Z1 Z2 Z3 q12 q13 q23')
X = {1: Z1, 2: Z2, 3: Z3}
q = {(1, 2): q12, (1, 3): q13, (2, 3): q23}
B = [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]


@lru_cache(None)
def reduce(word):
    for i in range(len(word)-1):
        a,b = word[i:i+2]
        if a == b:
            return {k:s.expand(X[a]*v)
                    for k,v in reduce(word[:i]+word[i+2:]).items()}
        if a > b:
            v1=reduce(word[:i]+(b,a)+word[i+2:])
            v2=reduce(word[:i]+word[i+2:])
            keys=set(v1)|set(v2)
            return {k:s.expand(-v1.get(k,0)+2*q[b,a]*v2.get(k,0))
                    for k in keys
                    if s.expand(-v1.get(k,0)+2*q[b,a]*v2.get(k,0))!=0}
    return {word:s.Integer(1)}


T={(a,b):reduce(a+b) for a in B for b in B}
assert len(T)==64 and all(set(v).issubset(set(B)) for v in T.values())
assert all(s.Poly(c,q12,q13,q23).total_degree()<=2
           for v in T.values() for c in v.values())
assert all(s.degree(c,q23)<=1 for v in T.values() for c in v.values())
assert all(s.diff(c,q12,q12)==s.diff(c,q13,q13)==s.diff(c,q23,q23)==0
           for v in T.values() for c in v.values())
quads=[]
for (a,b),v in T.items():
    for k,c in v.items():
        if s.Poly(c,q12,q13,q23).total_degree()>=2:
            assert s.expand(c).coeff(q12*q23)==-4
            assert s.diff(c,q12,q23)==-4
            quads.append((a,b,k))
assert set(quads)=={
    ((2,3),(1,2),()),
    ((2,3),(1,2,3),(3,)),
    ((1,2,3),(1,2),(1,)),
    ((1,2,3),(1,2,3),(1,3)),
}
print('PASS 1: full 8x8 PBW table has four q12*q23 quadratic terms')

omega={(1,2,3):s.Integer(1), (3,):-q12,(2,):q13,(1,):-q23}
def multiply(v,w):
    out={}
    for a,x in v.items():
        for b,y in w.items():
            for k,c in T[a,b].items():out[k]=s.expand(out.get(k,0)+x*y*c)
    return {k:s.factor(c) for k,c in out.items() if s.factor(c)!=0}
for i in (1,2,3):
    left=multiply(omega,{(i,):1});right=multiply({(i,):1},omega)
    assert all(s.expand(left.get(k,0)-right.get(k,0))==0
               for k in set(left)|set(right))
mat=s.Matrix([[Z1,q12,q13],[q12,Z2,q23],[q13,q23,Z3]])
omega2=multiply(omega,omega)
assert set(omega2)=={()} and s.factor(omega2[()]+mat.det())==0
print('PASS 2: normalized volume is central with square minus determinant')

Y1,Y2,Y3,z=s.symbols('Y1 Y2 Y3 z')
rows={
    'E00':{0:Y1},
    'R0':{0:Y1+Y2+Y3},
    'C0':{0:Y1,1:Y1,2:Y1},
    'I3':{0:Y1,1:Y2,2:Y3},
}
for name,mixing in rows.items():
    subs={q23:-Z1+s.Rational(1,2)*z*mixing.get(0,0),
          q13:-Z2+s.Rational(1,2)*z*mixing.get(1,0),
          q12:-Z3+s.Rational(1,2)*z*mixing.get(2,0)}
    maxdeg=max(s.Poly(s.expand(c.subs(subs)),z).degree()
               for v in T.values() for c in v.values())
    expected=2 if name in ('C0','I3') else 1
    assert maxdeg==expected,(name,maxdeg)
    print('  ',name,'PBW degree',maxdeg)
print('PASS 3: minimal four probes: two affine and two quadratic')

ix={k:i for i,k in enumerate(B)}
first={}
for (a,b),v in T.items():
    for k,c in v.items():
        d=s.diff(c,q23)
        if d!=0:first.setdefault((ix[a],ix[b]),{})[ix[k]]=d
assert len(first)==16
for i in range(8):
    for j in range(8):
        for k in range(8):
            out={}
            for m0,c in first.get((i,j),{}).items():
                for n,d in first.get((m0,k),{}).items():
                    out[n]=out.get(n,0)+c*d
            for m0,c in first.get((j,k),{}).items():
                for n,d in first.get((i,m0),{}).items():
                    out[n]=out.get(n,0)-c*d
            assert all(s.expand(v)==0 for v in out.values())
print('PASS 4: first-order cochain self-composes to zero in 512 triples')

for name,mixing in rows.items():
    subs={q23:-Z1+z*mixing.get(0,0)/2,
          q13:-Z2+z*mixing.get(1,0)/2,
          q12:-Z3+z*mixing.get(2,0)/2}
    assert all(s.degree(s.expand(c.subs(subs)),z)<=1
               for c in omega.values())
print('PASS 5: central volume curvature is affine on all probes')

D1,D2,H=s.symbols('D1 D2 H',commutative=False)
Delta=z*D1+z**2*D2
transfer=s.expand(Delta-Delta*H*Delta+Delta*H*Delta*H*Delta)
c1=D1
c2=D2-D1*H*D1
c3=-D1*H*D2-D2*H*D1+D1*H*D1*H*D1
assert s.expand(s.diff(transfer,z).subs(z,0)-c1)==0
assert s.expand(s.diff(transfer,z,2).subs(z,0)/2-c2)==0
assert s.expand(s.diff(transfer,z,3).subs(z,0)/6-c3)==0
print('PASS 6: exact ordered second- and third-order transfer formulas')
