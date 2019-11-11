'''
Dynamic Programming
줄 세우기

엘리스 초등학교에서는 합창 대회에 출전하기 위한 학생 n명을 선발중이다. 
합창 대회에 나가게 되면, n명의 학생이 모두 한 눈에 보일 수 있게끔 
좌우로 한 줄로 서서 노래를 부르게 된다.

엘리스 초등학교의 남학생끼리는 사이가 별로 좋지 않기 때문에 바로 옆에 
서는 것을 싫어한다. 즉, 남학생의 좌우에는 항상 여학생이 서 있어야 
남학생들끼리 싸우는 것을 막을 수 있다. 예를 들어, P를 남학생, 
Q를 여학생이라고 한다면 아래와 같은 배치는 가능하다.

P Q Q P Q Q Q Q Q Q

하지만 아래와 같은 배치는 불가능하다

P P Q Q Q P Q Q P P

n명의 학생을 선발하려 하고, 남학생과 여학생은 충분히 많다고 하자. 
n명의 학생을 배치하는 경우의 수를 구하는 프로그램을 작성하시오. 
단, 그 경우의 수가 매우 커질 수 있으므로, 경우의 수를 1,000,000,007로 
나눈 나머지를 출력한다

입력

합창 대표 학생의 수 n이 주어진다. (1 ≤ n ≤ 100)

출력

학생 대표를 일렬로 세우는 경우의 수를 1,000,000,007로 나눈 나머지를 
출력한다.

입력 예시
5

출력 예시
13

예제 설명
아래와 같이 13가지의 경우가 있다.

Q Q Q Q Q   Q Q Q Q P   Q Q Q P Q   Q Q P Q Q   Q P Q Q Q   
P Q Q Q Q   Q Q P Q P   Q P Q Q P   P Q Q Q P   Q P Q P Q   
P Q Q P Q   P Q P Q Q   P Q P Q P

'''


import sys

LIMIT_NUMBER = 1000000007


def lining(n):
    '''
    n명의 학생을 일렬로 줄세우는 경우의 수를 1,000,000,007 로 나눈 
    나머지를 반환하는 함수를 작성하세요.


    T(i) : i명의 학생을 일렬로 세우는 경우의 수
    P로 시작 시 다음에 무조건 Q가 와야 함 => PQ + T(i-2)
    Q로 시작 시 다음에 아무거나 와도 됨 => Q + T(i-1)

    T(i) = T(i-1) + T(i-2)
    '''
    Table = [0 for i in range(n+1)]
    Table[1] = 2
    Table[2] = 3

    for i in range(3, n+1):
        Table[i] = (Table[i-1] + Table[i-2]) % LIMIT_NUMBER

    return Table[n]


def main():
    data = int(input())
    print(lining(data))


if __name__ == "__main__":
    main()
