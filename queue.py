CONST_MAX = 100
    
class Queue:
    def __init__(self, max):
        self.myData = []
        self.maxSize = max

    def getCurrentSize(self):
        return len(self.myData)

    def enQueue(self, item):
        if self.isFull() == True:
            print("The queue is full. hence, you can't enqueue!")
            return False
        else:
            self.myData.append(item)
            return True

    def deQueue(self):
        if self.isEmpty() == True:
            print("The queue is empty. thefore, you can't dequeue!")
            return False
        else:            
            # self.myData.pop()
            self.myData = self.myData[1:]
            return True

    def isEmpty(self):
        if self.getCurrentSize() == 0:
            print("The queue is empty!")
            return True
        else:
            return False
    
    def isFull(self):
        if self.getCurrentSize() == CONST_MAX:
            return True
        else:
            return False


def main():
    max = int(input('type the maximum size of your queue: '))
    myQueue = Queue(max)

    myQueue.enQueue(1)
    myQueue.deQueue()
    myQueue.deQueue()
    
if __name__ == "__main__":
    main()