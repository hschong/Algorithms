'''
1 ~ m 까지의 수를 더하여 n을 만드는 경우의 수를 1,000,000,007로 
나눈 나머지를 반환하는 함수를 작성하세요.
'''

LIMIT_NUMBER = 1000000007

def makeNumber(n, m) :
  '''
  T(i) : 1 ~ m 까지의 수를 더하여 n를 만드는 경우의 수
  T(i) : T(i-1) + T(i-2) + T(i-3) + ... + T(i-m)
  
  Base condition
  m = 3
  T[1] T[2] T[3]
  '''  
  
  Table = [ 0 for i in range(n+1)]

  # Base condition
  for i in range(1, m+1) :
    Table[i] = (sum(Table[1:i]) + 1) % LIMIT_NUMBER

  for i in range(m+1, n+1) :
    Table[i] = (sum(Table[i-m:i])) % LIMIT_NUMBER
  
  return Table[n]
  

def main():
    '''
    아래 부분은 수정하지 마세요.
    '''

    firstLine = [int(x) for x in input().split()]

    n = firstLine[0]
    m = firstLine[1]

    print(makeNumber(n, m))

if __name__ == "__main__":
    main()
