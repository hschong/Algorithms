# Find the maximum sum of sub consecutive numbers in the list.
def getMaxSum(numbers) :
    maxSum = -9078942340913534
    length = len(numbers)

    for start in range(0, length) :
        for end in range(start, length) :
            # all cases n x (n-1)/2
            tempSum = 0

            for i in range(start, end+1) :
                tempSum += numbers[i]
            
            maxSum = max(maxSum, tempSum)
    
    return maxSum