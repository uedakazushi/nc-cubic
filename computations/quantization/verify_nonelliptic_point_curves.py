#!/usr/bin/env python3
"""Exact QQ[h] determinants of the nodal and cuspidal quantum blocks.

Run: python3 computations/quantization/verify_nonelliptic_point_curves.py
The polynomial assertions were separated from the classical component checker.
"""
from pathlib import Path
import json
import sympy as s
x,y,z=s.symbols('x y z')
def verify(kind):
    h=s.symbols('h')
    if kind=='node':
        B=s.Matrix([[0,-(1+h/2)*z,(1-h/2)*y],[(1-h/2)*z,-3*h*y,-(1+h/2)*x],[-(1+h/2)*y,(1-h/2)*x,-3*h*z]])
        e=-h*((h*h+12)*x*y*z+(12-3*h*h)*(y**3+z**3))/4
        condition='h != 0; h^2 != 4,-12'
    else:
        B=s.Matrix([[0,-z,y-h*z],[z,-3*h*y,-x],[-y-h*z,x,-h*x]])
        e=-3*h*(x*z*z+y**3-h*h*y*z*z)
        assert s.expand((x*z*z+y**3-h*h*y*z*z).subs(x,x+h*h*y))==x*z*z+y**3
        condition='h != 0'
    assert s.expand(B.det()-e)==0
    return {'kind':kind,
            'quantum_multilinear_matrix':[[str(v) for v in row] for row in B.tolist()],
            'quantum_multilinear_determinant':str(s.factor(e)),
            'determinant_curve_condition':condition}

def main():
    saved=json.loads(Path(__file__).with_name('nonelliptic_point_curves_certificate.json').read_text())
    assert saved['examples']==[verify(k) for k in ('node','cusp')]
    print('PASS: two exact quantum determinants and the cusp coordinate change.')
    print('SCOPE: homogeneous relation matrices; no categorical reconstruction assertion.')
if __name__=='__main__':
    main()
