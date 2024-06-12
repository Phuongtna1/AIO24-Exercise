# (A)


def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

# (B)


def md_nre_single_sample1(y, y_hat, n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/2)  # Wrong. Not 1/2 but 1/n
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

# (C)


def md_nre_single_sample2(y, y_hat, n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root / y_hat_root  # Wrong. Not / but -
    loss = difference ** p
    return loss

# (D)


def md_nre_single_sample3(y, y_hat, n):  # , p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root - y_hat_root
    loss = difference  # Wrong. Missing **p
    return loss
