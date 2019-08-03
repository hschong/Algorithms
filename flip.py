'''
Algorithm I
3. Divide and Conquer I.mp4

뒤집기 

다음과 같이 n x m 의 판이 주어집니다. 
(1≤n≤1000,1≤m≤10) 각각의 판에는 흰색 혹은 검은색이 
칠해져 있으며, 흰색은 0, 그리고 검은색은 1로 주어진다.

이제 이 모든 판의 색깔을 흰색으로 만들려고 한다. 색을 
바꾸는 것은 특정 칸을 ‘클릭’ 함으로써 이루어진다. 
한 번에 한 칸을 ‘클릭’ 할 수 있으며, 한 칸을 ‘클릭’ 할 
경우에는 그 칸의 색깔 뿐만 아니라 상, 하, 좌, 우의 
모든 색깔이 바뀐다. 즉, 흰색일 경우에는 검은색으로, 
검은색일 경우에는 흰색으로 바뀐다. 만약 (0, 0)과 
같이 상, 하, 좌, 우 중에서 몇몇 칸만 존재할 경우, 
그 존재하는 칸의 색깔만 바뀌게 된다.

n x m 의 판의 상태가 주어질 때, 이를 모두 흰색으로 
만들기 위하여 ‘클릭’ 해야하는 최소 칸의 수를 출력하는 
프로그램을 작성하시오. 만약, '클릭’을 통하여 모두 
흰색으로 바꾸는 것이 불가능하다면 -1을 출력한다.
'''

'''
입력
첫째 줄에 n, m이 주어진다. (1≤n≤1000, 1≤m≤10) 두 번째 
줄부터 각 칸의 상태가 주어진다. 0은 흰색을 의미하며, 
1은 검은색을 의미한다.

출력
모든 칸을 흰색으로 만들기 위하여 ‘클릭’ 해야하는 최소 
칸의 수를 출력한다. 만약 '클릭’을 통하여 모두 흰색으로 
바꾸는 것이 불가능하다면 -1을 출력한다.


입력 예시 1
4 3
0 1 0
1 0 1
1 0 1
0 1 0

출력 예시 1
2

설명 1
(2, 1)을 클릭한 후, (1, 1)을 클릭하면 모든 칸이 흰색이 
된다.


입력 예시 2
4 6
0 1 1 0 1 0
1 1 0 0 1 1
1 0 0 0 1 0
0 1 0 0 0 0

출력 예시 2
4

설명 2
(1, 2), (2, 1), (1, 4), 그리고 (1, 1)을 차례대로 
클릭하면 모든 칸을 흰색으로 만들 수 있다.


입력 예시 3
4 4
0 0 0 0
0 0 1 1
0 0 1 0
0 0 0 0

출력 예시 3
-1

'''

import sys
import copy
sys.setrecursionlimit(100000)

def powerSetInternal(temp, n) :
    result = []

    if len(temp) == 0 :
        for i in range(1, n+1) :
            result.append([i])

            temp.append(i)
            result = result + powerSetInternal(temp, n)
            temp.pop()
    else :
        last = temp[-1]

        for i in range(last+1, n+1) :
            temp.append(i)
            result.append(list(temp))

            result = result + powerSetInternal(temp, n)
            temp.pop()

    return result


def singleFlip(myMap, y, x, n, m) :
    dy = [-1, 0, 0, 0, 1]
    dx = [0, -1, 0, 1, 0]

    for k in range(len(dy)) :
        yy = y + dy[k]
        xx = x + dx[k]

        if yy >= 0 and yy < n and xx >= 0 and xx < m :
            myMap[yy][xx] = 1 - myMap[yy][xx]

    return myMap


def isPossible(myMap, assignment) :
    cnt = 0 

    n = len(myMap)
    m = len(myMap[0])

    for x in assignment :
        singleFlip(myMap, 0, x-1, n, m)
        cnt += 1

    for i in range(1, n) :
        for j in range(m) :
            if myMap[i-1][j] == 1 :
                singleFlip(myMap, i, j, n, m)
                cnt += 1

    for j in range(m) :
        if myMap[n-1][j] == 1 :
            return -1

    return cnt


def flip(myMap, n, m) :
    '''
    모든 칸을 흰색으로 바꾸기 위해 최소로 클릭해야 
    하는 횟수를 반환하는 함수를 작성하세요.
    '''

    combinations = [[]] + powerSetInternal([], m)
    cnt = n * m + 1

    for assignment in combinations :
        localCnt = isPossible(copy.deepcopy(myMap), assignment)

        if localCnt != -1 :
            cnt = min(cnt, localCnt)

    if cnt == n * m + 1 :
        return -1
    else :
        return cnt


def main():
    data = [int(x) for x in input().split()]

    n = data[0]
    m = data[1]

    myMap = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        myMap.append(line)

    print(flip(myMap, n, m))

if __name__ == "__main__":
    main()