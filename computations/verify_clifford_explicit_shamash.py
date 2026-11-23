#!/usr/bin/env python3
"""Exact augmentation Koszul--Shamash factorization for S(1,1,tau).

Right-module matrices act by left multiplication. All polynomial identities
are over Q[tau, X1, X2, X3] in the 8-element Clifford PBW basis.
The two-factor curved comparison retract (i,p,h) is not asserted.
"""
from functools import lru_cache
import sympy as sp

tau = sp.symbols('tau')
X = {i: sp.Symbol('X'+str(i)) for i in (1,2,3)}
Delta = tau**3-1
q = {(1,2):-tau*X[3]/2,(1,3):-tau*X[2]/2,(2,3):-tau*X[1]/2}
PBW = [(),(1,),(2,),(3,),(1,2),(1,3),(2,3),(1,2,3)]

@lru_cache(None)
def reduce_word(word):
    for j in range(len(word)-1):
        a,b = word[j:j+2]
        if a == b:
            return {k:sp.expand(X[a]*c) for k,c in
                    reduce_word(word[:j]+word[j+2:]).items()}
        if a > b:
            v = reduce_word(word[:j]+(b,a)+word[j+2:])
            w = reduce_word(word[:j]+word[j+2:])
            return clean({k:-v.get(k,0)+2*q[(b,a)]*w.get(k,0)
                          for k in set(v)|set(w)})
    assert word in PBW
    return {word:sp.S.One}

def clean(a):
    return {k:sp.expand(v) for k,v in a.items() if sp.expand(v)!=0}

def raw(word, coefficient=1):
    return clean({k:coefficient*v for k,v in reduce_word(tuple(word)).items()})

def add(*elems):
    out = {}
    for e in elems:
        for k,v in e.items():out[k]=out.get(k,0)+v
    return clean(out)

def neg(e):return clean({k:-v for k,v in e.items()})
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            for k,z in reduce_word(i+j).items():out[k]=out.get(k,0)+x*y*z
    return clean(out)

def scale(e,c):return clean({k:c*v for k,v in e.items()})
def E(i):return raw((i,))
def sq(i):return raw((i,i))
def prod(i,j):return raw((i,j))
def z():return {}
def unit():return raw(())
def iso(c):return scale(unit(),c)

