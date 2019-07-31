# Using heap to implement priority queue.
# Heap is a complete binary tree which has the operations of 
# add(log n) and remove(log n).
 
# root node must starts from self.data[1] 
# because of finding left and right children 
# by the index calculation.
# the smallest index is the highest priority.
        
#             1                 <- root == self.data[index]
#     2               3         <- left == self.data[index * 2]
# 4       5       6       7     <- right  == self.data[index * 2 + 1]
# [0|1|2|3|4|5|6|7]

class priorityQueue:
    def __init__(self) :
        # Making an empty queue.
        self.data = [0]
        
    def getLength() :
        return len(self.data)

    def top(self) : # return the highest priority.
        if self.getLength() == 1 :
            return -1
        else :
            return self.data[1]

    def push(self, value) :
        self.data.append(value)

        # index is the current location of 
        # the added value in the list.
        index = self.getLength() - 1 
        
        # if index == root then exit from the loop.
        while index != 1 :
            # the smaller value is the higher priority.
            if self.data[index//2] > self.data[index] : 
                # move to the top by swapping.
                # self.data[index//2] is the parent node 
                # because the list(data) is a complete binary tree.
                self.data[index//2], self.data[index] = self.data[index], self.data[index//2]
                index = index // 2 # the new index because of swapping.
            else :
                break
                
    def pop(self) :
        if len(self.data) == 1 : # the list is empty.
            return
        
        # move the lowest priority node to the top.
        self.data[1] = self.data[-1] 
        self.data.pop()
        
        # index is the current location of 
        # the lowest priority node in the list.
        index = 1 

        # go down to the higher priority node 
        # at the same level in the tree.
        #    1. No child
        #    2. Only left child
        #    3. Both children
        while True : 
            # pointing to the higher priorty between the both children.
            priority = -1

            # No child 
            if self.getLength() - 1 < index * 2 : 
                break

            # No right child(only left child).    
            elif self.getLength() - 1 < index * 2 + 1 : 
                priority = index * 2 # the index of the left child

            # both children
            # the smaller is the higher priority.
            else : 
                if self.data[index*2] < self.data[index*2+1] :
                    priority = index * 2 
                else :
                    priority = index * 2 + 1
            
            # set the new index
            if self.data[index] > self.data[priority] :
                self.data[index], self.data[priority] = self.data[priority], self.data[index]
                index = priority # the priority is the new index.
            else :
                break

def main():
    myPQ = priorityQueue()

    myPQ.push(1)
    myPQ.push(4)
    myPQ.push(3)
    myPQ.push(2)

    print(myPQ.top())
    myPQ.pop()

    print(myPQ.top())
    myPQ.pop()

if __name__ == "__main__":
    main()