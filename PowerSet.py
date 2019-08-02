import sys

# The power set of any set S is the set of all subsets of S.

# Elements in the set are natural numbers and 
# the numbers starts from 1 to n.
# the n is the number of the elements in the set S. 

# For instance, n = 3
# set S = {1, 2, 3}
# power set of set A is { {}, {1}, {2}, {3}, 
# {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} }

# getPowerSet
# the first element of the each subset 
# in the power set should start with element k.
# ex) n = 3, k = 2
#     [1, 2, 3] == set A
#     [[2], [2, 3]] == getPowerSet(n, k)

def getPowerSet(n, k) :
    if n == k :
        return [ [k] ]
    else :
        nth_after_k = [ [k] ] # nothing after k
        sth_after_k = [] # something after k
        
        # getPowerSet(3, 1)
        # nth_after_k = [ [1] ]
        # sth_after_k = [ [2], [2, 3], [3] ]
        # nth_after_k + sth_after_k == 
        #   [ [1], [1, 2, ...], [1, 3, ...] ] 
        
        # getPowerSet(3, 2) == [[2], [2, 3]]
        # getPowerSet(3, 3) == [[3]]
        # getPowerSet(3, 2) + getPowerSet(3, 3) 
        #   == [[2], [2, 3], [3]]

        for i in range(k+1, n+1) :
            sth_after_k = sth_after_k + getPowerSet(n, i)
    
        for i in range(len(sth_after_k)) :
            sth_after_k[i] = [k] + sth_after_k[i]
            
        return nth_after_k + sth_after_k


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


def main():
    n = int(input())

    result = powerSet(n)
    
    for line in result :
        print(*line)

if __name__ == "__main__":
    main()