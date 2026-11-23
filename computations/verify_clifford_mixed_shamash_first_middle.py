#!/usr/bin/env python3
"""Exact 9-parameter middle Shamash homotopy at tau1=tau2=2.

All 9 one-way coefficients U_ab remain independent. The algorithm obtains
H(s,U)=H0+s H1(U)+s**2 H2(U) solving d2*H+u*d1=w*I6 exactly
(including the full cubic coefficient test). It uses only rational
Clifford PBW reductions and an EXACT rank-210 Koszul pivot minor.

This is the P1->P2 component of s1, not the remaining Shamash maps,
matrix factorization, or the Ku comparison kernel. Requires SymPy.
"""
from functools import lru_cache
from itertools import combinations
from fractions import Fraction as F
from collections import defaultdict
import sympy as S

DEG=3
# Key (s_degree, tuple-of-center-indices, sorted-squarefree-generator-word)

def clean(out):return {k:v for k,v in out.items() if v and k[0]<=DEG}
def add(*parts):
    d=defaultdict(F)
    for part in parts:
        for k,v in part.items():d[k]+=v
    return clean(d)
def scale(a,c):return clean({k:v*c for k,v in a.items()})
def zc(i):return {(0,(i,),()):F(1)}

B2keys=[((i,),()) for i in range(6)]+[((),p) for p in combinations(range(6),2)]
B3keys=[((i,), (j,)) for i in range(6) for j in range(6)]+[((),p) for p in combinations(range(6),3)]
I3={k:j for j,k in enumerate(B3keys)}
assert len(set(B2keys))==21 and len(set(B3keys))==56

class Cliff:
    def __init__(self,U,V):
        self.U=U;self.V=V
        self.q={}
        for b,c,xi in [(0,1,2),(0,2,1),(1,2,0)]:
            self.q[b,c]=add(scale(zc(xi),-1),*( {(1,(3+j,),()):F(U[xi][j],2)} for j in range(3) if U[xi][j]))
        for b,c,yi in [(3,4,5),(3,5,4),(4,5,3)]:
            self.q[b,c]=add(scale(zc(yi),-1),*( {(1,(i,),()):F(V[yi-3][i],2)} for i in range(3) if V[yi-3][i]))
        self.reduce=lru_cache(None)(self._reduce)
        self.z=[self.word(i) for i in range(6)]

    def _reduce(self,word):
        for k in range(len(word)-1):
            a,b=word[k:k+2]
            prefix=word[:k];suffix=word[k+2:]
            if a==b:
                return self.mul(zc(a),self.reduce(prefix+suffix))
            if a>b:
                cross=(a>=3 and b<3)
                part=self.reduce(prefix+(b,a)+suffix)
                if cross:return part
                return add(scale(part,-1),scale(self.mul(self.q[b,a],self.reduce(prefix+suffix)),2))
        return {(0,(),word):F(1)}
    def word(self,*w):return self.reduce(tuple(w))
    def mul(self,a,b):
        out=defaultdict(F)
        for (r,ce,w),v in a.items():
            for (s,cf,x),t in b.items():
                if r+s>DEG:continue
                for (r2,cg,y),u in self.reduce(w+x).items():
                    deg=r+s+r2
                    if deg<=DEG:out[(deg,tuple(sorted(ce+cf+cg)),y)]+=v*t*u
        return clean(out)
    def comm(self,i,j):return add(self.mul(self.z[i],self.z[j]),scale(self.mul(self.z[j],self.z[i]),-1))
    def vec(self,e):
        arr={}
        for (sd,cen,w),c in e.items():
            j=I3[(cen,w)]
            arr[(sd,j)]=arr.get((sd,j),F(0))+c
        return arr
    def get_d2(self):
        z=self.z
        cols=[]
        xcols=[[(2,0),(1,2),(1,1)],[(1,2),(2,1),(1,0)],[(1,1),(1,0),(2,2)]]
        ycols=[[(2,3),(1,5),(1,4)],[(1,5),(2,4),(1,3)],[(1,4),(1,3),(2,5)]]
        for a in range(3):
            col=[{} for _ in range(6)]
            for i,(fac,j) in enumerate(xcols[a]):col[i]=scale(z[j],fac)
            for b in range(3):
                if self.U[a][b]:col[3+b]=scale(z[3+b],-self.U[a][b])
                if self.U[a][b]:col[3+b]={(1,ce,w):v for (_,ce,w),v in col[3+b].items()}
            cols.append(col)
        for b in range(3):
            col=[{} for _ in range(6)]
            for a in range(3):
                if self.V[b][a]:col[a]={(1,ce,w):v for (_,ce,w),v in scale(z[a],-self.V[b][a]).items()}
            for j,(fac,k) in enumerate(ycols[b]):col[j+3]=scale(z[k],fac)
            cols.append(col)
        for a in range(3):
            for b in range(3):
                col=[{} for _ in range(6)]
                col[a]=z[3+b];col[3+b]=scale(z[a],-1)
                cols.append(col)
        assert len(cols)==15
        for col in cols:
            e=add(*(self.mul(z[i],col[i]) for i in range(6)))
            assert not e,e
        return cols

    def volume(self,shift):
        i,j,k=shift,shift+1,shift+2
        return add(self.word(i,j,k),
                   scale(self.mul(self.q[i,j],self.z[k]),-1),
                   self.mul(self.q[i,k],self.z[j]),
                   scale(self.mul(self.q[j,k],self.z[i]),-1))

    def get_u_w(self):
        # alpha = 2*(1-2^3)=-14 for both factors
        u=[]
        for shift in (0,3):
            for a in range(3):
                ii=shift+(a+1)%3;jj=shift+(a+2)%3
                u.append(scale(self.comm(ii,jj),F(-7,3)))
        w=add(*(self.mul(self.z[i],u[i]) for i in range(6)))
        assert w==add(*(self.mul(u[i],self.z[i]) for i in range(6)))
        assert w==scale(add(self.volume(0),self.volume(3)),-14)
        for generator in self.z:
            assert self.mul(w,generator)==self.mul(generator,w)
        return u,w

    def stage_matrix(self,cols):
        stages=[defaultdict(F) for _ in range(DEG+1)]
        B2=[zc(i) for i in range(6)]+[self.word(*word) for word in combinations(range(6),2)]
        for j,col in enumerate(cols):
            for k,b in enumerate(B2):
                for i in range(6):
                    for (degree,l),v in self.vec(self.mul(col[i],b)).items():
                        stages[degree][(i*56+l,j*21+k)]+=v
        return [clean_sparse_dict(d) for d in stages]

