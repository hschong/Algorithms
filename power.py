def power(base, expo):
    result = 1

    if expo == 0:
        return 1

    if expo > 0:
        while expo > 0:
            result *= base
            expo -= 1
    else:
        while expo < 0:
            result /= base
            expo += 1

    return result


def power_using_recursion(base, expo):
    if expo == 0:
        return 1

    return power_using_recursion(base, expo - 1) * base if expo > 0 else power_using_recursion(base, expo + 1) / base


print(power(2, 10))
print(power(2, -3))
print(power_using_recursion(2, 10))
print(power_using_recursion(2, -3))
