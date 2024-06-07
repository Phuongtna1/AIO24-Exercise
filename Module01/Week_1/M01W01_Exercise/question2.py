import math
def is_number(x):
    try:
        float(x)
    except (ValueError):
        return False
    return True
assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print(is_number(1))
print(is_number('n'))