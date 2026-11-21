#!/usr/bin/env python3
"""Exact second central action on two-dimensional simple modules.

2026-11-22 / v45.  Dependency: SymPy.  Run with Python 3; --universal
adds a symbolic verification over QQ(a,b), c=-1/b, r=1 (several minutes).
--zero-example verifies a cubic-field 2D simple with zero second action
and checks that no one-dimensional representation has its central value.
The two coefficient triples are (1,4,9) and (16,25,49).  We compute after
homothety over QQ(sqrt(-11)) and QQ(sqrt(35351)), then rescale the second
action by s^3.  The generator in Ext^0 and the representative in Ext^3
are both the identity in End(M), using the ordered generator x,y,z.

Every free differential and higher-homotopy identity is verified by exact
linear algebra in the indicated number field.  No numerical approximation
or interpolation is used.  Filtered exactness, Shamash exactness, homotopy
transfer in all degrees and projective dimension are proved in the paper;
the finite calculations do not independently prove those statements or
global smoothness of the central quotient.
"""
from functools import lru_cache
from itertools import product, permutations
import argparse
import sympy as sp

Q = sp.QQ


def add(*items):
    ans = {}
    for item in items:
        for w, c in item.items():
            ans[w] = ans.get(w, Q.zero) + c
    return {w:c for w,c in ans.items() if c}


def scale(c, p):
    return {w:Q.convert(c)*d for w,d in p.items() if c*d}


def mul(p, q):
    ans = {}
    for v,c in p.items():
        for w,d in q.items():
            ans[v+w] = ans.get(v+w,Q.zero) + c*d
    return {w:c for w,c in ans.items() if c}


def eye_poly(p,n):
    return [[p if i==j else {} for j in range(n)] for i in range(n)]


def matadd(*items):
    return [[add(*(item[i][j] for item in items)) for j in range(len(items[0][0]))]
            for i in range(len(items[0]))]


def matneg(A):
    return [[scale(-1,p) for p in row] for row in A]


def matmul(A,B):
    return [[add(*(mul(A[i][k],B[k][j]) for k in range(len(B))))
             for j in range(len(B[0]))] for i in range(len(A))]


class Algebra:
    def __init__(self,alpha):
        self.alpha = tuple(map(Q.convert,alpha))
        self.relations = []
        for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
            self.relations.append({(j,k):Q.one,(k,j):-Q.one,(i,i):-Q.one,():self.alpha[i]})

    @lru_cache(None)
    def reducer(self,degree):
        words = tuple(w for d in range(degree,-1,-1) for w in product(range(3),repeat=d))
        pos = {w:i for i,w in enumerate(words)}
        rows = []
        for extra in range(degree-1):
            for l in range(extra+1):
                for v in product(range(3),repeat=l):
                    for w in product(range(3),repeat=extra-l):
                        for rel in self.relations:
                            row = {}
                            for u,c in rel.items():
                                if c:
                                    row[pos[v+u+w]] = row.get(pos[v+u+w],Q.zero)+c
                            rows.append(row)
        if rows:
            dm = sp.polys.matrices.DomainMatrix.from_dod(dict(enumerate(rows)),(len(rows),len(words)),Q)
            rr,piv = dm.rref()
            rr = rr.to_dod()
        else:
            rr,piv = {},()
        pivmap = {p:i for i,p in enumerate(piv)}
        free = tuple(i for i in range(len(words)) if i not in pivmap)
        basis = tuple(words[i] for i in free)
        red = {}
        for i,w in enumerate(words):
            if i in pivmap:
                row = rr[pivmap[i]]
                red[w] = {words[j]:-row[j] for j in free if j in row and row[j]}
            else:
                red[w] = {w:Q.one}
        assert len(basis)==(degree+1)*(degree+2)*(degree+3)//6
        def reduce(p):
            return add(*(scale(c,red[w]) for w,c in p.items()))
        return basis,reduce

    def reduce_matrix(self,A,degree):
        _,red = self.reducer(degree)
        return [[red(p) for p in row] for row in A]

    def equal(self,A,B,degree):
        C = self.reduce_matrix(matadd(A,matneg(B)),degree)
        assert all(not p for row in C for p in row),C

    def rightdivide(self,A,B,degree,outdegree):
        """Return X with X B=A and entries of filtered degree <=degree."""
        basis,_ = self.reducer(degree)
        outbasis,red = self.reducer(outdegree)
        pos = {w:i for i,w in enumerate(outbasis)}
        nin,nout,nrhs = len(B),len(B[0]),len(A)
        nw,no = len(basis),len(outbasis)
        nvar = nin*nw
        nrow = nout*no
        rows = {}
        for j in range(nin):
            for u,w in enumerate(basis):
                col = j*nw+u
                for k in range(nout):
                    p = red(mul({w:Q.one},B[j][k]))
                    for v,c in p.items():
                        rows.setdefault(k*no+pos[v],{})[col] = c
        for i,row in enumerate(A):
            for k,p in enumerate(row):
                for w,c in red(p).items():
                    rows.setdefault(k*no+pos[w],{})[nvar+i] = c
        dm = sp.polys.matrices.DomainMatrix.from_dod(rows,(nrow,nvar+nrhs),Q)
        rr,piv = dm.rref()
        assert all(p<nvar for p in piv),('inconsistent',nvar,piv)
        rr = rr.to_dod()
        result = [[{} for _ in range(nin)] for _ in range(nrhs)]
        for k,col in enumerate(piv):
            j,u = divmod(col,nw)
            for i in range(nrhs):
                value = rr[k].get(nvar+i,Q.zero)
                if value:
                    result[i][j][basis[u]] = value
        self.equal(matmul(result,B),A,outdegree)
        return result


