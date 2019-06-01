
mylist = []

# Sort the items.
mylist.sort() # Sort the items of the list in place.
newList = sorted(mylist) # Return a new sorted list from the items in iterable.

# Remove Duplicates From a List.
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# add/remove an object in a list.
mylist.append('1')
mylist.remove('1')
mylist.reverse()

# for in loop
for item in mylist:
    print(item)

for index in range(len(mylist)):
    print(mylist[index])

for idx, val in enumerate(mylist):
    print(idx, val)


