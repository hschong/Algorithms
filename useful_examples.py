import math

mylist = []

# Sort the items.
mylist.sort()  # Sort the items of the list in place.
# Return a new sorted list from the items in iterable.
newList = sorted(mylist)

# Remove Duplicates From a List.
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# add/remove an object in a list.
mylist.append('1')
mylist.remove('1')
mylist.reverse()

# remove all elements in list.
mylist.clear()  # Python 3.3+
del mylist[:]
mylist[:] = []
mylist *= 0

# for in loop
for item in mylist:
    print(item)

for index in range(len(mylist)):
    print(mylist[index])

for idx, val in enumerate(mylist):
    print(idx, val)

# get the index of a given number
print(mylist)
if 'a' not in mylist:
    print(-1)
else:
    print(mylist.index('a'))


def reverseString(x):
    return x[::-1]


mytxt = reverseString("I wonder how this text looks like backwards")
print(mytxt)


# Using infinity
# import math
INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf
