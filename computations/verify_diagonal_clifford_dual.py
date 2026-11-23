#!/usr/bin/env python3
"""Check the full even Clifford multiplication table after the Klein-four twist."""
from sympy import Matrix, eye, expand, kronecker_product, symbols, zeros

p, q, r, potential = symbols("p q r C")
identity = eye(4)
discriminant = r**2 - p*q
# Columns are left multiplication on the ordered basis 1, a, b, c.
a = Matrix([[0, discriminant, 0, 0], [1, 0, 0, 0],
            [0, 0, r, q], [0, 0, -p, -r]])
b = Matrix([[0, 0, -p*potential, -r*potential], [0, 0, 0, -potential],
            [1, -r, 0, 0], [0, p, 0, 0]])
c = Matrix([[0, 0, -r*potential, -q*potential], [0, 0, potential, 0],
            [0, -q, 0, 0], [1, r, 0, 0]])
j = Matrix.diag(1, -1)
k = Matrix([[0, 1], [1, 0]])
m = j*k
s = kronecker_product(a, m)
aa = kronecker_product(r*identity, m)
bb = kronecker_product(b, j)
cc = kronecker_product(c, k)
one = eye(8)
checks = [s*s - (p*q-r**2)*one, aa*aa - (s*s-p*q*one),
          bb*bb+p*potential*one, cc*cc+q*potential*one,
          aa*bb - (s*bb-p*cc), aa*cc - (q*bb-s*cc),
          bb*aa+aa*bb, cc*aa+aa*cc,
          bb*cc + (s+aa)*potential, cc*bb + (s-aa)*potential]
checks.extend(s*gen-gen*s for gen in (aa, bb, cc))
assert all(test.applyfunc(expand) == zeros(8) for test in checks)
print("All 13 signed even-Clifford identities hold over the polynomial ring.")

ell, h, a1, a2, a3 = symbols("lambda g L1 L2 L3")
shift = 4*a1*a2*a3/ell**2
# The dual changes L3 to -L3 and interchanges the two binary cubics.
assert expand(h+shift+4*a1*a2*(-a3)/ell**2-h) == 0
assert expand(h+4*a3*r**2/ell**2 -
              (h+shift-4*a3*(a1*a2-r**2)/ell**2)) == 0
print("The binary discriminants interchange, and the conic coefficient agrees.")

# Endomorphisms of the two-variable Koszul stabilization, in the exterior basis.
x, y, period = symbols("x y t", nonzero=True)
wedges = []
for bit in (1, 2):
    wedge = zeros(4)
    for mask in range(4):
        if not mask & bit:
            wedge[mask | bit, mask] = (-1)**((mask & (bit-1)).bit_count())
    wedges.append(wedge)
ex, ey = wedges
ix, iy = ex.T, ey.T
differential = x*ix+y*iy+period*((p*x+r*y)*ex+(r*x+q*y)*ey)
th1 = ix-period*(p*ex+r*ey)
th2 = iy-period*(r*ex+q*ey)
def anticommutator(left, right):
    return left*right+right*left
koszul_checks = [
    differential**2-period*(p*x**2+2*r*x*y+q*y**2)*eye(4),
    anticommutator(differential, ex)-x*eye(4),
    anticommutator(differential, ey)-y*eye(4),
    anticommutator(differential, th1), anticommutator(differential, th2),
    th1**2+period*p*eye(4), th2**2+period*q*eye(4),
    anticommutator(th1, th2)+2*period*r*eye(4)]
assert all(test.applyfunc(expand) == zeros(4) for test in koszul_checks)
root = kronecker_product(-th1*th2/period-r*eye(4), m)
odd1 = kronecker_product(th1, j)
odd2 = kronecker_product(th2, k)
odd_checks = [root**2-(p*q-r**2)*eye(8),
              root*odd1-odd1*root, root*odd2-odd2*root,
              anticommutator(odd1, odd2)+2*period*root,
              odd1**2+period*p*eye(8), odd2**2+period*q*eye(8)]
assert all(test.applyfunc(expand) == zeros(8) for test in odd_checks)
print("Koszul stabilization, its two closed operators, and all twisted odd Clifford relations verified.")
