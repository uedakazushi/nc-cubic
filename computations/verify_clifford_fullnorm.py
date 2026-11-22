#!/usr/bin/env python3
"""Exact algebra certificates for the full rank-one Clifford central norm discriminant.

No categorical Morita equivalence, completeness of residual dg smoothness locus,
or formal deformation theorem is checked by this script.
"""
import sympy as S

X,Y,l,m,t,u,A,B,x2,x3,y2,y3=S.symbols('X Y l m t u A B x2 x3 y2 y3')
qx=S.Matrix([[X,-t*x3/2,-t*x2/2],
             [-t*x3/2,x2,(l*Y-t*X)/2],
             [-t*x2/2,(l*Y-t*X)/2,x3]])
qy=S.Matrix([[Y,-u*y3/2,-u*y2/2],
             [-u*y3/2,y2,(m*X-u*Y)/2],
             [-u*y2/2,(m*X-u*Y)/2,y3]])
N=S.expand(4*(-A*qx.det()+B*qy.det()))
P=A*X*(l*Y-t*X)**2-B*Y*(m*X-u*Y)**2
kx=((4-t**3)*X+t**2*l*Y)/(3*t**2)
ky=((4-u**3)*Y+u**2*m*X)/(3*u**2)
expected=S.expand(P+A*t**2*(x2**3+x3**3-3*kx*x2*x3)
                  -B*u**2*(y2**3+y3**3-3*ky*y2*y3))
assert S.simplify(N-expected)==0
print('PASS 1: six-variable Clifford norm reduction')

for v1,v2,k in [(x2,x3,kx),(y2,y3,ky)]:
    assert S.simplify(S.diff(N,v1).subs({v1:k,v2:k}))==0
    assert S.simplify(S.diff(N,v2).subs({v1:k,v2:k}))==0
    assert S.simplify(S.diff(N,v1).subs({v1:0,v2:0}))==0
    assert S.simplify(S.diff(N,v2).subs({v1:0,v2:0}))==0
print('PASS 2: critical branches in both transverse pairs')

F={}
for i in (0,1):
    for j in (0,1):
        F[i,j]=S.expand(P-i*A*t**2*kx**3+j*B*u**2*ky**3)
        subs={x2:i*kx,x3:i*kx,y2:j*ky,y3:j*ky}
        assert S.simplify(N.subs(subs)-F[i,j])==0
        assert S.simplify(S.diff(N,X).subs(subs)-S.diff(F[i,j],X))==0
        assert S.simplify(S.diff(N,Y).subs(subs)-S.diff(F[i,j],Y))==0
print('PASS 3: four reduced binary cubics and envelope derivatives')

sub={t:2,u:2,A:1,B:1}
D={idx:S.factor(S.discriminant(f.subs(sub).subs(Y,1),X))
   for idx,f in F.items()}
assert len(D)==4
assert all(S.factor(D[k].subs({l:0,m:0}))!=0 for k in D)
assert S.factor(D[0,0]-(l*m-4)**2*
                (8*l**3+l**2*m**2+72*l*m+8*m**3-432))==0
print('PASS 4: all four binary-cubic discriminants; smooth separated fiber')

G01=16*l**4*m-56*l**3+157*l**2*m**2-1456*l*m+16*m**3+3136
assert S.factor(D[0,1]+(l*m-8)**2*G01/27)==0
print('PASS 5: explicit non-axis discriminant component')

# Exact ordinary node over Q[m]/(m^3+196), with a_1=a_2=1
# (hence A=B=196): divide the norm by the common factor 196.
r=S.Rational(28,13)/m
coord={l:0,t:2,u:2,A:1,B:1,Y:1,X:r,
       x2:0,x3:0,y2:S.Rational(5,13),y3:S.Rational(5,13)}
variables=[X,x2,x3,y2,y3]
def zero_mod(f):
    num,den=S.fraction(S.cancel(f))
    assert S.rem(den,m**3+196,m)!=0
    return S.rem(num,m**3+196,m)==0
assert zero_mod(N.subs(coord))
for z in variables:
    assert zero_mod(S.diff(N,z).subs(coord))
assert zero_mod((qx.det()-qy.det()).subs(coord))
assert not zero_mod(qx.det().subs(coord))
assert not zero_mod(qy.det().subs(coord))
assert S.rem((8*m**3-432),m**3+196,m)==-2000
H=S.hessian(N.subs({l:0,t:2,u:2,A:1,B:1,Y:1}),variables)
Hdet=S.factor(H.det().subs(coord))
assert zero_mod(Hdet-S.Rational(12902400,2197))
assert not zero_mod(Hdet)
print('PASS 6: off-axis Azumaya ordinary node, h=49, Q != 0')
