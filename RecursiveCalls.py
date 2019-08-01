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
    if len(source) <= 0 :
        return True
    else :
        if source[0] in target :
            return hasCharacters(source[1:], target)
        else :
            return False