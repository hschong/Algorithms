# Fibonacci number
# F0 = 0, F1= 1, Fn+2 = Fn + Fn+1

INPUT_NUMBER = 9
MAX_MEMOIZATION = 1000


def fibonacci_using_loop(n):  # return fn
    if n < 0:
        print('n must be greater than -1')
        return None

    if n == 0 or n == 1:
        return n  # return f1 or f2

    f0, f1 = 0, 1
    index = 2
    while index < n+1:  # from f2 to fn
        fn = f0 + f1
        f0, f1 = f1, fn
        index += 1

    return fn


print(fibonacci_using_loop(INPUT_NUMBER))


def list_fibonacci_using_loop(n):
    # return a list which has fib numbers from f0 to fn
    fib_lst = []
    f0, f1 = 0, 1

    if n < 0:
        print('input number must be greater than 0 or equal to 0')
        return None
    elif n == 0:
        fib_lst.append(f0)
    else:
        fib_lst.append(f0)
        fib_lst.append(f1)

        index = 2
        while index < n+1:  # from f2 to fn-1
            fib_lst.append(f0 + f1)
            f0, f1 = f1, f0 + f1
            index += 1

    return fib_lst


print(list_fibonacci_using_loop(INPUT_NUMBER))


def fibonacci_using_recursion(n):
    # return fn
    return n if n < 2 else fibonacci_using_recursion(n-2) + fibonacci_using_recursion(n-1)


print(fibonacci_using_recursion(INPUT_NUMBER))


def list_fibonacci_using_recursion(n):
    # return a list which has fib numbers from f0 to fn
    fib_lst = []
    for i in range(0, n+1):
        fib_lst.append(fibonacci_using_recursion(i))

    return fib_lst


print(list_fibonacci_using_recursion(INPUT_NUMBER))


def fibonacci_using_memoization(n):
    if n in dic_fibo:
        return dic_fibo[n]

    if n < 2:
        dic_fibo[n] = n
    else:
        dic_fibo[n] = fibonacci_using_memoization(
            n-2) + fibonacci_using_memoization(n-1)

    return dic_fibo[n]


dic_fibo = {}
print(fibonacci_using_memoization(INPUT_NUMBER))
for i in sorted(dic_fibo):
    print(i, ':', dic_fibo[i])
