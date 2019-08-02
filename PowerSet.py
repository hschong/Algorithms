import sys

# The power set of any set S is the set of all subsets of S.

# Elements in the set are natural numbers and 
# the numbers starts from 1 to n.
# the n is the number of the elements in the set A. 

# For instance, n = 3
# set A = {1, 2, 3}
# power set of set A is { {}, {1}, {2}, {3}, 
# {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} }

def powerSet(n) :
    '''
    set A has n elements.
    elements in power set of A should be added into list by ascending.
    return the list.
    ex) n = 3 
        [ [1], [1, 2], [1, 3], [1, 2, 3], [2], [2, 3], [3] ]
    '''

    result = []
    for i in range(1, n+1) :
        result = result + getPowerSet(n, i)
    
    return result


# the first element of the each subset 
# in the power set should start with element k.
# ex) n = 3, k = 2
#     [1, 2, 3] == set A
#     [[2], [2, 3]] == getPowerSet(n, k)

def getPowerSet(n, k) :
    if n == k :
        return [ [n] ]
    else :
        # getPowerSet(3, 1)
        # result = [ [1], [1, 2, ...], [1, 3, ...] ] 
        # temp = [ [2], [2, 3], [3] ]
        result = [ [k] ] # k 뒤에 아무 것도 없는 경우
        temp = [] # k 뒤에 붙는 경우
        
        for i in range(k+1, n+1) : # i = k+1 ~ n
            temp = temp + getPowerSet(n, i)
    
        for i in range(len(temp)) :
            temp[i] = [k] + temp[i]
            
        return result + temp

def main():
    n = int(input())

    result = powerSet(n)
    
    for line in result :
        print(*line)

if __name__ == "__main__":
    main()