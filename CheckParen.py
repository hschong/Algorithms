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
            
            
def checkParen(p) :
    '''
    p = "((()())())"
    '''
    myStack = Stack()
    
    for x in p :
        if x == '(' :
            myStack.push(x)
        else :
            if myStack.empty() == 1 :
                return "NO"
            else :
                myStack.pop()

    if myStack.empty() == 1 :
        return "YES"
    else :
        return "NO"

def main():
    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()