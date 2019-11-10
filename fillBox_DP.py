'''
2 x n 의 상자를 2 x 1 의 블럭으로 채우는 경우의 수를 
1,000,000,007로 나눈 나머지를 반환하는 함수를 작성하세요.
'''
LIMIT_NUMBER = 1000000007

def fillBox(n) :
  '''
  T(i) : 2 x i 의 상자를 2 x 1 의 블럭으로 채우는 경우의 수
  T(i) : T(i-1) + T(i-2)
  '''

  if n == 1 :
    return 1
  elif n == 2 :
    return 2

  Table = [ 0 for i in range(n+1)]
  Table[1] = 1
  Table[2] = 2

  for i in range(3, n+1):
    Table[i] = (Table[i-1] + Table[i-2]) % LIMIT_NUMBER

  return Table[n]


def main():
  '''
  아래 부분은 수정하지 마세요.
  '''

  n = int(input())

  print(fillBox(n))

if __name__ == "__main__":
    main()