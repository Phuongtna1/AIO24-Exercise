import math
def approx_cosh(x, n):
    return sum([(x**(2*i))/math.factorial(2*i) for i in range(n)])
assert round(approx_cosh(x=1, n=10), 2) ==1.54
print(round(approx_cosh(x=3.14, n=10), 2))