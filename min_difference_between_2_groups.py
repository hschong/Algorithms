'''
1. there are n numbers. separate the numbers 
   into 2 groups.
2. get each sum by adding all elements in a group.
3. return the groups if the difference between 
   the sums is the minimum.

ex) numbers = [1, -3, 4, 5, -2]
    group_A = [1, 4, -2],      gropu_B = [-3, 5]
    abs(sum(group_A) - sum(group_B)) = |3 - 2| = 1 
    
    input: (1≤n≤20)
    1 -3 4 5 -2

    output:
    The gropus: [1, 4, -2], [-3, 5]
    The minimum difference: 1
'''

import sys

def getPowerSet(n, k) :
    if n == k :
        return [ [k] ]
    else :
        nth_after_k = [ [k] ]
        sth_after_k = []
        
        for i in range(k+1, n+1) :
            sth_after_k = sth_after_k + getPowerSet(n, i)
    
        for i in range(len(sth_after_k)) :
            sth_after_k[i] = [k] + sth_after_k[i]
            
        return nth_after_k + sth_after_k


def powerSet(n) :
    result = []
    for i in range(1, n+1) :
        result = result + getPowerSet(n, i)
    
    return result


def minimizeDifferenceBetween2Groups(numbers) :
    '''
    Big O(n x 2 to the power of n)
    square: 2 x 2
    cubic:  2 x 2 x 2
    2 to the n
    2 to the power of n
    2 power n
    '''

    combinations = powerSet(len(numbers))
    totalSum = sum(numbers)
    result = 908324897092234
    
    for p in combinations :
        sumGroupA = 0

        for i in p :
            # an element of the p starts from 1.
            sumGroupA += numbers[i-1] 
        
        sumGroupB = totalSum - sumGroupA
        result = min(result, abs(sumGroupA - sumGroupB))
    
    return result


def main():
    numbers = [int(x) for x in input().split()]
    print(minimizeDifferenceBetween2Groups(numbers))

if __name__ == "__main__":
    main()