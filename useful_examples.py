import math

integer_list = [1, 2, 5, 4, 7]

# Sort the items of the list in place.
integer_list.sort()

# Return a new sorted list from the items in iterable.
new_integer_list = sorted(integer_list, reverse=False)
print(sorted([1, 3, 2, 5, 6, 4]))

# Reverse a list
new_integer_list.reverse()
reversed_list = list(reversed(new_integer_list))

# Split a string into a list where each word is a list item:
# setting the maxsplit parameter to 3, will return a list with 4 elements!
txt = "apple#banana#cherry#orange"
x = txt.split("#", 3)
print(x)

# make a string into a list
src_str = 'abc'
print(list(src_str))

# make a list into a string
# convert a list of integers into a string list
string_list = [str(integer) for integer in integer_list]
print(''.join(string_list))

# Remove Duplicates From a List.
integer_list = ["a", "b", "a", "c", "c"]
integer_list = list(dict.fromkeys(integer_list))
print(integer_list)

# add/remove an object in a list.
integer_list.append('1')
integer_list.remove('1')
integer_list.reverse()

# remove all elements in list.
integer_list.clear()  # Python 3.3+
del integer_list[:]
integer_list[:] = []
integer_list *= 0

# for in loop
for item in integer_list:
    print(item)

for index in range(len(integer_list)):
    print(integer_list[index])

for idx, val in enumerate(integer_list):
    print(idx, val)

# get the index of a given number
if 'a' not in integer_list:
    print(-1)
else:
    print(integer_list.index('a'))


# Using infinity
# import math
INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf
