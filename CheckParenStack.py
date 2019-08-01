CONST_STACK_MAX = 100
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
        if self.getSize() == 0 :
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
            
# '''
# 괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
# '''

# '''
# 1. p에서 인접한 괄호 '()'를 찾는다
# 2. 찾은 '()'를 제거한다
# 3. checkParen 에게 다시 물어 본다
# ...
            
def checkParen(p) :
    # '''
    # p = "((()())())"
    # '''
    myStack = Stack(CONST_STACK_MAX)
    
    for x in p :
        if x == '(' :
            if myStack.push(x) == False :
                break
        else :
            if myStack.isEmpty() == True :
                return "NO"
            else :
                myStack.pop()

    if myStack.isEmpty() == True :
        return "YES"
    else :
        return "NO"

def main():
    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()