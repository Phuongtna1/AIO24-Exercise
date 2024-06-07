# (A)
def md_nre_single_sample(y, y_hat , n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

# (B)
def md_nre_single_sample1(y, y_hat , n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/2) #Wrong. Not 1/2 but 1/n
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

# (C)
def md_nre_single_sample2(y, y_hat , n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root / y_hat_root #Wrong. Not / but -
    loss = difference ** p
    return loss

# (D)
def md_nre_single_sample3(y, y_hat , n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root - y_hat_root
    loss = difference #Wrong. Missing **p
    return loss

# import numpy as np

# #checking with numbers in the table
# y = [100, 50, 20, 5.5, 1.0, 0.6]
# y_hat = [99.5, 49.5, 19.5, 5.0, 0.5, 0.1]
# expected = np.array([0.025, 0.035, 0.056, 0.110, 0.293, 0.458])
# a, b, c, d = [], [], [], []

# for i in range(6): 
#     a.append(md_nre_single_sample(y[i], y_hat[i] , 2, 1))
#     b.append(md_nre_single_sample1(y[i], y_hat[i] , 2, 1))
#     c.append(md_nre_single_sample2(y[i], y_hat[i] , 2, 1))
#     d.append(md_nre_single_sample3(y[i], y_hat[i] , 2, 1))

# print(np.sum(np.array(expected)-np.array(a)))
# print(np.sum(np.array(expected)-np.array(b)))
# print(np.sum(np.array(expected)-np.array(c)))
# print(np.sum(np.array(expected)-np.array(d)))