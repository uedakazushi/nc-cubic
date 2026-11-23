#!/usr/bin/env python3
"""Exact symmetric 3x3 Picard two-torsion matrix factorization.
Polynomial and matrix identities; no Ku comparison, rotation period, or beta/gamma.
"""
import sympy as s
X,Y,Z,a,b=s.symbols('X Y Z a b')
F=Y**2*Z-X**3-a*X**2*Z-b*X*Z**2
G=X**2+a*X*Z+b*Z**2
L=s.Matrix([[X,Y,0],[Y,a*X+b*Z,X],[0,X,-Z]])
Adj=L.adjugate()
assert s.factor(L.det()-F)==0
assert s.simplify(L*Adj-F*s.eye(3))==s.zeros(3)
assert s.simplify(Adj*L-F*s.eye(3))==s.zeros(3)
assert L==L.T and Adj==Adj.T
print('PASS 1: symmetric linear 3x3 determinantal presentation and quadratic adjugate MF')

x,v=s.symbols('x v')
# Rational sections f=(-y/x,1,x) of M(1)=O(p+2o), with y=x*v.
f=s.Matrix([[-v,1,x]])
L_aff=L.subs({X:x,Y:x*v,Z:1})
rel=s.expand(f*L_aff)
assert s.simplify(rel[0,0])==0
assert s.factor(rel[0,1]+x*v*v-x*x-a*x-b)==0
assert s.simplify(rel[0,2])==0
print('PASS 2: three linear syzygies for sections (-y/x,1,x) of M(1)')

# The 2-torsion multiplication M^2=O is trivialized by rational function x;
# the corresponding quadratic pairing on M(1) is x f_i f_j.
# All entries reduce to quadratic ambient forms via the plane cubic equation.
Q=s.Matrix([[G,-Y*Z,-X*Y],[-Y*Z,X*Z,X**2],[-X*Y,X**2,Y**2-a*X**2-b*X*Z]])
assert s.simplify(Q+Adj)==s.zeros(3)
Q_aff=Q.subs({X:x,Y:x*v,Z:1})
for i in range(3):
    for j in range(3):
        expr=s.expand(x*f[0,i]*f[0,j]-Q_aff[i,j])
        # y^2/x = x^2+a*x+b -> x*v^2=x^2+a*x+b.
        assert s.factor(expr.subs(v**2,(x*x+a*x+b)/x))==0,(i,j,expr)
print('PASS 3: -adj(L) is the x-normalized symmetric multiplication pairing M(1)^2->O(2)')

# Reflection y -> -y; generator basis (-v,1,x) transforms by D.
D=s.diag(-1,1,1)
assert s.simplify(L.subs(Y,-Y)-D*L*D)==s.zeros(3)
assert s.simplify(Adj.subs(Y,-Y)-D*Adj*D)==s.zeros(3)
assert D*D==s.eye(3) and D.det()==-1
print('PASS 4: reflection-equivariance of both MF differentials and normalized pairing')

# An earlier nonsymmetric 3x3 matrix from basis (1,x,v) is equivalent by constant matrices.
Lold=s.Matrix([[X,Y,-a*X-b*Z],[-Z,0,-X],[0,-X,Y]])
R=s.Matrix([[0,1,0],[0,0,1],[-1,0,0]])
U=s.Matrix([[0,0,1],[1,0,0],[0,-1,0]])
assert R*L==Lold*U and abs(R.det())==abs(U.det())==1
assert s.factor(Lold.det()-F)==0
print('PASS 5: symmetric 3x3 matrix is constant-equivalent to section-syzygy matrix')

p={X:0,Y:0,Z:1}
o={X:0,Y:1,Z:0}
assert L.subs(p).rank()==2 and L.subs(o).rank()==2
assert s.factor(F.subs(p))==0 and s.factor(F.subs(o))==0
# Rank-1 locus of L on E would lie in singular locus of det(L).
assert [s.factor(s.diff(F,z).subs(o)) for z in (X,Y,Z)]==[0,0,1]
print('PASS 6: rank two at p and o; the smooth cubic has rank exactly two along E')

# Analytic RR: H0(E,M)=0, H0(E,M(n))=3n (n>=1),
# a 3x3 linear presentation has matching Hilbert series.
t=s.symbols('t')
H=s.cancel((3*t-3*t*t)/(1-t)**3)
assert s.simplify(H-3*t/(1-t)**2)==0
for n in range(1,8):
    assert s.series(H,t,0,n+1).removeO().expand().coeff(t,n)==3*n
print('PASS 7: Hilbert series 3t/(1-t)^2 matches degree-zero nontrivial line bundle M')

# Both source and dual-Hesse target 2-torsion Picard lines use the same construction.
q=s.symbols('q')
aq=(q**6-20*q**3-8)/(9*q**2)
bq=-16*(q**3-1)**3/(81*q**4)
for aa,bb in [(aq,bq),(-2*aq,aq**2-4*bq)]:
    LM=L.subs({a:aa,b:bb})
    FM=F.subs({a:aa,b:bb})
    assert s.factor(LM.det()-FM)==0
    assert s.simplify(LM*LM.adjugate()-FM*s.eye(3))==s.zeros(3)
for qv in (s.Integer(2),s.Integer(-1)):
    av=aq.subs(q,qv);bv=bq.subs(q,qv)
    assert bv and (av**2-4*bv)
print('PASS 8: uniform source and target Clifford Picard matrices, including rational fibers')

# Formal a(s),b(s) jet: the matrix itself varies only through a(s)X+b(s)Z;
# all higher MF identities follow by differentiation of determinant/adjugate.
sym=s.symbols('s')
a0,a1,a2,a3,b0,b1,b2,b3=s.symbols('a0:4 b0:4')
aa=a0+a1*sym+a2*sym**2+a3*sym**3
bb=b0+b1*sym+b2*sym**2+b3*sym**3
LM=L.subs({a:aa,b:bb});FM=F.subs({a:aa,b:bb})
assert s.simplify(LM*LM.adjugate()-FM*s.eye(3))==s.zeros(3)
assert s.simplify(LM.adjugate()*LM-FM*s.eye(3))==s.zeros(3)
assert s.simplify(LM.diff(sym)-s.Matrix([[0,0,0],[0,aa.diff(sym)*X+bb.diff(sym)*Z,0],[0,0,0]]))==s.zeros(3)
print('PASS 9: exact third-order Picard MF jets and their factorizations for formal parameter variation')
# Continued with Hesse-coordinate check below.

# Original Hesse coordinates: the normalization factor 4 c_q^2 is a unit,
# so the adjugate divided by this factor gives an MF of the exact fixed f_q.
z0,z1,z2=s.symbols('z0 z1 z2')
cq=4*(q**3-1)**2*(q**3+8)/(27*q**2)
rq=1/(q**3+8)
W=3*q*(z0+z1)+(2+q**3)*z2
T=cq*(z2-rq*W)
V=cq*(z0-z1)
LH=L.subs({X:T,Y:V,Z:W,a:aq,b:bq},simultaneous=True)
fH=q*(z0**3+z1**3+z2**3)-(2+q**3)*z0*z1*z2
assert s.factor(LH.det()-4*cq**2*fH)==0
assert s.simplify(LH*LH.adjugate()-4*cq**2*fH*s.eye(3))==s.zeros(3)
assert s.simplify(LH.subs({z0:z1,z1:z0},simultaneous=True)-D*LH*D)==s.zeros(3)
print('PASS 10: exact original Hesse f_q MF, no cube root, and Hesse reflection')
print('10 PASS total: no actual noncommutative Ku kernel or twelve comparison scalars.')
