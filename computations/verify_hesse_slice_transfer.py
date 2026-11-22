#!/usr/bin/env python3
"""Exact cubic Hesse slice and third-order coordinate normalization.

Finite algebra only: this does not compute an nc comparison kernel.
Requires SymPy. Run: python3 computations/verify_hesse_slice_transfer.py
"""
from itertools import combinations_with_replacement
import sympy as s

z = s.symbols('x0 x1 x2 y0 y1 y2')
h1,h2 = s.symbols('h1 h2')
t1,t2 = s.symbols('t1 t2', nonzero=True)
h,t = (h1,h2),(t1,t2)

def split_monomial(e):
    assert sum(e)==3
    A=s.zeros(6)
    deg=[sum(e[3*g:3*g+3]) for g in range(2)]
    mon=s.prod(z[j]**e[j] for j in range(6))
    if deg in ([3,0],[0,3]):
        g=0 if deg[0] else 1
        k=3*g
        E=e[k:k+3]
        if sorted(E)==[0,0,3]:
            i=k+E.index(3)
            A[i,i]=1/t[g]
            return h[g]*s.prod(z[k:k+3]),A
        if sorted(E)==[0,1,2]:
            i=k+E.index(2); j=k+E.index(1)
            other=k+3-(i-k)-(j-k)
            scale=1/(t[g]*(1-h[g]**3))
            A[i,j]=scale
            A[j,other]=h[g]*scale
            A[other,i]=h[g]**2*scale
            return s.Integer(0),A
        return mon,A
    g=0 if deg[0]==2 else 1
    k=3*g
    sq=[j for j in range(k,k+3) if e[j]==2]
    if not sq: return mon,A
    i=sq[0]
    j=next(j for j in range(6) if j//3!=g and e[j]==1)
    other=[q for q in range(k,k+3) if q!=i]
    A[i,j]=1/t[g]
    return h[g]*z[other[0]]*z[other[1]]*z[j],A

def project_and_J(poly):
    if poly==0: return s.Integer(0),s.zeros(6)
    P=s.Integer(0); A=s.zeros(6)
    for ex,c in s.Poly(poly,*z).terms():
        if sum(ex)!=3: raise ValueError('homogeneous cubic required')
        pi,J=split_monomial(ex)
        P+=c*pi; A+=c*J
    return s.expand(P),A

def jacobian(A):
    grad=[t[g]*(z[3*g+i]**2-h[g]*z[3*g+(i+1)%3]*z[3*g+(i+2)%3])
          for g in range(2) for i in range(3)]
    Az=A*s.Matrix(z)
    return s.expand(sum(Az[i]*grad[i] for i in range(6)))

def equal(a,b):
    return all(s.cancel(c)==0 for c in s.Poly(s.expand(a-b),*z).coeffs())

basis=[s.prod(z[j] for j in I)
       for I in combinations_with_replacement(range(6),3)]
assert len(basis)==56
for m in basis:
    P,J=project_and_J(m)
    assert equal(m,P+jacobian(J))
    assert project_and_J(P)[1]==s.zeros(6)
print('PASS 1: 56 monomial splitting identities over generic h_i,t_i')

C=[z[a]*z[3+(b+1)%3]*z[3+(b+2)%3] for a in range(3) for b in range(3)]
C += [z[(a+1)%3]*z[(a+2)%3]*z[3+b] for a in range(3) for b in range(3)]
C += [z[0]*z[1]*z[2],z[3]*z[4]*z[5]]
assert len(C)==20
assert all(equal(project_and_J(m)[0],m) for m in C)
for m in basis:
    P,_=project_and_J(m)
    assert P==0 or all(s.prod(z[i]**k for i,k in enumerate(ex)) in C
                       for ex,c in s.Poly(P,*z).terms())
print('PASS 2: exact 20-dimensional image and 36-dimensional Jacobian kernel')

# Test the Taylor recurrence by direct substitution for two smooth factors:
# tau_1=2, tau_2=3, a_1=1, a_2=2.
special={h1:s.Rational(5,3),h2:s.Rational(29,9),t1:6,t2:18}
def PS(poly):
    P,J=project_and_J(poly)
    return s.expand(P.subs(special)),J.applyfunc(lambda q:s.cancel(q.subs(special)))
def D(A,p):
    V=A*s.Matrix(z)
    return s.expand(sum(V[i]*s.diff(p,z[i]) for i in range(6)))
def H2(A,B,p):
    V,W=A*s.Matrix(z),B*s.Matrix(z)
    return s.expand(sum(V[i]*W[j]*s.diff(p,z[i],z[j])
                        for i in range(6) for j in range(6)))
def H3(A,p):
    V=A*s.Matrix(z)
    return s.expand(sum(V[i]*V[j]*V[k]*s.diff(p,z[i],z[j],z[k])
                        for i in range(6) for j in range(6)
                        for k in range(6)))
x0,x1,x2,y0,y1,y2=z
F=2*(x0**3+x1**3+x2**3)-10*x0*x1*x2+6*(y0**3+y1**3+y2**3)-58*y0*y1*y2
G1=2*x0**2*x1+3*x0*y0**2+y0**2*y1+x1*y1*y2
G2=2*x2**3+3*x1**2*y1+y2**3+x0*x1*y0
G3=x0**2*y2-x2*y1**2+y0*y1*y2
P1,A=PS(G1); A=-A
R2=s.expand(G2+D(A,G1)+s.Rational(1,2)*H2(A,A,F))
P2,B=PS(R2); B=-B
R3=s.expand(G3+D(A,G2)+D(B,G1)+s.Rational(1,2)*H2(A,A,G1)
            +H2(A,B,F)+s.Rational(1,6)*H3(A,F))
P3,C3=PS(R3); C3=-C3
u=s.symbols('u')
T=s.Matrix(z)+(u*A+u**2*B+u**3*C3)*s.Matrix(z)
sub={z[i]:T[i] for i in range(6)}
direct=s.Poly(F.subs(sub,simultaneous=True)
              +u*G1.subs(sub,simultaneous=True)
              +u**2*G2.subs(sub,simultaneous=True)
              +u**3*G3.subs(sub,simultaneous=True),u)
for k,expected in enumerate((F,P1,P2,P3)):
    assert equal(direct.coeff_monomial(u**k),expected)
    if k: assert equal(PS(expected)[0],expected)
print('PASS 3: order-three recurrence equals direct cubic coordinate substitution')

toy1=x0*y1*y2
toy2=x0**2*y0
assert project_and_J(toy1)[1]==s.zeros(6)
toyPi,toyJ=project_and_J(toy2)
assert equal(toyPi,h1*x1*x2*y0)
assert equal(project_and_J(D(-toyJ,toy1))[0],-y0*y1*y2/t1)
print('PASS 4: genuine nonzero third-order gauge term, even when G_1 is in C')
print('4 PASS. LIMIT: no nc comparison kernel, period, or 12 scalar values tested.')
