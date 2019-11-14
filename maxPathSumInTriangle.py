'''
Dynamic Programming

Maximum path sum in a triangle(숫자 삼각형).

다음과 같이 높이 n의 숫자 삼각형이 주어진다.

4
3 5
1 3 8
2 5 3 4
3 6 6 8 2

맨 위에서 출발하여 맨 아래까지 내려갈 것인데, 내려갈 때에는 항상 바로 아래, 혹은 오른쪽 아래로밖에 
내려가지 못한다. 예를 들어, 현재 꼭지점에는 4 가 있으며, 여기서는 3 혹은 5로 내려갈 수 있다. 
하지만 5의 입장에서는 바로 아래인 3, 혹은 오른쪽 아래인 8로는 내려갈 수 있지만, 왼쪽 아래인 1로는 
내려가지 못한다. 맨 위에서 맨 아래까지 내려갈 수 있는 경로는 여러가지가 있을 수 있다. 
이 중 그 경로에 포함되는 숫자의 합을 최대화 하는 경로가 존재한다. 이를 최대 경로라고 정의할 때, 
최대 경로에 존재하는 숫자의 합을 구하는 프로그램을 작성하시오. 

위의 예에서는 ‘4 - 5 - 8 - 4 - 8’ 의 경로가 최대 경로이며, 그 합은 29이다.

입력
첫 번째 줄에 숫자 삼각형의 높이 n이 주어진다. 
(1≤n≤100) 두 번째 줄부터 숫자 삼각형이 주어진다.

출력
최대 경로에 존재하는 숫자의 합을 출력한다.

입력 예시
5
4
3 5
1 3 8
2 5 3 4
3 6 6 8 2

출력 예시
29
'''


import sys


def getMaxPathSum(numbers):
    '''
    숫자삼각형 traingle이 주어질 때, 최대 경로에 존재하는 숫자의 합을 반환하는 함수를 작성하세요.
    T(i, j)는 T(i, j)에 도착하였을 때, 얻을 수 있는 합의 최댓값
    T(i, j) = max(T(i-1, j-1), T(i-1, j)) + numbers(i, j)
    '''

    height = len(numbers)
    Table = [[0 for j in range(i+1)] for i in range(height)]
    Table[0][0] = numbers[0][0]

    for i in range(1, height):
        for j in range(i+1):
            if j == 0:
                Table[i][j] = Table[i-1][j] + numbers[i][j]
            elif i == j:
                Table[i][j] = Table[i-1][j-1] + numbers[i][j]
            else:
                Table[i][j] = max(Table[i-1][j], Table[i-1]
                                  [j-1]) + numbers[i][j]

    return max(Table[height-1])


def main():
    height = int(input())
    numbersInTriangle = []

    for i in range(height):
        numbersInTriangle.append([int(v) for v in input().split()])

    print(getMaxPathSum(numbersInTriangle))


if __name__ == "__main__":
    main()
