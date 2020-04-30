'''
Write a function add(x, y) that returns sum of two integers.
The function should not use any of the arithmetic operators (+, ++, –, -, .. etc).
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
    if y == 0:
        return x
    else:
        # add(sum of bits of x and y without carry, carry)
        return add(x ^ y, (x & y) << 1)


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
    if y == 0:
        return x
    else:
        # subtract(subtraction of bits of x and y without borrow, borrow)
        return subtract(x ^ y, (((~x) & y) << 1))


'''
Write a function swap(x, y) that does not use a temporary variable.
'''


def swap(x, y):
    print('called swap({}, {})'.format(x, y))
    x = x ^ y
    y = x ^ y   # y = (x ^ y) ^ y, y = x
    x = x ^ y   # x = (x ^ y) ^ x, x = y
    print('x = {}, y = {}'.format(x, y))


# Driver Code
x = 5
y = 2
sum = add(x, y)
print('x = {}, y = {}, x + y = {}'.format(x, y, sum))

x = 25
y = 21
print('x = {}, y = {}, x - y = {}'.format(x, y, subtract(x, y)))

x = 3
y = 5
print('x = {}, y = {}'.format(x, y))
swap(x, y)
