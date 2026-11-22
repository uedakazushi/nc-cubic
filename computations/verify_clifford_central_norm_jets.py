#!/usr/bin/env python3
"""Universal 3x3 one-way Clifford central determinant: exact s-jets and Hesse reductions.
Finite polynomial algebra only, not a comparison of Ku categories or actual beta/gamma.
"""
import sympy as S
from itertools import permutations
x=S.symbols('X0 X1 X2'); y=S.symbols('Y0 Y1 Y2'); tau,h1,h2,s=S.symbols('tau h1 h2 s')
u=S.Matrix(3,3,lambda a,b: S.Symbol(f'u{a}{b}'))
L=[sum(u[a,b]*y[b] for b in range(3)) for a in range(3)]
q=S.Matrix([[x[i] if i==j else (s*L[3-i-j]-tau*x[3-i-j])/2 for j in range(3)] for i in range(3)])
D=S.expand(q.det())
Dj=[S.expand(D.coeff(s,j)) for j in range(4)]
d0=(1-tau**3/S.Integer(4))*S.prod(x)-tau**2/S.Integer(4)*sum(z**3 for z in x)
d1=tau**2/S.Integer(4)*sum(x[(i+1)%3]*x[(i+2)%3]*L[i] for i in range(3))+tau/S.Integer(2)*sum(x[i]**2*L[i] for i in range(3))
d2=-sum(x[i]*(L[i]**2+tau*L[(i+1)%3]*L[(i+2)%3]) for i in range(3))/4
d3=S.prod(L)/4
assert all(S.expand(a-b)==0 for a,b in zip(Dj,(d0,d1,d2,d3)))
print('PASS 1: generic exact determinant coefficients D0 through D3')

# Project homogeneous cubics onto fixed Hesse Jacobian complement by monomials.
variables=x+y
def pi(mon):
    p=S.Poly(mon,*variables)
    out=S.Integer(0)
    for expo,c in p.terms():
        n=[sum(expo[:3]),sum(expo[3:])]
        z=[x,y]
        if n==[3,0] or n==[0,3]:
            b=0 if n[0] else 1; base=expo[3*b:3*b+3]
            if sorted(base)==[0,0,3]: out += c*(h1 if b==0 else h2)*S.prod(z[b])
            elif sorted(base)==[1,1,1]: out += c*S.prod(z[b])
            continue
        b=0 if n[0]==2 else 1; base=expo[3*b:3*b+3]
        if sorted(base)==[0,0,2]:
            a=base.index(2)
            remainder=next(variables[k] for k in range(6) if k//3!=b and expo[k]==1)
            out+=c*(h1 if b==0 else h2)*z[b][(a+1)%3]*z[b][(a+2)%3]*remainder
        else:
            out+=c*S.prod(variables[j]**e for j,e in enumerate(expo))
    return S.expand(out)

Q0=lambda a,b:u[a,b]**2
Qr=lambda a,b:u[(a+1)%3,b]*u[(a+2)%3,b]
Qc=lambda a,b:u[a,(b+1)%3]*u[a,(b+2)%3]
Qd=lambda a,b:u[(a+1)%3,(b+1)%3]*u[(a+2)%3,(b+2)%3]+u[(a+1)%3,(b+2)%3]*u[(a+2)%3,(b+1)%3]
expected2=-sum(x[a]*y[(b+1)%3]*y[(b+2)%3]*(h2*Q0(a,b)+2*Qc(a,b)+tau*h2*Qr(a,b)+tau*Qd(a,b)) for a in range(3) for b in range(3))/4
assert S.expand(pi(Dj[2])-expected2)==0
print('PASS 2: quadratic Hesse covariant h2 Q0 + 2 Qc + tau*h2 Qr + tau Qd')

Ic=sum(S.prod(u[a,b] for a in range(3)) for b in range(3))
Id=sum(S.prod(u[a,p[a]] for a in range(3)) for p in permutations(range(3)))
assert S.expand(pi(Dj[3])-(h2*Ic+Id)*S.prod(y)/4)==0
print('PASS 3: cubic Hesse invariant (h2 Ic + Id)/4 and no other invariants')
I0=sum(u[a,b]**3 for a in range(3) for b in range(3))
Ir=sum(S.prod(u[a,b] for b in range(3)) for a in range(3))
Potential=h2*I0/S.Integer(3)+2*Ir+tau*(h2*Ic+Id)
assert S.expand(S.diff(Potential,tau)-(h2*Ic+Id))==0
for a in range(3):
    for b in range(3):
        rhs=h2*Q0(a,b)+2*Qc(a,b)+tau*h2*Qr(a,b)+tau*Qd(a,b)
        assert S.expand(S.diff(Potential,u[a,b])-rhs)==0
print('PASS 4: quadratic central norm is gradient of a single cubic invariant potential')

expected1=(tau**2/S.Integer(4)+tau*h1/S.Integer(2))*sum(u[a,b]*x[(a+1)%3]*x[(a+2)%3]*y[b] for a in range(3) for b in range(3))
assert S.expand(pi(Dj[1])-expected1)==0
print('PASS 5: linear variation occupies C21 (2X,1Y), not Ku C12 (1X,2Y)')

probes={
'E00':{(0,0):1},
'R0':{(0,0):1,(0,1):1,(0,2):1},
'C0':{(0,0):1,(1,0):1,(2,0):1},
'I3':{(0,0):1,(1,1):1,(2,2):1}}
expected_cubic={'E00':0,'R0':0,'C0':h2*S.prod(y)/4,'I3':S.prod(y)/4}
for label,entries in probes.items():
    sub={u[a,b]:entries.get((a,b),0) for a in range(3) for b in range(3)}
    assert S.expand(pi(Dj[3]).subs(sub)-expected_cubic[label])==0
    assert (S.expand(Dj[3].subs(sub))!=0)==(label in ('C0','I3'))
print('PASS 6: exactly C0,I3 have nonzero cubic central norm on minimal probes')

t=S.symbols('t')
HesseSing=S.expand((1-t/4)**3-27*t**2/64)
assert S.expand(HesseSing+(t-1)*(t+8)**2/S.Integer(64))==0
print('PASS 7: smooth Hesse determinant outside tau^3=1,-8; different fixed-f_tau tangent')
print('7 PASS; no Ku comparison, higher Bockstein, or beta/gamma values computed.')
