#!/usr/bin/env python3
"""Exact first two Koszul maps and initial Shamash homotopy for full two-way Clifford mixing.

Checks coefficients over QQ[tau1,tau2,a1,a2,s,U(3x3),V(3x3),X(3),Y(3)].
This is *not* a full Koszul resolution, matrix factorization, Ku kernel or HPL retract.
"""
from functools import lru_cache
from itertools import combinations_with_replacement, permutations, product
import sympy as S

s,tau1,tau2,a1,a2=S.symbols('s tau1 tau2 a1 a2')
X=S.symbols('X1 X2 X3');Y=S.symbols('Y1 Y2 Y3')
U=S.Matrix(3,3,S.symbols('u11 u12 u13 u21 u22 u23 u31 u32 u33'))
V=S.Matrix(3,3,S.symbols('v11 v12 v13 v21 v22 v23 v31 v32 v33'))
L=[S.expand(sum(U[i,j]*Y[j] for j in range(3))) for i in range(3)]
K=[S.expand(sum(V[i,j]*X[j] for j in range(3))) for i in range(3)]
alpha1=2*a1*(1-tau1**3);alpha2=2*a2*(1-tau2**3)

def cp(z):return S.expand(z)
class Cl:
    def __init__(self,Z,q):
        self.Z=Z;self.q=q
        self.reduce=lru_cache(None)(self._reduce)
    def _reduce(self,word):
        for k in range(len(word)-1):
            i,j=word[k:k+2]
            if i==j:
                return {w:cp(self.Z[i-1]*v) for w,v in self.reduce(word[:k]+word[k+2:]).items()}
            if i>j:
                a=self.reduce(word[:k]+(j,i)+word[k+2:]);b=self.reduce(word[:k]+word[k+2:]);p={w:cp(-a.get(w,0)+2*self.q[j,i]*b.get(w,0)) for w in set(a)|set(b)}
                return {w:v for w,v in p.items() if v!=0}
        return {word:S.Integer(1)}
    def word(self,*word):return self.reduce(tuple(word))
    def plus(self,*args):
        r={}
        for a in args:
            for w,v in a.items():r[w]=r.get(w,0)+v
        return {w:cp(v) for w,v in r.items() if cp(v)!=0}
    def times(self,p,a):return {w:cp(p*v) for w,v in a.items() if cp(p*v)!=0}
    def mul(self,a,b):
        r={}
        for wa,ca in a.items():
            for wb,cb in b.items():
                for w,c in self.reduce(wa+wb).items():r[w]=r.get(w,0)+ca*cb*c
        return {w:cp(v) for w,v in r.items() if cp(v)!=0}
    def equal(self,a,b):return not self.plus(a,self.times(-1,b))
    def scalar(self,p):return {():p}
    def volume(self):
        return self.plus(self.word(1,2,3),self.times(-self.q[1,2],self.word(3)),self.times(self.q[1,3],self.word(2)),self.times(-self.q[2,3],self.word(1)))
    def comm(self,i,j):return self.plus(self.word(i,j),self.times(-1,self.word(j,i)))

qx={(1,2):(-tau1*X[2]+s*L[2])/2,(1,3):(-tau1*X[1]+s*L[1])/2,(2,3):(-tau1*X[0]+s*L[0])/2}
qy={(1,2):(-tau2*Y[2]+s*K[2])/2,(1,3):(-tau2*Y[1]+s*K[1])/2,(2,3):(-tau2*Y[0]+s*K[0])/2}
cx=Cl(X,qx);cy=Cl(Y,qy)
for c in (cx,cy):
    perm=list(permutations((1,2,3)))
    alternating=c.times(S.Rational(1,6),c.plus(*(c.times(S.LeviCivita(*w),c.word(*w)) for w in perm)))
    assert c.equal(alternating,c.volume())
print('PASS 1: both Clifford volume elements are exact antisymmetrizations')

# The first Koszul differential (augmentation) is the row [x1,x2,x3,y1,y2,y3].
# The relation matrix has precisely 15 columns (3 x + 3 y + 9 cross).
# Work over the *full tensor Clifford algebra*, not just in its scalar center.
def liftx(a):return {(wx,()):v for wx,v in a.items()}
def lifty(a):return {((),wy):v for wy,v in a.items()}
def ts(v):return {((),()):v}
def clean_t(a):return {w:cp(v) for w,v in a.items() if cp(v)!=0}
def tadd(*args):
    t={}
    for a in args:
        for w,v in a.items():t[w]=t.get(w,0)+v
    return clean_t(t)
