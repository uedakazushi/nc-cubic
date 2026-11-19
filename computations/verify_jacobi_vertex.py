"""Verify the N=10 vertex certificate with exact GF(2) arithmetic.

The 220 symmetric tensor entries are integers. This is a rank certificate for
characteristic-zero equations, not a statement about characteristic-two cubics.
An untracked 450 MB matrix is regenerated; direct elimination uses about 220 MB.
Requires Python 3, NumPy, and a C++17 compiler (GCC or Clang).
"""
from pathlib import Path
import argparse,hashlib,json,shutil,struct,subprocess,time
from itertools import combinations,combinations_with_replacement
from collections import defaultdict
import numpy as np
from verify_jacobi_rank import jacobi_matrix, nonstandard_columns
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--verify',type=Path,required=True)
parser.add_argument('--build-dir',type=Path,default=Path('build/jacobi-vertex'))
args=parser.parse_args()
cert=json.loads(args.verify.read_text())
assert cert['schema']==1 and cert['N']==10 and cert['prime']==2
N=cert['N']; root=args.build_dir;root.mkdir(parents=True,exist_ok=True);start=time.time()
tensor={tuple(t[:3]):t[3] for t in cert['hessian_tensor']}
assert set(tensor)==set(combinations_with_replacement(range(N),3))
assert all(v in (0,1) for v in tensor.values())
triples=list(combinations(range(N),3)); m=len(triples); ti={t:i for i,t in enumerate(triples)}
pairs=list(combinations_with_replacement(range(m),2)); pi={t:i for i,t in enumerate(pairs)}
ns=nonstandard_columns(N); nspos={v:i for i,v in enumerate(ns)}; q=len(ns)
# Give nonstandard monomials the low coordinates for eliminating Plucker quadrics.
std=[i for i in range(len(pairs)) if i not in nspos]
order=ns+std; inv={v:i for i,v in enumerate(order)}
piv={}
for I in combinations(range(N),2):
    for J in combinations(range(N),4):
        v=0
        for j in J:
            if j in I:continue
            a=ti[tuple(sorted(I+(j,)))]; b=ti[tuple(k for k in J if k!=j)]
            v^=1<<inv[pi[tuple(sorted((a,b)))]]
        while v:
            k=(v&-v).bit_length()-1
            if k in piv:v^=piv[k]
            else:piv[k]=v;break
assert set(piv)==set(range(q)),len(piv)
for k in range(q-1,-1,-1):
    v=piv[k]; u=(v&((1<<q)-1))^(1<<k)
    while u:
        j=(u&-u).bit_length()-1;v^=piv[j];u^=1<<j
    piv[k]=v
rules=[]
for k in range(q):
    v=piv[k];terms=[]
    while v:
        j=(v&-v).bit_length()-1;v^=1<<j;terms.append(pairs[order[j]])
    assert terms[0]==pairs[ns[k]]
    assert all(t[0]<terms[0][0] for t in terms[1:])
    rules.append(terms)
print(json.dumps({'stage':'plucker','q':q,'max_terms':max(map(len,rules)),'seconds':time.time()-start}),flush=True)
a=jacobi_matrix(N,tensor,2)
b=np.packbits(a[:,ns].astype(np.uint8),axis=1,bitorder='little')
ip={}
for v in (int.from_bytes(bytes(r),'little') for r in b):
    while v:
        k=(v&-v).bit_length()-1
        if k in ip:v^=ip[k]
        else:ip[k]=v;break
free=[i for i in range(q) if i not in ip]; d=len(free); fi={v:i for i,v in enumerate(free)}
images=[0]*q
for k in range(q-1,-1,-1):
    if k in fi:images[k]=1<<fi[k]
    else:
        v=ip[k]^(1<<k);out=0
        while v:
            j=(v&-v).bit_length()-1;v^=1<<j;out^=images[j]
        images[k]=out
