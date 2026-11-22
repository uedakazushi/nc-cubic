#!/usr/bin/env python3
"""Exact algebraic double cover, anti-invariant ideal and homogeneous MF.
No categorical Ku comparison or beta/gamma coefficients are computed.
"""
import sympy as s
q,a,b,u,v,xi,eta,X,Y,Z=s.symbols('q a b u v xi eta X Y Z')
aq=(q**6-20*q**3-8)/(9*q**2)
bq=-16*(q**3-1)**3/(81*q**4)
g0=a*a-4*b
g=lambda x:x*x-2*a*x+g0
F_aff=Y**2-X*g(X)
assert s.factor(aq**2-4*bq-(q**3+8)**3/(81*q))==0
assert s.factor(bq+16*(q**3-1)**3/(81*q**4))==0
print('PASS 1: smoothness factors b and a^2-4b over Clifford parameter')
# u,v are the source Weierstrass coordinates: v^2=u^3+a*u^2+b*u.
# xi=v/u, eta=u-b/u, and target scaled coordinates X=xi^2,Y=xi*eta.
Xi=v/u; Eta=u-b/u
src_reln=v**2-u**3-a*u**2-b*u
assert s.factor((Xi**2-(u+a+b/u)).subs(v**2,u**3+a*u**2+b*u))==0
assert s.factor(Eta**2-g(u+a+b/u))==0
assert s.factor(Xi*Eta-v*(1-b/u**2))==0
print('PASS 2: source Weierstrass to quartic eta^2=g(xi^2)')
assert s.expand((xi*eta)**2-xi**2*g(xi**2)-xi**2*(eta**2-g(xi**2)))==0
assert s.expand(F_aff.subs({X:xi**2,Y:xi*eta})-xi**2*(eta**2-g(xi**2)))==0
# from xi^2=u+a+b/u, eta=u-b/u, obtain u=(xi^2-a+eta)/2, v=xi*u.
assert s.factor(((Xi**2-a+Eta)/2-u).subs(v**2,u**3+a*u**2+b*u))==0
print('PASS 3: quotient invariants X=xi^2,Y=xi*eta and rational inverse')
# deck translation p of order two: u->b/u,v->-b*v/u^2 gives xi->-xi, eta->-eta.
deck_u=b/u;deck_v=-b*v/u**2
assert s.factor((deck_v/deck_u)+Xi)==0
assert s.factor(deck_u-b/deck_u+Eta)==0
print('PASS 4: deck involution is (xi,eta)->(-xi,-eta)')
# N as ideal I=(X,Y) on target affine E'\{o'}; I^2=(X).
assert s.expand(Y**2-X*g(X)-F_aff)==0
assert s.factor(s.factor((Y**2-(X-2*a)*X**2)/g0-X).subs(Y**2,X*g(X)))==0
# all quadratic products of ideal generators are divisible by X
assert s.factor(s.factor((Y**2/X)-g(X)).subs(Y**2,X*g(X)))==0
# negative generators: (X,Y) -> (xi,eta): xi^2=X, xi*eta=Y, eta^2=g.
assert s.expand(xi*eta*xi-xi**2*eta)==0
assert s.expand(eta**2*xi-g(xi**2)*xi-xi*(eta**2-g(xi**2)))==0
print('PASS 5: ideal I=(X,Y) has I^2=(X), anti-invariant multiplication ij/X')
# Affine 2x2 matrix factorization presenting I: columns (Y,-X), (-g,Y).
Aaff=s.Matrix([[Y,-g(X)],[-X,Y]])
Baff=s.Matrix([[Y,g(X)],[X,Y]])
assert s.simplify(Aaff*Baff-s.eye(2)*F_aff)==s.zeros(2)
assert s.simplify(Baff*Aaff-s.eye(2)*F_aff)==s.zeros(2)
# [X,Y] Aaff = [0,F]
assert s.simplify(s.Matrix([[X,Y]])*Aaff-s.Matrix([[0,F_aff]]))==s.zeros(1,2)
print('PASS 6: affine rank-2 matrix factorization and exact ideal syzygies')
G=X**2-2*a*X*Z+g0*Z**2
Fh=Y**2*Z-X*G
Ah=s.Matrix([[Y,-G],[-X,Y*Z]])
Bh=s.Matrix([[Y*Z,G],[X,Y]])
assert s.simplify(Ah*Bh-s.eye(2)*Fh)==s.zeros(2)
assert s.simplify(Bh*Ah-s.eye(2)*Fh)==s.zeros(2)
assert s.simplify(s.Matrix([[X,Y]])*Ah-s.Matrix([[0,Fh]]))==s.zeros(1,2)
assert all(s.Poly(v,X,Y,Z).is_homogeneous for v in [G,Fh])
assert [s.Poly(v,X,Y,Z).total_degree() for v in [Ah[0,0],Ah[1,0],Ah[0,1],Ah[1,1]]]==[1,1,2,2]
print('PASS 7: homogeneous graded matrix factorization presenting O_E(-p)')
# Naive square-root cover has an ordinary node at the target 2-torsion point.
t=s.symbols('t')
Hnaive=Y**2-t**2*g(t**2)
Hessian=s.hessian(Hnaive,(t,Y)).subs({t:0,Y:0})
assert s.factor(Hessian.det()+4*g0)==0
assert s.factor(g0.subs({a:aq,b:bq})-(q**3+8)**3/(81*q))==0
print('PASS 8: naive square-root cover has a node at 2-torsion; eta=Y/t normalizes it')
# No fixed points of sign involution on quartic: xi=eta=0 ruled out by g0!=0.
for q0 in [s.Integer(2),s.Integer(-1)]:
    aa=aq.subs(q,q0);bb=bq.subs(q,q0);gg0=s.factor(aa**2-4*bb)
    assert bb!=0 and gg0!=0
    # quartic discriminant has no double roots, since b and g0 nonzero
    H=(t*t-aa)**2-4*bb
    assert s.gcd(s.Poly(H,t),s.Poly(s.diff(H,t),t)).degree()==0
print('PASS 9: finite etale double cover in sample smooth Clifford parameters')
# Source Picard M_tau also has a rank-two matrix factorization (with alpha=a,beta=b).
def factorization(alpha,beta):
    f=Y**2*Z-X*(X**2+alpha*X*Z+beta*Z**2)
    g=X**2+alpha*X*Z+beta*Z**2
    A=s.Matrix([[Y,-g],[-X,Y*Z]])
    B=s.Matrix([[Y*Z,g],[X,Y]])
    return f,A,B
for al,be in [(a,b),(-2*a,g0)]:
    ff,AA,BB=factorization(al,be)
    assert s.simplify(AA*BB-s.eye(2)*ff)==s.zeros(2)
    assert s.simplify(BB*AA-s.eye(2)*ff)==s.zeros(2)
    assert s.simplify(s.Matrix([[X,Y]])*AA-s.Matrix([[0,ff]]))==s.zeros(1,2)
print('PASS 10: source M_tau and target M_tau^vee have uniform rank-two graded MF models')

# Pulling back the target sign line to the double cover becomes trivial;
# (xi,eta) generate the unit ideal of B by an explicit Bezout identity.
bez=s.expand((eta**2-xi**2*(xi**2-2*a))/g0)
assert s.cancel(bez-1-(eta**2-g(xi**2))/g0)==0
print('PASS 11: pullback of target sign line is trivial (sign-equivariant obstruction remains)')
print('11 PASS. Graded MF sheaf O(-p) needs O(o) point twist for M; no Ku comparison.')
