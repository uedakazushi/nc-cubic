#!/usr/bin/env python3
"""Exact universal 9-parameter Shamash s1: P2->P3 at tau1=tau2=2.

Uses the verified sibling P1->P2 certificate and its rational 210-pivot gauge.
Constructs all 15 columns of G=G0+s G1(U)+s^2 G2(U) through the
336-pivot right inverse of d3_0, split into six x/y bidegree blocks.
Checks every 840-row PBW equation for 9 linear, 45 quadratic and 165
cubic coefficient monomials, without numerical specialization or fitting.
Only this middle homotopy is verified: not the full Shamash MF or Ku kernel.
"""
import runpy,time,itertools,collections
from pathlib import Path
from fractions import Fraction as F
import sympy as S
T=time.monotonic();R=runpy.run_path(str(Path(__file__).with_name('verify_clifford_mixed_shamash_first_middle.py')))
print('Loaded verified universal P1 first middle:',round(time.monotonic()-T,2),flush=True)
Cliff=R['Cliff'];Cliff.mul.__globals__['DEG']=5
add=R['add'];scale=R['scale'];zc=R['zc'];ZERO=R['ZERO']
B2keys=R['B2keys'];B3keys=R['B3keys'];B3I={k:i for i,k in enumerate(B3keys)}
B2= [zc(i) for i in range(6)]+[Cliff(ZERO,ZERO).word(*p) for p in itertools.combinations(range(6),2)]
assert len(B2)==21
K2p=[2]*3+[0]*3+[1]*9
K3p=[3,0]+[2]*9+[1]*9
rkeys=[('rx',a) for a in range(3)]+[('ry',b) for b in range(3)]+[('c',a,b) for a in range(3) for b in range(3)]
rindex={k:i for i,k in enumerate(rkeys)}

