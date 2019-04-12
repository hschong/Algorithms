# Find 2 elements in array. those sum is 8.
# [1, 2, 3, 9] sum = 8 : There is no elements for sum is 8.
# [1, 2, 4, 4, 4, 4, 6, 6] sum = 8, 2 pairs[[2,6], [4,4] for sum is 8.

import random

CONST_MAX = 1000000 # 1M
CONST_MIN = 0

# 1. Sorting
# 2. Find the index whose value is equal to givenSum in the list.
# 3. Binary Search: Find larest(givenSum - smallest) in the list.

class Pair:
    def __init__(self):
        self.list = []

    def addPair(self, number1, number2):
        self.list.append([number1, number2])

    def findMaxIndex(self, targetList, targetItem):
        startIndex = 0
        endIndex = len(targetList)

        while startIndex <= endIndex:
            midIndex = (startIndex + endIndex) // 2
            guess = targetList[midIndex]
            
            if guess == targetItem:
                return midIndex
            elif guess > targetItem:
                endIndex = midIndex - 1
            else:
                startIndex = midIndex + 1
        
        return startIndex - 1

    def binarySearch(self, startIndex, maxIndex, targetList, item):
        while startIndex <= maxIndex:
            midIndex = (startIndex + maxIndex) // 2
            guess = targetList[midIndex]
            
            if guess == item:
                return midIndex
            elif guess > item:
                maxIndex = midIndex - 1
            else:
                startIndex = midIndex + 1
        
        return None

    def hasPairWithSum(self, maxIndex, targetList, givenSum):
        stop = maxIndex + 1

        for index in range(stop):
            smallest = targetList[index]
            largest = givenSum - smallest

            guessIndex = self.binarySearch(index, maxIndex, targetList, largest)
            if (None != guessIndex):
                self.addPair(targetList[index], targetList[guessIndex])

        if len(self.list) == 0:
            return False
        else:
            return True


def main():
    myPair = Pair()

    # Making a list.
    data = []
    length = random.randint(CONST_MIN, CONST_MAX)
    print('The length is ', length, '.')

    for count in range(length):
        data.append(random.randint(CONST_MIN, CONST_MAX))

    givenSum = int(input('Type your sum: '))
    data.sort()

    if (data[0] <= givenSum):
        maxIndex = myPair.findMaxIndex(data, givenSum)
        
        if (myPair.hasPairWithSum(maxIndex, data, givenSum) == False):
            print('No, thre is no pair with your sum.')
        else:
            print('Yes, there is(are) ' + str(len(myPair.list)) + ' pair(s) with your sum.')
            # for item in myPair.list:
            #     print(item)

            # for index in range(len(myPair.list)):
            #     print(myPair.list[index])
            
            for idx, val in enumerate(myPair.list):
                print(idx, val)
    else:
        print('No, thre is no pair with your sum.')

if __name__ == "__main__":
    main()