'''
Graph

Virus

바이러스

엘리스 바이러스는 그 개체 수가 불규칙하기로 매우 유명한 바이러스입니다. 이 바이러스의 
개체 수는 1초가 지날때마다 변화하는데, 그 개체 수가 2배로 늘어날 수도 있고, 1/3배로 줄어들 
수도 있습니다. 예를 들어, 현재 시간에 바이러스가 10마리라면, 1초 후에는 20마리가 될 수도 
있고, 3마리가 될 수도 있습니다.

엘리스 바이러스는 특성상 10000 마리를 초과하지 못합니다. 예를 들어, 현재 개체수가 7000개라면, 
2배로 늘어날 수 없다는 의미입니다. 왜냐하면 2배로 늘어날 경우 그 개체 수가 14000 마리가 
되는데, 이는 10000 마리를 초과하기 때문입니다.

엘리스 바이러스는 초기에 그 개체 수가 1개라고 할 때, 일정 시간이 지나면 특정한 개체수 m마리가 
될 수 있는지를 판단하는 프로그램을 작성하세요. 예를 들어, m = 10일 경우, 엘리스 바이러스의 
개체 수가 10마리가 될 수 있는가를 묻는 것이며, 이는 가능합니다. 그 가능한 방법 중 하나는 
다음과 같습니다.

1 2 4 8 16 32 5 10


입력
첫째 줄에 엘리스 바이러스의 최종 개체 수 m이 주어집니다.

출력
엘리스 바이러스의 개체 수가 1부터 시작할 때, 개체 수가 m개가 될 수 있다면 True, 아니면 False를 
출력합니다.

입력 예시
10

출력 예시
True

'''

import sys
sys.setrecursionlimit(100000)

MAX_VIRUS = 10000


def findTarget(startNode, target, visited):
    if startNode == target:
        return True

    visited[startNode] = True
    connectedNodes = [startNode*2, startNode//3]

    for node in connectedNodes:
        if 0 < node and node <= MAX_VIRUS and visited[node] == False:
            if findTarget(node, target, visited) == True:
                return True

    return False


def checkVirus(m):
    visited = [False for i in range(MAX_VIRUS+1)]

    return findTarget(1, m, visited)


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    m = int(input())
    print(checkVirus(m))


if __name__ == "__main__":
    main()
