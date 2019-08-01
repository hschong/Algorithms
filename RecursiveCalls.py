def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))


def getPower(m, n) :
    if n == 0 :
        return 1
    else :
        if n % 2 == 0 :
            temp = getPower(m, n // 2)
            return temp * temp
        else :
            return m * getPower(m, n - 1) 

# convert a decimal number to a binary number.
def convertBinary(number) :
    if number == 1 :
        return '1'
    else :
        return convertBinary(number // 2) + str(number % 2)

# source = “mef” and target = “myself”
# return True when target has one of each in the source.
def hasCharacters(source, target) :
    if len(source) == 0 :
        return True
    else :
        if source[0] in target :
            return hasCharacters(source[1:], target)
        else :
            return False

# stringReverse("Elice is so coooool") == "loooooc os si ecilE" 
def stringReverse(string) :
    if len(string) == 1 :
        return string
    else :
        return string[-1] + stringReverse(string[1:-1]) + string[0]

# In mathematics, the Euclidean algorithm, or Euclid's algorithm, is 
# an efficient method for computing the greatest common divisor (GCD) 
# of two numbers, the largest number that divides both of them without 
# leaving a remainder. GCD(x, y) == GCD(y, x%y)
def getGCD(x, y) :
    if x % y == 0 :
        return y
    else :
        return getGCD(y, x % y)