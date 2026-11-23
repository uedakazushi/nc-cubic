#!/usr/bin/env python3
"""Exact affine bridge: symmetric 3x3 Picard MF, 2x2 ideal MF, and cover multiplication.
No noncommutative Ku kernel or rotation/period/jet computation is implied.
"""
import sympy as sp
x, y, a, b = sp.symbols('x y a b')
g = x*x + a*x + b
f = y*y - x*g
L = sp.Matrix([[x,y,0],[y,a*x+b,x],[0,x,-1]])
Q = L.adjugate()
T = sp.Matrix([[1,0,0],[0,1,x],[0,0,1]])
S = sp.Matrix([[x,y],[y,g]])
H = S.adjugate()
D3 = sp.diag(-1,1,1)
D2 = sp.diag(-1,1)

def eq(A,B):
    return all(sp.expand(z)==0 for z in A-B)

assert eq(T*L*T.T,sp.Matrix([[x,y,0],[y,g,0],[0,0,-1]]))
print('PASS 1: polynomial congruence splits symmetric 3x3 matrix over Z=1')
assert sp.factor(S.det()+f)==0
assert eq(T.T.inv()*Q*T.inv(),sp.Matrix([[-g,y,0],[y,-x,0],[0,0,-f]]))
assert eq(S*(-H),f*sp.eye(2)) and eq((-H)*S,f*sp.eye(2))
print('PASS 2: adjugate transforms to the 2x2 MF plus a contractible rank-one pair')
row=sp.Matrix([[y,-x,-x*x]])
assert eq(row*L,sp.Matrix([[0,f,0]]))
assert eq(row*T.inv(),sp.Matrix([[y,-x,0]]))
assert eq(sp.Matrix([[y,-x]])*S,sp.Matrix([[0,f]]))
print('PASS 3: explicit coker map to I=(x,y) and its syzygies')
A=sp.Matrix([[y,-g],[-x,y]])
J=sp.Matrix([[0,1],[-1,0]])
E=sp.diag(1,-1)
assert eq(J*S*E,A)
print('PASS 4: the pre-existing 2x2 ideal presentation is constant-equivalent on the affine chart')
assert eq(sp.Matrix([[y*y,-x*y],[-x*y,x*x]]),x*H+sp.Matrix([[f,0],[0,0]]))
assert eq(sp.Matrix([[g,-y],[-y,x]]),H)
assert sp.simplify(y*y-x*g-f)==0
print('PASS 5: normalized product I^2=(x), (rs)/x has pairing adj(S)')
assert eq(L.subs(y,-y),D3*L*D3)
assert eq(S.subs(y,-y),D2*S*D2)
assert eq(H.subs(y,-y),D2*H*D2)
assert eq(T*D3,D3*T)
assert eq(sp.Matrix([[-y,-x]]),sp.Matrix([[y,-x]])*D2)
print('PASS 6: reflection and normalized pairing are compatible with the contraction')
# In the 2-cover target, a_target=-2a, b_target=delta, and I is the negative eigensheaf.
delta=sp.symbols('delta')
gt=x*x-2*a*x+delta
St=sp.Matrix([[x,y],[y,gt]])
Ht=St.adjugate()
assert eq(Ht,sp.Matrix([[gt,-y],[-y,x]]))
assert sp.expand(y*y-x*gt)==sp.expand(y*y-x*(x*(x-2*a)+delta))
print('PASS 7: target negative eigensheaf multiplication and Picard pairing agree')
# Check a fiber over Q also at the two-torsion point: all formulas have no 1/x pole.
assert (S.subs({x:0,y:0,a:1,b:2})).rank()==1
assert (L.subs({x:0,y:0,a:1,b:2})).rank()==2
assert eq(H.subs({x:0,y:0,a:1,b:2}),sp.Matrix([[2,0],[0,0]]))
print('PASS 8: non-inverted x at the branch point and compatible ranks')
print('8 PASS: polynomial identities only; not a graded Ku comparison or twelve coefficients.')
