class HashTable : # Using a dictionary to implement a hashtable.
    def __init__(self) :
        self.data = {}

    def put(self, key, value) :
        self.data[key] = value

    def get(self, key) :
        if key in self.data :
            return self.data[key]
        else :
            return -1

def main():
    myHash = HashTable()

    myHash.put(1, 3)
    myHash.put(2, 7)
    myHash.put(3, 8)
    myHash.put(403, 9)

    print(myHash.get(3))
    print(myHash.get(403))

if __name__ == "__main__":
    main()