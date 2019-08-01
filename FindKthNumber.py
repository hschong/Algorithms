# 1. get an element from first to last in the input list.
# 2. add the element into a new list.
# 3. find the kth smallest number in the new list.
# 4. add the smallest number into the kth smallest list if found.
# 5. add '-1' into the smallest list if not found.

# example: input list
#     10 3                    10 is the length of the list and 3 is the k.
#     1 9 8 5 2 3 5 6 2 10

# example: kth smallest number list
#     -1 -1 9 8 5 3 3 3 2 2

def findKthNumber(myInput, k) :

    data = []
    result = []

    for element in myInput:
        data.append(element)
        
        # 오름차순 정렬
        data.sort() 

        if len(data) < k:
            result.append(-1)
        else:
            result.append(data[k-1])

    return result

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    firstLine = [int(x) for x in input().split()]
    myInput = [int(x) for x in input().split()]

    print(*findKthNumber(myInput, firstLine[1]))
if __name__ == "__main__":
    main()

