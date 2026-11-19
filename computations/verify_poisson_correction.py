#!/usr/bin/env python3
"""Exact identities for the intrinsic Hessian correction and split Hesse chart.

Run with Python 3 and SymPy. These identities do not prove formality,
centrality in the noncommutative algebra, or the conditional MF comparison.
"""
import sympy as s


def zero(expr):
    assert s.cancel(s.expand(expr)) == 0


x, y, z, t, eps, lam = s.symbols("x y z t eps lam")
a, b, c, d, e, f = s.symbols("a b c d e f")
M = s.Matrix([[a, b, c], [b, d, e], [c, e, f]])
p = s.Matrix([x, y, z])
C = s.Matrix([[0, -z, y], [z, 0, -x], [-y, x, 0]])
assert C.adjugate() == p * p.T
zero((C + t*M).det() - t*(p.T*M*p)[0] - t**3*M.det())
print("PASS: universal skew/symmetric determinant and adjugate identities")

monomials = [x**3, x*x*y, x*x*z, x*y*y, x*y*z,
             x*z*z, y**3, y*y*z, y*z*z, z**3]
coeffs = s.symbols("c0:10")
g = sum(q*m for q, m in zip(coeffs, monomials))
Hg = s.hessian(g, (x, y, z))
zero((p.T*Hg*p)[0] - 6*g)
zero((C - eps*Hg/2).det() + 3*eps*(g + eps**2*Hg.det()/24))
print("PASS: all ten independent ternary cubic coefficients give the point cubic")

S = x**3 + y**3 + z**3
P = x*y*z
g = S/3 + lam*P
Hg = s.hessian(g, (x, y, z)).det()
zero(Hg - ((8 + 2*lam**3)*P - 2*lam**2*S))
A = 1 - eps**2*lam**2/4
B = lam + eps**2*(4 + lam**3)/12
zero(g + eps**2*Hg/24 - (A*S/3 + B*P))
R = B/A
zero(R-lam-eps**2*(1+lam**3)/(3*A))
print("PASS: corrected Hesse coefficients and exact parameter displacement")

u = 1 + eps**2*lam**2/2 + eps**4*lam/6 - eps**4*lam**4/48
v = lam - eps**2*lam**3/6 - 2*eps**2/3 + eps**4*lam**2/6 - eps**4*lam**5/48
zero(v-lam*u + s.Rational(2, 3)*eps**2*(1+lam**3))
aa = 1 - eps*lam/2
bb = -1 - eps*lam/2
cc = -eps
zero(-(aa**3 + bb**3 + cc**3)/(3*aa*bb*cc) - R)
zero(aa**3 + bb**3 + cc**3 + 3*R*aa*bb*cc)
# Use C-D=eps*S+(eps*lam/2)*(C+D), C+D=6*sym(xyz),
# to convert the standard central expression to -9*eps*(u*S/3+v*sym(xyz)).
qC = aa*(bb**3-cc**3)
qD = bb*(cc**3-aa**3)
qS = cc*(aa**3-bb**3)
zero((qC-qD)*eps/2 + qS + 3*eps*u)
zero(6*((qC+qD)/2+(qC-qD)*eps*lam/4) + 9*eps*v)
Psi = lam*(8-lam**3)*g/48
zero(u*S/3+v*P - (g-eps**2*Hg/12+eps**4*Psi))
print("PASS: central coefficients, Hessian normalization, point parameter and section")

h = s.symbols("h")
Rdiag = R.subs({lam:h, eps:h})
zero(Rdiag - (h+h**2/3+h**5/12)/(1-h**4/4))
zero(s.series(R, eps, 0, 5).removeO()
     - (lam + eps**2*(1+lam**3)/3
        + eps**4*lam**2*(1+lam**3)/12))
print("PASS: diagonal comparison input and uniform second/fourth coefficients")

