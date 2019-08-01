# ‘(())’ is YES. 
# ‘(()))’ or ‘(()()(’ is NO.

def checkParen(parentheses):    
    # 0. return YES if the length of the parentheses is 0 or "()"
    # 1. find an adjacent '(' and ')' in the parentheses.
    # 2. remove them in the parentheses.
    # 3. go to #0
    
    if len(parentheses) <= 1:
        if len(parentheses) == 0:
            return "YES"
        else: #parentheses include '(' or ')'.
            return "NO"
    elif parentheses == "()":
        return "YES"
        
    # find '()'  
    #'        i '
    #'((())())))'
    for i in range(len(parentheses)-1):
        if parentheses[i] == '(' and parentheses[i+1] == ')':
            newParentheses = parentheses[:i] + parentheses[i+2:]
            return checkParen(newParentheses)
    
    return "NO"

def main():
    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()