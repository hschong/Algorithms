'''
n개의 정렬된 숫자가 list로 주어지고, 숫자 k이 
주어질 때, m보다 작거나 같은 숫자 중 최댓값, k보다 
큰 숫자 중 최솟값을 반환하는 함수를 작성하세요.
'''
import sys
import math

def getNearestInternal(list, k) :
    length = len(list)
    if length == 1 :
        if list[0] <= k :
            return [list[0], math.inf]
        else :
            return [-math.inf, list[0]]

    elif length == 2 :
        if list[1] <= k : 
            # list = [1,2], k = 3
            return [list[1], math.inf]

        elif list[0] <= k and k < list[1] :
            # list = [1, 3], k = 2
            return [list[0], list[1]]
        
        else :
            # list = [2, 3], k = 1
            return [-math.inf, list[0]]
    
    else :
        mid = length // 2
        if list[mid] <= k :
            return getNearestInternal(list[mid:], k)
        else :
            return getNearestInternal(list[:mid+1], k)


def getNearest(list, k) :
    '''
    n개의 정렬된 숫자가 list로 주어지고, 숫자 k이 
    주어질 때, n개의 숫자 중에서 k과 가장 가까운 숫자를 
    반환하는 함수를 작성하세요.
    '''
    numbers = getNearestInternal(list, k)
    min = numbers[0]
    max = numbers[1]

    if (max - k) == (k - min) :
        return min
    elif (max - k) > (k - min) :
        return min
    else :
        return max


def main():
    numbers = [int(x) for x in input().split()]
    k = int(input())

    print(getNearest(numbers, k))


if __name__ == “__main__“:
    main()