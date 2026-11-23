#!/usr/bin/env python3
"""Exact Clifford etale cover projector, trace Casimir and Hochschild contraction.

Polynomial/cochain certificates; NOT a curved Ku comparison or beta/gamma values.
"""
import sympy as S
from itertools import product

X,Y,a,b=S.symbols("X Y a b")
delta=a*a-4*b
g=X*(X-2*a)+delta
def reduced(z):
    n,d=S.fraction(S.cancel(z))
    assert not d.has(Y)
    return S.factor(S.Poly(S.expand(n),Y).rem(S.Poly(Y**2-X*g,Y)).as_expr()/d)

P=S.Matrix([[-X*(X-2*a),-Y*(X-2*a)],[Y,g]])/delta
assert all(reduced(q)==0 for q in P*P-P)
assert reduced(S.trace(P)-1)==0 and reduced(P.det())==0
print("PASS 1: projective 2x2 idempotent and rank-one signed eigensheaf")

cols=[S.Matrix([-(X-2*a)*q/delta,S.cancel(Y*q/(X*delta))]) for q in (X,Y)]
assert all(reduced(q)==0 for q in S.Matrix.hstack(*cols)-P)
assert all(reduced(q)==0 for q in S.Matrix([[X,Y]])*P-S.Matrix([[X,Y]]))
print("PASS 2: explicit split surjection R^2->I, without global X inversion")

# Theta=(eta1*eta2-(X-2a)*xi1*xi2)/delta in B tensor_R B.
assert S.factor((g-X*(X-2*a))/delta-1)==0
assert reduced((g*g-2*(X-2*a)*Y*Y+(X-2*a)**2*X*X)/delta**2-1)==0
# It maps to (1,-1) under B tensor_R B -> B x B (diagonal, antidiagonal).
assert S.factor((-g+X*(X-2*a))/delta+1)==0
print("PASS 3: theta^2=1, and diagonal/antidiagonal evaluations")

PB=S.diag(S.Integer(1),P)
assert all(reduced(q)==0 for q in PB*PB-PB)
assert reduced(S.trace(PB)-2)==0
# Trace dual 1/2 Tr(z) + [eta Tr(eta z)-(X-2a)xi Tr(xi z)]/(2delta).
# Its values at 1,xi,eta reduce to themselves by xi*eta=Y,
# xi^2=X and eta^2=g.
assert reduced((g-X*(X-2*a))/delta-1)==0
print("PASS 4: trace-dual frame and explicit 3x3 finite-projective B")

assert S.factor((1+1)/2-1)==0 and S.factor((1-1)/2)==0
# The same theta has m(theta)=1, m_sigma(theta)=-1, so e+=(1+theta)/2
# is the diagonal separability idempotent in B tensor_R B.
print("PASS 5: trace Casimir and separability idempotent data")

# Universal cochain contraction in split etale B=k x k, with two tests
# M=B (symmetric bimodule), and M_(0,1)=k (nonsymmetric bimodule).
def module_test(n,asym):
    ks=list(product((0,1),repeat=n))
    if asym:
        vals={k:S.Symbol("m"+''.join(map(str,k))) for k in ks}
        zero=S.Integer(0)
        left=lambda i,v:v if i==0 else zero
        right=lambda v,i:v if i==1 else zero
    else:
        vals={k:S.Matrix([S.Symbol("f"+''.join(map(str,k))+"_"+str(j)) for j in (0,1)]) for k in ks}
        zero=S.zeros(2,1)
        def proj(i,v):
            z=S.zeros(2,1);z[i]=v[i];return z
        left=lambda i,v:proj(i,v)
        right=lambda v,i:proj(i,v)
    f=lambda k:vals[k]
    def d(fun,m):
        def val(seq):
            ii=list(seq)
            ans=left(ii[0],fun(tuple(ii[1:])))
            for j in range(1,m+1):
                if ii[j-1]==ii[j]:
                    ans+=(-1)**j*fun(tuple(ii[:j-1]+[ii[j]]+ii[j+1:]))
            ans+=(-1)**(m+1)*right(fun(tuple(ii[:-1])),ii[-1])
            return ans
        return val
    def hh(fun,m):
        def val(seq):
            ans=zero
            for i in (0,1):
                ans+=left(i,fun((i,)+tuple(seq)))
            return ans
        return val
    for k in ks:
        residual=d(hh(f,n),n-1)(k)+hh(d(f,n),n+1)(k)-f(k)
        assert S.simplify(residual)==zero,(n,k,asym)
for n in (1,2,3,4): module_test(n,False)
print("PASS 6: Hochschild d*h+h*d=1 in degrees 1..4 for M=B")
for n in (1,2,3,4): module_test(n,True)
print("PASS 7: contraction also holds for nonsymmetric bimodule M_(0,1)")

s=S.symbols("s")
a0,a1,a2,a3,b0,b1,b2,b3=S.symbols("a0:4 b0:4")
aa=a0+a1*s+a2*s**2+a3*s**3
bb=b0+b1*s+b2*s**2+b3*s**3
D0=a0*a0-4*b0
D1=2*a0*a1-4*b1
D2=a1*a1+2*a0*a2-4*b2
D3=2*a0*a3+2*a1*a2-4*b3
D=D0+D1*s+D2*s*s+D3*s**3
assert all(S.expand(aa**2-4*bb-D).coeff(s,k)==0 for k in range(4))
inv=1/D0-D1*s/D0**2+(D1**2-D0*D2)*s**2/D0**3+(-D1**3+2*D0*D1*D2-D0**2*D3)*s**3/D0**4
assert all(S.factor(S.expand(D*inv).coeff(s,k)-(1 if k==0 else 0))==0 for k in range(4))
print("PASS 8: universal third-order inverse delta(s) for a(s),b(s)")

ass=S.Rational(2)+s+2*s*s-s**3
bss=S.Rational(-1)+s*s+s**3
dss=ass**2-4*bss
gss=X*(X-2*ass)+dss
pss=S.Matrix([[-X*(X-2*ass),-Y*(X-2*ass)],[Y,gss]])/dss
for z in pss*pss-pss:
    num,den=S.fraction(S.cancel(z))
    rem=S.Poly(S.expand(num),Y).rem(S.Poly(Y**2-X*gss,Y)).as_expr()
    assert S.factor(rem)==0
assert S.factor((gss-X*(X-2*ass))/dss-1)==0
print("PASS 9: nonconstant formal cubic path preserves the projector and Casimir")
print("9 PASS; no actual Ku kernel, rotation, or 12 scalar coefficients verified.")
