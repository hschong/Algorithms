'''
거듭제곱 구하기

본 연습문제에서는 m의n승 을 구하는 프로그램을 작성합니다.
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

def getPower(m, n) :
    if n == 0 :
        return 1
    elif n % 2 == 0 :
        temp = getPower(m, n//2)
        return (temp * temp) % LIMIT_NUMBER
    else :
        return (m * getPower(m, n-1)) % LIMIT_NUMBER