def binarySearchWithIndices(startIndex, endIndex, targetList, item):
    while startIndex <= endIndex:
        midIndex = (startIndex + endIndex) // 2
        guess = targetList[midIndex]
        
        if guess == item:
            return midIndex
        elif guess > item:
            endIndex = midIndex - 1
        else:
            startIndex = midIndex + 1
    
    return None


def binarySearch(targetList, item):
    minIndex = 0
    maxIndex = len(targetList) - 1

    while minIndex <= maxIndex:
        midIndex = (minIndex + maxIndex) // 2
        guess = targetList[midIndex]

        if guess == item:
            return midIndex
        elif guess > item:
            maxIndex = midIndex - 1
        else:
            minIndex = midIndex + 1

    return None

mylist = [1, 3, 5, 7, 9]
print(binarySearch(mylist, 3))