def mm(a,b):
    assert all(len(x)==len(b) for x in a)
    return [[add(*(mul(a[i][k],b[k][j]) for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]

def madd(a,b):return [[add(x,y) for x,y in zip(i,j)] for i,j in zip(a,b)]
def mdiag(c,n):return [[c if i==j else z() for j in range(n)] for i in range(n)]
def assert_m(a,b):
    assert len(a)==len(b) and all(len(x)==len(y) for x,y in zip(a,b))
    for i in range(len(a)):
        for j in range(len(a[i])):
            assert not sub(a[i][j],b[i][j]),(i,j,a[i][j],b[i][j])

def sigma(i):return i%3+1
def sigma2(i):return sigma(sigma(i))
def rotate(e):
    rotXi={X[i]:X[sigma(i)] for i in (1,2,3)}
    return add(*(scale(raw(tuple(sigma(k) for k in w)),c.xreplace(rotXi))
                 for w,c in e.items()))

def weighted_degree(e):
    degrees=set()
    for word,c in e.items():
        for exps,cc in sp.Poly(c,*X.values()).terms():
            if cc:degrees.add(len(word)+2*sum(exps))
    assert len(degrees)<=1,degrees
    return next(iter(degrees)) if degrees else None

# Quadratic Sklyanin Koszul resolution in right-module matrix convention.
d1=[[E(1),E(2),E(3)]]
d2=[[scale(E(1),tau),E(3),E(2)],
    [E(3),scale(E(2),tau),E(1)],
    [E(2),E(1),scale(E(3),tau)]]
d3=[[E(1)],[E(2)],[E(3)]]
assert_m(mm(d1,d2),[[z(),z(),z()]])
assert_m(mm(d2,d3),[[z()],[z()],[z()]])
print('PASS 1: exact length-three quadratic Koszul differential identities')

omega=add(raw((1,2,3)),scale(raw((3,3,3)),tau/2),
          scale(raw((2,2,2)),-tau/2),scale(raw((1,1,1)),tau/2))
Omega=scale(omega,-2*Delta)
for i in (1,2,3):assert not sub(mul(E(i),Omega),mul(Omega,E(i)))
assert not sub(rotate(Omega),Omega)
print('PASS 2: exact central cubic Omega=2(1-tau^3)*omega, cyclic invariant')

# Cyclic choice of the first homotopy s1=(u,A,u^t).
u=[add(scale(prod(sigma(i),sigma2(i)),-2*Delta/3),
       scale(sq(i),-tau*Delta/3)) for i in (1,2,3)]
A=[[z() for _ in (1,2,3)] for _ in (1,2,3)]
for i in (1,2,3):
    j,k=sigma(i),sigma2(i)
    A[i-1][i-1]=add(scale(sq(i),-2*Delta/3),scale(prod(j,k),-tau**2))
    A[i-1][j-1]=add(scale(sq(k),tau),scale(prod(i,j),-(tau**3-4)/3))
    A[j-1][i-1]=scale(sq(k),-tau)
v=add(scale(Omega,(tau**3-4)/6),
      *(scale(raw((i,i,i)),-tau*Delta*(tau**3+8)/18) for i in (1,2,3)))
uc=[[u[i]] for i in range(3)]
ur=[u]
assert_m(mm(d1,uc),[[Omega]])
assert_m(mm(ur,d3),[[Omega]])
assert_m(madd(mm(d2,A),mm(uc,d1)),mdiag(Omega,3))
assert_m(madd(mm(A,d2),mm(d3,ur)),mdiag(Omega,3))
print('PASS 3: six first higher-homotopy identities d*s1+s1*d=Omega')

assert_m(madd(mm(A,uc),mm(d3,[[v]])),[[z()],[z()],[z()]])
assert_m(madd(mm(ur,A),mm([[v]],d1)),[[z(),z(),z()]])
print('PASS 4: six second higher-homotopy identities d*s2+s2*d=-s1^2')

# F^0=S (+) S(1)^3, F^{-1}=S(-1)^3 (+) S.
Dplus=[[d1[0][0],d1[0][1],d1[0][2],z()]]
Dplus += [[A[i][0],A[i][1],A[i][2],d3[i][0]] for i in range(3)]
Dminus=[[u[i],*d2[i]] for i in range(3)]+[[v,*u]]
assert_m(mm(Dplus,Dminus),mdiag(Omega,4))
assert_m(mm(Dminus,Dplus),mdiag(Omega,4))
print('PASS 5: both noncommutative 4x4 MF compositions equal Omega*I4')

for i in range(1,4):
    assert not sub(rotate(u[i-1]),u[sigma(i)-1])
    for j in range(1,4):
        assert not sub(rotate(A[i-1][j-1]),A[sigma(i)-1][sigma(j)-1]),(i,j)
assert not sub(rotate(v),v)
print('PASS 6: strict cyclic covariance of u, A and the cubic s2')

for o in [d1[0][j] for j in range(3)]+[d2[i][j] for i in range(3) for j in range(3)]+[d3[i][0] for i in range(3)]:
    assert weighted_degree(o)==1
for o in u+[A[i][j] for i in range(3) for j in range(3)]:
    assert weighted_degree(o)==2
assert weighted_degree(v)==3 and weighted_degree(Omega)==3
print('PASS 7: degrees 1/2/3 agree with graded folding and 3-period')

for val in (sp.Integer(2),sp.Integer(-1),sp.Rational(1,2)):
    assert sp.factor(Delta.subs(tau,val))!=0
    for matrix in (Dplus,Dminus):
        for row in matrix:
            for entry in row:
                for c in entry.values():
                    assert not sp.denom(sp.cancel(c)).has(tau)
print('PASS 8: polynomial tau-formulas require no tau^3-1 denominator')
print('8 PASS: explicit one-factor Shamash stabilization; not the mixed Ku retract or 12 scalars.')
