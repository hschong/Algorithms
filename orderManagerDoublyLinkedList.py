class LinkedListElement :
    def __init__(self, data, prev, next) :
        self.data = data
        self.next = next
        self.prev = prev


class OrderManger :
    def __init__(self) :
        self.start = None
        self.end = None

        # Using dictionary(hash) for a better searching.
        self.orderHash = {}

    # targetOrder <--> (newOrder) <--> targetOrder.next
    def addOrderAfter(self, newID, targetID) :
        targetOrder = self.orderHash[targetID]
        newOrder = LinkedListElement(newID, targetOrder, targetOrder.next)

        targetOrder.next.prev = newOrder
        targetOrder.next = newOrder
        
        self.orderHash[newID] = newOrder
    
    # targetOrder.prev <--> (newOrder) <--> targetOrder
    def addOrderBefore(self, newID, targetID) :
        targetOrder = self.orderHash[targetID]
        newOrder = LinkedListElement(newID, targetOrder.prev, targetOrder)

        targetOrder.prev.next = newOrder
        targetOrder.prev = newOrder
        
        self.orderHash[newID] = newOrder

    # Add an order after the self.end.
    def appendOrder(self, orderID) :
        newOrder = LinkedListElement(orderID, None, None)

        if self.begin == None :
            self.begin = newOrder
            self.end = newOrder
        else :
            self.end.next = newOrder
            newOrder.prev = self.end
            self.end = newOrder

        self.orderHash[orderID] = newOrder

    def removeOrder(self, orderID) :
        order = self.orderHash[orderID]

        if order is None :
            return False
        
        else :
            prevOrder = order.prev
            nextOrder = order.next

            if prevOrder != None :
                prevOrder.next = order.next

            if nextOrder != None :
                nextOrder.prev = order.prev

            if order is self.begin :
                self.begin = nextOrder

            if order is self.end :
                self.end = prevOrder

            del self.orderHash[orderID]
            return True

    # Order prioity
    def getOrder(self, orderId) :
        count = 1
        current = self.begin

        while current != None :
            if orderId == current.data :
                return count
            else :
                count += 1
                current = current.next 

        return -1


def main():
    manager = OrderManger()

    manager.appendOrder(1)
    manager.appendOrder(2)
    manager.appendOrder(3)
    manager.removeOrder(2)

    print(manager.getOrder(1))
    print(manager.getOrder(2))
    print(manager.getOrder(3))


if __name__ == "__main__":
    main()