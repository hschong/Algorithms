class ListPipe:
    def __init__(self):
        self.pipe = []

    def addLeft(self, number):
        # Add operation: 1+2+3+4+5+6+ ... + n = n(n+1)/2, O(n**2)
        self.pipe = [number] + self.pipe

    def addRight(self, number):
        # 1+1+1 + ... + 1 = n, O(n)
        self.pipe.append(number)

    def getBeads(self):
        return self.pipe


def processBeads(myInput):
    '''
    myInput[i][0] : Elements' index
    myInput[i][1] : Direction to add, 0 : left, 1 : right

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0

    myInput[0] = ball = [1, 0]
    myInput[1] = ball = [2, 1]
    myInput[2] = ball = [3, 0]
    [[1,0], [2,1], [3,0]]
    '''

    myPipe = ListPipe()

    for ball in myInput:
        if ball[1] == 0:
            myPipe.addLeft(ball[0])
        else:
            myPipe.addRight(ball[0])

    return myPipe.getBeads()


def main():
    n = int(input())
    myList = []

    for i in range(n):
        myList.append([int(v) for v in input().split()])

    print(*processBeads(myList))


if __name__ == "__main__":
    main()

'''
Input sample
3
1 0
2 1
3 0

Output sample
3 1 2
'''
