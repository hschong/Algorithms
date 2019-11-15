'''
Dynamic Programming

주어진 문자열을 팰린드롬으로 만들기

팰린드롬이란, 앞으로 읽으나 뒤로 읽으나 똑같은 문자열을 말한다. 예를 들어, “aba”, “abdba”, “abffba”
는 모두 팰린드롬이다.

임의의 문자열이 주어질 때, 몇 개의 문자를 적당히 삭제하면 이를 팰린드롬으로 만들 수 있다. 예를 들어,
"abca"가 주어질 경우, 알파벳 'b’를 삭제하면 "aca"가 되므로, 팰린드롬으로 만들 수 있다.
이때, 제거해야 하는 문자의 최소 개수를 출력하는 프로그램을 작성하세요.

입력
첫 번째 줄에 문자열이 주어진다. 문자열의 길이는 3000을 넘지 않는다.

출력
팰린드롬을 만들기 위해 제거해야 하는 문자의 개수의 최솟값을 출력한다.

입력 예시 1
abcfba

출력 예시 1
1

입력 예시 2
abcdefg

출력 예시 2
6

입력 예시 3
abcbaac

출력 예시 3
2
'''

import sys


def makeStrPalindromic(str):
    '''
    문자열 data가 주어질 때, 이를 팰린드롬으로 만들기 위해 제거해야 하는 문자 개수의 최솟값을
    반환하는 함수를 작성하세요.

    T(i, j)는 주어진 문자열 str의 i번째 문자부터 j번째 문자까지를 palindrome으로 만들기 위해
    제거해야 하는 문자의 최소 개수

    O(i, j-1)     𝑇(i, j)     
    O(i+1, j-1)   O(i+1, j)   

    '''

    str_length = len(str)
    Table = [[0 for j in range(str_length)] for i in range(str_length)]

    for i in range(str_length-2, -1, -1):
        for j in range(i+1, str_length):
            if str[i] == str[j]:
                Table[i][j] = Table[i+1][j-1]
            else:
                Table[i][j] = min(Table[i+1][j], Table[i][j-1]) + 1

    return Table[0][str_length-1]


def main():
    str = input()

    print(makeStrPalindromic(str))


if __name__ == "__main__":
    main()
