'''
Dynamic Programming
1 ~ m 까지의 수를 더하여 n을 만드는 경우의 수를 1,000,000,007로 
나눈 나머지를 반환하는 함수를 작성하세요.
'''

LIMIT_NUMBER = 1000000007


def makeNumber(n, m):
    '''
    T(n) : 1 ~ m 까지의 수를 더하여 n를 만드는 경우의 수

    ex) n = 5, m = 3
    T(5)      T(4)          T(3)             T(2)
          1 + 1+1+1+1   2 + 1+1+1     3(m) + 1+1          
          1 + 1+1+2     2 + 1+2       3(m) + 2
          1 + 1+2+1     2 + 2+1     
          1 + 1+3       2 + 3       
          1 + 2+1+1     
          1 + 2+2       
          1 + 3+1

    T(5) = T(4) + T(3) + T(2) = 7 + 4 + 2

    T(n) : T(n-1) + T(n-2) + ... + T(n-m)

    '''

    Table = [0 for i in range(n+1)]

    '''
  Base cases
  m = 3, T[1] T[2] ... T[m] 
  '''
    for i in range(1, m+1):
        Table[i] = (sum(Table[1:i]) + 1) % LIMIT_NUMBER

    '''
  T[m+1] ... T[n]
  '''
    for i in range(m+1, n+1):
        Table[i] = (sum(Table[i-m:i])) % LIMIT_NUMBER

    return Table[n]


def main():
    inputLine = [int(x) for x in input().split()]

    n = inputLine[0]
    m = inputLine[1]

    print(makeNumber(n, m))


if __name__ == "__main__":
    main()
