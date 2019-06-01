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