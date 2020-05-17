INPUT_NUMBER = 9


def fibonacci_using_loop(n):
    # return a list which has fib numbers from f1 to fn
    fib_lst = []
    f1, f2 = 0, 1

    if n < 1:
        print('input number must be greater than 0')
        return None
    elif n == 1:
        return list(f1)
    elif n == 2:
        return list(f1) + list(f2)
    else:
        fib_lst.append(f1)
        fib_lst.append(f2)

    index = 3
    while index < n + 1:
        fib_lst.append(f1 + f2)
        f1, f2 = f2, f1 + f2
        index += 1

    return fib_lst


def fibonacci_using_recursion(n):
    # return a fib number
    if n == 1:
        return 0  # f1 = 0
    elif n == 2:
        return 1  # f2 = 1
    elif n > 2:
        return fibonacci_using_recursion(n-2) + fibonacci_using_recursion(n-1)


def list_fibonacci_using_recursion(n):
    # return a list which has fib numbers from f1 to fn
    fib_lst = []
    for i in range(1, n+1):
        fib_lst.append(fibonacci_using_recursion(i))

    return fib_lst


print(fibonacci_using_loop(INPUT_NUMBER))
print(list_fibonacci_using_recursion(INPUT_NUMBER))
