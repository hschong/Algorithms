'''
Add two numbers using bitwise operators only.
Write a function Add() that returns sum of two integers. The function should not use any of the arithmetic operators (+, ++, –, -, .. etc).
   
x y   (x ^ y)    (x & y) << 1)      (x ^ y) ^ (x & y) << 1)
0 0   0             0               0
0 1   1             0               1    
1 0   1             0               1
1 1   0             10              10
'''


def add_using_while(x, y):
    while y != 0:               # loops until no carry
        carry = (x & y) << 1        # find the carry when adding x to y
        xor_sum = x ^ y             # sum of x and y without carry
        x = xor_sum
        y = carry

    return x


def add(x, y):
    if y != 0:
        # add(sum of x and y without carry, carry)
        add(x ^ y, (x & y) << 1)

    return x

