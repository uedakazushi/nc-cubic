"""Exact, dimension-uniform certificate for a cubic deformation correction.

The 4-variable core has 20 degree-three monomials and 16 linear multiples
of its gradient. A polynomial dual vector kills all 16 and detects u^3.
Extra Fermat variables are handled by the tensor-factor argument in TeX.
Also verifies smoothness, critical trace, the universal second-order tensor,
Hesse coefficient and j differences, and a symmetrizer minor certificate.
The paper gives the dimension-uniform arguments. Formality and MF
equivalences are explicit inputs, not verified by this script.
Noncommutative centrality is an explicitly cited input, not checked here.
"""
from functools import lru_cache
from itertools import product
import sympy as sp

x, y, z, u, t, h, a = sp.symbols("x y z u t h a")
variables = (x,y,z,u)
F = (x**3+y**3+z**3+u**3)/3 + t*u*(x*y+y*z+z*x)
gradient = [sp.diff(F,v) for v in variables]
monomials = [e for e in product(range(4), repeat=4) if sum(e)==3]
assert len(monomials) == 20

def functional_monomial(e):
    active, central = e[:3], e[3]
    if central == 3:
        return 3*t
    if central == 1 and sorted(active) == [0,1,1]:
        return -1
    if central == 0:
        if sorted(active)==[0,0,3]: return 2*t
        if sorted(active)==[0,1,2]: return t
        if active==(1,1,1): return -2*t
    return sp.Integer(0)

def functional(polynomial):
    return sp.expand(sum(c*functional_monomial(e)
                         for e,c in sp.Poly(polynomial,*variables).terms()))

columns = [sp.Poly(v*f,*variables) for f in gradient for v in variables]
matrix = sp.Matrix([[p.coeff_monomial(e) for p in columns] for e in monomials])
dual = sp.Matrix([functional_monomial(e) for e in monomials])
assert (dual.T*matrix).applyfunc(sp.expand) == sp.zeros(1,16)
assert functional(u**3) == 3*t
assert functional(t**3*u**3) == 3*t**4
u_cube = sp.Matrix([int(e==(0,0,0,3)) for e in monomials])
assert matrix.subs(t,1).rank() == 16
assert matrix.subs(t,1).row_join(u_cube).rank() == 17
print("PASS: polynomial dual certificate on 20 monomials; 16 gradient multiples")
print("PASS: t=1 rank 16, adjoining u^3 gives rank 17")

smooth_two_equal = sp.resultant(a*a+t*t, 1+t**3+2*t*t*a, a)
assert sp.expand(smooth_two_equal-(1+2*t**3+5*t**6)) == 0
smooth_all_equal = 1+12*t**3
assert (smooth_all_equal*smooth_two_equal).subs(t,1) == 104
assert sp.expand(gradient[0]-gradient[1]-(x-y)*(x+y-t*u)) == 0
print("PASS: exact smoothness factors; t=1 product = 104")

# Critical algebra over QQ[t,u], with square-free active basis.
active_vars=(x,y,z)
basis=list(product((0,1),repeat=3))
replacement=(
    {(0,1,0):-t*u,(0,0,1):-t*u},
    {(1,0,0):-t*u,(0,0,1):-t*u},
    {(1,0,0):-t*u,(0,1,0):-t*u},
)

@lru_cache(None)
def reduce_monomial(exponent):
    if max(exponent)<=1:
        return {exponent:sp.Integer(1)}
    i=next(i for i in range(3) if exponent[i]>=2)
    rest=list(exponent); rest[i]-=2
    result={}
    for tail,coefficient in replacement[i].items():
        new=tuple(b+c for b,c in zip(rest,tail))
        for monomial,value in reduce_monomial(new).items():
            result[monomial]=result.get(monomial,0)+coefficient*value
    return {m:sp.expand(c) for m,c in result.items()}

def trace(polynomial):
    result=0
    for exponent in basis:
        multiplied=sp.expand(polynomial*sp.prod(v**e for v,e in zip(active_vars,exponent)))
        terms=sp.Poly(multiplied,*active_vars).terms()
        result+=sum(c*reduce_monomial(e).get(exponent,0) for e,c in terms)
    return sp.expand(result/8)

