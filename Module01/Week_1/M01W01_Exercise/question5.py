import math
def calc_elu(x):
    a = 0.01
    return x if x>0 else a*(math.exp(x) - 1)
assert round(calc_elu(1)) == 1
print(round(calc_elu(-1), 2))