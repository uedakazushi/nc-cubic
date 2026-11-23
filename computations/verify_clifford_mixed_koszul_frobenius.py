#!/usr/bin/env python3
"""Exact one-fiber finite Frobenius construction of mixed Clifford d4,d5,d6.

Specialization tau1=tau2=2, U_11=V_11=1, others zero, s=1.
Uses Gorenstein socle of the commutative dual complete intersection D,
with the Z/2 x Z/2 cocycle to recover E=B^!, and globally canonical
squarefree bases in degrees 2,3. Exact rational arithmetic only.
"""
import sympy as S
from functools import lru_cache
from itertools import combinations

# Requires sibling verifier, which checks all 20 universal d3 columns.
import verify_clifford_mixed_koszul_full_d3 as src

u=S.symbols('u1:4');v=S.symbols('v1:4');z=(*u,*v)
G=[u[0]**2-2*u[1]*u[2]+v[1]*v[2],
   u[1]**2-2*u[0]*u[2],u[2]**2-2*u[0]*u[1],
   v[0]**2-2*v[1]*v[2]+u[1]*u[2],
   v[1]**2-2*v[0]*v[2],v[2]**2-2*v[0]*v[1]]
gb=S.groebner(G,*z,order='grevlex',domain=S.QQ)

@lru_cache(None)
def rem_monom(exp):
    p=S.prod(z[j]**exp[j] for j in range(6))
    return S.expand(gb.reduce(p)[1])
def monom_exp(expr):
    p=S.Poly(expr,*z)
    assert len(p.terms())==1
    return p.monoms()[0]
def rem(p):
    poly=S.Poly(p,*z)
    result=0
    for exp,c in poly.terms():result+=c*rem_monom(exp)
    return S.expand(result)
def coeff_poly(p,mons):
    pp=S.Poly(p,*z)
    return [pp.coeff_monomial(m) for m in mons]
def standard_matrix(bs):
    reps=[rem(expr) for expr in bs]
    monoms=sorted(set().union(*(S.Poly(p,*z).monoms() for p in reps)))
    mm=[S.prod(z[j]**ex[j] for j in range(6)) for ex in monoms]
    mat=S.Matrix([coeff_poly(p,mm) for p in reps]).T
    assert mat.shape==(len(bs),len(bs)) and mat.det()!=0,mat.shape
    return mm,mat

# These 20 cubic dual basis vectors are dual to the 20 distinguished
# R2 ⊗ W coordinate functionals used in the v87 cubic Koszul basis.
e2=[u[1]*u[2],u[2]*u[0],u[0]*u[1],v[1]*v[2],v[2]*v[0],v[0]*v[1]]+[u[a]*v[b] for a in range(3) for b in range(3)]
e3=[u[0]*u[1]*u[2],v[0]*v[1]*v[2]]+[u[(a+1)%3]*u[(a+2)%3]*v[b] for a in range(3) for b in range(3)]+[v[(b+1)%3]*v[(b+2)%3]*u[a] for b in range(3) for a in range(3)]
assert len(e2)==15 and len(e3)==20
mon2,M2=standard_matrix(e2);mon3,M3=standard_matrix(e3)
M2i=M2.inv();M3i=M3.inv()
assert M2.rank()==15 and M3.rank()==20
print('PASS 1: the 15 quadratic and 20 cubic squarefree dual monomials are bases')

A=S.Matrix(6,6,lambda i,j:S.diff(G[i],z[j])/2)
gamma=rem(A.det())
top=u[0]*u[1]*u[2]*v[0]*v[1]*v[2]
assert rem(top)!=0
ratio=S.cancel(gamma/rem(top))
assert ratio==33,ratio
print('PASS 2: normalized socle gamma=det((1/2)dg)=33*u1u2u3v1v2v3')

def coeffs_reduced_expr(exp,mons,inv):
    expr=rem_monom(exp)
    return inv*S.Matrix(coeff_poly(expr,mons))

