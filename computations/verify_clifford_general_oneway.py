#!/usr/bin/env python3
"""Exact symbolic tests of the one-direction Clifford norm discriminant.

Scope: polynomial/critical-point identities and sample Hessians, NOT the
categorical comparison kernel or the full residual smooth locus.
Requires SymPy >=1.12.
"""
import sympy as S

s,t,u,A,B,X,Y,x2,x3,y2,y3=S.symbols('s t u A B X Y x2 x3 y2 y3')
g=(u**3-1)*(u**3+8)**2/(27*u**6)
Kx=((4-t**3)*X+t**2*s*Y)/(3*t**2)
Ky=(4-u**3)*Y/(3*u**2)
P=X*(s*Y-t*X)**2
N=A*(P+t**2*(x2**3+x3**3-3*Kx*x2*x3))-B*u**2*(Y**3+y2**3+y3**3-3*Ky*y2*y3)
assert S.factor(N.subs({x2:0,x3:0,y2:0,y3:0})-(A*P-B*u**2*Y**3))==0
print('PASS 1: exact rank-one six-variable norm')

phi={0:P.subs(Y,1),1:S.expand((P-t**2*Kx**3).subs(Y,1))}
gamma={0:S.Integer(1),1:g}
alpha={0:S.factor(27*B*t*u**2/(4*A)),1:S.factor(-B*u**2*(t**3-1)**2*(t**3+8)/(4*A*t**2))}
for e in (0,1):
    for d in (0,1):
        f=S.expand(A*phi[e]-B*u**2*gamma[d])
        coeff=S.Poly(f,X).all_coeffs()
        aa,bb,cc,dd=coeff
        disc=S.expand(bb**2*cc**2-4*aa*cc**3-4*bb**3*dd-27*aa**2*dd**2+18*aa*bb*cc*dd)
        if e==0:
            target=A**2*B*t**3*u**2*gamma[d]*(4*A*s**3-27*B*t*u**2*gamma[d])
        else:
            target=-A**2*B*u**2*gamma[d]*(t**3+8)**3/(27*t**8)*(4*A*t**2*s**3+B*u**2*gamma[d]*(t**3-1)**2*(t**3+8))
        assert S.cancel(disc-target)==0,(e,d)
print('PASS 2: all four general binary discriminant identities')

r={0:s/(3*t),1:s*t**2*(t**3+5)/((t**3-1)*(t**3+8))}
for e in (0,1):
    assert S.cancel(S.diff(phi[e],X).subs(X,r[e]))==0
    want=(4*s**3/(27*t)) if e==0 else (-4*s**3*t**2/((t**3-1)**2*(t**3+8)))
    assert S.cancel(phi[e].subs(X,r[e])-want)==0
    # First-order parameter transversality at every critical point.
    ds=S.factor(S.diff(phi[e],s).subs(X,r[e]))
    expected=4*s**2/(9*t) if e==0 else -12*s**2*t**2/((t**3-1)**2*(t**3+8))
    assert S.cancel(ds-expected)==0
print('PASS 3: critical values, roots and transverse smoothing')

# At each branch the second factor determinant is nonzero in allowed range.
qy=S.Matrix([[Y,-u*y3/2,-u*y2/2],[-u*y3/2,y2,-u*Y/2],[-u*y2/2,-u*Y/2,y3]])
for d in (0,1):
    vd={Y:1,y2:d*Ky.subs(Y,1),y3:d*Ky.subs(Y,1)}
    assert S.factor(qy.det().subs(vd)+u**2*gamma[d]/4)==0
print('PASS 4: both transverse branches have nonzero Clifford determinant')

# Specialize t=3,u=2; choose A/B for each branch so that s=1 is singular.
# This checks the generic ordinary-node property away from t^3=-2,u^3=4.
variables=(X,x2,x3,y2,y3)
H=S.hessian(N.subs({Y:1,s:1,t:3,u:2,B:1}),variables)
for e in (0,1):
    for d in (0,1):
        a_val=S.factor(alpha[e].subs({t:3,u:2,B:1,A:1})*gamma[d].subs(u,2))
        rv=r[e].subs({s:1,t:3})
        kx=S.factor(Kx.subs({s:1,t:3,X:rv,Y:1}))
        ky=S.factor(Ky.subs({u:2,Y:1}))
        subs={A:a_val,X:rv,x2:e*kx,x3:e*kx,y2:d*ky,y3:d*ky}
        # The chosen A equals the numerator giving a zero at s=1.
        val=S.factor(N.subs({Y:1,s:1,t:3,u:2,B:1}).subs(subs))
        assert val==0,(e,d,val)
        for v in variables:
            assert S.factor(S.diff(N,v).subs({Y:1,s:1,t:3,u:2,B:1}).subs(subs))==0,(e,d,v)
        det=S.factor(H.subs(subs).det())
        assert det!=0,(e,d)
        print('  witness',e,d,'det Hess',det)
print('PASS 5: four genuinely nondegenerate generic nodes')

# Crossover of two branches is possible for special t,u; generic hypotheses
# only require noncollision when asserting twelve distinct parameter values.
assert S.factor(27*t**3+(t**3-1)**2*(t**3+8))==(t**3+2)**3
assert S.cancel(1-g-(4-u**3)**3/(27*u**6))==0
h=S.symbols('h')
x0=s/(3*t)
assert S.cancel(phi[0].subs(X,x0+h)-phi[0].subs(X,x0)+t*s*h**2-t**2*h**3)==0
collision_k=S.together(Kx.subs({X:x0+h,Y:1})-2*h/t**2).as_numer_denom()[0]
assert S.rem(collision_k,t**3+2,t)==0
# At t^3=-2, elimination of the Morse variable h leaves x2^3+x3^3,
# with Jacobian quotient length 4; with u^3=4 it leaves four cubes,
# with Jacobian quotient length 2^4=16.
assert S.rem(S.together(Ky.subs(Y,1)).as_numer_denom()[0], u**3-4,u)==0
print('PASS 6: collision equations and cubic D4 local 3-jets')
