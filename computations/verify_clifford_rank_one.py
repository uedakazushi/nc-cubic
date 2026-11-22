#!/usr/bin/env python3
"""Exact rank-one slice and Azumaya A2 local equations (2026-11-23/v65).

No floating point, interpolation, or random samples. The residual categorical
conclusion uses the graded localization and gluing proofs in the manuscript.
"""

import sympy as sp


def zero(expr):
    assert sp.expand(expr) == 0, sp.factor(expr)


def clifford_matrix(diagonal, off):
    return sp.Matrix([[diagonal[0],off[2]/2,off[1]/2],
                      [off[2]/2,diagonal[1],off[0]/2],
                      [off[1]/2,off[0]/2,diagonal[2]]])


def main():
    t1,t2,lam,mu,U,V = sp.symbols("t1 t2 lam mu U V")
    rho,sigma = sp.symbols("rho sigma")
    u = (U,t1*rho*U,t1*rho**2*U)
    v = (V,t2*sigma*V,t2*sigma**2*V)
    equations = [u[a]**2-t1*u[(a+1)%3]*u[(a+2)%3] + (mu*v[1]*v[2] if a==0 else 0) for a in range(3)]
    equations += [v[b]**2-t2*v[(b+1)%3]*v[(b+2)%3] + (lam*u[1]*u[2] if b==0 else 0) for b in range(3)]
    rel = sp.groebner([rho**3-1,sigma**3-1],rho,sigma,domain=sp.QQ.frac_field(t1,t2,lam,mu,U,V))
    reduced = [sp.expand(rel.reduce(sp.expand(e))[1]) for e in equations]
    expected_reduced = [(1-t1**3)*U**2+mu*t2**2*V**2,0,0,
                        lam*t1**2*U**2+(1-t2**3)*V**2,0,0]
    for actual, expected in zip(reduced, expected_reduced):
        zero(actual-expected)
    h = (1-t1**3)*(1-t2**3)-t1**2*t2**2*lam*mu
    zero(sp.Matrix([[1-t1**3,mu*t2**2],[lam*t1**2,1-t2**3]]).det()-h)
    print("PASS 1: nonzero projective branches and their exact two-by-two determinant.")

    tau = sp.symbols("tau", nonzero=True)
    X = sp.symbols("X1 X2 X3"); Y = sp.symbols("Y1 Y2 Y3")
    px = [-tau*X[i] + (-3*tau*Y[0] if i==0 else 0) for i in range(3)]
    py = [-tau*Y[i] + (-3*tau*X[0] if i==0 else 0) for i in range(3)]
    qx,qy = clifford_matrix(X,px),clifford_matrix(Y,py)
    D = sp.expand(qy.det()-qx.det())
    point = dict(zip(X+Y,(1,0,0,1,0,0)))
    zero(qx.det().subs(point)+4*tau**2)
    zero(qy.det().subs(point)+4*tau**2)
    zero(D.subs(point))
    for z in X+Y:
        zero(sp.diff(D,z).subs(point))
    print("PASS 2: a singular norm point with two nondegenerate Clifford forms for all allowed tau.")

    t = sp.symbols("t")
    local = sp.expand(D.subs({Y[0]:1,X[0]:1+t}))
    s = tau**3
    expected = (tau**2*(t**3+X[1]**3+X[2]**3-Y[1]**3-Y[2]**3)/4
                +(s-1+(s/4-1)*t)*X[1]*X[2]
                -(s-1+3*s*t/4)*Y[1]*Y[2])
    zero(local-expected)
    transverse = (X[1],X[2],Y[1],Y[2])
    section = dict.fromkeys(transverse,0)
    for z in transverse:
        zero(sp.diff(local,z).subs(section))
    zero(local.subs(section)-tau**2*t**3/4)
    zero(sp.hessian(local,transverse).subs(section).subs(t,0).det()-(s-1)**4)
    print("PASS 3: exact local cubic, nondegenerate transverse Hessian, and A2 critical section.")

    specialized_h = h.subs({t1:tau,t2:tau,lam:-3*tau,mu:-3*tau})
    zero(specialized_h+(4*s-1)*(2*s+1))
    c = tau**2*(1-s)**2
    assert specialized_h.subs(tau,2) == -527
    assert c.subs(tau,2) == 196
    assert qx.det().subs(point).subs(tau,2) == -16
    print("PASS 4: ambient regularity exceptions and the explicit tau=2 values h=-527, c=196.")
    print("4 PASS. LIMIT: local equations only; Azumaya/graded/residual implications need the manuscript.")


if __name__ == "__main__":
    main()
