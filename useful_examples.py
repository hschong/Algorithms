import math

my_list = [1, 2, 5, 4, 7]

# Sort the items of the list in place.
my_list.sort()

# Return a new sorted list from the items in iterable.
new_list = sorted(my_list, reverse=False)
print(sorted([1, 3, 2, 5, 6, 4]))

# Reverse a list
new_list.reverse()
reversed_list = list(reversed(new_list))

# Remove Duplicates From a List.
my_list = ["a", "b", "a", "c", "c"]
my_list = list(dict.fromkeys(my_list))
print(my_list)

# add/remove an object in a list.
my_list.append('1')
my_list.remove('1')
my_list.reverse()

# remove all elements in list.
my_list.clear()  # Python 3.3+
del my_list[:]
my_list[:] = []
my_list *= 0

# for in loop
for item in my_list:
    print(item)

for index in range(len(my_list)):
    print(my_list[index])

for idx, val in enumerate(my_list):
    print(idx, val)

# get the index of a given number
if 'a' not in my_list:
    print(-1)
else:
    print(my_list.index('a'))


# Using infinity
# import math
INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf
