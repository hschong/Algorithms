# Find index to insert item in the list.
def find_index_to_insert_item(list, item):
    length = len(list)
    for index in range(0, length):
        if item < list[index]:
            return index

    return len(list)

# A simple insertion sort
def simple_insertion_sort(list):
    new_sorted_list = []
    
    for i in range(0, len(list)):
        index = find_index_to_insert_item(new_sorted_list, list[i])
        new_sorted_list.insert(index, list[i])
    
    return new_sorted_list

# general insertion sort
def insertion_sort(list):
    length = len(list)

    for i in range(1, length):
        key = list[i]
        j = i - 1

        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -=1

        list[j+1] = key

    return list

data1 = [2, 4, 5, 1, 3]
data2 = [2, 4, 5, 1, 3]

print(data1)
print(simple_insertion_sort(data1))

print(data2)
print(insertion_sort(data2))