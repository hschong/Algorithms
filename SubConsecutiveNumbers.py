'''
Largest Sum Contiguous Subarray
Write an efficient program to find the sum of contiguous 
subarray within a one-dimensional array of numbers which 
has the largest sum.

https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

입력
첫째 줄에 n개의 숫자가 주어진다. (1≤n≤100,000)

출력
n개의 숫자에 대하여 연속 부분 최대합을 출력한다.

입력 예시
1 2 -4 5 3 -2 9 -10
-3 -3 -2 -4 -5 -2 -3 -4
출력 예시
15
'''

import math

# Using Brute-force. O(n x n x n)
def getLSCSByBF(numbers):
    maxSum = -math.inf
    length = len(numbers)

    for i in range(0, length):
        for j in range(i, length):
            '''
            All cases n x (n-1)/2
            O(n) == sum for each case.
            O(n x n x (n-1) / 2)
            '''
            tempSum = sum(numbers[i:j+1])
            maxSum = max(maxSum, tempSum)

    return maxSum


'''
Using Divide and Conquer like merge sort. O(nlog n)
Algorithm I 3. Divide and Conquer II.mp4
get max sub sum in consecutive numbers.
'''
def getLSCSByDC(numbers):
    length = len(numbers)
    if length == 1:
        return numbers[0]

    mid = length // 2
    # Largest Sum Contiguous Subarray
    LSCSInLeft = getLSCSByDC(numbers[:mid])
    LSCSInRight = getLSCSByDC(numbers[mid:])
    LSCSInMiddle = 0
    leftMaxSum = 0
    rightMaxSum = 0

    tempSum = 0
    for i in range(mid-1, -1, -1):
        tempSum += numbers[i]
        leftMaxSum = max(leftMaxSum, tempSum)

    tempSum = 0
    for i in range(mid, length):
        tempSum += numbers[i]
        rightMaxSum = max(rightMaxSum, tempSum)

    LSCSInMiddle = leftMaxSum + rightMaxSum

    return max(LSCSInLeft, LSCSInMiddle, LSCSInRight)


# Kadane’s Algorithm
def getLSCSByKadane(numbers):
    max_so_far = 0
    max_ending_here = 0
    length = len(numbers)

    for i in range(0, length):
        max_ending_here += numbers[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


'''
Dynamic Programming
T(i) i(index)번째 숫자를 오른쪽 끝으로 하는 연속 부분 최대합
T(i) = max(T(i-1) + numbers[i], numbers[i])
'''
def getLSCSByDP(numbers):
    n = len(numbers)
    Table = [0 for i in range(n)]
    Table[0] = numbers[0]

    for i in range(1, n):
        Table[i] = max(Table[i-1] + numbers[i], numbers[i])

    return max(Table)


def main():
    numbers = [int(x) for x in input().split()]
    print(getLSCSByBF(numbers))
    print(getLSCSByDC(numbers))
    print(getLSCSByKadane(numbers))
    print(getLSCSByDP(numbers))


if __name__ == "__main__":
    main()
