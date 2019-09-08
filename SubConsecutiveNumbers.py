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
def getMaxSubArraySum1(numbers) : 
    maxSum = -math.inf
    length = len(numbers)

    for i in range(0, length) :
        for j in range(i, length) :
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
def getMaxSubArraySum2(numbers) :
    length = len(numbers)
    if length == 1 :
        return numbers[0]
    
    mid = length // 2
    # Largest Sum Contiguous Subarray
    LSCSInLeft = getMaxSubArraySum2(numbers[:mid])
    LSCSInRight = getMaxSubArraySum2(numbers[mid:]) 
    LSCSInMiddle = 0
    leftMaxSum = 0 
    rightMaxSum = 0

    tempSum = 0
    for i in range(mid-1, -1, -1) :
        tempSum += numbers[i]
        leftMaxSum = max(leftMaxSum, tempSum)

    tempSum = 0
    for i in range(mid, length) :
        tempSum += numbers[i]
        rightMaxSum = max(rightMaxSum, tempSum)

    LSCSInMiddle = leftMaxSum + rightMaxSum

    return max(LSCSInLeft, LSCSInMiddle, LSCSInRight)


# Kadane’s Algorithm
def getMaxSubArraySum3(numbers): 
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


def main():
    numbers = [int(x) for x in input().split()]
    print(getMaxSubArraySum1(numbers))
    print(getMaxSubArraySum2(numbers))
    print(getMaxSubArraySum3(numbers))
    

if __name__ == "__main__":
    main()