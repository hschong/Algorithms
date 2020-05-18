# Fibonacci number
# F0 = 0, F1= 1, Fn+2 = Fn + Fn+1

INPUT_NUMBER = 9


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


def fibonacci_using_recursion(n):
    # return fn
    if n == 0 or n == 1:
        return n  # return f0 or f1
    elif n > 1:
        return fibonacci_using_recursion(n-2) + fibonacci_using_recursion(n-1)


def list_fibonacci_using_recursion(n):
    # return a list which has fib numbers from f0 to fn
    fib_lst = []
    for i in range(0, n+1):
        fib_lst.append(fibonacci_using_recursion(i))

    return fib_lst


print(fibonacci_using_loop(INPUT_NUMBER))
print(list_fibonacci_using_loop(INPUT_NUMBER))
print(fibonacci_using_recursion(INPUT_NUMBER))
print(list_fibonacci_using_recursion(INPUT_NUMBER))
