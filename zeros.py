# Find the zeros of a polynomial function and output the factorized form
from sympy import symbols , factor, roots, Function
from math import gcd
x = symbols('x')
y = symbols('y')

# Example polynomial
f = 1*x**4 + 3*x**2 - 4
fac = factor(f)
rt = roots(f)

print('Factorized: ', fac)
print('Roots dict: ', rt)
print('Zeros: ', list(rt.keys()))

# Perform rational root test viable numbers: ± factors of 20 / factors of 12
viable_num = []
const_factors = [1, -1]
leadco_factors = [1, 2, 4, -1, -2, -4]
for a in const_factors:
    for b in leadco_factors:
        viable_num += [a/b, -a/b]
viable_num = sorted(set(viable_num))
print('Root candidates: ', viable_num[:8])