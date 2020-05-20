class LinkedListElement:
    def __init__(self):
        self.value = None
        self.next = None


class LinkedListPipe:
    def __init__(self):
        self.startElement = None
        self.endElement = None

    def addLeft(self, number):
        # Add operation: O(n)
        newElement = LinkedListElement()
        newElement.value = number

        if self.startElement == None:
            self.startElement = newElement
            self.endElement = newElement
        else:
            newElement.next = self.startElement
            self.startElement = newElement

    def addRight(self, number):
        newElement = LinkedListElement()
        newElement.value = number

        if self.startElement == None:
            self.startElement = newElement
            self.endElement = newElement
        else:
            self.endElement.next = newElement
            self.endElement = newElement

    # Converting the pipe into the list, and returning the list.
    def getBeads(self):
        c = self.startElement
        result = []

        while c != None:
            result.append(c.value)
            c = c.next

        return result


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

    myPipe = LinkedListPipe()
    result = []

    for ball in myInput:
        if ball[1] == 0:
            myPipe.addLeft(ball[0])
        else:
            myPipe.addRight(ball[0])

    result = myPipe.getBeads()
    return result


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
