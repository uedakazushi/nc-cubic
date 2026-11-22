#!/usr/bin/env python3
"""Exact finite cubic linear system realizing Clifford-Hesse 2-isogeny.

Polynomial/linear-algebra certificate. Geometric divisor and Picard arguments
are proved separately in the paper. No Ku comparison or 12 scalars computed.
"""
import sympy as s

q=s.symbols('q',nonzero=True)
z=s.symbols('z0 z1 z2')
z0,z1,z2=z
Q=q**3+2
c=4*(q**3-1)**2*(q**3+8)/(27*q**2)
r=1/(q**3+8)
a=(q**6-20*q**3-8)/(9*q**2)
b=-16*(q**3-1)**3/(81*q**4)
W=3*q*(z0+z1)+Q*z2
T=c*(z2-r*W)
S=c*(z0-z1)
f=q*sum(v**3 for v in z)-Q*z0*z1*z2
Fw=W*S**2-T**3-a*W*T**2-b*W**2*T
assert s.factor(Fw-4*c**2*f)==0
J=s.Matrix([[s.diff(t,x) for x in z] for t in (W,T,S)])
assert s.factor(J.det())!=0
print('PASS 1: global linear Weierstrass change and exact plane cubic identity')

# Six cubic ambient monomials; their restrictions are a basis of H^0(E,O(3)(-2o-p)).
sextet=[W**2*T,W**2*S,W*T**2,W*T*S,T**3,T**2*S]
vars=s.symbols('W T S')
w,t,v=vars
base=[w*w*t,w*w*v,w*t*t,w*t*v,t**3,t*t*v]
assert len(set(base))==6 and all(s.Poly(x,*vars).total_degree()==3 for x in base)
assert all(s.Poly(x,*vars).coeff_monomial(w*v**2)==0 for x in base)
assert s.Poly(w*v**2-t**3-a*w*t**2-b*w*w*t,*vars).coeff_monomial(w*v**2)==1
print('PASS 2: six independent degree-three monomial classes modulo E equation')

U,V=s.symbols('U V')
def deck(expr):
    return s.cancel(U**4/b**2*expr.subs({U:b/U,V:-b*V/U**2},simultaneous=True))
source=[U,V,U**2,U*V,U**3,U**2*V]
images=[U**3/b,-U**2*V/b,U**2,-U*V,b*U,-b*V]
assert all(s.cancel(deck(x)-y)==0 for x,y in zip(source,images))
assert all(s.cancel(deck(deck(x))-x)==0 for x in source)
print('PASS 3: exact six-by-six deck involution (including automorphy factor U^4/b^2)')

plus=[U**2,U**3+b*U,V*(U**2-b)]
minus=[U*V,U**3-b*U,V*(U**2+b)]
assert all(s.cancel(deck(x)-x)==0 for x in plus)
assert all(s.cancel(deck(x)+x)==0 for x in minus)
# Coefficient matrix in the six monomial basis, over Q(q):
co=s.Matrix([[s.Poly(s.expand(x),U,V).coeff_monomial(y) for y in source] for x in plus+minus])
assert s.factor(co.det())!=0
print('PASS 4: explicit +/- eigenbasis; both are three-dimensional')

G0=w*t*t
G1=t**3+a*w*t*t+b*w*w*t
G2=v*(t*t-b*w*w)
assert s.expand((G1-w*v*v)+(w*v*v-t**3-a*w*t*t-b*w*w*t))==0
assert all(s.cancel(deck(x)-x)==0 for x in (U**2,U**3+a*U**2+b*U,V*(U**2-b)))
print('PASS 5: plus eigenspace contains the three target-Weierstrass cubics')

qd=-2/q
ad=-2*a/q**2
bd=(a*a-4*b)/q**4
Xprime=G1/q**2
Yprime=G2/q**3
Zprime=G0
Ftarget=s.expand(Yprime**2*Zprime-Xprime**3-ad*Xprime**2*Zprime-bd*Xprime*Zprime**2)
extra=t*t*(t*t-b*w*w)**2*(w*v*v-t**3-a*w*t*t-b*w*w*t)
assert s.factor(q**6*Ftarget-extra)==0
print('PASS 6: exact degree-nine factorization of the cubic isogeny map')

cv=4*(qd**3-1)**2*(qd**3+8)/(27*qd**2)
rv=1/(qd**3+8)
Qv=qd**3+2
P2=Xprime/cv+rv*Zprime
YP=Yprime/cv
Sum=(Zprime-Qv*P2)/(3*qd)
P0=(Sum+YP)/2
P1=(Sum-YP)/2
# For q=2 and q=-1, the Hesse target vanishes modulo the source equation.
for q0 in (s.Integer(2),s.Integer(-1)):
    poly=lambda e:s.Poly(s.cancel(e.subs(q,q0)),*vars)
    FT=qd*(P0**3+P1**3+P2**3)-Qv*P0*P1*P2
    remainder=poly(FT).rem(poly(w*v*v-t**3-a*w*t*t-b*w*w*t))
    assert remainder.is_zero
print('PASS 7: recovered Hesse target, exact polynomial division at q=2 and q=-1')

# The reflection z0 <-> z1 makes W,T even and S odd; the target map respects it.
assert s.factor(W.subs({z0:z1,z1:z0},simultaneous=True)-W)==0
assert s.factor(T.subs({z0:z1,z1:z0},simultaneous=True)-T)==0
assert s.factor(S.subs({z0:z1,z1:z0},simultaneous=True)+S)==0
assert s.factor(P0.subs({v:-v},simultaneous=True)-P1)==0
assert s.factor(P1.subs({v:-v},simultaneous=True)-P0)==0
assert s.factor(P2.subs({v:-v},simultaneous=True)-P2)==0
print('PASS 8: reflection-equivariant target Hesse cubics')
print('8 PASS. No perfect comparison kernel, deck equivariant Koszul-Shamash contraction, or beta/gamma computed.')
