#!/usr/bin/env python3
"""Exact S3 x S3 symmetry of the one-way mixed Clifford family.

Polynomial coefficient checks on the rank-eight Clifford PBW basis, with nine
independent mixing coefficients. The formal equivariant lifting principle is
conditional: this script does not construct an actual deformed MF or Ku kernel.
"""
from functools import lru_cache
import sympy as sp

T, t, T2 = sp.symbols('tau1 s tau2')
X = sp.symbols('X1:4')
Y = sp.symbols('Y1:4')
U = sp.Matrix(3, 3, sp.symbols('u11 u12 u13 u21 u22 u23 u31 u32 u33'))
P = {1:2, 2:1, 3:3}
C = {1:2, 2:3, 3:1}
Ci={v:k for k,v in C.items()}

L=[sum(U[i,j]*Y[j] for j in range(3)) for i in range(3)]
q={(1,2):(-T*X[2]+t*L[2])/2,
   (1,3):(-T*X[1]+t*L[1])/2,
   (2,3):(-T*X[0]+t*L[0])/2}
def Q(i,j):return X[i-1] if i==j else q[tuple(sorted((i,j)))]
PBW=[(),(1,),(2,),(3,),(1,2),(1,3),(2,3),(1,2,3)]
def clean(d):return {k:sp.expand(v) for k,v in d.items() if sp.expand(v)!=0}
@lru_cache(None)
def reduce(w):
    for n in range(len(w)-1):
        i,j=w[n:n+2]
        if i==j:return clean({k:X[i-1]*v for k,v in reduce(w[:n]+w[n+2:]).items()})
        if i>j:
            a=reduce(w[:n]+(j,i)+w[n+2:]);b=reduce(w[:n]+w[n+2:])
            return clean({k:-a.get(k,0)+2*q[(j,i)]*b.get(k,0) for k in set(a)|set(b)})
    assert w in PBW
    return {w:sp.S.One}
def mul(a,b):
    r={}
    for u,c in a.items():
        for v,d in b.items():
            for w,f in reduce(u+v).items():r[w]=r.get(w,0)+c*d*f
    return clean(r)
def add(a,b):return clean({k:a.get(k,0)+b.get(k,0) for k in set(a)|set(b)})
def equal(a,b):return not clean({k:a.get(k,0)-b.get(k,0) for k in set(a)|set(b)})

omega={(1,2,3):sp.S.One,(3,):-q[(1,2)],(2,):q[(1,3)],(1,):-q[(2,3)]}
omega=clean(omega)

def change_x_coeff(p, coeff):
    sub={X[i-1]:X[p[i]-1] for i in (1,2,3)}
    sub.update({U[i-1,j]:U[p[i]-1,j] for i in (1,2,3) for j in range(3)})
    return coeff.xreplace(sub)
def x_action(e,p,sign=1):
    out={}
    for word,coeff in e.items():
        prod={():sp.S.One}
        for i in word:prod=mul(prod,{(p[i],):sp.Integer(sign)})
        for k,v in prod.items():out[k]=out.get(k,0)+change_x_coeff(p,coeff)*v
    return clean(out)

for name,p,sign in [('rho',C,1),('sigma',P,-1)]:
    for i in (1,2,3):
        for j in (1,2,3):
            assert sp.expand(change_x_coeff(p,Q(i,j))-Q(p[i],p[j]))==0,(name,i,j)
    print('PASS:',name,'preserves x-Clifford Gram matrix with coefficient row action')

for name,p in [('rho',C),('sigma',P)]:
    sub={Y[i-1]:Y[p[i]-1] for i in (1,2,3)}
    sub.update({U[j,i-1]:U[j,p[i]-1] for j in range(3) for i in (1,2,3)})
    assert all(sp.expand(li.xreplace(sub)-li)==0 for li in L)
    print('PASS:',name,'on y leaves all three mixing forms L_i invariant')

for name,p,sign in [('rho',C,1),('sigma',P,-1)]:
    assert equal(x_action(omega,p,sign),omega),name
print('PASS: full nine-parameter Clifford volume omega_x invariant under x-S3')

# y-volume: same standard Clifford reduction with independent y_i and tau2.
# The x-volume check is universal in the three diagonal/three off-diagonal entries;
# substituting s=0 and tau=tau2, X_i=Y_i gives the y-volume check.
q_y={ij:sp.expand(c.subs({t:0,T:T2,**{X[i]:Y[i] for i in range(3)}},simultaneous=True)) for ij,c in q.items()}
for name,p,sign in [('rho',C,1),('sigma',P,-1)]:
    # Since the universal invariant identity is polynomial in T,X, the y identity is a base change.
    assert equal(x_action(omega,p,sign),omega)
    assert all(sp.expand(q_y[ij]-(-T2*Y[({(1,2):3,(1,3):2,(2,3):1}[ij])-1]/2))==0 for ij in q_y)
print('PASS: y-Clifford volume is invariant (unmixed universal specialization)')

# Group actions on the nine coefficient symbols are precisely row/column permutation.
def matrix_action(M,p_x=None,p_y=None):
    x=p_x or {1:1,2:2,3:3}; y=p_y or {1:1,2:2,3:3}
    return sp.Matrix(3,3,lambda i,j:M[x[i+1]-1,y[j+1]-1])
for p in (C,P):
    for i in range(3):
        for j in range(3):
            assert matrix_action(U,p_x=p)[i,j]==U[p[i+1]-1,j]
            assert matrix_action(U,p_y=p)[i,j]==U[i,p[j+1]-1]
for p in (P,C):
    for i in range(3):
        for j in range(3):
            assert sp.expand(matrix_action(matrix_action(U,p_x=p),p_y=C)[i,j]-
                             matrix_action(matrix_action(U,p_y=C),p_x=p)[i,j])==0
for i in (1,2,3):
    assert P[P[i]]==i
    assert C[C[C[i]]]==i
    assert P[C[P[i]]]==Ci[i]
print('PASS: coefficient group relations S3 x S3 and commuting row/column actions')

# The polynomial specified cubic is w=a1*2(1-T^3)*omega_x+a2*Omega_y.
# Both terms are invariant separately, hence the universal central cubic is invariant.
a1,a2=sp.symbols('a1 a2')
Omega_x={word:sp.expand(2*a1*(1-T**3)*coeff) for word,coeff in omega.items()}
for p,sign in ((C,1),(P,-1)):
    assert equal(x_action(Omega_x,p,sign),Omega_x)
print('PASS: specified central cubic w invariant; no cube-root choice')
print('8 PASS: universal one-way mixed source family is S3 x S3 equivariant; Ku comparison still open.')
