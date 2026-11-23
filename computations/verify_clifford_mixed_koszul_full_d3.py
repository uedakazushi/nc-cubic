#!/usr/bin/env python3
"""All 20 degree-three quadratic Koszul syzygies of two-way mixed Clifford.

Exact polynomial/rational-function certificate in the FREE tensor algebra,
not merely after taking the quotient.  Parameters tau1,tau2,s,U9,V9
remain algebraically independent, with 1-tau_i**3 invertible.

The script certifies cubic tensor identities, triangular 20x20 unit projection,
and s-degree bounds.  The global-basis proof additionally uses the
published free degree-three Hilbert component of the mixed PBW family.
It does not construct d4..d6, Shamash higher maps or Ku comparison.
"""
from itertools import product
import sympy as S

s, tau1, tau2 = S.symbols('s tau1 tau2')
U=S.Matrix(3,3,S.symbols('u11 u12 u13 u21 u22 u23 u31 u32 u33'))
V=S.Matrix(3,3,S.symbols('v11 v12 v13 v21 v22 v23 v31 v32 v33'))
D1,D2=1-tau1**3,1-tau2**3

def normalize(v):
    return S.cancel(v)
def clean(dic):
    return {w:normalize(c) for w,c in dic.items() if normalize(c)!=0}
def plus(*elems):
    ret={}
    for obj in elems:
        for word,coeff in obj.items():ret[word]=ret.get(word,0)+coeff
    return clean(ret)
def scale(q,obj):
    return clean({w:q*c for w,c in obj.items()})
def mul(a,b):
    result={}
    for wa,ca in a.items():
        for wb,cb in b.items():
            word=wa+wb
            result[word]=result.get(word,0)+ca*cb
    return clean(result)
def comm(a,b):return plus(mul(a,b),scale(-1,mul(b,a)))

def gen(n):return {(n,):S.S.One}
x=lambda i:gen(i)
y=lambda j:gen(3+j)
zero={}

def other(i,j):return next(k for k in range(3) if k!=i and k!=j)

def sprod(z):return mul(z,z)
rx=[];ry=[];cross={}
for a in range(3):
    j,k=(a+1)%3,(a+2)%3
    rx.append(plus(mul(x(j),x(k)),mul(x(k),x(j)),scale(tau1,sprod(x(a))),
                   *(scale(-s*U[a,c],sprod(y(c))) for c in range(3))))
    ry.append(plus(mul(y(j),y(k)),mul(y(k),y(j)),scale(tau2,sprod(y(a))),
                   *(scale(-s*V[a,c],sprod(x(c))) for c in range(3))))
for a,b in product(range(3),repeat=2):cross[(a,b)]=comm(x(a),y(b))

REL={('rx',a):rx[a] for a in range(3)}
REL.update({('ry',b):ry[b] for b in range(3)})
REL.update({('c',a,b):cross[a,b] for a,b in product(range(3),repeat=2)})
assert len(REL)==15

def Ax(i,a):
    return scale(tau1,x(a)) if i==a else x(other(i,a))
def By(j,b):
    return scale(tau2,y(b)) if j==b else y(other(j,b))

def triple(i,j,tau):
    """The 3 terms in (1-tau**3)[z_i**2,z_j], i!=j.

    Return (generator-index, relation-index, coefficient).
    """
    assert i!=j
    k=other(i,j)
    return ((i,k,S.S.One),(k,j,tau),(j,i,tau**2))

def insert(dic,key,val):
    dic[key]=plus(dic.get(key,zero),val)

def col_topx():
    out={}
    for a in range(3):insert(out,('rx',a),x(a))
    for a,b in product(range(3),repeat=2):
        insert(out,('c',a,b),scale(-s*U[a,b],y(b)))
    return out

def col_topy():
    out={}
    for b in range(3):insert(out,('ry',b),y(b))
    for b,a in product(range(3),repeat=2):
        insert(out,('c',a,b),scale(s*V[b,a],x(a)))
    return out

def col_xxy(a,b):
    """Right coefficients in R_2 tensor generators (xrel a, y index b)."""
    out={('rx',a):y(b)}
    for i in range(3):insert(out,('c',i,b),scale(-1,Ax(i,a)))
    for c in range(3):
        if c==b:continue
        for j,l,lam in triple(c,b,tau2):
            insert(out,('ry',l),scale(-s*U[a,c]*lam/D2,y(j)))
            for i in range(3):
                insert(out,('c',i,j),scale(-s**2*U[a,c]*lam*V[l,i]/D2,x(i)))
    return out

def col_xyy(b,a):
    out={('ry',b):x(a)}
    for j in range(3):insert(out,('c',a,j),By(j,b))
    for d in range(3):
        if d==a:continue
        for j,l,lam in triple(d,a,tau1):
            insert(out,('rx',l),scale(-s*V[b,d]*lam/D1,x(j)))
            for e in range(3):
                insert(out,('c',j,e),scale(s**2*V[b,d]*lam*U[l,e]/D1,y(e)))
    return out

def rhs(column):
    return plus(*(mul(REL[key],linear_form) for key,linear_form in column.items()))

def lhs_topx():
    return plus(*(mul(x(a),rx[a]) for a in range(3)),
                *(scale(s*U[a,b],mul(y(b),cross[a,b])) for a,b in product(range(3),repeat=2)))
def lhs_topy():
    return plus(*(mul(y(b),ry[b]) for b in range(3)),
                *(scale(-s*V[b,a],mul(x(a),cross[a,b])) for b,a in product(range(3),repeat=2)))