def blocks(blockrows):
    n=len(blockrows[0][0]); m=len(blockrows[0][0][0])
    return [[blockrows[br][bc][i][j] for bc in range(len(blockrows[br])) for j in range(m)]
            for br in range(len(blockrows)) for i in range(n)]


def setup(a,b,c,r):
    a,b,c,r = map(sp.sympify,(a,b,c,r))
    assert sp.simplify(r*r+b*c) == 0 and a*b*c != 0
    I=sp.eye(2)
    reps=[a*I+sp.diag(r,-r),b*I+sp.Matrix([[0,1],[-c*a,0]]),
          c*I+sp.Matrix([[0,r/c],[r*a,0]])]
    alpha=[a*a-b*c,b*b-c*a,c*c-a*b]
    alg=Algebra(alpha)
    shifted=[]; diag=[]
    for j in range(3):
        R=reps[j].T
        shifted.append([[add({(j,):Q.one} if u==v else {},{():-Q.convert(R[u,v])})
                         for v in range(2)] for u in range(2)])
        diag.append([[add({(j,):-Q.one} if u==v else {},{():-Q.convert(R[u,v])})
                      for v in range(2)] for u in range(2)])
    A,B,C=shifted
    d1=blocks([[A],[B],[C]])
    d2=blocks([[diag[0],matneg(C),B],[C,diag[1],matneg(A)],[matneg(B),A,diag[2]]])
    d3=blocks([[A,B,C]])
    central={}
    for j in range(3):
        central=add(central,{(j,j,j):Q.convert(sp.Rational(1,3)),(j,):-Q.convert(alpha[j])})
    for p in permutations(range(3)):
        central=add(central,{p:-Q.convert(sp.Rational(1,9))})
    lam=-sp.Rational(2,3)*(a**3+b**3+c**3+a*b*c)
    central=add(central,{():-Q.convert(lam)})
    alg.equal(matmul(d2,d1),[[{} for _ in range(2)] for _ in range(6)],2)
    alg.equal(matmul(d3,d2),[[{} for _ in range(6)] for _ in range(2)],2)
    return alg,reps,(d1,d2,d3),central,lam


def eval_hom(A,reps):
    """Hom(A,M) map: each noncommutative entry acts on a column in M."""
    reps=[sp.polys.matrices.DomainMatrix.from_Matrix(R).convert_to(Q) for R in reps]
    ans={}
    for i,row in enumerate(A):
        for j,p in enumerate(row):
            val=sp.polys.matrices.DomainMatrix.zeros((2,2),Q)
            for w,c in p.items():
                m=sp.polys.matrices.DomainMatrix.eye(2,Q)
                for k in w:
                    m=m*reps[k]
                val=val+m.scalarmul(c)
            for u,rw in val.to_dod().items():
                for v,c in rw.items():
                    if c:
                        ans.setdefault(2*i+u,{})[2*j+v]=c
    return sp.polys.matrices.DomainMatrix.from_dod(ans,(2*len(A),2*len(A[0])),Q)


def second_action(a,b,c,r):
    alg,reps,d,f,lam=setup(a,b,c,r)
    d1,d2,d3=d
    h0=alg.rightdivide(eye_poly(f,2),d1,2,3)
    h1=alg.rightdivide(matadd(eye_poly(f,6),matneg(matmul(d1,h0))),d2,2,3)
    h2=alg.rightdivide(matadd(eye_poly(f,6),matneg(matmul(d2,h1))),d3,2,3)
    alg.equal(matmul(d3,h2),eye_poly(f,2),3)
    g=alg.rightdivide(matneg(matmul(h0,h1)),d3,3,4)
    alg.equal(matmul(d1,g),matneg(matmul(h1,h2)),4)
    print('PASS: exact free differential and all higher-homotopy identities',flush=True)

    D=[eval_hom(x,reps) for x in d]
    H=[eval_hom(x,reps) for x in (h0,h1,h2)]
    G=eval_hom(g,reps)
    assert (D[1]*D[0]).is_zero_matrix
    assert (D[2]*D[1]).is_zero_matrix
    ranks=[len(x.rref()[1]) for x in D]
    assert ranks==[3,9,3]
    # H^3 is represented by the vectorized identity.  P_3 has basis indexed
    # by M^*, so Hom(P_3,M) is End(M).  Trace is the projection onto H^0.
    top=sp.polys.matrices.DomainMatrix.from_dod({0:{0:Q.one},3:{0:Q.one}},(4,1),Q)
    assert (D[0]*top).is_zero_matrix
    assert (top.transpose()*D[2]).is_zero_matrix
    assert (top.transpose()*top).to_Matrix()[0]==2
    # H2(top) is a degree-two cocycle and has a primitive in degree one.
    rhs=H[2]*top
    assert (D[2]*rhs).is_zero_matrix
    rr,piv=D[1].hstack(rhs).rref()
    assert all(p<12 for p in piv)
    rd=rr.to_dod()
    middle=sp.polys.matrices.DomainMatrix.from_dod(
        {p:{0:rd[i][12]} for i,p in enumerate(piv) if rd[i].get(12)},(12,1),Q)
    out=G*top-H[0]*middle
    # The transfer to H^0 must be a cocycle.
    assert (D[0]*out).is_zero_matrix
    kappa=out.to_dod().get(0,{}).get(0,Q.zero)
    assert (out-top.scalarmul(kappa)).is_zero_matrix
    kappa=sp.factor(Q.to_sympy(kappa))
    print(f'PASS: ambient ranks={ranks}, identity-normalized second action={kappa}',flush=True)
    return kappa