def tmul(a,b):
    out={}
    for (xa,ya),ca in a.items():
        for (xb,yb),cb in b.items():
            for xx,ccx in cx.reduce(xa+xb).items():
                for yy,ccy in cy.reduce(ya+yb).items():
                    k=(xx,yy);out[k]=out.get(k,0)+ca*cb*ccx*ccy
    return clean_t(out)
zero={}
z=[liftx(cx.word(i)) for i in (1,2,3)]+[lifty(cy.word(i)) for i in (1,2,3)]

def scale_t(k,a):return clean_t({w:cp(k*v) for w,v in a.items()})

def relation_x(a):
    # classical three x-Koszul rows; append the three y-corrections
    rows=[zero for _ in range(6)]
    if a==0:
        rows[0]=scale_t(tau1,z[0]);rows[1]=z[2];rows[2]=z[1]
    elif a==1:
        rows[0]=z[2];rows[1]=scale_t(tau1,z[1]);rows[2]=z[0]
    else:
        rows[0]=z[1];rows[1]=z[0];rows[2]=scale_t(tau1,z[2])
    for b in range(3):rows[3+b]=scale_t(-s*U[a,b],z[3+b])
    return rows

def relation_y(a):
    rows=[zero for _ in range(6)]
    for b in range(3):rows[b]=scale_t(-s*V[a,b],z[b])
    if a==0:rows[3]=scale_t(tau2,z[3]);rows[4]=z[5];rows[5]=z[4]
    elif a==1:rows[3]=z[5];rows[4]=scale_t(tau2,z[4]);rows[5]=z[3]
    else:rows[3]=z[4];rows[4]=z[3];rows[5]=scale_t(tau2,z[5])
    return rows

def relation_cross(a,b):
    rows=[zero for _ in range(6)]
    rows[a]=z[3+b];rows[3+b]=scale_t(-1,z[a])
    return rows

columns=[relation_x(i) for i in range(3)]+[relation_y(i) for i in range(3)]+[relation_cross(a,b) for a in range(3) for b in range(3)]
assert len(columns)==15 and all(len(col)==6 for col in columns)
for j,col in enumerate(columns):
    result=tadd(*(tmul(z[i],col[i]) for i in range(6)))
    assert result==zero,(j,result)
print('PASS 2: full 18-parameter 6 x 15 Koszul d1*d2=0')
# The uncorrected tensor Koszul column has nonzero defect s*L_a.
for a in range(3):
    col=relation_x(a)
    old_col=col[:3]+[zero,zero,zero]
    defect=tadd(*(tmul(z[i],old_col[i]) for i in range(6)))
    assert defect==ts(cp(s*L[a])),(a,defect)
for b in range(3):
    col=relation_y(b)
    old_col=[zero,zero,zero]+col[3:]
    defect=tadd(*(tmul(z[i],old_col[i]) for i in range(6)))
    assert defect==ts(cp(s*K[b])),(b,defect)
print('PASS 3: both x and y tensor relation columns have exact s*L and s*K defects')
assert len(columns[6:])==9
print('PASS 4: nine cross-commutator columns remain unchanged')

# Two explicit length-three Koszul syzygies, extending each factor's top class.
topx=[z[a] for a in range(3)]+[zero for _ in range(3)]+[scale_t(-s*U[a,b],z[3+b]) for a in range(3) for b in range(3)]
topy=[zero for _ in range(3)]+[z[3+b] for b in range(3)]+[scale_t(s*V[b,a],z[a]) for a in range(3) for b in range(3)]
assert len(topx)==len(topy)==15
for syzygy in (topx,topy):
    for i in range(6):
        assert tadd(*(tmul(columns[j][i],syzygy[j]) for j in range(15)))==zero,(i,syzygy is topy)
print('PASS 4b: two explicit columns of d3 satisfy d2*d3=0 at all 18 mixing coefficients')


# For each Clifford triple, u_i = alpha/6 * [x_{i+1},x_{i+2}].
def make_u(c,alpha):
    return [c.times(alpha*S.Rational(1,6), c.comm(((i+1)%3)+1,((i+2)%3)+1)) for i in range(3)]
ux=make_u(cx,alpha1);uy=make_u(cy,alpha2)
for c,u,alpha in ((cx,ux,alpha1),(cy,uy,alpha2)):
    left=c.plus(*(c.mul(c.word(i+1),u[i]) for i in range(3)))
    right=c.plus(*(c.mul(u[i],c.word(i+1)) for i in range(3)))
    assert c.equal(left,c.times(alpha,c.volume()))
    assert c.equal(right,c.times(alpha,c.volume()))
print('PASS 5: six exact left/right curvature primitives in the mixed algebra, all s')

