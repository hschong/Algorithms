# 1. get an element from index 0 to -1 in the input list.
# 2. add the element into a temp list.
# 3. find the kth smallest number in the temp list.
# 4. add the smallest number into the kth smallest list if found.
# 5. add '-1' into the smallest list if not found.

# example: input list
#     10 3                    '10' is the length of the list and '3' is the k.
#     1 9 8 5 2 3 5 6 2 10

# example: kth smallest number list
#     -1 -1 9 8 5 3 3 3 2 2

def findKthNumber(myInput, k) :
    temp = []
    kthSmallest = []

    for element in myInput:
        temp.append(element)
        temp.sort() 

        if len(temp) < k:
            kthSmallest.append(-1)
        else:
            kthSmallest.append(temp[k-1])

    return kthSmallest


def main():
    firstLine = [int(x) for x in input().split()]
    myInput = [int(x) for x in input().split()]

    print(*findKthNumber(myInput, firstLine[1]))


if __name__ == "__main__":
    main()