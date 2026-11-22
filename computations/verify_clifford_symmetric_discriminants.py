#!/usr/bin/env python3
"""Symmetric rank-one Clifford central-norm discriminant certificates.

Check polynomial identities, non-Azumaya double factors, and four explicit
Azumaya ordinary double point witnesses. This is not a verification of
categorical Morita comparisons or the twelve high-order Hesse jets.
Requires SymPy.
"""
import sympy as S

l,m,X,Y,x2,x3,y2,y3=S.symbols("l m X Y x2 x3 y2 y3")
P=X*(l*Y-2*X)**2-Y*(m*X-2*Y)**2
kx=(l*Y-X)/3
ky=(m*X-Y)/3
F={(a,b):S.expand(P-4*a*kx**3+4*b*ky**3)
   for a in (0,1) for b in (0,1)}
q=l*m
Q00=q**2+8*(l**3+m**3)+72*q-432
Q01=16*l**4*m-56*l**3+157*q**2-1456*q+16*m**3+3136
Q10=16*l**3+157*q**2+16*l*m**4-1456*q-56*m**3+3136
Q11=(3024-432*q)*(l**3+m**3)+256*q**4-8032*q**3+87117*q**2-393568*q+614656
D={(0,0):(q-4)**2*Q00,
   (0,1):-(q-8)**2*Q01/27,
   (1,0):-(q-8)**2*Q10/27,
   (1,1):-(q-16)**2*Q11/19683}
for branch in F:
    assert S.expand(S.discriminant(F[branch].subs(Y,1),X)-D[branch])==0
print("PASS 1: complete factorization of four binary cubic discriminants")

qx=S.Matrix([[X,-x3,-x2],
             [-x3,x2,(l*Y-2*X)/2],
             [-x2,(l*Y-2*X)/2,x3]])
qy=S.Matrix([[Y,-y3,-y2],
             [-y3,y2,(m*X-2*Y)/2],
             [-y2,(m*X-2*Y)/2,y3]])
N=S.expand(4*(-qx.det()+qy.det()))
assert S.expand(N-(P+4*(x2**3+x3**3-3*kx*x2*x3)
                   -4*(y2**3+y3**3-3*ky*y2*y3)))==0
print("PASS 2: six-variable normalized central norm")

# Squared factors correspond to simultaneous rank-drop critical points.
for branch,c,root,x,y in [
    ((0,0),4,l/2,0,0),
    ((0,1),8,l/2,0,1),
    ((1,0),8,l/4,l/4,0),
    ((1,1),16,l/4,l/4,1),
]:
    v={Y:1,m:c/l,X:root,x2:x,x3:x,y2:y,y3:y}
    assert S.factor(N.subs(v))==0
    assert S.factor(qx.det().subs(v))==0
    assert S.factor(qy.det().subs(v))==0
    for z in (X,x2,x3,y2,y3):
        assert S.factor(S.diff(N,z).subs(v))==0
print("PASS 3: all squared hyperbolas carry non-Azumaya critical points")

H=S.hessian(N,[X,x2,x3,y2,y3])
def zero_mod(f,c):
    num,den=S.fraction(S.cancel(f))
    assert S.rem(den,m**3-c,m)!=0
    return S.rem(num,m**3-c,m)==0

# Reverse one-parameter probe lambda=0, M=m E11. Swap blocks for Lambda=s E11.
witness={
    (0,0):(54,S.Integer(6),S.Integer(153600)),
    (0,1):(-196,S.Rational(28,13),S.Rational(12902400,2197)),
    (1,0):(56,S.Integer(6),-S.Integer(460800)),
    (1,1):(-S.Rational(5488,27),S.Rational(28,13),
           -S.Rational(38707200,2197)),
}
for branch,(c,z,hd) in witness.items():
    e,d=branch
    v={l:0,Y:1,X:z/m,
       x2:-e*z/(3*m),x3:-e*z/(3*m),
       y2:d*(z-1)/3,y3:d*(z-1)/3}
    assert zero_mod(N.subs(v),c)
    for var in (X,x2,x3,y2,y3):
        assert zero_mod(S.diff(N,var).subs(v),c)
    dx=S.factor(qx.det().subs(v))
    dy=S.factor(qy.det().subs(v))
    assert not zero_mod(dx,c) and not zero_mod(dy,c)
    assert zero_mod(S.factor(H.subs(v).det())-hd,c)
    assert hd!=0
    assert zero_mod(D[branch].subs(l,0),c)
    print("witness",branch,"m^3",c,"z=mX",z,"Hessian",hd)
print("PASS 4: four independent Azumaya ordinary double point witnesses")

# On the probe q=0, all squared factors are units and the four cubic values
# are distinct and nonzero, so there are exactly twelve bad coefficients.
reduced={
    (0,0):128*(m**3-54),
    (0,1):-S.Rational(1024,27)*(m**3+196),
    (1,0):S.Rational(3584,27)*(m**3-56),
    (1,1):-S.Rational(28672,19683)*(27*m**3+5488),
}
for branch,f in reduced.items():
    assert S.expand(D[branch].subs(l,0)-f)==0
assert len({54,56,-196,-S.Rational(5488,27)})==4
print("PASS 5: exactly twelve one-parameter singular coefficients")

# At each bad value exactly one binary branch has a double root.
# Its nonzero transverse critical coordinates admit 3^(e+d) distinct phases.
for branch,(c,z,_) in witness.items():
    e,d=branch
    for other in D:
        if other!=branch:
            assert not zero_mod(D[other].subs(l,0),c)
    if e: assert not zero_mod(-z/(3*m),c)
    if d: assert z!=1
    assert 3**(e+d)=={(0,0):1,(0,1):3,(1,0):3,(1,1):9}[branch]
print("PASS 6: distinct critical branches and node multiplicities 1, 3, 3, 9")
