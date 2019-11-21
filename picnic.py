'''
Dynamic Programming

Picnic

상훈이는 엘리스 유치원 선생님입니다. 엘리스 유치원 학생들은 다 같이 어은동산으로 소풍을 
갔습니다. 그런데 엘리스 유치원 학생들은 서로 파벌이 나뉘어 있어서 절대로 다른 조직과는 
점심을 같이 먹지 않습니다. 상훈 선생님은 점심을 먹는 애들을 보면서 어느 조직에 몇명이 
있는 지를 알려고 합니다.

학생들은 다음과 같이 앉아 있습니다. 그림 1
0 1 1 0 1 0 0
0 1 1 0 1 0 1
1 1 1 0 1 0 1
0 0 0 0 1 1 1
0 1 0 0 0 0 0
0 1 1 1 1 1 0
0 1 1 1 0 0 0

다음과 같이 파벌이 나뉩니다. 그림 2
0 1 1 0 2 0 0
0 1 1 0 2 0 2
1 1 1 0 2 0 2
0 0 0 0 2 2 2
0 3 0 0 0 0 0
0 3 3 3 3 3 0
0 3 3 3 0 0 0

여러분이 출력해야 할 것은 파벌이 몇 개 있는지, 그리고 각 파벌에는 몇 명이 있는 지를 
오름차순으로 정리한 결과입니다.

입력
첫째 줄에는 지도의 크기가 주어집니다. 지도는 항상 정사각형입니다. 두 번째 줄부터 지도의 
정보가 주어집니다. 1은 해당 자리에 학생이 있다는 뜻이고, 0은 없다는 뜻입니다.

출력
첫 번째 줄에는 파벌의 전체 개수를 출력합니다. 두 번째 줄부터 각 파벌에 속한 학생의 수를
오름차순으로 정렬한 결과를 출력합니다.

입력 예시
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

출력 예시
3
7
8
9

'''
import queue


# Direction to find adjacent nodes: Above -> Left -> Right -> below
# When the coordinate of the current node is [0][0],
direction = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def isValid(groupMap, i, j):
    length = len(groupMap)

    if 0 <= i and i < length and 0 <= j and j < length:
        return True
    else:
        return False


def getStudentsByDFS(groupMap, visited, i, j, numStudents):
    visited[i][j] = True
    numStudents += 1

    '''
    Find adjacent nodes from the current node.
    x and y are the coordinate of the adjacent nodes. 
    The coordinate of the current node is (i, j).
    The coordinates of the adjacent node of the current node are (x, y)
    '''
    for x, y in direction:
        x = i + x
        y = j + y

        if isValid(groupMap, x, y) and groupMap[x][y] == 1 and visited[x][y] == False:
            numStudents = getStudentsByDFS(
                groupMap, visited, x, y, numStudents)

    return numStudents


def getStudentsByBFS(groupMap, visited, i, j, numStudents):
    '''
    1. Queue에다가 시작점을 enqueue, BFS 시작!
    2. Queue에서 dequeue, 현재 내가 있는 위치
    3. 내 위치에서 인접한 정점 중 방문하지 않은 점점을 모두 enqueu
    4. goto 2. 로 돌아간다.
    '''
    myQueue = queue.Queue()
    myQueue.put((i, j))
    visited[i][j] = True

    while not myQueue.empty():
        current = myQueue.get()
        numStudents += 1

        i = current[0]
        j = current[1]

        for x, y in direction:
            x = i + x
            y = j + y

            if isValid(groupMap, x, y) and groupMap[x][y] == 1 and visited[x][y] == False:
                myQueue.put((x, y))
                visited[x][y] = True

    return numStudents


# find the students belong to the same group and return the number of the students
def findStudentsInGroup(groupMap, visited, i, j):
    numStudents = 0
    return getStudentsByDFS(groupMap, visited, i, j, numStudents)
    # return getStudentsByBFS(groupMap, visited, i, j, numStudents)


def getGroups(groupMap):
    # groupMap[i][j] : (i, j)의 데이터

    length = len(groupMap)
    visited = [[False for j in range(length)] for i in range(length)]
    result = []

    for i in range(length):
        for j in range(length):
            if groupMap[i][j] == 1 and visited[i][j] == False:
                numStudents = findStudentsInGroup(
                    groupMap, visited, i, j)  # 학생수
                result.append(numStudents)

    result.sort()
    return (len(result), result)


def read_input():
    size = int(input())
    returnMap = []

    for i in range(size):
        line = input()
        __line = []

        for j in range(len(line)):
            __line.append(int(line[j]))

        returnMap.append(__line)
    return returnMap


def main():
    groupMap = read_input()
    print(getGroups(groupMap))


if __name__ == "__main__":
    main()
