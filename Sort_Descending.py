class maxMachine :
    '''
    이곳에 '최댓값 기계' 문제에서 작성했던 코드를 붙여넣으세요
    '''
    def __init__(self) :
        self.data = []

    def addNumber(self, n) :
        self.data.append(n)

    def removeNumber(self, n) :
        self.data.remove(n)

    def getMax(self) :
        return max(self.data)

def sorting(myList) :
    '''
    myList를 내림차순으로 정렬하여 반환하는 함수를 작성하세요.

    예를 들어, myList = [5, 2, 3, 1] 이라면 [5, 3, 2, 1] 을 반환해야 합니다.

    단, maxMachine class를 이용하도록 합니다. 
    '''

    myMachine = maxMachine()
    result = []
    
    for item in myList:
        myMachine.addNumber(item)
    
    for item in range(len(myList)):
        myMax = myMachine.getMax()
        result.append(myMax)
        myMachine.removeNumber(myMax)

    return result
class maxMachine :
    '''
    이곳에 '최댓값 기계' 문제에서 작성했던 코드를 붙여넣으세요
    '''
    def __init__(self) :
        self.data = []

    def addNumber(self, n) :
        self.data.append(n)

    def removeNumber(self, n) :
        self.data.remove(n)

    def getMax(self) :
        return max(self.data)

def sorting(myList) :
    '''
    myList를 내림차순으로 정렬하여 반환하는 함수를 작성하세요.

    예를 들어, myList = [5, 2, 3, 1] 이라면 [5, 3, 2, 1] 을 반환해야 합니다.

    단, maxMachine class를 이용하도록 합니다. 
    '''

    myMachine = maxMachine()
    result = []
    
    for item in myList:
        myMachine.addNumber(item)
    
    for item in range(len(myList)):
        myMax = myMachine.getMax()
        result.append(myMax)
        myMachine.removeNumber(myMax)

    return result

def main():
    '''
    이 곳은 수정하지 마세요.
    '''

    myList = [int(v) for v in input().split()]

    print(sorting(myList))

if __name__ == "__main__":
    main()