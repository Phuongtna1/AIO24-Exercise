import math
def approx_sinh(x, n):
    return sum([(x**(2*i+1))/math.factorial(2*i+1) for i in range(n)])
assert round(approx_sinh(x=1, n=10), 2) ==1.18
print(round(approx_sinh(x=3.14, n=10), 2))