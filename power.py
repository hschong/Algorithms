def power(base, expo):
    result = 1
    while expo > 0:
        result *= base
        expo -= 1

    return result


def power_using_recursion(base, expo):
    return 1 if expo == 0 else base * power_using_recursion(base, expo - 1)


print(power(2, 10))
print(power_using_recursion(2, 10))
