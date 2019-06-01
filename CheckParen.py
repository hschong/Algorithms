# 올바른 괄호인지 판단하기
# 본 문제에서는 입력으로 주어지는 괄호가 올바른 괄호인지를 판단하는 
# 프로그램을 작성합니다. 예를 들어, ‘(())’ 은 올바른 괄호이지만, 
# ‘(()))’, 혹은 ‘(()()(’ 는 올바른 괄호가 아닙니다.

def checkParen(p):
    '''
    괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    '''
    
    '''
    1. p에서 인접한 괄호 '()'를 찾는다
    2. 찾은 '()'를 제거한다
    3. checkParen 에게 다시 물어 본다
    '''
    
    if len(p) <= 1:
        if len(p) == 0:
            return "YES"
        else: #'(' or ')'
            return "NO"
    elif p == "()":
        return "YES"
        
    # find '()'  
    #'        i '
    #'((())())))'
    for i in range(len(p)-1):
        if p[i] == '(' and p[i+1] == ')':
            q = p[:i] + p[i+2:]
            
            return checkParen(q)
    
    return "NO"

def main():
    '''
    Do not change this code
    '''

    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()