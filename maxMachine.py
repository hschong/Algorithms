class maxMachine:
    def __init__(self):
        self.data = list()

    def addNumber(self, number):
        self.data.append(number)

    def removeNumber(self, number):
        self.data.remove(number)

    def getMax(self):
        return max(self.data)


def main():
    myMachine = maxMachine()
    myMachine.addNumber(1)
    myMachine.addNumber(2)
    myMachine.addNumber(3)
    myMachine.addNumber(2)

    print(myMachine.getMax())
    myMachine.removeNumber(3)

    print(myMachine.getMax())
    myMachine.removeNumber(2)

    print(myMachine.getMax())
    myMachine.removeNumber(2)