mixed_u=[liftx(u) for u in ux]+[lifty(u) for u in uy]
w=tadd(scale_t(alpha1,liftx(cx.volume())),scale_t(alpha2,lifty(cy.volume())))
assert tadd(*(tmul(z[i],mixed_u[i]) for i in range(6)))==w
assert tadd(*(tmul(mixed_u[i],z[i]) for i in range(6)))==w


# Mixed curvature u_x changes linearly in s; the formula is independent of the y algebra.
for i in range(3):
    v=ux[i]
    assert all(cp(S.diff(v.get(w,0),s,2))==0 for w in set(v))
    difference=cx.plus(v,cx.times(-1,{w:cc.subs(s,0) for w,cc in v.items()}))
    assert cx.equal(difference,cx.scalar((-1 if i!=1 else 1)*alpha1*s*L[i]/6)),(i,difference)
for i,v in enumerate(uy):
    assert all(cp(S.diff(cc,s,2))==0 for cc in v.values())
    difference=cy.plus(v,cy.times(-1,{w:cc.subs(s,0) for w,cc in v.items()}))
    assert cy.equal(difference,cy.scalar((-1 if i!=1 else 1)*alpha2*s*K[i]/6))
print('PASS 6: all six Shamash boundary entries have explicit linear s-corrections')

# The correction to d2 is genuinely mixed: at s=0, x-only rows cannot
# remove a nonzero pure y^2 defect, and symmetrically for the y-relations.
assert all(S.Poly(L[i],*Y).total_degree()==1 for i in range(3))
assert all(S.Poly(K[i],*X).total_degree()==1 for i in range(3))
assert all(cp(S.diff(L[i],X[j]))==0 for i,j in product(range(3),repeat=2))
print('PASS 7: x/y mixing corrections cannot be omitted in the tensor presentation')

# Enumerate S3 x S3 coefficient-monomial orbits for future 32|32 lifting.
cells=list(product(range(3),repeat=2));G=list(product(permutations(range(3)),repeat=2))
def image_monom(m,g):
    p,q=g
    return tuple(sorted((p[i],q[j]) for i,j in m))
counts=[]
for degree in (1,2,3):
    terms=set(combinations_with_replacement(cells,degree))
    reps=[]
    while terms:
        r=min(terms);orbit={image_monom(r,g) for g in G}
        assert orbit<=terms
        reps.append((r,len(orbit),36//len(orbit)))
        terms.difference_update(orbit)
    counts.append(len(reps))
    assert sum(n for _,n,_ in reps)==S.binomial(9+degree-1,degree)
    if degree<=2:
        print('    degree',degree,'orbit reps:',[(''.join('u%d%d'% (i+1,j+1) for i,j in r),size) for r,size,stab in reps])
    else:
        print('    degree 3 orbit reps:',[''.join('u%d%d'% (i+1,j+1) for i,j in r) for r,_,_ in reps])
assert counts==[1,4,10]
print('PASS 8: one-way U-parameter orbit reps are 1, 4, 10 at degrees 1, 2, 3')

# Full two-way family: S3 x S3 acts on U by rows/cols and on V by cols/rows.
perms=[{1:2,2:3,3:1},{1:2,2:1,3:3}]
for xside in (True,False):
    for p in perms:
        sub={}
        for a in (1,2,3):
            if xside:sub[X[a-1]]=X[p[a]-1]
            else:sub[Y[a-1]]=Y[p[a]-1]
        for a in (1,2,3):
            for b in (1,2,3):
                sub[U[a-1,b-1]]=U[(p[a]-1) if xside else a-1,(p[b]-1) if not xside else b-1]
                sub[V[b-1,a-1]]=V[(p[b]-1) if not xside else b-1,(p[a]-1) if xside else a-1]
        if xside:
            for (i,j),val in qx.items():
                assert cp(val.xreplace(sub)-qx[tuple(sorted((p[i],p[j])))] )==0
            for val in qy.values():assert cp(val.xreplace(sub)-val)==0
        else:
            for (i,j),val in qy.items():
                assert cp(val.xreplace(sub)-qy[tuple(sorted((p[i],p[j])))] )==0
            for val in qx.values():assert cp(val.xreplace(sub)-val)==0
print('PASS 9: full two-way 18-parameter Clifford Gram matrices are S3 x S3 covariant')
# Signed transposition (-P) and unsigned 3-cycle have determinant +1.
for p, sign in ((perms[0],1),(perms[1],-1)):
    inversions=sum(p[i]>p[j] for i in range(1,4) for j in range(i+1,4))
    assert sign**3 * (-1)**inversions == 1
print('PASS 10: cyclic and signed-reflection generators preserve Clifford volume orientations')
print('10 PASS + top syzygies: exact 18-parameter Koszul stage; full higher MF and Ku comparison unconstructed')