assert len(ip)==1980 and d==330
# Verify all full Jacobi polynomials have exactly their Plucker-basis expansion.
fullrules=[]
for terms in rules:
    out=0
    for t in terms:out^=1<<pi[t]
    fullrules.append(out)
for row in a:
    full=int.from_bytes(bytes(np.packbits(row.astype(np.uint8),bitorder='little')),'little')
    for k in np.flatnonzero(row[ns]):full^=fullrules[int(k)]
    assert full==0
# Every coordinate exponent of a product of three Plucker variables is at
# most three, so two-bit weight encoding has no carries.
weights=[sum(1<<(2*i) for i in t) for t in triples]
for terms in rules:
    assert len({weights[x]+weights[y] for x,y in terms})==1
groups=defaultdict(list)
for k,terms in enumerate(rules):
    x,y=terms[0]
    for s in range(m):
        groups[weights[x]+weights[y]+weights[s]].append((s,k))
print(json.dumps({'stage':'quotient','d':d,'weight_blocks':len(groups),'max_block':max(map(len,groups.values())),'seconds':time.time()-start}),flush=True)
width=m*d;nbytes=(width+7)//8
count=rankj3=0
with (root/'syzygies.bin').open('wb') as f:
    f.write(struct.pack('<II',width,0))
    for w,entries in sorted(groups.items()):
        mons=sorted({tuple(sorted((s,)+p)) for s,k in entries for p in rules[k]})
        mi={t:i for i,t in enumerate(mons)}; bp={}
        for s,k in entries:
            poly=0
            for pair in rules[k]:poly^=1<<mi[tuple(sorted((s,)+pair))]
            tag=images[k]<<(s*d)
            while poly:
                p=(poly&-poly).bit_length()-1
                if p in bp:
                    pp,tt=bp[p];poly^=pp;tag^=tt
                else:bp[p]=(poly,tag);break
            if not poly:
                f.write(tag.to_bytes(nbytes,'little'));count+=1
        rankj3+=len(bp)
    f.seek(4);f.write(struct.pack('<I',count))
print(json.dumps({'stage':'syzygies','width':width,'relations':count,'J3_rank':rankj3,'bytes':(root/'syzygies.bin').stat().st_size,'seconds':time.time()-start}),flush=True)
assert count==90860 and rankj3==186340
assert q==cert['quadratic_plucker_dimension']
assert len(ip)==cert['quadratic_jacobi_rank'] and d==cert['quadratic_quotient_dimension']
assert rankj3==cert['cubic_plucker_dimension'] and count==cert['linear_syzygy_dimension']
assert width==cert['projected_columns']==cert['minor_order']
h=hashlib.sha256()
with (root/'syzygies.bin').open('rb') as f:
    while b:=f.read(8*1024*1024):h.update(b)
assert h.hexdigest()==cert['matrix_sha256'], 'Regenerated matrix hash differs'
ids=[]
for lo,hi in cert['minor_rows_inclusive_ranges']:
    assert 0<=lo<=hi<count
    ids.extend(range(lo,hi+1))
assert len(ids)==len(set(ids))==width and ids==sorted(ids)
(root/'witness_rows.txt').write_text('\n'.join(map(str,ids))+'\n')
compiler=shutil.which('c++') or shutil.which('g++') or shutil.which('clang++')
if not compiler:raise RuntimeError('A C++17 compiler is required for direct determinant verification')
source=Path(__file__).with_name('verify_binary_minor.cpp')
exe=(root/'verify_binary_minor').resolve()
subprocess.run([compiler,'-O3','-std=c++17',str(source),'-o',str(exe)],check=True)
result=subprocess.run([str(exe),str(root/'syzygies.bin'),str(root/'witness_rows.txt')],check=True,text=True,stdout=subprocess.PIPE)
verified=json.loads(result.stdout)
assert verified=={'order':width,'prime':2,'determinant':cert['minor_determinant_mod_prime'],'verified':True}
print(json.dumps({'stage':'verified',**verified,'matrix_sha256':h.hexdigest(),'seconds':time.time()-start}),flush=True)
