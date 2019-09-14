PRIME = 7  # PRIME < self.max
DELETED = -1

class HashTable : # Using a list to implement a hash table.
    def __init__(self, max) :
        self.data = []
        self.max = max
        self.occupied_size = 0
        self.mark_as_deleted_size = 0
        self.makeHashTable(max)
        
    def makeHashTable(self, max) :
        for i in range(max):
            # [key, value]    
            # self.data = [(None, None) for i in range(max)]
            self.data.append([None, None])

    def getCurSize(self) :
        return self.occupied_size + self.mark_as_deleted_size

    def isFull(self) :
        if self.max == self.getCurSize():
            return True
        else :
            return False

    def isEmpty(self) :
        if self.occupied_size == 0 :
            return True
        else :
            return False

    def getHashCode1(self, key) :        
        return key % self.max

    def getHashCode2(self, key) :
        # Double Hashing
        return PRIME - (key % PRIME)

    def put(self, key, value) :
        if self.isFull() == True :
            return False

        hashCode = self.getHashCode1(key)
        max = self.max
        
        for i in range(1, max+1) :
            if self.data[hashCode][0] == None : 
                # The element is empty.
                self.data[hashCode] = (key, value)
                self.occupied_size += 1
                return True

            elif self.data[hashCode][0] == DELETED :
                # The element is marked as deleted.
                self.data[hashCode] = (key, value)
                self.mark_as_deleted_size -= 1
                self.occupied_size += 1
                return True

            else :
                '''
                A collision was found. There are 2 ways to avoid the collision by Linear Probing or Double Hashing. 
                Note) hashCode has to be smaller than the max. 
                '''
                # Linear Probing
                # hashCode = (hashCode + 1) % max
                
                # DoubleHashing
                hashCode2 = self.getHashCode2(key)
                hashCode = (hashCode + i * hashCode2) % max
        
        '''
        Hash table does not have any available element with the hashCode.
        The program should increase the max of the table to do 'put' function.
        '''
        return False

    def get(self, key) :
        if self.isEmpty() == True :
            return False
        
        hashCode = self.getHashCode1(key)

        if self.data[hashCode][0] == None :
            return None
        
        # Found the element matching with hashCode.
        for i in range(1, self.max+1) :
            if self.data[hashCode][0] == key :
                # Found the element matching with the key.
                return self.data[hashCode][1]
            else :
                '''
                Avoiding a collision by Linear Probing or Double Hashing When found a collision. 
                ''' 
                # Linear Probing
                # hashCode = (hashCode + 1) % self.max
                
                # DoubleHashing
                hashCode = (hashCode + i * self.getHashCode2(key)) % self.max
        
        # There is no element matching with the key.
        return None
    
    def delete(self, key) :
        if self.isEmpty() == True :
            return False
            
        hashCode = self.getHashCode1(key)
        for i in range(1, self.max+1) :
            if self.data[hashCode][0] == key :
                # Marking the element as deleted.
                self.data[hashCode] = (DELETED, None)
                self.mark_as_deleted_size += 1
                self.occupied_size -= 1
                return True
            else :
                hashCode2 = self.getHashCode2(key)
                hashCode = (hashCode + i * hashCode2) % self.max

        return False

    def rebuild(self, max) :
        if max < self.max :
            return False

        new_data = self.data
        self.data.clear()
        self.makeHashTable(max)

        for key, value in new_data :
            if key != DELETED and key != None :
                self.put(key, value)

        return True

    def refresh(self) :
        if self.occupied_size >= ((self.max*7)//10) :
            # over 70%
            if self.mark_as_deleted_size >= (self.max//10) :
                # remove the deleted marks and rebuild.
                return self.rebuild(self.max)
            else :
                # increase the max 100%
                return self.rebuild(self.max * 2)

        elif self.mark_as_deleted_size >= ((self.max * 2)//10) :
            return self.rebuild(self.max)

        return True


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