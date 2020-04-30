'''
Add two numbers using bitwise operators only.

      Sub sum(^)    Carry(&)    (Carry << 1) ^ Sub sum  Total sum
0 0   0             0           (00) ^ 00               00
0 1   1             0           (00) ^ 01               01    
1 0   1             0           (00) ^ 01               01
1 1   0             1           (10) ^ 00               10

'''


def add(x, y):  # x -> sub sum, y -> carry
    if y != 0:
        add(x ^ y, (x & y) << 1)

    return x  # x = sum sum ^ carry


def add_simple(x, y):
    while y != 0:
        carry = x & y  # carry
        x = x ^ y   # sub sum
        y = carry << 1

    return x  # x = sum sum ^ carry
