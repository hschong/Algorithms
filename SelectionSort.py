# Find the index of the minimum from list 
def find_idx_for_min(list):
    min_value = list[0]
    min_idx = 0
    length = len(list)

    for i in range(1, length):
        if min_value > list[i]:
            min_value = list[i]
            min_idx = i
    
    return min_idx

# A simple selection sort
def simple_selection_sort(list):
    new_sorted_list = []
    length = len(list)

    for i in range(0, length):
        idx = find_idx_for_min(list)
        new_sorted_list.append(list.pop(idx))

    return new_sorted_list

# A general selection sort
def selection_sort(list):
    length = len(list)

    for i in range(0, length-1):
        idx_for_min = i
        for j in range(i+1, length):
            if list[j] < list[idx_for_min]:
                idx_for_min = j
        list[i], list[idx_for_min] = list[idx_for_min], list[i]

data1 = [5, 3, 6, 2, 10, 15, 9, 1, 11, 7]
data2 = [5, 3, 6, 2, 10, 15, 9, 1, 11, 7]

print(data1)
print(simple_selection_sort(data1))

print(data2)
selection_sort(data2)
print(data2)