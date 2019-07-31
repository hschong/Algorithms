from heapq import heappush, heappop

class priorityQueue:
    def __init__(self) :
        self.data = []

    def top(self) :
        if len(self.data) <= 0 :
            return -1
        else :
            return self.data[0]

    def push(self, value) :
        heappush(self.data, value)

    def pop(self) :
        if len(self.data) <= 0 :
            return
        else :
            heappop(self.data)
        

def main():
    myPQ = priorityQueue()

    myPQ.push(1)
    myPQ.push(4)
    myPQ.push(3)
    myPQ.push(2)

    print(myPQ.top())
    myPQ.pop()

    print(myPQ.top())
    myPQ.pop()

if __name__ == "__main__":
    main()