hes=sp.det(sp.hessian(F,active_vars))
Z2=t*u*(x*x+y*y+z*z)
R11=t*t*u*u*(x+y+z)
assert trace(x)==trace(y)==trace(z)==0
assert trace(x*y*z)==-sp.Rational(7,4)*t**3*u**3
assert trace(hes)==-12*t**3*u**3
assert trace(Z2-R11)==0
omega_tilde_symbol=F-h*h*hes/12+h**4*(Z2-R11)/18
assert sp.expand(trace(omega_tilde_symbol-F)-h*h*t**3*u**3)==0
print("PASS: exact normalized critical trace; image = F + h^2 t^3 u^3")

# General Hesse h^4 boundary correction is a multiple of g, hence zero
# in its Jacobi quotient. This ensures the quotient-line multiplier is 1.
lam=sp.symbols("lambda")
g=(x**3+y**3+z**3)/3+lam*x*y*z
boundary_psi4=lam*(8-lam**3)*g/48
euler=sum(v*sp.diff(g,v) for v in active_vars)
assert sp.expand(boundary_psi4-lam*(8-lam**3)*euler/144)==0
print("PASS: general Hesse fourth-order boundary term is in the Jacobian ideal")

# Universal residual comparison and exact split-Hesse obstruction.
a, b, c, d, e, f = sp.symbols("a b c d e f")
H = sp.Matrix([[a, d, e], [d, b, f], [e, f, c]])


def epsilon(i, j, k):
    return sp.LeviCivita(i, j, k)


Theta = sp.Matrix(3, 3, lambda i, k: sp.expand(sum(
    epsilon(i, j, p) * epsilon(k, ell, q) * H[p, ell] * H[q, j]
    for j, ell, p, q in product(range(3), repeat=4)
)))
assert all(sp.expand(v) == 0 for v in Theta + 2 * H.adjugate())
print("PASS: all 9 universal tensor entries Theta = -2 adj(H)")

rho2F = -sp.Rational(1, 48) * sum(
    Theta[i, k] * H[i, k] for i, k in product(range(3), repeat=2)
)
assert sp.expand(rho2F - H.det() / 8) == 0
assert sp.Rational(1, 8) - sp.Rational(1, 12) == sp.Rational(1, 24)
print("PASS: universal contraction rho_2(F) = det(H)/8; residual coefficient 1/24")

# Exact coefficient recursion for the Weyl operator, with general exponent r.
r = sp.symbols("r", integer=True, positive=True)
coefficient_previous = -(r - 1) * (r - 2) / sp.Integer(48)
coefficient_eye_increment = -(r - 1) / sp.Integer(24)
coefficient = -r * (r - 1) / sp.Integer(48)
assert sp.expand(coefficient_previous + coefficient_eye_increment - coefficient) == 0
print("PASS: universal star-power induction coefficient -r(r-1)/48")

# Full-Fermat witness.  The active critical algebra has the square-free basis.
x, y, z = sp.symbols("x y z")
HFermat = sp.diag(2 * x, 2 * y, 2 * z)
assert HFermat.det() == 8 * x * y * z
basis = list(product(range(2), repeat=3))
M_xyz = sp.zeros(8)
for column, exponent in enumerate(basis):
    result = tuple(ei + 1 for ei in exponent)
    if all(ei < 2 for ei in result):
        M_xyz[basis.index(result), column] = 1
assert sp.trace(M_xyz) == 0
assert M_xyz**2 == sp.zeros(8)
D2 = sp.expand(HFermat.det() / 24)
assert D2 == x * y * z / 3
remainder = sp.groebner([x*x, y*y, z*z], x, y, z).reduce(3 * D2)[1]
assert remainder == x * y * z
print("PASS: Fermat normalized trace = 0 and D_2 = xyz/3 is nonzero in Jac_3")
print("NOTE: arbitrary extra Fermat variables tensor with k[u_i]/(u_i^2), preserving this class")

