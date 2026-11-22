#!/usr/bin/env python3
"""Exact h=1 matrix factorization and finite curved contraction for D=B^sigma.

Python 3 and SymPy are required.  Run from any directory:
    python3 computations/verify_mixed_curved_dual.py

The program constructs the rank 64+64 Shamash stabilization of k_R for
R=D/(Omega_1+100 Omega_2), then contracts its constant differential to a
rank 40+40 graded matrix factorization.  It checks the full curvature,
both comparison maps, retraction, and homotopy over the actual noncommutative
algebra using exact rational arithmetic.  It also checks why a strict
Clifford pairing on the unchanged quadratic dual cannot encode -vL.

The deterministic boundary lifts use finite homogeneous relation spaces,
not numerical sampling or truncation of the h-adic formal equivalence.
The construction is at h=1.  It does not give a kernel to a commutative
cubic threefold or perform a Knorrer/Morita elimination of the pair (v,L).

Optional --export PATH writes the actual rational matrices as JSON for
subsequent kernel and restriction computations.  This generated output
need not be tracked: the matrices are reproduced by this script.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, permutations
from pathlib import Path
import time
import sympy as sp

import verify_mixed_invariant_pbw_dual as old

def tidy(a):
    return {k: v for k, v in a.items() if v}

def add(*vs):
    a = defaultdict(Q)
    for v in vs:
        for k, c in v.items(): a[k] += c
    return tidy(a)

def scale(v, c):
    return tidy({k: c*x for k, x in v.items()})

def minus_inplace(a, b, c):
    for k,v in b.items():
        z = a.get(k, 0) - c*v
        if z: a[k] = z
        elif k in a: del a[k]

class OneRing:
    def __init__(self, alpha):
        self.alpha = alpha
    @lru_cache(None)
    def reducer(self, n):
        mons = [(r, ''.join(w)) for r in range(n//2+1)
                for w in product('xyz', repeat=n-2*r)]
        pos = {m:i for i,m in enumerate(mons)}
        echelon = {}
        for r in range(n//2+1):
            m = n - 2*r
            for p in range(max(0,m-1)):
                for left in product('xyz', repeat=p):
                    for right in product('xyz', repeat=m-2-p):
                        l, rr = ''.join(left), ''.join(right)
                        for x,y,z,a in [('x','y','z',self.alpha[0]),
                                        ('y','z','x',self.alpha[1]),
                                        ('z','x','y',self.alpha[2])]:
                            row = add({pos[r,l+y+z+rr]:Q(1)},
                                      {pos[r,l+z+y+rr]:Q(-1)},
                                      {pos[r,l+x+x+rr]:Q(-1)},
                                      {pos[r+1,l+rr]:Q(a)})
                            while row:
                                k = min(row)
                                if k not in echelon:
                                    row = scale(row, 1/row[k])
                                    echelon[k] = row
                                    break
                                minus_inplace(row, echelon[k], row[k])
        free = tuple(m for i,m in enumerate(mons) if i not in echelon)
        def reduce(poly):
            row = {pos[m]:Q(c) for m,c in poly.items() if c}
            for pivot, erow in sorted(echelon.items()):
                if pivot in row: minus_inplace(row, erow, row[pivot])
            return {mons[i]:c for i,c in row.items()}
        return free, reduce
    def basis(self,n):
        if n<0: return ()
        return self.reducer(n)[0]
    def normal(self,p):
        pieces=defaultdict(dict)
        for (r,w),c in p.items(): pieces[2*r+len(w)][r,w]=c
        return add(*(self.reducer(n)[1](v) for n,v in pieces.items()))
    def mul(self,a,b):
        out=defaultdict(Q)
        for (r,w),c in a.items():
            for (s,z),d in b.items(): out[r+s,w+z]+=c*d
        return self.normal(out)

class ManyRing:
    def __init__(self, alphas):
        self.blocks=tuple(OneRing(a) for a in alphas)
        self.nblocks=len(alphas)
        self.one=(0,)+('',)*self.nblocks
    @lru_cache(None)
    def basis(self,n):
        if n<0:return ()
        # Quotient echelon keeps v last, hence the pure free words form a
        # C[v]-basis. The count is also checked independently.
        out=[]
        def rec(rem,b,ws):
            if b==self.nblocks:
                if rem==0:out.append(tuple(ws))
                return
            for d in range(rem+1):
                for v,w in self.blocks[b].basis(d):
                    if v==0:rec(rem-d,b+1,ws+[w])
        for r in range(n//2+1):
            start=len(out);rec(n-2*r,0,[])
            for j in range(start,len(out)):out[j]=(r,)+out[j]
        return tuple(out)
    @lru_cache(None)
    def monmul(self,a,b):
        out={(a[0]+b[0],):Q(1)}
        for j,ring in enumerate(self.blocks):
            piece=ring.normal({(0,a[j+1]+b[j+1]):1})
            nxt=defaultdict(Q)
            for prefix,c in out.items():
                for (r,w),d in piece.items():
                    nxt[(prefix[0]+r,)+prefix[1:]+(w,)]+=c*d
            out=tidy(nxt)
        return out
    def mul(self,a,b):
        out=defaultdict(Q)
        for x,c in a.items():
            for y,d in b.items():
                for z,e in self.monmul(x,y).items():out[z]+=c*d*e
        return tidy(out)
    def var(self,b,j):
        if j==3:return {(1,)+('',)*self.nblocks:Q(1)}
        ws=['']*self.nblocks;ws[b]='xyz'[j]
        return {(0,)+tuple(ws):Q(1)}
    def omega(self,weights):
        out={}
        for b,(ring,q) in enumerate(zip(self.blocks,weights)):
            for j in range(3):
                x=self.var(b,j)
                out=add(out,scale(self.mul(self.mul(x,x),x),Q(q,3)),
                        scale(self.mul(self.var(b,3),x),-q*ring.alpha[j]))
            for perm in permutations(range(3)):
                term={self.one:Q(1)}
                for j in perm:term=self.mul(term,self.var(b,j))
                out=add(out,scale(term,Q(-q,9)))
        return out

class Koszul:
    def __init__(self, alphas):
        self.alphas=alphas
        self.ring=ManyRing(alphas)
        self.nb=len(alphas)
        self.basis=tuple((ws,e) for ws in product(old.ONE_BASIS,repeat=self.nb)
                         for e in (0,1))
        self.pos={a:i for i,a in enumerate(self.basis)}
        self.deg=[sum(map(len,ws))+e for ws,e in self.basis]
        self.wt=[sum(map(len,ws))+2*e for ws,e in self.basis]
        self.bydeg={i:tuple(j for j,d in enumerate(self.deg) if d==i)
                    for i in range(3*self.nb+2)}
        self.top=3*self.nb+1
        self.unit=self.pos[(('',)*self.nb,0)]
        self.eps=self.pos[(('',)*self.nb,1)]
        self.q={}
        for b,alpha in enumerate(alphas):
            for letter,a in zip('abc',alpha):
                for word,c in old.NORMAL[letter*2].items():
                    ws=['']*self.nb;ws[b]=word
                    self.q=add(self.q,{self.pos[tuple(ws),0]:-a*Q(c)})
        self.d={i:{} for i in range(len(self.basis))}
        for target,(ws,e) in enumerate(self.basis):
            for b in range(self.nb):
                for j,letter in enumerate('abc'):
                    gs=['']*self.nb;gs[b]=letter
                    sourcevec=self.emul({self.pos[tuple(gs),0]:1},{target:1})
                    for source,c in sourcevec.items():
                        self.d[source]=add(self.d[source],self.mvec(target,self.ring.var(b,j),c))
            for source,c in self.emul({self.eps:1},{target:1}).items():
                self.d[source]=add(self.d[source],self.mvec(target,self.ring.var(0,3),c))
            if e:
                noeps=self.pos[ws,0]
                for source,c in self.emul({noeps:(-1)**sum(map(len,ws))},self.q).items():
                    self.d[source]=add(self.d[source],{(target,self.ring.one):c})
        self.lift_cache={}
    @lru_cache(None)
    def emonmul(self,ii,jj):
        aa,ae=self.basis[ii];bb,be=self.basis[jj]
        if ae+be>1:return {}
        exponent=ae*sum(map(len,bb))+sum(len(aa[j])*len(bb[k])
                                     for j in range(self.nb) for k in range(j))
        result={():Q((-1)**exponent)}
        for a,b in zip(aa,bb):
            piece=old.one_multiply({a:1},{b:1})
            result={prefix+(word,):c*Q(v) for prefix,c in result.items()
                    for word,v in piece.items()}
        return {self.pos[ws,ae+be]:c for ws,c in result.items()}
    def emul(self,a,b):
        out=defaultdict(Q)
        for i,c in a.items():
            for j,d in b.items():
                for k,e in self.emonmul(i,j).items():out[k]+=c*d*e
        return tidy(out)
    def mvec(self,i,p,c=1):return {(i,m):c*x for m,x in p.items() if c*x}
    def leftmul(self,p,v):
        out=defaultdict(Q)
        for a,c in p.items():
            for (i,b),d in v.items():
                for m,e in self.ring.monmul(a,b).items():out[i,m]+=c*d*e
        return tidy(out)
    def apply(self,mat,v):
        out={}
        for (i,m),c in v.items():out=add(out,self.leftmul({m:c},mat.get(i,{})))
        return out
    def compose(self,a,b):
        return {i:self.apply(a,v) for i,v in b.items()}
    def lift(self,i,weight,target):
        key=i,weight
        if key not in self.lift_cache:
            columns=[(j,m) for j in self.bydeg.get(i+1,())
                     for m in self.ring.basis(weight-self.wt[j])]
            imagebasis={}
            for j,m in columns:
                image=self.leftmul({m:1},self.d[j])
                preimage={(j,m):Q(1)}
                while image:
                    pivot=min(image)
                    if pivot not in imagebasis:
                        c=image[pivot]
                        imagebasis[pivot]=(scale(image,1/c),scale(preimage,1/c))
                        break
                    row,pre=imagebasis[pivot];c=image[pivot]
                    minus_inplace(image,row,c);minus_inplace(preimage,pre,c)
            self.lift_cache[key]=imagebasis
            print('lifting matrix',key,'cols',len(columns),'rank',len(imagebasis),flush=True)
        result={};work=dict(target)
        for pivot,(image,preimage) in sorted(self.lift_cache[key].items()):
            if pivot in work:
                c=work[pivot];minus_inplace(work,image,c)
                result=add(result,scale(preimage,c))
        if work:raise ValueError(('not boundary',key,work))
        assert self.apply(self.d,result)==target
        return result
    def shamash(self,weights):
        w=self.ring.omega(weights)
        sigmas=[self.d]
        assert all(not x for x in self.compose(self.d,self.d).values())
        print('PASS d squared zero',len(self.basis),flush=True)
        for n in range(1,(self.top+1)//2+1):
            sigma={}
            for i in range(self.top+1):
                for s in self.bydeg[i]:
                    target=self.mvec(s,w) if n==1 else {}
                    target=add(target,scale(self.apply(sigma,self.d[s]),-1))
                    for a in range(1,n):
                        target=add(target,scale(self.apply(sigmas[a],sigmas[n-a].get(s,{})),-1))
                    if target:
                        sigma[s]=self.lift(i+2*n-2,self.wt[s]+3*n,target)
                    else:sigma[s]={}
            sigmas.append(sigma)
            print('sigma',n,'entries',sum(map(len,sigma.values())),flush=True)
        for n in range(2*len(sigmas)-1):
            for s in range(len(self.basis)):
                result={}
                for a in range(len(sigmas)):
                    b=n-a
                    if 0<=b<len(sigmas):result=add(result,self.apply(sigmas[a],sigmas[b][s]))
                assert result==(self.mvec(s,w) if n==1 else {}),(n,s,result)
        print('PASS all Shamash equations',len(sigmas),flush=True)
        return sigmas


def contraction(k):
    size=len(k.basis)
    d=sp.zeros(size)
    for src,col in k.d.items():
        for (tar,mon),c in col.items():
            if mon==k.ring.one:d[tar,src]=c
    pivots=d.rref()[1]
    b=[d[:,p] for p in pivots]
    elts={}
    def independent(v):
        row={i:Q(c) for i,c in enumerate(v) if c}
        while row:
            pivot=min(row)
            if pivot not in elts:
                elts[pivot]=scale(row,1/row[pivot]);return True
            minus_inplace(row,elts[pivot],row[pivot])
        return False
    for v in b:assert independent(v)
    h=[v for v in d.nullspace() if independent(v)]
    l=[sp.eye(size)[:,p] for p in pivots]
    t=sp.Matrix.hstack(*(h+l+b));ti=t.inv()
    nh=len(h);r=len(l)
    canonical=sp.zeros(size)
    for j in range(r):canonical[nh+j,nh+r+j]=1
    hh=t*canonical*ti
    inc=t[:,:nh];proj=ti[:nh,:]
    assert d*hh+hh*d==sp.eye(size)-inc*proj
    assert hh*hh==sp.zeros(size) and proj*inc==sp.eye(nh)
    assert hh*inc==sp.zeros(size,nh) and proj*hh==sp.zeros(nh,size)
    def mat(m):
        return {s:{(a,k.ring.one):Q(m[a,s]) for a in range(m.rows) if m[a,s]}
                for s in range(m.cols)}
    # Original homological degree and epsilon give the finite filtration.
    for s in range(size):
        for a in range(size):
            if hh[a,s]:
                assert k.basis[s][1]==1 and k.basis[a][1]==0
                assert k.deg[a]==k.deg[s]+1
                assert k.wt[a]==k.wt[s]
    return nh,mat(d),mat(hh),mat(inc),mat(proj)

def matrix_add(*ms):
    keys=set().union(*(m.keys() for m in ms))
    return {key:add(*(m.get(key,{}) for m in ms)) for key in keys}
def matrix_scale(m,c):return {key:scale(v,c) for key,v in m.items()}
def matrix_equal(a,b):
    return all(a.get(i,{})==b.get(i,{}) for i in a.keys()|b.keys())
def identity(k,n):return {s:{(s,k.ring.one):Q(1)} for s in range(n)}

def transfer(k,ss):
    size=len(k.basis);start=time.time()
    nh,d0,h,inc,p=contraction(k)
    assert nh == 80
    homology_degrees = []
    homology_weights = []
    for source in range(nh):
        pairs = {(k.deg[target], k.wt[target]) for target, _ in inc[source]}
        assert len(pairs) == 1
        degree, weight = pairs.pop()
        homology_degrees.append(degree)
        homology_weights.append(weight)
    assert [homology_degrees.count(i) for i in range(8)] == [1,6,14,19,19,14,6,1]
    assert sum(degree % 2 == 0 for degree in homology_degrees) == 40
    print('PASS: constant contraction has rank 80, split into 40 even and 40 odd generators',flush=True)
    d=matrix_add(*ss)
    delta=matrix_add(d,matrix_scale(d0,-1))
    dh=k.compose(delta,h)
    term=identity(k,size);inv=term
    for j in range(1,5):
        term=k.compose(dh,term)
        count=sum(map(len,term.values()))
        print('(Delta h)^',j,'terms',count,flush=True)
        if j<4:inv=matrix_add(inv,matrix_scale(term,(-1)**j))
        else:assert not count
    print('PASS: finite inverse (1+Delta h)^(-1) terminates by the fourth power',flush=True)
    a=k.compose(inv,delta)
    ai=k.compose(a,inc);ah=k.compose(a,h)
    ii=matrix_add(inc,matrix_scale(k.compose(h,ai),-1))
    pp=matrix_add(p,matrix_scale(k.compose(p,ah),-1))
    hh=matrix_add(h,matrix_scale(k.compose(h,ah),-1))
    dd=k.compose(p,ai)
    # Check the actual grading of the reduced periodic matrices, not only
    # the uncurved cohomology dimensions.
    folded_weights=[w-3*(d//2) for d,w in zip(homology_degrees,homology_weights)]
    for source,vector in dd.items():
        for (target,monomial),coefficient in vector.items():
            assert (homology_degrees[source]-homology_degrees[target]) % 2 == 1
            weight=2*monomial[0]+sum(map(len,monomial[1:]))
            assert weight == folded_weights[source]-folded_weights[target]+(
                3 if homology_degrees[source] % 2 == 0 else 0)
    w=k.ring.omega((1,100))
    scalar={s:k.mvec(s,w) for s in range(nh)}
    checks=[('reduced curvature',k.compose(dd,dd),scalar),
            ('inclusion',k.compose(d,ii),k.compose(ii,dd)),
            ('projection',k.compose(pp,d),k.compose(dd,pp)),
            ('retraction',k.compose(pp,ii),identity(k,nh)),
            ('homotopy',matrix_add(k.compose(d,hh),k.compose(hh,d)),
                         matrix_add(identity(k,size),matrix_scale(k.compose(ii,pp),-1)))]
    for name,left,right in checks:
        assert matrix_equal(left,right),name
        print('PASS',name,flush=True)
    print('MF80 entries',sum(map(len,dd.values())),flush=True)
    print('seconds',time.time()-start,flush=True)
    return (dd,ii,pp,hh)


def check_grading(k, ss):
    for n, matrix in enumerate(ss):
        for source, vector in matrix.items():
            for (target, monomial), coefficient in vector.items():
                weight = 2 * monomial[0] + sum(map(len, monomial[1:]))
                assert k.deg[target] == k.deg[source] + 2*n - 1
                assert weight == 3*n + k.wt[source] - k.wt[target]
    assert all(not v for matrix in ss[3:] for v in matrix.values())
    print("PASS: internal grading and homological shifts; sigma_3=sigma_4=0", flush=True)


def check_strict_pairing_obstruction():
    # An odd derivation with da=A, db=B, dc=C must preserve bc+a^2=0,
    # ca+b^2=0, ab+c^2=0. Their derivatives force all three scalars to vanish.
    a, b, c = sp.symbols("A B C")
    equations = sp.Matrix([b, -c, c, -a, a, -b])
    assert equations.jacobian([a, b, c]).rank() == 3
    print("PASS: unchanged S! admits no nonzero scalar-valued odd contraction", flush=True)


def export_matrices(path, k, ss, transferred):
    import json
    def encode(matrix):
        return [[source, target, list(monomial), coefficient.numerator,
                 coefficient.denominator]
                for source, vector in sorted(matrix.items())
                for (target, monomial), coefficient in sorted(vector.items())]
    reduced, inclusion, projection, homotopy = transferred
    reduced_basis=[]
    for source in range(len(reduced)):
        vector={target:coefficient for (target,monomial),coefficient in inclusion[source].items()
                if monomial == k.ring.one}
        gradings={(k.deg[target],k.wt[target]) for target in vector}
        assert len(gradings)==1
        degree,weight=gradings.pop()
        reduced_basis.append({"homological_degree":degree,"internal_weight":weight,
                              "constant_inclusion":[[target,c.numerator,c.denominator]
                                                    for target,c in sorted(vector.items())]})
    data = {
        "alphas": k.alphas,
        "block_weights": [1, 100],
        "basis_128": [[list(words), epsilon] for words, epsilon in k.basis],
        "basis_degree": k.deg,
        "basis_internal_weight": k.wt,
        "basis_80": reduced_basis,
        "coefficient_convention": "left D-modules; composition multiplies source coefficient first",
        "right_model": "K^r_i=Hom_D(K_{7-i},D)(-8); transpose sigma, exchange inclusion/projection",
        "monomial_convention": "[v_exponent, first_block_word, second_block_word]",
        "sigma": [encode(matrix) for matrix in ss],
        "reduced_differential": encode(reduced),
        "inclusion": encode(inclusion),
        "projection": encode(projection),
        "homotopy": encode(homotopy),
    }
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"Exported reproducible matrix data to {destination}", flush=True)


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export", help="optional JSON matrix export")
    args = parser.parse_args()
    started = time.time()
    k = Koszul(((1, 4, 9), (16, 25, 49)))
    # Check the expected homogeneous basis sizes actually used in the lifts.
    for n in range(6):
        expected = sum(sp.binomial(n-2*r+5, 5) for r in range(n//2+1))
        assert len(k.ring.basis(n)) == expected
    print("PASS: coefficient-ring quotient bases through internal degree five", flush=True)
    sigmas = k.shamash((1, 100))
    check_grading(k, sigmas)
    transferred = transfer(k, sigmas)
    check_strict_pairing_obstruction()
    if args.export:
        export_matrices(args.export, k, sigmas, transferred)
    print(f"Elapsed seconds: {time.time()-started:.3f}", flush=True)
    print("Scope: actual stabilized residue generator and finite curved contraction at h=1; "
          "commutative comparison kernel and derived (v,L) elimination remain unconstructed.", flush=True)


if __name__ == "__main__":
    main()
