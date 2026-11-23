#!/usr/bin/env python3
"""Universal one-way Clifford curved PBW Maurer--Cartan certificate.

Checks all 512 triples over a rational polynomial ring with symbolic base Clifford
coefficients and symbolic linear variations, then checks curvature centrality
through cubic order. No actual Ku comparison kernel or period is computed.
"""
from functools import lru_cache
import sympy as sp

X1,X2,X3,Q12,Q13,Q23,D12,D13,D23 = sp.symbols(
    'X1 X2 X3 Q12 Q13 Q23 D12 D13 D23')
q={(1,2):Q12,(1,3):Q13,(2,3):Q23}
base=[(),(1,),(2,),(3,),(1,2),(1,3),(2,3),(1,2,3)]
Ix={b:j for j,b in enumerate(base)}
Z={1:X1,2:X2,3:X3}

@lru_cache(None)
def reduce(word):
    for k in range(len(word)-1):
        i,j=word[k:k+2]
        if i==j:
            return {u:sp.expand(Z[i]*c) for u,c in reduce(word[:k]+word[k+2:]).items()}
        if i>j:
            p=reduce(word[:k]+(j,i)+word[k+2:])
            t=reduce(word[:k]+word[k+2:])
            out={u:sp.expand(-p.get(u,0)+2*q[(j,i)]*t.get(u,0)) for u in set(p)|set(t)}
            return {u:v for u,v in out.items() if v!=0}
    return {word:sp.S.One}
raw={(i,j):reduce(i+j) for i in base for j in base}
mm={}
for (i,j),out in raw.items():
    for k,c in out.items():
        poly=sp.Poly(c.subs({Q12:Q12+D12*sp.Symbol('z'),Q13:Q13+D13*sp.Symbol('z'),Q23:Q23+D23*sp.Symbol('z')},simultaneous=True),sp.Symbol('z'))
        assert poly.degree()<=2,(i,j,k,c,poly)
        for t in range(3):
            cc=poly.nth(t)
            if cc!=0:mm.setdefault(t,{})[(Ix[i],Ix[j],Ix[k])]=cc
print('PASS 1: PBW table decomposes into m0+s*m1+s^2*m2')

m2=mm[2]
expected={
 (Ix[(2,3)],Ix[(1,2)],Ix[()]): -4*D12*D23,
 (Ix[(2,3)],Ix[(1,2,3)],Ix[(3,)]): -4*D12*D23,
 (Ix[(1,2,3)],Ix[(1,2)],Ix[(1,)]): -4*D12*D23,
 (Ix[(1,2,3)],Ix[(1,2,3)],Ix[(1,3)]): -4*D12*D23,
}
assert m2==expected,(m2,expected)
print('PASS 2: four explicit m2 entries, and no hidden quadratic products')

def p(t,i,j):
    return {k:c for (a,b,k),c in mm[t].items() if a==i and b==j}

def comp(t,u,i,j,k):
    # m_t(m_u(a,b),c) - m_t(a,m_u(b,c))
    s={}
    for h,a in p(u,i,j).items():
        for out,b in p(t,h,k).items():s[out]=s.get(out,0)+a*b
    for h,a in p(u,j,k).items():
        for out,b in p(t,i,h).items():s[out]=s.get(out,0)-a*b
    return {z:sp.expand(v) for z,v in s.items() if sp.expand(v)!=0}

def check_zero(triples,what):
    for i,j,k in ((i,j,k) for i in range(8) for j in range(8) for k in range(8)):
        a={}
        for t,u,sign in triples:
            for b,v in comp(t,u,i,j,k).items():a[b]=a.get(b,0)+sign*v
        assert all(sp.expand(v)==0 for v in a.values()),(what,i,j,k,a)
    print(what)

check_zero([(0,0,1)],'PASS 3: 512 associativity triples of m0')
check_zero([(0,1,1),(1,0,1)],'PASS 4: 512 first-order cocycle triples')
check_zero([(0,2,1),(1,1,1),(2,0,1)],'PASS 5: 512 second-order obstruction exactness triples')
check_zero([(1,2,1),(2,1,1)],'PASS 6: 512 third-order mixed MC triples')
check_zero([(2,2,1)],'PASS 7: 512 fourth-order MC triples')

# Central Clifford volume omega= e123 - q12 e3 + q13 e2 - q23 e1
w0={Ix[(1,2,3)]:1,Ix[(3,)]:-Q12,Ix[(2,)]:Q13,Ix[(1,)]:-Q23}
w1={Ix[(3,)]:-D12,Ix[(2,)]:D13,Ix[(1,)]:-D23}

def central_order(n,i):
    out={}
    for t in range(3):
        u=n-t
        if u not in (0,1):continue
        w=(w0 if u==0 else w1)
        for j,c in w.items():
            for k,z in p(t,j,i).items():out[k]=out.get(k,0)+c*z
            for k,z in p(t,i,j).items():out[k]=out.get(k,0)-c*z
    return {j:sp.expand(v) for j,v in out.items() if sp.expand(v)!=0}
for n in range(4):
    for i in range(8):
        assert not central_order(n,i),(n,i,central_order(n,i))
print('PASS 8: 0--3 jets of the curved central volume commute with every PBW basis element')

# The obstruction is nonzero as a cochain in the two quadratic probes.
witness=comp(1,1,Ix[(2,)],Ix[(3,)],Ix[(1,2)])
assert witness=={Ix[()]:4*D12*D23},witness
nslots=sum(len(comp(1,1,i,j,k)) for i in range(8) for j in range(8) for k in range(8))
assert nslots==80,nslots
print('PASS 9: 80 nonzero obstruction cochain slots; a concrete triple detects 4*D12*D23')

# For one-way parameters D23=L1/2, D13=L2/2, D12=L3/2,
# E00 and R0 have L3=0; C0 and I3 have L1*L3 nonzero.
Y1,Y2,Y3=sp.symbols('Y1 Y2 Y3')
for name,L1,L2,L3,nonzero in [
    ('E00',Y1,0,0,False),('R0',Y1+Y2+Y3,0,0,False),
    ('C0',Y1,Y1,Y1,True),('I3',Y1,Y2,Y3,True)]:
    vals={D23:L1/2,D13:L2/2,D12:L3/2}
    m2val={key:sp.expand(value.subs(vals)) for key,value in m2.items()}
    assert (any(v!=0 for v in m2val.values()))==nonzero,(name,m2val)
    if nonzero:
        assert all(sp.expand(v+L1*L3)==0 for v in m2val.values())
        assert sp.expand(witness[Ix[()]].subs(vals)-L1*L3)==0
    else:
        assert all(v==0 for v in m2val.values())
print('PASS 10: exactly the two nonlinear Clifford probes require m2; four entries equal -L1*L3')
print('10 PASS: all polynomial MC and curvature jets; no actual KS retract, rotation or Ku scalar')
