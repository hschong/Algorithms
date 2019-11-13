'''
Dynamic Programming

Longest Common Subsequence(최대 공통 부분 수열)

두 개의 문자열 s1, s2 가 주어질 때, 공통 부분 수열이란, s1과 s2가 공통으로 갖는 부분 수열을 
일컫는다. 예를 들어, s1 = “Television”, s2 = "Telephone"이라고 하면, s1과 s2의 공통 부분 수열이 
될 수 있는 문자열은 “T”, “To”, “Teln” 등이 있다.

최대 공통 부분 수열이란, 공통 부분 수열 중에서 그 길이가 최대인 것을 일컫는다. 예를 들어, 
s1 = “Television”, s2 = "Telephone"이라고 하면, 그 최대 공통 부분 수열은 "Teleon"으로써, 
그 길이는 6이다.

두 개의 문자열이 주어질 때, 최대 공통 부분 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 문자열 s1, 두 번째 줄에 문자열 s2가 주어진다. 각 길이는 1000을 넘지 않는다.

출력
최대 공통 부분 수열의 길이를 출력한다.

입력 예시
Television
Telephone

출력 예시
6

'''

import sys


def LCS(s1, s2):
    '''
    문자열 s1, s2의 최대 공통 부분 수열의 길이를 반환하는 함수를 작성하세요.
    '''

    return 0


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    s1 = input()
    s2 = input()

    print(LCS(s1, s2))


if __name__ == "__main__":
    main()
