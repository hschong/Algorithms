INPUT_NUMBER = 9

def fibonacci_using_loop(n):
    lst = []
    f1, f2 = 0, 1
    
    while f1 < n:
        lst.append(f1)
        f1, f2 = f2, f1 + f2

    return lst

print(fibonacci_using_loop(INPUT_NUMBER))
