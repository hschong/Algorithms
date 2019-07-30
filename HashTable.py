class HashTable : # Using a list to implement a hash table.
    def __init__(self, size) :
        # self.myData = [(-1, -1) for i in range(size)]
        self.myData = []
        for i in range(size):
            self.myData.append([-1, -1]) # [-1, -1] means that the program assigns a key with a value into the element.

    def put(self, key, value) :
        index = self.hashFunction(key)
        
        for i in range(len(self.myData)) :
            if self.myData[index][0] == -1 : 
                # It is empty bacause there is no key in the element.
                self.myData[index] = (key, value)
                return True

            else :
                # It is not empty. check the availablity of the next element.
                index = (index + 1) % len(self.myData)
        
        # It is impossible to do put function due to Hash table is full.
        # The program should increase the size of the table to do put function.
        return False

    def get(self, key) :
        index = self.hashFunction(key)
        
        if self.myData[index][0] == -1 :
            # the element is empty with the given index.
                return -1

        for i in range(len(self.myData)) :
            if self.myData[index][0] == key :
                # Found the value with the key.
                return self.myData[index][1]
            else :
                # Move to the next element.
                index = (index + 1) % len(self.myData)
        
        # There is no value with/matching with the key.
        return -1

    def hashFunction(self, key) :        
        return key % len(self.myData)

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