def power_using_loop(base, expo):
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


def power_using_divide_and_conquer(base, expo):
    if expo == 0:
        return 1

    # Time Complexity of optimized solution: O(log n)
    temp = power_using_divide_and_conquer(base, int(expo/2))
    if expo % 2 == 0:
        return temp * temp
    else:
        return temp * temp * base if expo > 0 else temp * temp / base


print(power_using_loop(2, 10))
print(power_using_loop(2, -3))
print(power_using_recursion(2, 10))
print(power_using_recursion(2, -3))
print(power_using_divide_and_conquer(2, -3))