def star_sign(a,b):return (-1)**(sum(a[3:])*sum(b[:3]))
def star_monom(a,b):
    return star_sign(a,b),tuple(a[i]+b[i] for i in range(6))

def expand_basis_product(x,y,monoms,inv):
    a=monom_exp(x);b=monom_exp(y)
    sign,ex=star_monom(a,b)
    return sign*coeffs_reduced_expr(ex,tuple(monoms),inv)

# Full degree-two multiplication M_jk as coefficients of the 15 chosen E2 monomials.
T={}
for j in range(6):
    for k in range(6):
        T[(j,k)]=expand_basis_product(z[j],z[k],mon2,M2i)
assert all(len(T[j,k])==15 for j in range(6) for k in range(6))
print('PASS 3: all 36 ordered degree-two products reduced in E=B^!')

# d3 coefficient arrays: C_j: K3 -> K2, encoded via E2 ⋆ E1 -> E3 (right Koszul).
C=[]
for j in range(6):
    cj=S.zeros(15,20)
    for r,e in enumerate(e2):
        coord=expand_basis_product(e,z[j],mon3,M3i)
        for nu in range(20):cj[r,nu]=coord[nu]
    C.append(cj)
print('PASS 4: d3 reconstructed exactly from E2*E1 multiplication')
# Compare each of the 20 columns with the published v87 formulas, over
# a sample having BOTH mixing directions nonzero (not just a trivial limit).
sub={src.s:1,src.tau1:2,src.tau2:2}
sub.update({src.U[a,b]:(1 if a==b==0 else 0) for a in range(3) for b in range(3)})
sub.update({src.V[b,a]:(1 if a==b==0 else 0) for a in range(3) for b in range(3)})
sourceRows=[('rx',a) for a in range(3)]+[('ry',b) for b in range(3)]+[('c',a,b) for a in range(3) for b in range(3)]
for nu,(tag,coeffs,_) in enumerate(src.cols):
    for r,relation in enumerate(sourceRows):
        for j in range(6):
            val=coeffs.get(relation,{}).get((j,),0)
            expected=S.cancel(val.subs(sub)) if val!=0 else S.S.Zero
            assert C[j][r,nu]==expected,(tag,relation,j,C[j][r,nu],expected)
print('PASS 4b: all 20 published v87 d3 columns match the dual multiplication exactly')

# trace takes [gamma] to 1, and each degree-six element to its coefficient.
def twisted_trace_prod(p1,p2,p3):
    a=monom_exp(p1);b=monom_exp(p2);c=monom_exp(p3)
    sign1,ex1=star_monom(a,b);sign2,ex2=star_monom(ex1,c)
    return S.cancel(sign1*sign2*rem_monom(ex2)/gamma)

# d4 coefficients D_j: K4≈E2 -> K3; entries are t(e3 ⋆ e1 ⋆ e2) (right Frobenius).
D=[]
for j in range(6):
    dj=S.zeros(20,15)
    for nu,p3 in enumerate(e3):
        for r,p2 in enumerate(e2):dj[nu,r]=twisted_trace_prod(p3,z[j],p2)
    D.append(dj)
print('PASS 5: all 6*20*15 Frobenius trace coefficients of d4 are exact rational numbers')

# d5 coefficients F_j: K5≈E1 -> K4≈E2; entries of right factor z_j ⋆ source z_i.
F=[]
for j in range(6):
    fj=S.zeros(15,6)
    for i in range(6):
        coordinates=expand_basis_product(z[j],z[i],mon2,M2i)
        for r in range(15):fj[r,i]=coordinates[r]
    F.append(fj)
print('PASS 6: all six columns of d5 determined by quadratic dual relations')

# d6 G_j: K6≈E0 -> K5≈E1.
Q=[S.eye(6)[:,j] for j in range(6)]
print('PASS 7: d6 is the augmentation column (x1,x2,x3,y1,y2,y3)^T')

