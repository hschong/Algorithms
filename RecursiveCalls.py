def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))


def getPower(m, n) :
    if n == 0 :
        return 1
    else :
        if n % 2 == 0 :
            temp = m * getPower(m, n // 2)
            return temp * temp
        else :
            return m * getPower(m, n - 1) 