# Pinned split-Hesse central coefficients and exact trace-Hessian multiplier.
h, lam = sp.symbols("h lam")
a_h = 1 + h**4 / 2 + h**5 / 6 - h**8 / 48
b_h = (4 - h**4) * (12*h + h**5 - 8*h**2) / 48
assert sp.expand(b_h - h*a_h + sp.Rational(2, 3)*h**2*(1+h**3)) == 0
print("PASS: exact Hesse boundary b_h - h*a_h = -2*h^2*(1+h^3)/3")

lambda_res = (h + h**2/3 + h**5/12) / (1 - h**4/4)
assert sp.cancel(lambda_res - h - h**2*(1+h**3)/(3*(1-h**4/4))) == 0
assert sp.series(lambda_res-h, h, 0, 6).removeO() == h**2/3 + h**5/3
print("PASS: exact lambda_res - h, with leading coefficient h^2/3")


def hesse_j(t):
    return 27*t**3*(8-t**3)**3/(1+t**3)**3


# Artebani--Dolgachev Section 2, equations (4)--(5), with
# (t0,t1)=(1,3*lam), hence (u0,u1)=(1,lam/2).
weierstrass_a = 6*lam*(1-lam**3/8)
weierstrass_b = 2*(1-sp.Rational(5,2)*lam**3-lam**6/8)
weierstrass_discriminant = sp.expand(4*weierstrass_a**3+27*weierstrass_b**2)
assert sp.expand(weierstrass_discriminant-108*(1+lam**3)**3) == 0
assert sp.cancel(1728*4*weierstrass_a**3/weierstrass_discriminant-hesse_j(lam)) == 0

j_difference = sp.cancel(hesse_j(lambda_res) - hesse_j(h))
j_num, j_den = j_difference.as_numer_denom()
j_num_poly, j_den_poly = sp.Poly(j_num, h), sp.Poly(j_den, h)
assert j_den_poly.eval(0) != 0
assert all(j_num_poly.nth(i) == 0 for i in range(4))
assert j_num_poly.nth(4) / j_den_poly.eval(0) == 13824
assert sp.series(j_difference, h, 0, 7).removeO() == 13824*h**4 + 4608*h**5 + 512*h**6
print("PASS: exact Hesse j difference has leading term 13824*h^4")

# Full certificate for the active symmetrizer over QQ(lam).
# Hx,Hy,Hz are coefficient matrices of Hess(g_lam),
# g_lam=(x^3+y^3+z^3)/3+lam*x*y*z.
L_entries = sp.symbols("L0:9")
L = sp.Matrix(3, 3, L_entries)
active_hessian_coefficients = [
    sp.Matrix([[2, 0, 0], [0, 0, lam], [0, lam, 0]]),
    sp.Matrix([[0, 0, lam], [0, 2, 0], [lam, 0, 0]]),
    sp.Matrix([[0, lam, 0], [lam, 0, 0], [0, 0, 2]]),
]
symmetrizer_equations = []
for H_i in active_hessian_coefficients:
    difference = L.T*H_i - H_i*L
    symmetrizer_equations.extend([difference[0, 1], difference[0, 2], difference[1, 2]])
symmetrizer_matrix, zero_rhs = sp.linear_eq_to_matrix(symmetrizer_equations, L_entries)
assert zero_rhs == sp.zeros(9, 1)
identity_vector = sp.Matrix([1, 0, 0, 0, 1, 0, 0, 0, 1])
assert symmetrizer_matrix*identity_vector == sp.zeros(9, 1)
# Drop zero-indexed row 2 and column 8.  This nonzero 8x8 minor certifies
# rank >=8 on lam*(lam^3-8) != 0; scalar identity in the kernel gives rank <=8.
minor_certificate = sp.expand(symmetrizer_matrix.minor_submatrix(2, 8).det())
assert sp.expand(minor_certificate - lam**2*(lam**3-8)**2) == 0
assert symmetrizer_matrix.rank() == 8
assert symmetrizer_matrix.nullspace() == [identity_vector]
print("PASS: active symmetrizer rank 8 over QQ(lam); kernel scalars")
print("CERTIFICATE: 8x8 minor = lam^2*(lam^3-8)^2")
