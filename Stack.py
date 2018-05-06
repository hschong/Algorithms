class Stack:
    def __init__(self) :
        self.data = []

    def push(self, n) :
        self.data.append(n)

    def pop(self) :
        if len(self.data) == 0 :
            return
        else :
            # self.data = self.data[:-1]
            self.data.pop()

    def size(self) :
        return len(self.data)

    def empty(self) :
        if len(self.data) == 0 :
            return 1
        else :
            return 0
            
    def top(self) :
        if len(self.data) == 0 :
            return -1
        else :
            return self.data[-1]

def main():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(4)
    stack.pop()

    print(stack.size()) 
    print(stack.top())


if __name__ == "__main__":
    main()
