"""Exact finite checks supporting the trace--Hessian research draft.

The argument uniform in n is in papers/sections/poisson_morphism.tex.  This script checks
the printed EG homogeneous formula and a coefficient-universal Fermat
trace example; no numerical interpolation or external data is used.

Input for the optional mixed-center comparison: nc-cubic commit
eabe601c1341777742964584dde5314c0bcf64a9,
papers/support/papers/sections/hesse_mixed_universal_center.tex,
Corollary cor:pg-hesse-hessian-form. Its centrality is an input; this
script checks commutative evaluation and trace, not that centrality.
"""
from functools import lru_cache
from itertools import product
import sympy as sp

x, y, z, h, lam = sp.symbols("x y z h lam")
variables = (x, y, z)
delta = 1 - h * lam / 2
q, t = (1 + h * lam / 2) / delta, h / delta
g = (x**3 + y**3 + z**3) / 3 + lam * x*y*z
psi_ab = t*(q+1)*(t*(t**3+1)*y**3
                       + (q**3-t**3)*x*y*z
                       - q*(t**3+1)*x*y*z
                       + t*(q**3-t**3)*z**3)
kappa = -4*h**4*(1+lam**3)/delta**6
certificate = t**2*(q+1)*((t**3+1)*y*sp.diff(g,y)
                              +(q**3-t**3)*z*sp.diff(g,z))
assert sp.factor(psi_ab-kappa*x*y*z-certificate) == 0
hes = sp.det(sp.hessian(g, variables))
assert sp.expand(hes - 8*(1+lam**3)*x*y*z
                 + 2*lam**2*(x*sp.diff(g,x)
                              + y*sp.diff(g,y)+z*sp.diff(g,z))) == 0
U = 1+h**2*lam**2/2+h**4*lam/6-h**4*lam**4/48
W = (4-h**2*lam**2)*(12*lam+h**2*(lam**3-8))/48
assert sp.factor(W-lam*U + sp.Rational(2,3)*h**2*(1+lam**3)) == 0
print("PASS: EG central evaluation, exact ideal certificate and Hessian socle")

# Coefficient-universal finite flat algebra at Fermat active leading term.
# The three leading monomials x^2,y^2,z^2 are relatively prime, hence the
# relations below are a Groebner basis for the degree filtration.  Their
# eight square-free standard monomials give an exact free basis over
# QQ[A,B,C,D,E,H].  All trace computations use that fixed basis.
A, B, C, D, E, H = sp.symbols("A B C D E H")
replacement = (
    { (0,1,0): -A, (0,0,1): -C, (0,0,0): -D },
    { (1,0,0): -A, (0,0,1): -B, (0,0,0): -E },
    { (0,1,0): -B, (1,0,0): -C, (0,0,0): -H },
)
basis = list(product((0,1), repeat=3))

@lru_cache(None)
def reduce_monomial(exponent):
    if max(exponent) <= 1:
        return {exponent: sp.Integer(1)}
    i = next(i for i in range(3) if exponent[i] >= 2)
    rest = list(exponent)
    rest[i] -= 2
    result = {}
    for tail, coefficient in replacement[i].items():
        new = tuple(a+b for a,b in zip(rest,tail))
        for monomial, value in reduce_monomial(new).items():
            result[monomial] = result.get(monomial,0) + coefficient*value
    return {m:sp.expand(c) for m,c in result.items()}

def trace(polynomial):
    result = 0
    for exponent in basis:
        terms = sp.Poly(sp.expand(polynomial*sp.prod(
            v**a for v,a in zip(variables,exponent))), *variables).terms()
        result += sum(c*reduce_monomial(m).get(exponent,0) for m,c in terms)
    return sp.expand(result/8)

F = (x**3+y**3+z**3)/3 + A*x*y+B*y*z+C*z*x+D*x+E*y+H*z
hessian = sp.det(sp.hessian(F,variables))
assert trace(x) == trace(y) == trace(z) == 0
assert trace(hessian) == -12*A*B*C
psi4 = (A*z*z+B*x*x+C*y*y-A*C*x-A*B*y-B*C*z)/18
assert trace(psi4) == -(A*H+B*D+C*E)/18
omega_symbol = F - h**2*hessian/12 + h**2*A*B*C/6 + h**4*psi4
assert sp.expand(trace(omega_symbol-F)
                 - sp.Rational(7,6)*h**2*A*B*C
                 + h**4*(A*H+B*D+C*E)/18) == 0
print("PASS: normalized trace and finite-h central correction, universal coefficients")