def clean_sparse_dict(d):return {key:val for key,val in d.items() if val}

def stage_rhs(c,u,w):
    stages=[]
    for col in range(6):
        v=[add(w if i==col else {},scale(c.mul(u[i],c.z[col]),-1)) for i in range(6)]
        arr=[defaultdict(F) for _ in range(DEG+1)]
        for i,p in enumerate(v):
            for (degree,r),val in c.vec(p).items():arr[degree][i*56+r]+=val
        stages.append([dict(x) for x in arr])
    return stages

# Generate once the fixed matrix at U=V=0 and choose an exact 210x210 minor.
ZERO=[[0]*3 for _ in range(3)]
base=Cliff(ZERO,ZERO)
A0data=base.stage_matrix(base.get_d2())[0]
# Find a 210x210 pivot minor by exact rational row reduction.
A0exact=S.SparseMatrix(336,315,{(i,j):S.Rational(v.numerator,v.denominator)
                              for (i,j),v in A0data.items()})
_,candidates=A0exact.rref(simplify=False,normalize_last=True)
pivcols=list(candidates)
_,candidates=A0exact[:,pivcols].T.rref(simplify=False,normalize_last=True)
pivrows=list(candidates)
rank=len(pivcols)
assert rank==210 and len(pivrows)==210
fix=S.SparseMatrix(rank,rank,{(i,j):S.Rational(A0data.get((rr,pivcols[j]),0)) for i,rr in enumerate(pivrows) for j in range(rank) if (rr,pivcols[j]) in A0data})
inv=fix.inv()
assert fix*inv==S.eye(rank)
print('PASS 1: exact 336x315 rational rank 210, with an exactly invertible 210x210 pivot minor',flush=True)

def apply(mat,x):
    out=defaultdict(F)
    for (i,j),value in mat.items():
        if x.get(j):out[i]+=value*x[j]
    return {i:v for i,v in out.items() if v}

def exact_solve(rhs):
    b=S.Matrix([S.Rational(rhs.get(i,F(0))) for i in pivrows])
    x=inv*b
    sol={pivcols[j]:F(int(S.numer(x[j])),int(S.denom(x[j]))) for j in range(rank) if x[j]}
    assert apply(A0data,sol)=={i:v for i,v in rhs.items() if v},'Incompatible with fixed image!'
    return sol

def combine(a,b):
    out=defaultdict(F,a)
    for k,v in b.items():out[k]+=v
    return {k:v for k,v in out.items() if v}
def minus(a,b):return combine(a,{i:-v for i,v in b.items()})

