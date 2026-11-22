#!/usr/bin/env python3
"""Exact finite Hesse/Clifford theta obstruction and self-isogeny CM check.

The curve/line-bundle arguments are proved in the paper. This script verifies
the level-three linear algebra and CM j identity, NOT Ku or its higher jets.
Run: python3 computations/verify_clifford_hesse_theta.py
"""
import sympy as s

z=(-1+s.sqrt(-3))/2
assert s.simplify(z**2+z+1)==0 and s.simplify(z**3-1)==0
C=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
D=s.diag(1,z,z**2)
assert s.simplify(C*D-z**2*D*C)==s.zeros(3)
assert s.simplify(C*D.inv()-z*D.inv()*C)==s.zeros(3)
print("PASS 1: Hesse cyclic/diagonal lifts have inverse commutators after Q->-Q")

Tvars=s.symbols('T0:9')
T=s.Matrix(3,3,Tvars)
eq=list(T*C-C*T)+list(T*D-D.inv()*T)
A,_=s.linear_eq_to_matrix(eq,Tvars)
assert A.rank()==9 and not A.nullspace()
print("PASS 2: no nonzero identity-labelled 3x3 Heisenberg intertwiner")

# Direct-sum model: pullback 6-sections = two dual 3-dimensional copies.
C6=s.diag(C,C)
D6=s.diag(D.inv(),D.inv())
deck=s.diag(s.eye(3),-s.eye(3))
assert s.simplify(C6*D6-z*D6*C6)==s.zeros(6)
assert deck*C6==C6*deck and deck*D6==D6*deck
assert sum(1 for q in deck.diagonal() if q==1)==3
assert sum(1 for q in deck.diagonal() if q==-1)==3
print("PASS 3: 6=3+3 deck eigenspaces, each with inverse central character")

# Quadratic coordinate polynomials have the same inverse central character:
# the 3x3 commutator scalar z^2 squares to z on Sym^2.
assert s.simplify(z**4-z)==0
print("PASS 4: inverse central character alone does not obstruct quadrics")

# Special self-isogeny tau^2=-2 and j=8000.
tau=s.symbols('tau')
tv=-2/tau
assert s.cancel(tv-tau+(tau**2+2)/tau)==0
assert s.simplify(-2/tv-tau)==0
print("PASS 5: self-isogeny exactly at tau^2=-2, with composition [-2]")

hh=(2+tau**3)/(3*tau)
j=s.cancel(27*hh**3*(hh**3+8)**3/(hh**3-1)**3)
num,den=s.fraction(s.cancel(j-8000))
assert s.rem(num,tau**2+2,tau)==0
assert s.rem(den,tau**2+2,tau)!=0
print("PASS 6: j(E_tau)=8000 at tau^2=-2 (nonvanishing denominator)")
print("6 PASS. Theta/Picard geometry relies on the mathematical proof; no Ku beta/gamma calculated.")
