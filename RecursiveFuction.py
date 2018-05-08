import sys

LIMIT_NUMBER = 1000000007
LIMIT_RECURSION = 5000

sys.setrecursionlimit(LIMIT_RECURSION)


def getFactorial(n) :
    if n == 0 :
        return 1
    else :
        return n * getFactorial(n-1)


def getPower(m, n) :
    if n == 0 :
        return 1
    elif n % 2 == 0 : # even numbers
        temp = getPower(m, n//2)
        return temp * temp
    else : # odd numbers
        return m * getPower(m, n-1)


def getPower2(m, n):
    if n == 0 :
        return 1
    elif n % 2 == 0 : # even numbers
        temp = getPower(m, n//2)
        return (temp * temp) % LIMIT_NUMBER
    else : # odd numbers
        return (m * getPower(m, n-1)) % LIMIT_NUMBER

def main():

    myList = [int(v) for v in input().split()]

    print(sys.getrecursionlimit())
    print(getPower2(myList[0], myList[1]))

if __name__ == "__main__":
    main()
