#!/usr/bin/env python3
"""Exact Clifford Hesse 2-isogeny and its marked 3-torsion action.

Polynomial identities only; Picard pullback and Ku comparison are not
formalized here. Run: python3 computations/verify_clifford_hesse_two_isogeny.py
"""
import sympy as S

q,Z0,Z1,Z2,x,y,X,Y=S.symbols("q Z0 Z1 Z2 x y X Y")
qd=-2/q
def f(t,z):
    return t*sum(v**3 for v in z)-(t**3+2)*S.prod(z)
D=(1-q**3/S.Integer(4))*Z0*Z1*Z2-q**2/S.Integer(4)*sum(z**3 for z in (Z0,Z1,Z2))
assert S.factor(D-q**3/S.Integer(8)*f(qd,(Z0,Z1,Z2)))==0
assert S.cancel(-2/qd-q)==0
print("PASS 1: center discriminant equals (q^3/8) f_{-2/q}")

Q=q**3+2;Delta=(q**3-1)**2*(q**3+8)
ell=3*q*(Z0+Z1)+Q*Z2
v=Z0-Z1
ident=27*q**2*ell*v**2+ell**3-6*Q*ell**2*Z2+9*Q**2*ell*Z2**2-4*Delta*Z2**3
assert S.factor(ident-108*q**2*f(q,(Z0,Z1,Z2)))==0
print("PASS 2: homogeneous tangent-chart cubic identity")

alpha=4*Delta/(27*q**2); xp=1/(q**3+8)
a=lambda t:(t**6-20*t**3-8)/(9*t**2)
b=lambda t:-16*(t**3-1)**3/(81*t**4)
P=(-1+6*Q*x-9*Q**2*x**2+4*Delta*x**3)/(27*q**2)
wx=alpha*(x-xp)
assert S.factor(alpha**2*P-(wx**3+a(q)*wx**2+b(q)*wx))==0
assert S.factor(wx.subs(x,xp))==0
print("PASS 3: Weierstrass model and p=(0,0)")

assert S.factor(q**2*a(qd)+2*a(q))==0
assert S.factor(q**4*b(qd)-(a(q)**2-4*b(q)))==0
print("PASS 4: quotient coefficients match the dual Hesse parameter")

Ub=(X+a(q)+b(q)/X)/q**2
Vb=Y*(1-b(q)/X**2)/q**3
source=Y**2-X**3-a(q)*X**2-b(q)*X
target=Vb**2-Ub**3-a(qd)*Ub**2-b(qd)*Ub
assert S.factor(target-(1-b(q)/X**2)**2*source/q**6)==0
assert S.factor(S.diff(Ub,X)/(Vb/Y)-q)==0
assert S.factor(q*qd+2)==0
print("PASS 5: degree-2 quotient, differential factor q and dual factor -2")

def jhesse(t):
    m=(t**3+2)**3/(27*t**3)
    return S.factor(27*m*(m+8)**3/(m-1)**3)
jE=S.factor(jhesse(q).subs(q,2))
jC=S.factor(jhesse(qd).subs(q,2))
assert jE==S.Rational(4956477625,941192)
assert jC==S.Rational(9938375,21952) and jE!=jC
print("PASS 6: point and center Hesse curves are generically not isomorphic")

J,K=S.symbols("J K")
Phi=J**3+K**3-J**2*K**2+1488*J*K*(J+K)-162000*(J**2+K**2)
Phi+=40773375*J*K+8748000000*(J+K)-157464000000000
assert S.factor(Phi.subs({J:jhesse(q),K:jhesse(qd)}))==0
print("PASS 7: classical Phi_2 modular equation")

zeta=(-1+S.sqrt(-3))/2
def marked_map(z):
    z0,z1,z2=z
    le=3*q*(z0+z1)+(q**3+2)*z2
    xx=z2/le
    yy=(z0-z1)/le
    U=S.factor(alpha*(xx-xp))
    V=S.factor(alpha*yy)
    Uv=S.factor((U+a(q)+b(q)/U)/q**2)
    Vv=S.factor(V*(1-b(q)/U**2)/q**3)
    av=4*(qd**3-1)**2*(qd**3+8)/(27*qd**2)
    rv=1/(qd**3+8)
    xv=S.factor(Uv/av+rv)
    yv=S.factor(Vv/av)
    uv=S.factor((1-(qd**3+2)*xv)/(3*qd))
    return (S.factor((uv+yv)/2),S.factor((uv-yv)/2),xv)
Pt=marked_map((0,1,-1))
assert S.factor(Pt[0])==0 and S.factor(Pt[1]+Pt[2])==0
Qt=marked_map((1,-zeta,0))
assert S.simplify(Qt[2])==0 and S.simplify(Qt[1]+zeta**2*Qt[0])==0
print("PASS 8: level-three P -> P, Q -> -Q, anti-symplectic")
print("8 PASS: no high-order Ku comparison or beta/gamma verified.")
