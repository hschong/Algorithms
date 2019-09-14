class HashTable : # Using a list to implement a hash table.
    def __init__(self, maxSize) :
        self.myData = []
        self.maxSize = maxSize
        self.occupiedSize = 0
        self.deletedSize = 0
        self.initHashTable(maxSize)
        
    def initHashTable(self, maxSize) :
        # [key, value]    
        # self.myData = [(None, None) for i in range(maxSize)]
        for i in range(maxSize):
            self.myData.append([None, None])
    
    def getMaxSize(self) :
        return self.maxSize

    def setMaxSize(self, newSize) :
        self.maxSize = newSize

    def getPrimeNumber(self) :
        #  Find a prime number and must be smaller than 'size'.
        size = self.getMaxSize()
        if size <= 2 :
            return None
        
        for i in range(2, size) :
            if size % i == 0 :
                primeNumber = i
        
        return primeNumber

    def put(self, key, value) :
        hashCode = self.hashFunction(key)
        size = self.getMaxSize()
        
        for i in range(size) :
            if self.myData[hashCode][0] == None : 
                # The element is empty.
                self.myData[hashCode] = (key, value)
                self.occupiedSize += 1
                return True

            elif self.myData[hashCode][0] == -1 :
                # The element is marked as deleted.
                self.myData[hashCode] = (key, value)
                self.deletedSize -= 1
                return True

            else :
                '''
                The element is occupied. But a collision was found.
                There are 2 ways to avoid the collision by Linear Probing 
                or Double Hashing. 
                Note) hashCode has to be smaller than the size. 
                '''
                
                '''
                Linear Probing
                hashCode = (hashCode + 1) % size
                '''
                # DoubleHashing
                jump = self.hashFunctionByDoubleHashing(key)
                hashCode = (hashCode + jump) % size
        
        '''
        Hash table is full or does not have any available 
        element with the hashCode.
        The program should increase the size of the table
        to do 'put' function.
        '''
        return False

    def get(self, key) :
        hashCode = self.hashFunction(key)
        size = self.getMaxSize()

        if self.myData[hashCode][0] == None :
            return None
        
        # Found the element matching with hashCode.
        for i in range(size) :
            if self.myData[hashCode][0] == key :
                # Found the element matching with the key.
                return self.myData[hashCode][1]
            else :
                '''
                Avoiding a collision by Linear Probing or Double Hashing When found a collision. 
                ''' 

                # Linear Probing
                # hashCode = (hashCode + 1) % size
                
                # DoubleHashing
                jump = self.hashFunctionByDoubleHashing(key)
                hashCode = (hashCode + jump) % size
        
        # There is no element matching with the key.
        return None
    
    def delete(self, key) :
        hashCode = self.hashFunction(key)
        size = self.getMaxSize()

        for i in range(size) :
            if self.myData[hashCode][0] == key :
                # Marking the element as deleted.
                self.myData[hashCode] = (-1, None)
                self.deletedSize += 1
                return True
            else :
                jump = self.hashFunctionByDoubleHashing(key)
                hashCode = (hashCode + jump) % size

        return False

    def hasCollision(self, hashCode, key) :
        if self.myData[hashCode][0] == key :
            return False
        else :
            return True

    def resize(self) :
        maxSize = self.getMaxSize()
        newSize = maxSize + maxSize // 2
        self.rebuild(newSize)

        return True

    def rebuild(self, newSize) :
        newData = []
        maxSize = self.getMaxSize()
        size = maxSize
        isNew = False

        if newSize > maxSize :
            size = newSize
            self.initHashTable(size)
            isNew = True
        
        # newData = self.makeNewList(newData, size)
        self.myData = newData
        return True

    def refresh(self) :
        maxSize = self.getMaxSize()
        occupiedSize = self.occupiedSize
        deletedSize = self.deletedSize

        if occupiedSize >= ((maxSize*7)//10) :
            # over 70%
            if deletedSize >= (maxSize//10) :
                # remove the deleted marks and rebuild.
                return self.rebuild(0)
            else :
                # increase the maximum hash size 50% more.
                return self.resize()

        elif deletedSize >= ((maxSize*2)//10) :
            return self.rebuild(0)

        return True

    def hashFunction(self, key) :        
        return key % self.getMaxSize()

    def hashFunctionByDoubleHashing(self, key) :
        return 1 + key % self.getPrimeNumber()


def main():
    myHash = HashTable(100)
    myHash.put(1, 3)
    myHash.put(2, 7)
    myHash.put(3, 8)
    myHash.put(403, 9)

    print(myHash.get(3))
    print(myHash.get(403))


if __name__ == "__main__":
    main()