class LinkedListElement :
    def __init__(self) :
        self.value = None
        self.next = None

class LinkedListPipe:
    def __init__(self) :
        self.start = None
        self.end = None

    def addLeft(self, n) :
        '''
        Adding an element into the pipe on the left.
        '''
        elem = LinkedListElement()
        elem.value = n

        if self.start == None :
            self.start = elem
            self.end = elem
        else :
            elem.next = self.start
            self.start = elem
        pass

    def addRight(self, n) :
        '''
        Adding an eleement into the pipe on the right.
        '''
        elem = LinkedListElement()
        elem.value = n

        if self.start == None :
            self.start = elem
            self.end = elem
        else :
            self.end.next = elem
            self.end = elem

    def getBeads(self) :
        '''
        Converting the pipe into the list, and returning the list.
        '''
        counter = self.start
        result = []

        while counter != None :
            result.append(counter.value)
            counter = counter.next

        return result

def processBeads(myInput) :
    '''
    myInput[i][0] : Elements' index
    myInput[i][1] : Direction to add, 0 : left, 1 : right

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0
    '''

    myPipe = LinkedListPipe()

    for x in myInput :
        if x[1] == 0 :
            myPipe.addLeft(x[0])
        else :
            myPipe.addRight(x[0])

    return myPipe.getBeads()

def main():
    n = int(input())

    myList = []

    for i in range(n) :
        myList.append([int(v) for v in input().split()])

    print(*processBeads(myList))

if __name__ == "__main__":
    main()


...
Input sample
3
1 0
2 1
3 0

Output sample
3 1 2
... 