# Direct numerical test of the 15x15 and 6x6 perfect Frobenius pairings.
e4=[S.prod(z[k] for k in idx) for idx in combinations(range(6),4)]
e5=[S.prod(z[k] for k in idx) for idx in combinations(range(6),5)]
_,M4=standard_matrix(e4); _,M5=standard_matrix(e5)
# The trace on two monomials uses the cocycle sign and the socle representative.
def pair_trace(a,b):
    ea=monom_exp(a);eb=monom_exp(b)
    sign,ex=star_monom(ea,eb)
    return S.cancel(sign*rem_monom(ex)/gamma)
P24=S.Matrix([[pair_trace(a,b) for b in e4] for a in e2])
P15=S.Matrix([[pair_trace(a,b) for b in e5] for a in z])
assert P24.det()!=0 and P15.det()!=0
print('PASS 7b: exact nondegenerate Frobenius pairings E2-E4 and E1-E5 (det !=0)')
print('d4 nonzero coefficients:',sum(value!=0 for mat in D for value in mat))


# The B2 quotient has dimension 21 (6 central squares + 3+3 skew pairs + 9 cross pairs).
# Do NOT annihilate the E2 basis: E2=R2^*, whereas the B2 quotient is dual
# to the 21-dimensional quadratic-RELATION space of E, not E2.
# We only use these six symbols as independent placeholders for center values.
cent=S.symbols('X1:4')+S.symbols('Y1:4')
qX={(0,1):-cent[2],(0,2):-cent[1],(1,2):-cent[0]+cent[3]/2}
qY={(0,1):-cent[5],(0,2):-cent[4],(1,2):-cent[3]+cent[0]/2}
B2=[('center',k) for k in range(6)]+[('xpair',i,j) for i,j in combinations(range(3),2)]+[('ypair',i,j) for i,j in combinations(range(3),2)]+[('cross',i,j) for i in range(3) for j in range(3)]
assert len(B2)==21
ix={b:k for k,b in enumerate(B2)}
def expand_B2(j,k):
    out=S.zeros(21,1)
    if j==k:out[ix[('center',j)]]=1
    elif j<3 and k<3:
        if j<k:out[ix[('xpair',j,k)]]=1
        else:
            out[ix[('xpair',k,j)]]=-1
            for centi,c in enumerate(cent):out[centi]=2*S.expand(qX[k,j]).coeff(c)
    elif j>=3 and k>=3:
        if j<k:out[ix[('ypair',j-3,k-3)]]=1
        else:
            out[ix[('ypair',k-3,j-3)]]=-1
            for centi,c in enumerate(cent):out[centi]=2*S.expand(qY[k-3,j-3]).coeff(c)
    else:
        if j<3:out[ix[('cross',j,k-3)]]=1
        else:out[ix[('cross',k,j-3)]]=1
    return out
TB={(j,k):expand_B2(j,k) for j in range(6) for k in range(6)}

def check_complex(left,right,name):
    nrow,nmid=left[0].shape
    assert right[0].rows==nmid
    ncol=right[0].cols
    for ell in range(21):
        total=S.zeros(nrow,ncol)
        for j in range(6):
            for k in range(6):
                q=TB[j,k][ell]
                if q:total+=q*(left[j]*right[k])
        assert total==S.zeros(nrow,ncol),(name,ell,total)
    print('PASS:',name,'all 21 PBW B2 coefficients vanish (full quadratic differential composition)')

check_complex(C,D,'d3*d4=0')
check_complex(D,F,'d4*d5=0')
check_complex(F,Q,'d5*d6=0')
assert D[3][0,3]==S.Rational(1,33)
print('PASS 12: explicit (d4)_{xxx,q_y1} coefficient of y1 is 1/33')
print('12 PASS: exact nonzero two-way Frobenius Koszul d4,d5,d6; source uses earlier d3 verifier (9 PASS).')
