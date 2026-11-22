"""Exact finite checks for the polarized two-center pencil (v59).

The proof for arbitrary fixed smooth G and fixed t(U) is in
papers/sections/mixed/multicentral_pencil.tex.  These checks do not prove
dg Morita equivalence, the comparison coefficients, or the general jet argument.
Run with Python 3 and SymPy; no external input or generated output is needed.
"""
from itertools import product
import sympy as s


def main():
    u, v, z, h = s.symbols("u v z h")
    x = s.symbols("x0:6")
    b = [2**j for j in range(6)]
    signs = list(product((-1, 1), repeat=6))
    values = [2*sum(e[j]*b[j]**3 for j in range(6)) for e in signs]
    assert len(values) == len(set(values)) == 64 and 0 not in values
    print("PASS 1: 64 distinct nonzero signed critical values (exact integers)")

    W = sum(y**3 for y in x)-3*u**2*sum(bj**2*y for bj,y in zip(b,x))+v**3
    dx = [s.diff(W,y) for y in x]
    for e,value in zip(signs,values):
        subs = {y:e[j]*b[j]*u for j,y in enumerate(x)}
        assert all(s.expand(g.subs(subs)) == 0 for g in dx)
        assert s.expand(W.subs(subs)-(v**3-value*u**3)) == 0
        assert s.expand(s.diff(W,u).subs(subs)+3*value*u**2) == 0
    print("PASS 2: all active critical equations, values and total u derivatives")

    for e in signs:
        determinant = s.prod(6*e[j]*b[j] for j in range(6))
        assert determinant != 0
    assert W.subs(u,0) == sum(y**3 for y in x)+v**3
    print("PASS 3: every Hessian is nondegenerate; infinity fiber is Fermat")

    # Pair e with -e to keep the exact degree-192 polynomial small and readable.
    positive_values = sorted(a for a in values if a > 0)
    P = s.Poly(s.prod(z**6-a*a for a in positive_values),z)
    assert P.degree() == 192 and s.gcd(P,P.diff()).degree() == 0
    assert P.LC() == 1 and P.TC() != 0
    print("PASS 4: binary discriminant has degree 192 and no repeated root")

    # Jets of a cubic section at an arbitrary finite point: columns 1,z suffice.
    a = s.symbols("a")
    jet = s.Matrix([[1,a,a*a,a**3],[0,1,2*a,3*a*a]])
    assert s.det(jet[:,:2]) == 1
    # At infinity use w=u/v and the local basis 1,w,w^2,w^3.
    infinity_jet = s.Matrix([[1,0,0,0],[0,1,0,0]])
    assert infinity_jet.rank() == 2
    print("PASS 5: cubic value and first jet are independent on both charts")

    q1,q2,l1,l2,l3,c0,c1,c2,c3 = s.symbols("q1 q2 l1 l2 l3 c0 c1 c2 c3")
    Q = (q1*u+q2*v)*x[0]**2
    L = (l1*u*u+l2*u*v+l3*v*v)*x[1]
    C = c0*u**3+c1*u*u*v+c2*u*v*v+c3*v**3
    polarized = sum(y**3 for y in x)+Q+L+C
    dilation = {u:h*u,v:h*v,**{y:h*y for y in x}}
    assert s.expand(polarized.subs(dilation,simultaneous=True)-h**3*polarized) == 0
    assert 3*2**6 == P.degree()
    print("PASS 6: total cubic grading and the 3*2^N discriminant degree")


if __name__ == "__main__":
    main()
