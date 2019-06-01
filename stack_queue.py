CONST_MAX = 10

class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        if len(self.myData) == 0:
            return True
        else:
            return False

    def isFull(self):
        if  CONST_MAX == self.getCurrentSize():
            return True
        else:
            return False

    def getCurrentSize(self):
        return len(self.myData)

    def push(self, item):
        if self.isFull():
            print("Your stack is full. hence, you can't push.")
        else:
            self.myData.append(item)

    def pop(self):
        if self.isEmpty():
            print("Your stack is empty. therefore you can't pop from the stack.")
        else:
            self.myData = self.myData[:-1]  # self.myData.pop()

    def getTop(self):
        if self.isEmpty():
            return -1
        else:
            return self.myData[-1]

    
class Queue:
    def __init__(self):
        self.myData = []

    def getCurrentSize(self):
        return len(self.myData)

    def enQueue(self, item):
        if self.isFull() != True:
            self.myData.append(item)
        else:
            print("Can't enqueue!")

    def deQueue(self):
        if self.isEmpty() != True:
            self.myData.pop()
        else:
            print("Can't dequeue!")

    def isEmpty(self):
        if self.getCurrentSize() == 0:
            print("The queue is empty!")
            return True
        else:
            return False
    
    def isFull(self):
        if self.getCurrentSize() == CONST_MAX:
            return True
        else:
            return False


def main():
    # size = int(input('type the maximum size of the stack: '))
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.pop()
    
    print("stack.getCurrentSize() = ", stack.getCurrentSize())
    
    if stack.isEmpty():
        print("Your stack is empty.")
    else:
        print("Your stack is not empty.")

    print("stack.getTop() = ", stack.getTop())

if __name__ == "__main__":
    main()