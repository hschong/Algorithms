# simple insertion sort
def find_ins_idx(sorted_list, value):
    for i in range(0, len(sorted_list)):
        if value < sorted_list[i]:
            return i

    return len(sorted_list) # the value will be added after the list

def ins_sort(list):
    new_list = []
    
    while list:
        value = list.pop(0)
        ins_idx = find_ins_idx(new_list, value)
        new_list.insert(ins_idx, value)
    

    return new_list


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
print(ins_sort(data1))

print(data2)
print(insertion_sort(data2))



