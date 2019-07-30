class Stack:
    def __init__(self, max) :
        self.data = []
        self.maxSize = max

    def push(self, n) :
        if self.isFull() == False :
            self.data.append(n)
            return True
        else :
            print("Your stack is full. hence, you can't push.")
            return False

    def pop(self) :
        if self.isEmpty() == True :
            print("Your stack is empty. hence, you can't pop from the stack.")
            return False
        else :
            # self.data = self.data[:-1]
            self.data.pop()
            return True

    def getSize(self) :
        return len(self.data)

    def isEmpty(self) :
        if len(self.data) == 0 :
            print('The stack is empty.')
            return True
        else :
            return False

    def isFull(self) :
        if self.getSize() == self.maxSize :
            print('The stack is full.')
            return True
        else :
            return False
            
    def getTop(self) :
        if self.isEmpty() == True :
            return -1
        else :
            return self.data[-1]

def main():
    stack = Stack(100)

    stack.push(1)
    stack.push(2)
    stack.push(4)
    stack.pop()

    print(stack.getSize()) 
    print(stack.getTop())


if __name__ == "__main__":
    main()