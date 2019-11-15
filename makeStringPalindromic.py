'''
Dynamic Programming

Function to find out the minimum number of deletions required to
convert a given string str[i..j] into a palindrome

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

입력 예시들
abcfba      abcdefg     abcbaac

출력 예시들
1           6           2

'''

import sys


def makeStrPalindrome(str):
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


def getMinDeletions(str):
    # Time complexity: O(2ⁿ), Space complexity: O(1)
    length = len(str)

    # base condition
    if length == 0 or length == 1:
        return 0

    if str[0] == str[-1]:
        return getMinDeletions(str[1:-1])
    else:
        '''
        last character of string is different to the first character
        1. Remove last character & recur for the remaining substring
        2. Remove first character & recur for the remaining substring
        return 1 (for remove operation) + minimum of the two values
        '''
        return min(getMinDeletions(str[1:]), getMinDeletions(str[0:-1])) + 1


def main():
    str = input()

    print(makeStrPalindrome(str))
    print(getMinDeletions(str))


if __name__ == "__main__":
    main()
