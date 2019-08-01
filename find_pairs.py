# Find 2 elements in array. their sum is 8.
# [1, 2, 3, 9] sum = 8 : There is no elements for sum is 8.
# [1, 2, 4, 4, 4, 4, 6, 6] sum = 8, 2 pairs[[2,6], [4,4] for sum is 8.
# (7)
import random

CONST_MAX = 1000000 # 1M
CONST_MIN = -1000000 # - 1M

def hasPairWithSum(givenSum, unorderedList):
    compSet = set()
    pairList = []
    
    for item in unorderedList:
        comp = givenSum - item

        if item in compSet:
            pairList.append([item, comp])
        else:
            compSet.add(comp)
    
    if len(pairList) == 0:
        return None
    else:
        return pairList

# Making a list.
unorderedList = []
size = int(input('type the number of elements: '))

for count in range(size):
    unorderedList.append(random.randint(CONST_MIN, CONST_MAX))
    print(count, unorderedList[count])

# unorderedList = [1, 6, 2, 5, 4, 4, 4, 6, 3, 6]
givenSum = int(input('type your sum: '))
pairList = hasPairWithSum(givenSum, unorderedList)

if pairList != None:
    for item in pairList:
        print(item)
else:
    print('There is no pair with the given sum in the list.')