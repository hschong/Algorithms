class priorityQueue:

    def __init__(self) :
        self.data = [0] # Making an empty queue. Do not use the index 0 because of root node position.
        # self.data[1] <-- root node


    def push(self, value) :
        self.data.append(value)
        index = len(self.data) - 1 # index :the current location of the added element in the list.
        
        # if index == root then exit from the loop.
        while index != 1 : 
            # the smaller value is higher priority.
            if self.data[index//2] > self.data[index] : 
                self.data[index//2], self.data[index] = self.data[index], self.data[index//2] # move to the top by swapping
                index = index // 2 # the new index because of swapping.
            else :
                break
                
                
    def top(self) : # return the highest priority.
        if len(self.data) == 1 :
            return -1
        else :
            return self.data[1]


    def pop(self) :
        if len(self.data) == 1 : # the list is empty.
            return
            
        self.data[1] = self.data[-1] # move the lowest priority node to the top.
        self.data.pop()
        
        index = 1 # index :the current location of the lowest priority node in the list.
        
        # go down to higher priority node at the same level in the tree.
        #    1. No child
        #    2. Only left child
        #    3. Both children
        while True : 
            priority = -1
            
            # No child : the length of the list is smaller than index * 2 in complete binary tree.
            if len(self.data) - 1 < index * 2 : 
                break
            # No right child(only left child) in complete binary tree.    
            elif len(self.data) - 1 < index * 2 + 1 : 
                priority = index * 2 # the index of the left child
            # both children
            else : 
                if self.data[index*2] < self.data[index*2+1] :
                    priority = index * 2 # the left child is higher than the right one.
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