def lhs_xxy(a,b):
    out=plus(mul(y(b),rx[a]),*(mul(Ax(i,a),cross[i,b]) for i in range(3)))
    for c in range(3):
        if c==b:continue
        for j,l,lam in triple(c,b,tau2):
            out=plus(out,scale(-s*U[a,c]*lam/D2,mul(y(j),ry[l])),
                     *(scale(s**2*U[a,c]*lam*V[l,i]/D2,mul(x(i),cross[i,j])) for i in range(3)))
    return out

def lhs_xyy(b,a):
    out=plus(mul(x(a),ry[b]),*(scale(-1,mul(By(j,b),cross[a,j])) for j in range(3)))
    for d in range(3):
        if d==a:continue
        for j,l,lam in triple(d,a,tau1):
            out=plus(out,scale(-s*V[b,d]*lam/D1,mul(x(j),rx[l])),
                     *(scale(-s**2*V[b,d]*lam*U[l,e]/D1,mul(y(e),cross[j,e])) for e in range(3)))
    return out

def verify(what,left,right):
    diff=plus(left,scale(-1,right))
    assert not diff,(what,diff)

# Underlying central-square commutator, with *undeformed* one-factor relations.
# This exact identity is the source of the correction denominator D_i.
for c,b in product(range(3),repeat=2):
    if c==b:continue
    undery=lambda j:plus(ry[j],*(scale(s*V[j,i],sprod(x(i))) for i in range(3)))
    underx=lambda i:plus(rx[i],*(scale(s*U[i,j],sprod(y(j))) for j in range(3)))
    cy=plus(*(scale(lam,comm(y(j),undery(l))) for j,l,lam in triple(c,b,tau2)))
    cx=plus(*(scale(lam,comm(x(j),underx(l))) for j,l,lam in triple(c,b,tau1)))
    verify('y-central-square',cy,scale(D2,comm(sprod(y(c)),y(b))))
    verify('x-central-square',cx,scale(D1,comm(sprod(x(c)),x(b))))
print('PASS 1: both cyclic central-square commutator identities, exact in the free tensor algebra')

cols=[('topx',col_topx(),lhs_topx()),('topy',col_topy(),lhs_topy())]
cols.extend((('xxy',a,b),col_xxy(a,b),lhs_xxy(a,b)) for a,b in product(range(3),repeat=2))
cols.extend((('xyy',b,a),col_xyy(b,a),lhs_xyy(b,a)) for b,a in product(range(3),repeat=2))
assert len(cols)==20
for label,parts,left in cols[:2]:verify(label,left,rhs(parts))
print('PASS 2: the two existing top Koszul cubic syzygies at all 18 parameters')
for label,parts,left in cols[2:11]:verify(label,left,rhs(parts))
print('PASS 3: all nine xxy cubic syzygies; terms of order s^2 U V included')
for label,parts,left in cols[11:]:verify(label,left,rhs(parts))
print('PASS 4: all nine xyy cubic syzygies; terms of order s^2 V U included')

# 20 distinguished coordinate functionals on the R_2 tensor V side.
functionals=[(('rx',0),0),(('ry',0),3)]
functionals.extend((('rx',a),3+b) for a,b in product(range(3),repeat=2))
functionals.extend((('ry',b),a) for b,a in product(range(3),repeat=2))
assert len(functionals)==20
for j,(label,column,left) in enumerate(cols):
    for i,(relation,generator) in enumerate(functionals):
        val=column.get(relation,{}).get((generator,),0)
        assert S.cancel(val-(1 if i==j else 0))==0,(i,j,label,relation,generator,val)
print('PASS 5: the distinguished 20x20 coefficient minor is exactly the identity over all parameters')

# Separately check that every coefficient belongs to the degree-one generator span,
# and the first, second order coefficients have precisely the expected mixed types.
deg_counts={0:0,1:0,2:0}
for label,col,left in cols:
    for form in col.values():
        for word,val in form.items():
            assert len(word)==1
            degree=S.Poly(S.cancel(val),s).degree()
            assert degree<=2,(label,word,val)
            deg_counts[degree]+=1
assert deg_counts[2]>0
print('PASS 6: all twenty d3 columns are linear in generators and polynomial of s-degree <=2')

# No terms of second order on the one-way locus V=0; the reverse direction too.
for label,col,left in cols:
    for form in col.values():
        for val in form.values():
            assert not S.cancel(S.diff(val,s,2)).subs({v:0 for v in list(V)})
            assert not S.cancel(S.diff(val,s,2)).subs({u:0 for u in list(U)})
print('PASS 7: d3 is exactly affine in s on either one-way nine-variable locus')

# Generic second-order correction is truly nonzero (not removable by the
# specified fixed 20-coordinate normalization).
quad=col_xxy(0,0)[('c',0,1)][(0,)]
quad2=S.expand(S.cancel(S.diff(quad,s,2)/2))
assert S.cancel(quad2+(U[0,1]*V[2,0]+tau2*U[0,2]*V[0,0])/D2)==0,quad2
print('PASS 8: concrete s^2 U V coefficient is nonzero for generic bidirectional mixing')

# The normal-form PBW theorem supplies a free degree-three algebra component
# of rank 56.  Thus the cubic quadratic-syzygy module is projective rank
# 2*(6*15)-(216-56)=20, and the explicit left inverse proves global freeness.
assert 6**3==216 and 6*15==90 and 2*90-(216-56)==20
assert S.binomial(8,3)==56
print('PASS 9: projective-rank arithmetic 180-(216-56)=20; basis proof also uses PBW freeness')
print('9 PASS: all 20 cubic Koszul columns over full 18-parameter base; d4--d6 and Ku still open.')
