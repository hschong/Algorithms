import math

integers = [1, 2, 5, 4, 7]

# Sort the items of the list in place.
integers.sort()

# Return a new sorted list from the items in iterable.
new_integers = sorted(integers, reverse=False)
print(sorted([1, 3, 2, 5, 6, 4]))

# Reverse a list
new_integers.reverse()
reversed_integers = list(reversed(new_integers))

# Split a string into a list where each word is a list item:
# setting the maxsplit parameter to 3, will return a list with 4 elements!
txt = 'apple#banana#cherry#orange'
x = txt.split("#", 3)
print(x)

# make a string into a list
src_str = 'abc'
print(list(src_str))

# make a list into a string
# convert a list of integers into a string list
string = [str(integer) for integer in integers]
print(''.join(string))

# Remove Duplicates From a List.
lst = ["a", "b", "a", "c", "c"]
lst = list(dict.fromkeys(lst))
print(lst)

# add/remove an object in a list.
lst.append('1')
lst.remove('1')
lst.reverse()

# remove all elements in list.
lst.clear()  # Python 3.3+
del lst[:]
lst[:] = []
lst *= 0

# for in loop
for item in lst:
    print(item)

for index in range(len(lst)):
    print(lst[index])

for idx, val in enumerate(lst):
    print(idx, val)

# get the index of a given number
if 'a' not in lst:
    print(-1)
else:
    print(lst.index('a'))

# Lambda
def add(a, b): return a+b
# add = lambda a, b: a+b


# Using infinity
# import math
INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf
