'''
if the parentheses are like ‘(())’, the program 
returns YES. 
The program return NO if the parentheses are like ‘
(()))’ or ‘(()()(’.
'''


def checkParen(parentheses):
    '''
    0. return YES if the length of the parentheses is 0 or "()".
    1. find an adjacent rounded brakets like '()' in the parentheses.
    2. remove them in the parentheses.
    3. go to step #0
    𝐎(n²)
    '''

    if len(parentheses) <= 1:
        if len(parentheses) == 0:
            return "YES"
        else:  # parentheses include '(' or ')'.
            return "NO"
    elif parentheses == "()":
        return "YES"

    '''    
    find '()'  
    '        i '
    '((())())))'
    '''
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