def zero_action_example():
    """A rigid 2D simple detects a central singularity invisible to 1D ones."""
    global Q
    t=sp.Symbol('t')
    p=t**3-2*t*t-11*t+8
    assert sp.Poly(p,t).is_irreducible
    assert sp.gcd(p,t*(t*t+3)*(1-t**4))==1
    N=(t**6-26*t**4+153*t*t-64)
    assert sp.expand(N-p*(t**3+2*t*t-11*t-8))==0
    a=sp.CRootOf(p,0)
    Q=sp.QQ.algebraic_field(a)
    assert second_action(a,1,-1,1)==0
    alpha=(t*t+1,t+1,1-t)
    basis=tuple(product(range(2),repeat=3))
    positions={e:i for i,e in enumerate(basis)}

    def multiplication(terms):
        mat=sp.zeros(8)
        for j,e in enumerate(basis):
            for word,coefficient in terms:
                powers=tuple(e[i]+word[i] for i in range(3))
                coefficient*=sp.prod(alpha[i]**(powers[i]//2) for i in range(3))
                mat[positions[tuple(n%2 for n in powers)],j]+=coefficient
        return mat

    # Numerator of kappa_1, in the 8-dimensional square-root algebra.
    kappa_terms=[((1,1,0),alpha[0]*alpha[1]),
                 ((0,1,1),alpha[1]*alpha[2]),
                 ((1,0,1),alpha[2]*alpha[0]),
                 ((0,0,0),9*sp.prod(alpha))]
    # -3/2 times (lambda_1-lambda_2).
    lambda_terms=[((1,0,0),alpha[0]),((0,1,0),alpha[1]),
                  ((0,0,1),alpha[2]),((1,1,1),1),
                  ((0,0,0),-(t**3-t))]
    for name,terms in [('all character second actions are nonzero',kappa_terms),
                       ('no character has the 2D central value',lambda_terms)]:
        determinant=multiplication(terms).det(method='domain-ge')
        assert sp.gcd(sp.Poly(determinant,t),sp.Poly(p,t)).degree()==0
        print(f'PASS: cubic-field obstruction: {name}',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--universal',action='store_true')
    parser.add_argument('--zero-example',action='store_true')
    args=parser.parse_args()
    cases = [
        ((1,4,9),(-5,1,11),sp.sqrt(-11),14,
         sp.Rational(5188576,3087),1297144*sp.sqrt(14)/151263),
        ((16,25,49),(-323,-53,667),sp.sqrt(35351),8730,
         sp.Rational(8803255656465568,19053225),
         2200813914116392*sp.sqrt(970)/121008460966875),
    ]
    for alpha,(a,b,c),r,scale_squared,expected,original in cases:
        Q=sp.QQ.algebraic_field(r)
        assert (a*a-b*c,b*b-c*a,c*c-a*b)==tuple(scale_squared*x for x in alpha)
        actual=second_action(a,b,c,r)
        assert actual==expected and actual!=0
        assert sp.simplify(actual/(scale_squared*sp.sqrt(scale_squared))-original)==0
        print(f'PASS: alpha={alpha}, kappa={original} is nonzero',flush=True)
    if args.universal:
        a,b=sp.symbols('a b',nonzero=True)
        c=-1/b
        Q=sp.QQ.frac_field(a,b)
        print('START: universal higher homotopies over QQ(a,b), c=-1/b, r=1',flush=True)
        actual=second_action(a,b,c,1)
        cubic=a**3+b**3+c**3-3*a*b*c
        sextic=(a**6+b**6+c**6+66*((a*b)**3+(b*c)**3+(c*a)**3)
                +26*a*b*c*(a**3+b**3+c**3)+153*a*a*b*b*c*c)
        assert sp.cancel(actual+sp.Rational(2,9)*sextic/cubic)==0
        print('PASS: universal kappa = -2*N_6(a,b,c)/(9*F(a,b,c)); no interpolation',flush=True)
    if args.zero_example:
        zero_action_example()
