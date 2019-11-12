'''
Dynamic Programming

짜장, 짬뽕, 볶음밥

중식을 좋아하는 상훈이는 늘 점심엔 짜장, 짬뽕, 볶음밥 셋 중 하나를 
먹어야 기분이 좋아진다. 상훈이에겐 규칙이 하나 있는데, 전날 먹은 음식은 
먹지 않는다는 것이다. 예를 들어 어제 짜장면을 먹었으면, 오늘은 짬뽕이나 
볶음밥 중 하나를 먹어야 하는 것이다.

짜장, 짬뽕, 볶음밥 선호도(먹고 싶은 정도)는 그날그날 다른데, 이 선호도가 
주어질 때, 상훈이의 총 선호도를 최대로 만들어주는 조합을 찾으면 된다. 
(선호도는 먹은 음식 선호도의 총합으로 계산된다.)

입력
첫 줄에는 며칠동안 먹을 것인지에 대한 정수(1≤n≤100,000)가 주어지고 
그 밑으로 각각 짜장, 짬뽕, 볶음밥에 대한 하루별 선호도가 주어진다. 
선호도는 양의 정수만 들어온다고 가정한다.

출력
상훈이가 얻을 수 있는 선호도 총합의 최댓값을 출력한다.

입력 예시
3
27 8 35
18 36 10
7 22 45

출력 예시
116

'''

import sys


def getFavoriteMenu(foodScoresDuringTheDays):
    '''
    각 날짜 별 음식의 선호도가 list로 주어질 때, 상훈이가 얻을 수 있는 
    선호도 총합의 최댓값을 반환하는 함수를 작성하세요.

    ex)
    Days    짜 짬 볶
    Day 1   27  8 35
    Day 2   18 36 10
    Day 3    7 22 45

    T(i, 1) : 매일 한 번씩 한 가지 음식만 먹으며, i번째 날에는 짬뽕
    T(i, 2) : 매일 한 번씩 한 가지 음식만 먹으며, i번째 날에는 볶음
    T(i, 0) : 매일 한 번씩 한 가지 음식만 먹으며, i번째 날에는 짜장

    T(i, 0) = max(T(i-1, 1), T(i-1, 2)) + food(i, 0)
    T(i, 1) = max(T(i-1, 0), T(i-1, 2)) + food(i, 1)
    T(i, 2) = max(T(i-1, 0), T(i-1, 1)) + food(i, 2)
    '''
    days = len(foodScoresDuringTheDays)
    Table = [[0 for i in range(3)] for j in range(days)]

    # Base conditions
    Table[0][0] = foodScoresDuringTheDays[0][0]
    Table[0][1] = foodScoresDuringTheDays[0][1]
    Table[0][2] = foodScoresDuringTheDays[0][2]

    for i in range(1, days):
        Table[i][0] = max(Table[i-1][1], Table[i-1][2]) + \
            foodScoresDuringTheDays[i][0]
        Table[i][1] = max(Table[i-1][0], Table[i-1][2]) + \
            foodScoresDuringTheDays[i][1]
        Table[i][2] = max(Table[i-1][0], Table[i-1][1]) + \
            foodScoresDuringTheDays[i][2]

    return max(Table[days-1])


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    days = int(input())
    foodScoresDuringTheDays = []

    for i in range(days):
        dailyFoodScores = [int(x) for x in input().split()]
        foodScoresDuringTheDays.append(dailyFoodScores)

    print(getFavoriteMenu(foodScoresDuringTheDays))


if __name__ == "__main__":
    main()