def cU(a):
 U=[[0]*3 for _ in range(3)];U[a//3][a%3]=1
 return U

def insert(d,key,p):d[key]=add(d.get(key,{}),p)

def syzygies(U,c):
 z=c.z
 def Ax(i,a):return scale(z[a],2) if i==a else z[next(k for k in range(3) if k not in (i,a))]
 def By(j,b):return scale(z[3+b],2) if j==b else z[3+next(k for k in range(3) if k not in (j,b))]
 def triple(i,j):
  k=next(t for t in range(3) if t not in (i,j))
  return [(i,k,1),(k,j,2),(j,i,4)]
 topx={('rx',a):z[a] for a in range(3)}
 for a,b in itertools.product(range(3),repeat=2):
  if U[a][b]:insert(topx,('c',a,b),{(1,(),(3+b,)):F(-U[a][b])})
 topy={('ry',b):z[3+b] for b in range(3)}
 out=[topx,topy]
 for a,b in itertools.product(range(3),repeat=2):
  h={('rx',a):z[3+b]}
  for i in range(3):insert(h,('c',i,b),scale(Ax(i,a),-1))
  for cc in range(3):
   if cc==b or not U[a][cc]:continue
   for j,l,w in triple(cc,b):insert(h,('ry',l),{(1,(),(3+j,)):F(U[a][cc]*w,7)})
  out.append(h)
 for b,a in itertools.product(range(3),repeat=2):
  h={('ry',b):z[a]}
  for j in range(3):insert(h,('c',a,j),By(j,b))
  out.append(h)
 return out

def xdeg(k):
 c,w=k
 return 2*sum(i<3 for i in c)+sum(i<3 for i in w)
indeg=[K3p[n]+xdeg(B2keys[k]) for n in range(20) for k in range(21)]
outdeg=[K2p[r]+xdeg(B3keys[k]) for r in range(15) for k in range(56)]
colblock={p:[i for i,d in enumerate(indeg) if d==p] for p in range(6)}
rowblock={p:[i for i,d in enumerate(outdeg) if d==p] for p in range(6)}

cl0=Cliff(ZERO,ZERO)
cldirs=[Cliff(cU(a),ZERO) for a in range(9)]

# Collect multiplication B2 * B1 -> B3 as mu0+s sum U_a*mu1_a.
M0={};M1=[{} for _ in range(9)]
for bb,b in enumerate(B2):
 for j in range(6):
  product=cl0.mul(b,cl0.z[j]);m0={B3I[(ce,w)]:v for (deg,ce,w),v in product.items() if deg==0}
  assert all(deg==0 for (deg,ce,w) in product)
  M0[bb,j]=m0
  for a,c in enumerate(cldirs):
   z=c.mul(b,c.z[j]);m1={B3I[(ce,w)]:v for (deg,ce,w),v in z.items() if deg==1}
   assert all(deg<=1 for (deg,ce,w) in z)
   assert {B3I[(ce,w)]:v for (deg,ce,w),v in z.items() if deg==0}==m0
   if m1:M1[a][bb,j]=m1
print('PASS A: B2*B1 PBW multiplication linear in all 9 independent U',round(time.monotonic()-T,2),flush=True)

# Right Koszul d2 = d20 + s sum U_a d21[a], explicit element as generator.
D20={};D21=[{} for _ in range(9)]
for cidx,col in enumerate(cl0.get_d2()):
 for gen,elem in enumerate(col):
  for (deg,ce,w),v in elem.items():
   assert deg==0 and not ce and len(w)==1
   D20[gen,cidx]=w[0],v
for a,c in enumerate(cldirs):
 for cidx,col in enumerate(c.get_d2()):
  for gen,elem in enumerate(col):
   for (deg,ce,w),v in elem.items():
    if deg==1:
     assert not ce and len(w)==1
     D21[a][gen,cidx]=w[0],v
    else:assert (w[0],v)==D20[gen,cidx]

# Syzygy d3 as 840x420 matrix D30 + s sum U_a D31[a].
def d3matrix(c,U):
 out=[collections.defaultdict(F) for _ in range(2)]
 for n,h in enumerate(syzygies(U,c)):
  for bb,b in enumerate(B2):
   col=n*21+bb
   for label,coeff in h.items():
    rel=rindex[label]
    for (deg,ce,w),v in c.mul(coeff,b).items():
     assert deg<2,('d3 contains higher s jet',n,label,deg)
     out[deg][rel*56+B3I[ce,w],col]+=v
 return [{k:v for k,v in part.items() if v} for part in out]
D30,_=d3matrix(cl0,ZERO)
D31=[]
for a,c in enumerate(cldirs):
 d0,d1=d3matrix(c,cU(a));assert d0==D30
 D31.append(d1)
for (r,c),v in D30.items():assert outdeg[r]==indeg[c]
for a in range(9):
 for (r,c),v in D31[a].items():assert indeg[c]==outdeg[r]+2
print('PASS B: full universal d3 action D30+s sum U_a D31_a, x-bidegree compatible',round(time.monotonic()-T,2),flush=True)

# H1 map P1 -> P2 is known exactly over all 9 U, coefficientwise.
H=[((),R['H0'])]+[((a,),R['H1'][a]) for a in range(9)]+[(pair,R['H2'][pair]) for pair in R['PAIR']]
# RHS R(s,U) = w I15 - H d2. Each h entry indexed rel*21+b2 and P1 gen.
# Accumulate dict coefficient monomial -> 15 vectors in B3^15.
RHS={}
def put(mono,source_col,index,coeff):
 if not coeff:return
 if mono not in RHS:RHS[mono]=[collections.defaultdict(F) for _ in range(15)]
 RHS[mono][source_col][index]+=coeff

# w stage0+stage1. w0 from a=0 direction at s0.
w0=cl0.get_u_w()[1]
for (deg,ce,w),val in w0.items():
 assert deg==0
 for cidx in range(15):put((),cidx,cidx*56+B3I[ce,w],val)
for a,c in enumerate(cldirs):
 for (deg,ce,w),val in c.get_u_w()[1].items():
  if deg==1:
   for cidx in range(15):put((a,),cidx,cidx*56+B3I[ce,w],val)

# H*d2: each H coefficient already represents s^len(mono) times U_mono.
for mono,HH in H:
 for gen in range(6):
  for ix,h in HH[gen].items():
   rel,bb=divmod(ix,21)
   for (g,cidx),(word,val) in D20.items():
    if g!=gen:continue
    for b3,mu in M0[bb,word].items():put(mono,cidx,rel*56+b3,-h*val*mu)
    for a in range(9):
     for b3,mu in M1[a].get((bb,word),{}).items():put(tuple(sorted(mono+(a,))),cidx,rel*56+b3,-h*val*mu)
   for a in range(9):
    for (g,cidx),(word,val) in D21[a].items():
     if g!=gen:continue
     m=tuple(sorted(mono+(a,)))
     for b3,mu in M0[bb,word].items():put(m,cidx,rel*56+b3,-h*val*mu)
     for b in range(9):
      for b3,mu in M1[b].get((bb,word),{}).items():put(tuple(sorted(m+(b,))),cidx,rel*56+b3,-h*val*mu)

for k in list(RHS):
 RHS[k]=[{r:v for r,v in col.items() if v} for col in RHS[k]]
RHS={k:v for k,v in RHS.items() if any(vv for vv in v)}
for k in range(5):print('RHS degree',k,'nonzero monomials:',sum(len(x)==k for x in RHS),'nonzero entries:',sum(len(v) for m,a in RHS.items() if len(m)==k for v in a),flush=True)
assert not any(len(m)>=4 for m in RHS),('RHS has degree >=4',[(m,sum(map(len,v))) for m,v in RHS.items() if len(m)>=4])
print('PASS C: all cubic and quartic source PBW products assembled exactly; order <=3',round(time.monotonic()-T,2),flush=True)

# One exact inverse per x-bidegree block, with rank [6,54,108,108,54,6].
block={};piv={}
for p in range(6):
 rows=rowblock[p];cols=colblock[p]
 ri={row:i for i,row in enumerate(rows)};ci={col:j for j,col in enumerate(cols)}
 mat=S.SparseMatrix(len(rows),len(cols),{(ri[r],ci[c]):S.Rational(v.numerator,v.denominator) for (r,c),v in D30.items() if r in ri and c in ci})
 _,pc=mat.rref(simplify=False,normalize_last=True)
 _,pr=mat[:,list(pc)].T.rref(simplify=False,normalize_last=True)
 pm=mat[list(pr),list(pc)]
 inv=pm.inv()
 assert pm*inv==S.eye(len(pr))
 block[p]=(rows,cols,mat)
 piv[p]=(list(pr),list(pc),inv)
 print('block',p,'rank',len(pc),'secs',round(time.monotonic()-T,1),flush=True)
assert [len(piv[p][0]) for p in range(6)]==[6,54,108,108,54,6]
print('PASS D: exact universal d3_0 coefficient split, rank336',round(time.monotonic()-T,2),flush=True)

# Sparse coefficient action and exact fixed right inverse.
def apply(matrix,x):
 out=collections.defaultdict(F)
 for (r,c),v in matrix.items():
  if x.get(c):out[r]+=v*x[c]
 return {r:v for r,v in out.items() if v}
def minus(a,b):
 c=collections.defaultdict(F,a)
 for i,v in b.items():c[i]-=v
 return {i:v for i,v in c.items() if v}

def solve_many(rhs,what):
 assert len(rhs)==15
 out=[{} for _ in range(15)]
 for p in range(6):
  rows,cols,mat=block[p];pr,pc,inv=piv[p]
  # choose a single rational matrix with 15 RHS columns.
  rr=S.Matrix([[S.Rational(rhs[j].get(rows[i],0)) for j in range(15)] for i in pr])
  xx=inv*rr
  for j in range(15):
   for a,cc in enumerate(pc):
    val=xx[a,j]
    if val:out[j][cols[cc]]=F(int(S.numer(val)),int(S.denom(val)))
 for j in range(15):
  check=apply(D30,out[j])
  assert check==rhs[j],('Incompatible P2 homotopy',what,j,len(rhs[j]),len(check),len(minus(rhs[j],check)))
 return out

G0=solve_many(RHS.get((),[{} for _ in range(15)]),'zero')
print('PASS E: exact 15-column constant P2 homotopy from fixed 336-pivot splitting',round(time.monotonic()-T,2),flush=True)

G1={}
for a in range(9):
 rr=[minus(RHS.get((a,),[{} for _ in range(15)])[j],apply(D31[a],G0[j])) for j in range(15)]
 G1[a]=solve_many(rr,('linear',a))
print('PASS F: all 9x15 first-order coefficient columns exact',round(time.monotonic()-T,2),flush=True)

G2={}
for a,b in itertools.combinations_with_replacement(range(9),2):
 rr=[]
 for j in range(15):
  tmp=minus(RHS.get((a,b),[{} for _ in range(15)])[j],apply(D31[a],G1[b][j]))
  if a!=b:tmp=minus(tmp,apply(D31[b],G1[a][j]))
  rr.append(tmp)
 G2[a,b]=solve_many(rr,('quadratic',a,b))
print('PASS G: all 45x15 quadratic coefficient columns exact',round(time.monotonic()-T,2),flush=True)

# Check cubic coefficients; the only LHS is sum_a D31_a * G2_(rest), no G3.
triple=set(itertools.combinations_with_replacement(range(9),3))
assert all(len(m)<=3 for m in RHS)
for aa,bb,cc in sorted(triple):
 for j in range(15):
  rhs=RHS.get((aa,bb,cc),[{} for _ in range(15)])[j]
  accum={}
  for d in sorted(set((aa,bb,cc))):
   remain=list((aa,bb,cc));remain.remove(d)
   z=apply(D31[d],G2[tuple(remain)][j]);accum=minus(accum,{r:-v for r,v in z.items()})
  assert accum==rhs,('cubic obstruction',aa,bb,cc,j,len(minus(rhs,accum)))
print('PASS H: all 165 cubic U monomials x all 15 columns x 840 PBW rows vanish',round(time.monotonic()-T,2),flush=True)
# The universal coefficient identities above imply all specializations.  As an
# independent safeguard, reconstruct both products in the ACTUAL Clifford PBW
# algebra at the four minimal probes and an arbitrary integer nine-tuple.
def specialize(q, U):
    return S.prod(U[a//3][a%3] for a in q)

def direct_check(name,U):
    cl=Cliff(U,ZERO)
    d2=cl.get_d2();d3=syzygies(U,cl);w=cl.get_u_w()[1]
    # Make 15x6 coefficients of H (first-middle component) and 20x15 of G.
    Hcoeff=[((),R['H0'])]+[((a,),R['H1'][a]) for a in range(9)]+[(p,R['H2'][p]) for p in R['PAIR']]
    Gcoeff=[((),G0)]+[((a,),G1[a]) for a in range(9)]+[(p,G2[p]) for p in itertools.combinations_with_replacement(range(9),2)]
    Hactual=[[{} for _ in range(6)] for _ in range(15)]
    for q,mat in Hcoeff:
        fac=specialize(q,U)
        if not fac:continue
        for gen in range(6):
            for ij,v in mat[gen].items():
                rel,bb=divmod(ij,21)
                for (deg,ce,word),a in B2[bb].items():
                    assert deg==0
                    Hactual[rel][gen]=add(Hactual[rel][gen],{(len(q),ce,word):v*a*fac})
    Gactual=[[{} for _ in range(15)] for _ in range(20)]
    for q,mat in Gcoeff:
        fac=specialize(q,U)
        if not fac:continue
        for col in range(15):
            for ij,v in mat[col].items():
                nu,bb=divmod(ij,21)
                for (deg,ce,word),a in B2[bb].items():
                    assert deg==0
                    Gactual[nu][col]=add(Gactual[nu][col],{(len(q),ce,word):v*a*fac})
    for rel in range(15):
        for col in range(15):
            part1=add(*(cl.mul(d3[nu].get(rkeys[rel],{}),Gactual[nu][col]) for nu in range(20)))
            part2=add(*(cl.mul(Hactual[rel][gen],d2[col][gen]) for gen in range(6)))
            total=add(part1,part2)
            assert total==(w if rel==col else {}),(name,rel,col,len(total))
    print('PASS: direct noncommutative 15x15 identity at',name,flush=True)

probes={
    'E00':[[1,0,0],[0,0,0],[0,0,0]],
    'row-sum':[[1,1,1],[0,0,0],[0,0,0]],
    'column-sum':[[1,0,0],[1,0,0],[1,0,0]],
    'diagonal':[[1,0,0],[0,1,0],[0,0,1]],
    'generic':[[-1,2,3],[1,3,-2],[2,-1,1]],
}
for name,U in probes.items():direct_check(name,U)
counts={'G0':sum(len(x) for x in G0),
        'G1':sum(len(z) for M in G1.values() for z in M),
        'G2':sum(len(z) for M in G2.values() for z in M)}
print('PASS I: all four minimal probes and independent generic specialization, sparse coefficient counts:',counts,flush=True)
print('9 PASS: exact universal nine-parameter P2->P3 quadratic first-Shamash homotopy; higher Shamash and Ku open.',flush=True)