# Universal in the NINE independent U parameters (V=0), tau1=tau2=2.
# Work in Sym^d(Q^9) by exact coefficient extraction; use sparse dictionary
# keys u_00,...,u_22, not numerical sampling or polynomial interpolation.
from itertools import combinations_with_replacement
Elist=[]
for p in range(9):
    U=[[0]*3 for _ in range(3)]
    U[p//3][p%3]=1
    Elist.append(U)

# s=0 input is independent of U; assemble one exact chosen quadratic homotopy.
baseU=Cliff(ZERO,ZERO)
assert all(x=={} for x in baseU.stage_matrix(baseU.get_d2())[1:])
baseU0,basew=baseU.get_u_w()
b0=stage_rhs(baseU,baseU0,basew)
H0=[exact_solve(b0[j][0]) for j in range(6)]
for j in range(6):assert all(not b0[j][k] for k in (1,2,3))
print('PASS 2: full six-column constant s1_1 solves d2_0*H0=w0*I-u0*d1',flush=True)

# All nine linear coefficient matrices and RHS, exactly.
A1=[];b1=[]
for U in Elist:
    C=Cliff(U,ZERO)
    a=C.stage_matrix(C.get_d2())
    assert a[0]==A0data and a[2]=={} and a[3]=={}
    right=stage_rhs(C,*C.get_u_w())
    assert all(not right[j][2] and not right[j][3] for j in range(6))
    assert all(right[j][0]==b0[j][0] for j in range(6))
    A1.append(a[1]);b1.append([right[j][1] for j in range(6)])
print('PASS 3: all nine Clifford PBW parameter directions are exactly affine in s',flush=True)

# First-order 9*6 vectors of dimension 315.
H1={}
for a in range(9):
    H1[a]=[]
    for j in range(6):
        residual=minus(b1[a][j],apply(A1[a],H0[j]))
        H1[a].append(exact_solve(residual))
print('PASS 4: all 54 first-order coefficient vectors solve the 336-row equation',flush=True)

# Second-order 45*6 vectors.  Polynomial coefficients of U_a U_b:
# for a<b: A1_a H1_b + A1_b H1_a, and for a=b: A1_a H1_a.
PAIR=list(combinations_with_replacement(range(9),2))
H2={}
for a,b in PAIR:
    out=[]
    for j in range(6):
        term=apply(A1[a],H1[b][j])
        if a!=b:term=combine(term,apply(A1[b],H1[a][j]))
        out.append(exact_solve({i:-v for i,v in term.items()}))
    H2[a,b]=out
print('PASS 5: all 270 quadratic coefficient vectors solve the 336-row equation',flush=True)

# Universal cubic obstruction in U: 165 coefficients, 6 columns,
# each of 336 B3 rows.  Must vanish identically, not modulo samples.
TRIPLE=list(combinations_with_replacement(range(9),3))
for a,b,c in TRIPLE:
    # In U_a U_b U_c the A1_d H2_{remaining} terms occur once per
    # distinct d, even when variables coincide.
    distinct=sorted(set((a,b,c)))
    for j in range(6):
        defect={}
        for d in distinct:
            rem=list((a,b,c));rem.remove(d)
            defect=combine(defect,apply(A1[d],H2[tuple(rem)][j]))
        assert not defect,(a,b,c,j,defect)
print('PASS 6: all 165 cubic parameter coefficients have zero remaining s^3 defect',flush=True)

# At every U the constructed s1_1=H0+s sum U_a H1_a+s^2 sum U_aU_b H2_ab
# solves d2*s1_1+s1_0*d1=w_s*Id EXACTLY (no higher power possible).
# Additional independent specializations verify source multiplication, not just
# the abstract cubic coefficient extraction.
def verify_polynomial_probe(name,U,V=ZERO):
    c=Cliff(U,V);mat=c.stage_matrix(c.get_d2());u,w=c.get_u_w()
    rhs=stage_rhs(c,u,w)
    values=[H0]
    v1=[];v2=[]
    for j in range(6):
        xx={}
        for a in range(9):
            if U[a//3][a%3]:xx=combine(xx,{i:v*U[a//3][a%3] for i,v in H1[a][j].items()})
        v1.append(xx)
        xx={}
        for a,b in PAIR:
            coeff=U[a//3][a%3]*U[b//3][b%3]
            if coeff:xx=combine(xx,{i:v*coeff for i,v in H2[a,b][j].items()})
        v2.append(xx)
    values.extend([v1,v2])
    for j in range(6):
        for k in range(4):
            left={}
            for l in range(min(k,2)+1):left=combine(left,apply(mat[k-l],values[l][j]))
            assert left==rhs[j][k],(name,j,k)
    print('PASS:',name,'all exact polynomial s coefficients incl s^3=0',flush=True)

E=Elist[0]
R=[[1,1,1],[0,0,0],[0,0,0]]
C=[[1,0,0],[1,0,0],[1,0,0]]
I=[[int(i==j) for j in range(3)] for i in range(3)]
for name,U in [('E00',E),('R0',R),('C0',C),('I3',I),('generic',[[-1,2,3],[1,3,-2],[2,-1,1]])]:
    verify_polynomial_probe(name,U)

counts={'H0':sum(len(y) for y in H0),
        'H1':sum(len(y) for x in H1.values() for y in x),
        'H2':sum(len(y) for x in H2.values() for y in x)}
print('PASS 7: exact universal quadratic polynomial Shamash s1_1 in 9 parameters; nonzero coefficient counts:',counts,flush=True)
print('7 PASS: middle Shamash equation for one-way mixed cubic at tau1=tau2=2. Full higher Shamash/Ku kernel remains open.',flush=True)
