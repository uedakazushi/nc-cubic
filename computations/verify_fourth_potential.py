"""Exact coefficient identities for the fourth mixed residual correction.

2026-11-20.  Requires SymPy.  This verifies commutative polynomial identities,
not noncommutative centrality, Kontsevich graph integration or MF comparison.

"""
from itertools import product, combinations_with_replacement
import sympy as sp
from verify_cubic_covariants import contraction, SE, IE, JE


def verify_classical_covariants():
    """Check the full polynomial identities on independent third-order jets."""
    indices = range(3)
    triple_keys = list(combinations_with_replacement(indices, 3))
    t = dict(zip(triple_keys, sp.symbols('t0:10')))
    T = {ijk: t[tuple(sorted(ijk))] for ijk in product(indices, repeat=3)}
    pair_keys = list(combinations_with_replacement(indices, 2))
    m = dict(zip(pair_keys, sp.symbols('m0:6')))
    M = {ij: m[tuple(sorted(ij))] for ij in product(indices, repeat=2)}
    q = sp.symbols('q0:3')
    I = contraction([T, T, M, M, M], IE)
    J = contraction([T, T, T, M, {(i,): q[i] for i in indices}], JE)
    S = contraction([T] * 4, SE)
    direction = {
        (i, j, k): (M[i, j]*q[k]+M[i, k]*q[j]+M[j, k]*q[i])/3
        for i, j, k in triple_keys
    }
    dS = sum(sp.diff(S, t[ijk])*direction[ijk] for ijk in triple_keys)
    assert sp.expand(dS-4*J) == 0
    print('PASS: universal J = (1/4) dS_T[M symmetric-product q]')

    x = sp.symbols('x0:3')
    linear_hessian = sp.Matrix(
        3, 3, lambda i, j: M[i, j]+sum(T[i, j, k]*x[k] for k in indices))
    hessian_of_det = sp.hessian(linear_hessian.det(), x).subs(dict.fromkeys(x, 0))
    initial_hessian = sp.Matrix(3, 3, lambda i, j: M[i, j])
    classical_I = sp.trace(initial_hessian.adjugate()*hessian_of_det)/12
    assert sp.expand(I-classical_I) == 0
    print('PASS: universal I = (1/12) tr(adj M * Hess(det M))')


def verify():
    x, y, z = sp.symbols('x y z')
    active = (x, y, z)
    lam, A, B, C, D, E, H, G = sp.symbols('lam A B C D E H G')
    g = (x**3 + y**3 + z**3) / 3 + lam*x*y*z
    Q = A*x*y + B*y*z + C*z*x
    L = D*x + E*y + H*z
    F = g + Q + L + G
    T = {ii: sp.diff(F, *(active[i] for i in ii))
         for ii in product(range(3), repeat=3)}
    M = {(i, j): sp.diff(F, active[i], active[j])
         for i, j in product(range(3), repeat=2)}
    q = {(i,): sp.diff(F, active[i]) for i in range(3)}
    S = contraction([T] * 4, SE)
    I = contraction([T, T, M, M, M], IE)
    J = contraction([T, T, T, M, q], JE)
    assert sp.expand(S - lam*(lam**3 - 8)) == 0
    Z2 = A*z*z + B*x*x + C*y*y
    R2 = B*B*x + C*C*y + A*A*z
    R11 = A*C*x + A*B*y + B*C*z
    K = A*H + B*D + C*E
    Psi = (-S*g/48 - lam**4*Q/48 + (2-lam**3)*Z2/36
           - S*L/144 - lam**2*R2/24 - (lam**3+4)*R11/72)
    C4 = (lam*(A**3+B**3+C**3)/60 + lam**2*A*B*C/40
          + (2-lam**3)*K/180 + S*G/80)
    assert sp.expand(Psi + S*F/80 + I/40 - J/60 - C4) == 0
    print('PASS: universal exact Hesse Psi identity and pure-central C4')

    # This is an algebraic compatibility check using the separately
    # evaluated graph coefficients; it does not independently integrate them.
    beta, gamma = sp.Rational(1, 60), sp.Rational(1, 240)
    delta, epsilon = beta + sp.Rational(1, 40), gamma-sp.Rational(1, 60)
    assert (delta, epsilon) == (sp.Rational(1, 24), -sp.Rational(1, 80))
    a4 = sp.expand(S*(sp.Rational(1, 30)-delta-epsilon))
    assert sp.expand(a4 - S/240) == 0
    Q5 = S*F/80 + beta*(I-S*F) + gamma*(J-S*F)
    W4 = Psi + delta*I + epsilon*J
    assert sp.expand(W4 - Q5 + a4*F - C4) == 0
    print('PASS: W4, tensor coefficient and a4=S/240 agree identically')

    F0, I0, J0 = [sp.expand(t.subs(lam, 0)) for t in (F, I, J)]
    gradient_combination = (A*sp.diff(F0, z) + B*sp.diff(F0, x)
                            + C*sp.diff(F0, y))
    assert sp.expand(J0 + sp.Rational(2, 3)*gradient_combination) == 0
    assert sp.expand(I0 + sp.Rational(8, 3)*gradient_combination
                     - sp.Rational(20, 3)*R11 - sp.Rational(8, 3)*K) == 0
    # tau(x)=tau(y)=tau(z)=0 gives tau(I0)=8 K/3.  Combining it
    # with the exact ideal identity yields the published Jacobi class.
    assert sp.expand((sp.Rational(20, 3)*R11+sp.Rational(8, 3)*K)/60
                     + (sp.Rational(8, 3)*K)/40-(R11+K)/9) == 0
    print('PASS: Fermat active Jacobi identity Delta4=(R11+K)/9')

    # A polynomial identity certificate for all dimensions: extra variables
    # enter only by independent cubes.  Two representatives suffice because
    # the formula for every additional derivative is w_i^2.
    u, v, w = sp.symbols('u v w')
    variables = (x, y, z, u, v, w)
    witness = sum(t**3 for t in variables)/3 + u*x*y + v*y*z
    def ell(poly):
        f = sp.Poly(sp.expand(poly), *variables)
        return (f.coeff_monomial(v*x*x)+f.coeff_monomial(u*z*z)
                - f.coeff_monomial(u*v*y))
    for left in variables:
        for right in variables:
            assert ell(left*sp.diff(witness, right)) == 0
    for i in range(4):
        for j in range(4-i):
            assert ell(u**i*v**j*w**(3-i-j)) == 0
    witness_I = sp.expand(I0.subs({A:u, B:v, C:0, D:0, E:0, H:0}))
    assert ell(witness_I) == -sp.Rational(20, 3)
    assert ell(u*v*y/9) == -sp.Rational(1, 9)
    print('PASS: exact uniform obstruction functional ell(Delta4)=-1/9')
    print('NOT CHECKED: graph integration, centrality, formality existence, MF equivalence')


if __name__ == '__main__':
    verify_classical_covariants()
    verify()
