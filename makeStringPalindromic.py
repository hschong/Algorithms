'''
Dynamic Programming

Function to find out the minimum number of deletions required to
convert a given string str[i..j] into a palindrome
https://www.techiedelight.com/find-minimum-number-deletions-convert-string-into-palindrome/

주어진 문자열을 팰린드롬으로 만들기

팰린드롬이란, 앞으로 읽으나 뒤로 읽으나 똑같은 문자열을 말한다. 예를 들어,
“aba”, “abdba”, “abffba”는 모두 팰린드롬이다.

임의의 문자열이 주어질 때, 몇 개의 문자를 적당히 삭제하면 이를 팰린드롬으로
만들 수 있다. 예를 들어, "abca"가 주어질 경우, 알파벳 'b’를 삭제하면 "aca"가
되므로, 팰린드롬으로 만들 수 있다.
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

#     The worst case time complexity of below solution is
#     Time complexity: 𝐎(2ⁿ) and Space complexity: 𝐎(1)
#     The worst case happens when there is no repeated character present
#     in the given string and each recursive call will end up in two
#     recursive calls.


def getMinNumOfDeletionsUsingDC(str):
    length = len(str)

    # base condition
    if length == 0 or length == 1:
        return 0

    if str[0] == str[-1]:
        return getMinNumOfDeletionsUsingDC(str[1:-1])
    else:
        '''
        last character of string is different to the first character
        1. Remove last character & recur for the remaining substring
        2. Remove first character & recur for the remaining substring
        return 1 (for remove operation) + minimum of the two values
        '''
        return min(getMinNumOfDeletionsUsingDC(str[1:]), getMinNumOfDeletionsUsingDC(str[0:-1])) + 1


# This problem is also a classic variation of LCS(Longest Common Subsequence)
# problem. The idea is to find the Longest Palindromic Substring of given string.
# Then the minimum number of deletions required will be size of the string minus
#  size of the longest palidromic subsequence. We can easily find the longest
#  palindromic substring by taking LCS of a given string with its reverse.
#  i.e. LCS(str, reverse(str))
# Time complexity: 𝐎(n²) and Space complexity: 𝐎(n²)

def getMinNumOfDeletionsUsingDP(str):
    str_length = len(str)
    str_x = str
    str_y = str[::-1]  # reverse str

    # make a table[i][j] which stores the length of LCS of substring
    # 𝑇(i-1, j-1)   𝑇(i-1, j)
    # 𝑇(i, j-1)     𝑇(i, j)
    table = [[0 for j in range(str_length+1)] for i in range(str_length+1)]

    for i in range(1, str_length+1):
        for j in range(1, str_length+1):
            if str_x[i-1] == str_y[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    return str_length - table[i][j]


def main():
    str = input()

    print(getMinNumOfDeletionsUsingDC(str))
    print(getMinNumOfDeletionsUsingDP(str))


if __name__ == "__main__":
    main()
