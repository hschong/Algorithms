'''
Write a function Add() that returns sum of two integers(variable x and y). The function should not use any of the arithmetic operators (+, ++, –, -, .. etc).
x and y are greater than 0.

x y   x ^ y    (x & y) << 1)    (x ^ y) ^ (x & y) << 1)
0 0   0        0                0
0 1   1        0                1
1 0   1        0                1
1 1   0        10               10
'''


def add_using_while(x, y):
    while y != 0:               # loops until no carry
        carry = (x & y) << 1        # find the carry when adding x to y
        xor_sum = x ^ y             # sum of bits of x and y without carry
        x = xor_sum
        y = carry

    return x


def add(x, y):
    if y != 0:
        # add(sum of bits of x and y without carry, carry)
        add(x ^ y, (x & y) << 1)

    return x


'''
Write a function subtract(x, y) that returns x-y where x and y are integers. The function should not use any of the arithmetic operators (+, ++, –, -, .. etc).
x and y are greater than 0 and x is always greater than y.

      sub(^)   Borrow()
0 0   0         0
0 1   1         1
1 0   1         0
1 1   0         0

'''


def subtract_using_while(x, y):
    while y != 0:
        borrow = ((~x) & y) << 1    # Find the borrow when subtracting x to y
        xor_subtraction = x ^ y     # Subtraction of bits of x and y without borrow
        x = xor_subtraction
        y = borrow

    return x


def subtract(x, y):
    if y != 0:
        # subtract(subtraction of bits of x and y without borrow, borrow)
        subtract(x ^ y, (((~x) & y) << 1))

    return x


# Driver Code
print(add(5, 2))

x = 25
y = 21
print("x - y is ", subtract_using_while(x, y))
print(bin(-3))
