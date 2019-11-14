'''
Dynamic Programming

Edit Distance(두 문자열 사이의 거리)

두 문자열 s1, s2가 주어진다. 이제 s1에서 문자 하나를 추가하거나 제거할 수 있으며, 
이를 반복함으로써 s2를 얻고싶다고 하자. 예를 들어, s1 = “abc”, s2 = “bdcf” 라고 하면, s1에서 
a를 제거하고 d를 추가, 그리고 f를 추가하면 s2를 얻을 수 있다. 즉, 다음과 같은 경로로 s1에서 
s2를 얻을 수 있다.

“abc” -> “bc” -> “bdc” -> “bdcf”

두 문자열 s1, s2 사이의 거리란, s1에서 s2를 만들기 위해 필요한 문자 삽입, 삭제 횟수의 최소값으로 
정의된다. 예를 들어, s1 = “abc”, s2 = "bdcf"라면, 두 문자열의 거리는 3이다. 왜냐하면, s1에서 
문자의 추가 및 삭제를 3번 하면 s2를 얻을 수 있기 때문이며, 이보다 더 적은 연산을 통해서는 s2를 
얻을 수 없다.

두 문자열이 주어질 때, 두 문자열 사이의 거리를 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에 문자열 s1, 두 번째 줄에 문자열 s2가 주어진다. 문자열의 길이는 2000을 넘지 않는다.

출력
두 문자열 사이의 거리를 출력한다.

입력 예시
abc
bdcf

출력 예시
3
'''

import sys


def editDistanceBetweenStrings(s1, s2):
    '''
    두 문자열이 주어질 때, 두 문자열 사이의 거리를 리턴하는 함수를 작성하세요.

    1. find LCS between the strings
    2. ((len(s1))-len(LCS)) + ((len(s2))-len(LCS))
    '''
    s1_len = len(s1)
    s2_len = len(s2)
    Table = [[0 for j in range(s2_len+1)] for i in range(s1_len+1)]

    # 각 문자열의 길이를 저장한다.
    for i in range(s1_len+1):
        Table[i][0] = i

    for j in range(s2_len+1):
        Table[0][j] = j

    for i in range(1, s1_len+1):
        for j in range(1, s2_len+1):
            if s1[i-1] == s2[j-1]:
                Table[i][j] = Table[i-1][j-1]
            else:
                Table[i][j] = min(Table[i][j-1], Table[i-1][j]) + 1

    return Table[i][j]


def main():
    s1 = input()
    s2 = input()

    print(editDistanceBetweenStrings(s1, s2))


if __name__ == "__main__":
    main()
