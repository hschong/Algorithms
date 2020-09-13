class Node:
    def __init__(self):
        self.value = None
        self.next = None


class LinkedListPipe:
    def __init__(self):
        self.start = None
        self.end = None

    def addLeft(self, value):  # Add operation: O(n**2)
        node = Node()
        node.value = value

        if self.start == None:
            self.start = node
            self.end = node
        else:
            node.next = self.start
            self.start = node

    def addRight(self, value):  # Add operation: O(n)
        node = Node()
        node.value = value

        if self.start == None:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

    # Converting the pipe into the list, and returning the list.
    def getBeads(self):
        node = self.start
        result = []

        while node != None:
            result.append(node.value)
            node = node.next

        return result


def processBeads(my_input):
    '''
    my_input[i][0] : Elements' index
    my_input[i][1] : Direction to add, 0 : left, 1 : right

    my_input[0][0] = 1, my_input[0][1] = 0,
    my_input[1][0] = 2, my_input[1][1] = 1,
    my_input[2][0] = 3, my_input[2][1] = 0

    my_input[0] = ball = [1, 0]
    my_input[1] = ball = [2, 1]
    my_input[2] = ball = [3, 0]
    [[1,0], [2,1], [3,0]]
    '''

    myPipe = LinkedListPipe()
    result = []

    for ball in my_input:
        if ball[1] == 0:
            myPipe.addLeft(ball[0])
        else:
            myPipe.addRight(ball[0])

    result = myPipe.getBeads()
    return result


def main():
    n = int(input())
    myList = []

    for _ in range(n):
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
