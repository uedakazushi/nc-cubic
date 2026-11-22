#!/usr/bin/env python3
"""Exact coefficient certificates for the rank-one Clifford residual caustic.

This verifies polynomial identities and Hessians, not categorical saturation,
Morita equivalences or global discriminant completeness.
Requires SymPy.
"""
import sympy as s

X,Y,t,u,L,M,A,B=s.symbols("X Y t u lambda mu A B")
x2,x3,y2,y3=s.symbols("x2 x3 y2 y3")
P=s.expand(A*X*(L*Y-t*X)**2-B*Y*(M*X-u*Y)**2)
Q=4*A**2*t*L**3+A*B*L**2*M**2+18*A*B*t*u*L*M-27*A*B*t**2*u**2+4*B**2*u*M**3
assert s.factor(s.discriminant(P.subs(Y,1),X)-A*B*(L*M-t*u)**2*Q)==0
print("PASS binary discriminant")

qx=s.Matrix([[X,-t*x3/2,-t*x2/2],[-t*x3/2,x2,(L*Y-t*X)/2],[-t*x2/2,(L*Y-t*X)/2,x3]])
qy=s.Matrix([[Y,-u*y3/2,-u*y2/2],[-u*y3/2,y2,(M*X-u*Y)/2],[-u*y2/2,(M*X-u*Y)/2,y3]])
N=-A*qx.det()+B*qy.det()
at0={x2:0,x3:0,y2:0,y3:0}
assert s.factor(4*N.subs(at0)-P)==0
assert all(s.simplify(s.diff(N,v).subs(at0))==0 for v in at0)
print("PASS axis restriction and criticality")

Cx=X+t*t*(L*Y-t*X)/4
Cy=Y+u*u*(M*X-u*Y)/4
assert s.simplify(s.diff(N,x2,x3)+A*Cx)==0
assert s.simplify(s.diff(N,y2,y3)-B*Cy)==0
print("PASS transverse Hessian coefficients")

v={A:1,B:1,t:2,u:2,L:s.Rational(15,2),M:-6,Y:1}
r=s.Rational(1,4)
assert s.factor(P.subs(v))==(X-16)*(4*X-1)**2/4
assert s.simplify(Q.subs(v))==0
assert s.simplify((L*M-t*u).subs(v))!=0
h=(1-t**3)*(1-u**3)-t**2*u**2*L*M
assert h.subs(v)==769
assert qx.det().subs({**v,X:r,**at0})==-s.Rational(49,16)
assert qy.det().subs({**v,X:r,**at0})==-s.Rational(49,16)
H=s.hessian(4*N.subs(v),[X,x2,x3,y2,y3])
assert s.simplify(H.det().subs({X:r,**at0}))==-10596600
print("PASS rational A1 witness and full Hessian")

w={A:1,B:1,t:2,u:2,L:-6,M:-6,Y:1}
assert s.factor(P.subs(w))==4*(X-1)**3
print("PASS previous A2 triple-root specialization")

z,l,m=s.symbols("z l m",nonzero=True)
q=l**2*m**2+4*(l**3+m**3)+18*l*m-27
lp=-z**2-2/z
mp=-2*z-1/z**2
assert s.factor(q.subs({l:lp,m:mp}))==0
assert s.factor((X*(l-X)**2-(m*X-1)**2).subs({l:lp,m:mp})-(X-z**2)**2*(X*z**4-1)/z**4)==0
assert s.simplify(s.diff(lp,z)+2*(z**3-1)/z**2)==0
assert s.simplify(s.diff(mp,z)+2*(z**3-1)/z**3)==0
assert s.simplify(l*s.diff(q,l)-m*s.diff(q,m)-12*(l**3-m**3))==0
subs=s.subresultants(z**3+l*z+2,m*z**2-2*l*z-3,z)
assert s.expand(subs[-1]-q)==0
assert s.expand(subs[-2]-((4*l**2+l*m**2+3*m)*z+6*l+2*m**2))==0
print("PASS tricuspidal rational quartic and birational inverse")
