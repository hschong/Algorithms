'''
Largest Sum Contiguous Subarray
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/


입력
첫째 줄에 n개의 숫자가 주어진다. (1≤n≤100,000)

출력
n개의 숫자에 대하여 연속 부분 최대합을 출력한다.

입력 예시
1 2 -4 5 3 -2 9 -10

출력 예시
15

'''

import math

# Using Brute-force. O(n x n x n)
def getMaxSum(numbers) : 
    maxSum = -math.inf
    length = len(numbers)

    for start in range(0, length) :
        for end in range(start, length) :
            '''
            All cases n x (n-1)/2
            O(n) == sum for each case.
            O(n x n x (n-1) / 2)
            '''
            tempSum = sum(numbers[start:end+1])
            maxSum = max(maxSum, tempSum)
    return maxSum


'''
Using Divide and Conquer like merge sort. O(nlog n)
Algorithm I 3. Divide and Conquer II.mp4
get max sub sum in consecutive numbers.
'''
def findMaxSum(numbers) :
    length = len(numbers)
    if length == 1 :
        return numbers[0]
    
    mid = length // 2
    # Largest Sum Contiguous Subarray
    LSCSInLeft = findMaxSum(numbers[:mid])
    LSCSInRight = findMaxSum(numbers[mid:]) 
    LSCSInMiddle = 0
    leftMaxSumInMiddle = 0 
    rightMaxSumInMiddle = 0

    tempSum = 0
    for i in range(mid-1, -1, -1) :
        tempSum += numbers[i]
        leftMaxSumInMiddle = max(leftMaxSumInMiddle, tempSum)

    tempSum = 0
    for i in range(mid, length) :
        tempSum += numbers[i]
        rightMaxSumInMiddle = max(rightMaxSumInMiddle, tempSum)

    LSCSInMiddle = leftMaxSumInMiddle + rightMaxSumInMiddle
    return max(LSCSInLeft, LSCSInMiddle, LSCSInRight)


def main():
    numbers = [int(x) for x in input().split()]
    print(findMaxSum(numbers))

if __name__ == "__main__":
    main()