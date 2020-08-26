import math

# Using infinity
# import math
INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf

integers = [1, 2, 5, 4, 7, 3]
characters = ['u', 'a', 'e', 'c', 'k', 'i']
duplicates = ['a', 'b', 'a', 'c', 'c']
string = 'apple#banana#cherry#orange'
languages = ['Korean']
languages_tuple = ('English', 'German')

# Sort the items of the list in place.
integers.sort()
integers.sort(reverse=True)

# Return a new sorted list from the items in iterable.
sorted_characters = sorted(characters)
sorted_characters = sorted(characters, reverse=True)

# Split a string into lists
# Setting the maxsplit parameter to 3, will return a list with 4
new_list = string.split('#', 3)

# Convert a string to a list
new_list = list(string)

# Convert a list to a string
new_string = ''.join(new_list)

# Reverse a list
integers.reverse()
# reversed() returns a reverse iterator
new_integers = list(reversed(integers))

# Remove duplicates from a list
new_list = list(dict.fromkeys(duplicates))

# Append/Insert an object in a list
new_list.append(1)
new_list.insert(0, 1)
new_list.remove(1)

# Remove and return item at index (default last)
last_item = new_list.pop()
item_at_1 = new_list.pop(1)

# Return first index of value from list
if 'a' not in new_list:
    print('a is not in the list.')
else:
    index = new_list.index('a')

# Remove all items from list
new_list.clear()
del new_list[:]
new_list = []
new_list[:] = []
new_list *= 0

# new_list = new_list[:1] + new_list[1:]
new_list[1:] = []

occurrences = new_list.count('a')
languages.extend(languages_tuple)

for idx, val in enumerate(new_list):
    print(idx, val)


# Lambda
def calculate(a, b, func):
    return func(a, b)


# add = lambda a, b: a+b
def add(a, b): return a+b

# judge = lambda score: 'pass' if score>=80 else 'fail'


def judge(score): return 'pass' if score >= 80 else 'fail'
