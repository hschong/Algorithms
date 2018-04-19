# simple quick sort
def simple_quick_sort(list):
    
    length = len(list)
    if length < 2:
        return list

    pivot = list[0]
    greater = []
    less = []

    for i in range(1, length):
        if list[i] > pivot:
            greater.append(list[i])
        else:
            less.append(list[i])
    
    return simple_quick_sort(less) + [pivot] + simple_quick_sort(greater)

# general quick sort
def quick_sort(list, start, end):
    if end - start < 1:
        return  # the element does not exist or is an only one in the list, or the given start and end are wrong.

    pivot = list[end]
    i = start

    for j in range(start, end):
        if list[j] <= pivot:
            if i != j:
                list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[end] = list[end], list[i]

    quick_sort(list, start, i-1)
    quick_sort(list, i+1, end)


data = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(simple_quick_sort(data))
print(data)
quick_sort(data, 0, len(data)-1)
print(data)