q = s.symbols("q", nonzero=True)
scaled_g = q*g
zero((eps/q)**2*s.hessian(scaled_g, (x, y, z)).det() - q*eps**2*Hg)
u1, u2 = s.symbols("u1 u2")
G = (u1**3 + u2**3)/3
res = S/3 + R*P + G
# Active coordinates scale by c with c^3=A^(-1): homogeneous substitution
# suffices, without choosing an algebraic branch of the cube root.
zero((A*S/3+B*P)/A + G - res)
print("PASS: equation-line covariance and active-only normalization")

pp, qq, target_p = s.symbols("p q target_p")
zero((eps*A).subs({lam:qq/pp, eps:pp}) - pp*(1-qq**2/4))
zero((eps*B).subs({lam:qq/pp, eps:pp}) - (qq+pp**3/3+qq**3/12))
qmap = qq+qq**3/12+target_p**3/(3*(1-qq**2/4)**3)
num, den = s.fraction(s.cancel(qmap))
field = s.QQ.frac_field(target_p)
num_poly = s.Poly(num, qq, domain=field)
den_poly = s.Poly(den, qq, domain=field)
assert num_poly.degree() == 9 and den_poly.degree() == 6
assert s.gcd(num_poly, den_poly).degree() == 0
print("PASS: framed two-parameter correction has generic degree nine")



x, y, z, p, q, b = s.symbols("x y z p q b")
g = p * (x**3 + y**3 + z**3) / 3 + q*x*y*z
hess = s.hessian(g, (x, y, z))
P = p*(1-q*q/4)
Q = q+p**3/3+q**3/12
assert s.expand(g+hess.det()/24-(P*(x**3+y**3+z**3)/3+Q*x*y*z)) == 0
assert s.factor(s.det(s.Matrix([P, Q]).jacobian([p, q]))-(8*p**3*q-q**4+16)/16) == 0
print("PASS: Hesse correction and two-dimensional Jacobian")

mons = [x*x, y*z, y*y, z*x, z*z, x*y]
L = s.zeros(6)
for j, mon in enumerate(mons):
    image = s.Poly(mon+s.trace(hess.adjugate()*s.hessian(mon, (x,y,z)))/24, x,y,z)
    for i, out in enumerate(mons):
        L[i,j] = image.coeff_monomial(out)
assert s.factor(L.det()-(1+(8*p**3*q-q**4)/144)**3) == 0
print("PASS: mixed quadratic block determinant")

# Optional, not needed for generic degree 9: derivative on all active cubics.
mons3 = [x**3,y**3,z**3,x*x*y,x*x*z,x*y*y,y*y*z,x*z*z,y*z*z,x*y*z]
J = s.zeros(10)
for j, mon in enumerate(mons3):
    image = s.Poly(mon+s.trace(hess.adjugate()*s.hessian(mon,(x,y,z)))/24,x,y,z)
    for i, out in enumerate(mons3):
        J[i,j] = image.coeff_monomial(out)
R = s.cancel(P*(P**3+Q**3)/(p*(p**3+q**3)))
assert s.factor(J.det()-(1+(8*p**3*q-q**4)/16)*R**2) == 0
print("PASS: active 10-dimensional derivative determinant")

# Optional monodromy certificate over the line p'=1.
poly = -q**9+12*b*q**6+96*q**5-144*b*q**4-512*q**3+576*b*q**2+768*q-768*b+256
branch = (59049*b**10-19683*b**9-1574640*b**8+708588*b**7
          +14870871*b**6+25194240*b**5-63004392*b**4
          +298539351*b**3-100776960*b**2+428452416*b+148976413)
disc = s.resultant(poly, s.diff(poly,q), q)
assert s.cancel(disc/branch) == 363087263602825104457728
assert s.gcd(s.Poly(branch,b),s.Poly(s.diff(branch,b),b)).degree() == 0
assert s.degree(branch,b) == 10
assert s.gcd(s.Poly(poly,q),s.Poly(1-q*q/4,q)).degree() == 0
print("PASS: ten distinct simple finite branch values; framed monodromy S9")

print("All Poisson-correction identities verified over rational function fields.")
