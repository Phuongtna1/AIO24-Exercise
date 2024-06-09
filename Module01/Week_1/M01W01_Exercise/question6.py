import math
def calc_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif act_name == 'relu':
        return max(0, x)
    elif act_name == 'elu':
        a = 0.01
        return x if x>0 else a*(math.exp(x) - 1)
    else:
        print("This activation function is not supported!")
assert calc_activation_func(x = 1, act_name = 'relu') == 1
print(round(calc_activation_func(x = 3, act_name ='sigmoid'), 2))