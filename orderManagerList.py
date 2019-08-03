class orderManager :
    def __init__(self) :
        self.data = []

    def addOrder(self, orderID) :
        self.data.append(orderID)

    def removeOrder(self, orderID) :
        self.data.remove(orderID)

    def getOrder(self, orderID) :
        '''
        주문번호 orderId가 몇 번째로 처리될지를 반환합니다.
        만약 주문번호 orderId가 존재하지 않으면 -1을 반환합니다. 
        '''
        if orderID not in self.data:
            return -1
        else:
            return self.data.index(orderID)+1


def main():
    manager = orderManager()

    manager.addOrder(2)
    manager.removeOrder(2)
    manager.addOrder(1818)
    manager.addOrder(8282)
    manager.addOrder(2255)
    manager.addOrder(6515)
    manager.removeOrder(1818)
    manager.addOrder(486)

    print(manager.getOrder(486))
    print(manager.getOrder(3))

    manager.addOrder(4860)


if __name__ == "__main__": # 1 -1 2
    main()