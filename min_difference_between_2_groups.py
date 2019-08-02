'''
균형 맞추기
n개의 숫자가 주어진다. 이제 이 숫자를 두 개의 그룹으로 나눌 것이다. 예를 들어 5개의 숫자 [1, -3, 4, 5, -2] 가 주어진다면, 이를 두 개의 그룹으로 나누는 경우는 여러가지가 있을 수 있다. 가능한 경우로써 [1, -3], [4, 5, -2] 가 있을 수 있고, 또 다른 경우로는 [1, 4, -2], [-3, 5] 가 있을 수 있다.

나눈 두 그룹을 A, B라고 할 때, (A의 원소의 합) - (B의 원소의 합) 의 절댓값을 최소화 하는 프로그램을 작성하시오. 위의 예제에서는 A = [1, 4, -2], B = [-3, 5] 라고 하였을 때 (A의 원소의 합) - (B의 원소의 합) 의 절댓값 = |3 - 2| = 1 이며, 이보다 더 작은 값을 만드는 A, B는 존재하지 않는다.

입력
첫째 줄에 n개의 숫자가 주어진다. (1≤n≤20)

출력
(A의 원소의 합) - (B의 원소의 합) 의 절댓값의 최솟값을 출력한다.

입력 예시
1 -3 4 5 -2

출력 예시
1
'''

import sys

def getPowerSet(n, k) :
    if n == k :
        return [ [k] ]
    else :
        nth_after_k = [ [k] ]
        sth_after_k = []
        
        for i in range(k+1, n+1) :
            sth_after_k = sth_after_k + getPowerSet(n, i)
    
        for i in range(len(sth_after_k)) :
            sth_after_k[i] = [k] + sth_after_k[i]
            
        return nth_after_k + sth_after_k


def powerSet(n) :
    result = []
    for i in range(1, n+1) :
        result = result + getPowerSet(n, i)
    
    return result


def minimizeDifferenceBetween2Groups(numbers) :
    '''
    n개의 숫자를 두 그룹 A, B로 나눈다고 할 때,
    | (A의 원소의 합) - (B의 원소의 합) | 의 
    최솟값을 반환하는 함수를 작성하시오.
    O(n x 2 to the power of n)
    '''

    '''
    제곱은 square, 세제곱은 cubic이라는 표현으로 읽습니다.
    2의 n제곱(또는 2의 n승)을 영어로 표현하면,
    2 to the n
    2 to the power of n
    2 power n
    '''

    combinations = powerSet(len(numbers))
    totalSum = sum(numbers)
    result = 908324897092234
    
    for p in combinations :
        sumGroupA = 0

        for i in p :
            # an element of the p starts from 1.
            sumGroupA += numbers[i-1] 
        
        sumGroupB = totalSum - sumGroupA
        result = min(result, abs(sumGroupA - sumGroupB))
    
    return result


def main():
    numbers = [int(x) for x in input().split()]
    print(minimizeDifferenceBetween2Groups(numbers))

if __name__ == "__main__":
    main()