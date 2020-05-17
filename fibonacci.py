INPUT_NUMBER = 9


def kth_fibonacci_using_loop(kth):
    # return kth fibonacci number
    f1, f2 = 0, 1

    if kth < 1:
        print('kth must be greater than 0')
        return None

    if kth == 1:    # f1
        return 0
    elif kth == 2:  # f2
        return 1

    index = 3
    while index <= kth:  # from f3 to fkth
        fkth = f1 + f2
        f1, f2 = f2, fkth
        index += 1

    return fkth


def list_fibonacci_using_loop(kth):
    # return a list which has fib numbers from f1 to fn
    fib_lst = []
    f1, f2 = 0, 1

    if kth < 1:
        print('input number must be greater than 0')
        return None
    elif kth == 1:
        return list(f1)
    elif kth == 2:
        return list(f1) + list(f2)
    else:
        fib_lst.append(f1)
        fib_lst.append(f2)

    index = 3
    while index < kth + 1:
        fib_lst.append(f1 + f2)
        f1, f2 = f2, f1 + f2
        index += 1

    return fib_lst


def kth_fibonacci_using_recursion(kth):
    # return kth fibonacci number
    if kth == 1:
        return 0  # f1 = 0
    elif kth == 2:
        return 1  # f2 = 1
    elif kth > 2:
        return kth_fibonacci_using_recursion(kth-2) + kth_fibonacci_using_recursion(kth-1)


def list_fibonacci_using_recursion(kth):
    # return a list which has fib numbers from f1 to fn
    fib_lst = []
    for i in range(1, kth+1):
        fib_lst.append(kth_fibonacci_using_recursion(i))

    return fib_lst


print(kth_fibonacci_using_loop(INPUT_NUMBER))
print(kth_fibonacci_using_recursion(INPUT_NUMBER))
print(list_fibonacci_using_loop(INPUT_NUMBER))
print(list_fibonacci_using_recursion(INPUT_NUMBER))
