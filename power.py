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


'''
만약 getPower 함수의 반환 값이 1,000,000,007 보다 클 
경우, 1,000,000,007로 나눈 나머지 값을 반환하세요.

입력
m과 n이 주어집니다. (1 ≤ n ≤ 1,000,000,000,000)

출력
m의n승 을 1,000,000,007으로 나눈 나머지를 출력합니다.

입력 예시
3 4

출력 예시
81
'''
LIMIT_NUMBER = 1000000007


def power_using_divide_and_conquer(base, expo):
    if expo == 0:
        return 1

    temp = power_using_divide_and_conquer(base, int(expo/2))
    if expo % 2 == 0:
        return temp * temp
    else:
        return temp * temp * base if expo > 0 else temp * temp / base


print(power_using_divide_and_conquer(2, -3))
