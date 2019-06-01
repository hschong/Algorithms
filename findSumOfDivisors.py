def printNum():
    for i in range(10, 100):
        total = 0
        for j in range(1, i):
            if i % j == 0:
                total += j
        
        if total == i:
            print(i)