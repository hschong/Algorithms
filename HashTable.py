class HashTable : # Using a list to implement a hash table.
    def __init__(self, size) :
        self.myData = []
        self.size = 0
        self.initHashTable(size) 
        self.setSizeOfHash()
        
    def initHashTable(self, size) :
        # [key, value]    
        # self.myData = [(None, None) for i in range(size)]
        for i in range(size):
            self.myData.append([None, None])
                
    def getSizeOfHash(self) :
        return self.size

    def setSizeOfHash(self) :
        self.size = len(self.myData)

    def getPrimeNumber(self) :
        #  Find a prime number and must be smaller than 'size'.
        size = self.getSizeOfHash()
        if size <= 2 :
            return None
        
        for i in range(2, size) :
            if size % i == 0 :
                primeNumber = i
        
        return primeNumber

    def put(self, key, value) :
        hashCode = self.hashFunction(key)
        size = self.getSizeOfHash
        
        for i in range(len(self.myData)) :
            if self.myData[hashCode][0] == None : 
                # The element is empty.
                self.myData[hashCode] = (key, value)
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
        size = self.getSizeOfHash()

        if self.myData[hashCode][0] == None :
            return None
        
        # Found the element matching with hashCode.
        for i in range(size) :
            if self.myData[hashCode][0] == key :
                # Found the element matching with the key.
                return self.myData[hashCode][1]
            else :
                '''
                Found a collision. Avoiding a collision by 
                Linear Probing or Double Hashing.
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
        size = self.getSizeOfHash()

        for i in range(size) :
            if self.myData[hashCode][0] == key :
                self.myData[hashCode] = (-1, None)
                return True
            else :     
                jump = self.hashFunctionByDoubleHashing(key)
                hashCode = (hashCode + jump) % size

        return False

    def hashFunction(self, key) :        
        return key % self.getSizeOfHash()

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