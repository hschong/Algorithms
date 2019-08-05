# simple merge sort
def simple_merge_sort(list):
    new_sorted_list = []
    length = len(list)
    mid = length // 2

    if length < 2:
        return list

    small_group = simple_merge_sort(list[:mid])
    large_group = simple_merge_sort(list[mid:])
    
    while small_group and large_group:
        if small_group[0] < large_group[0]:
            new_sorted_list.append(small_group.pop(0))
        else:
            new_sorted_list.append(large_group.pop(0))

    while small_group:
        new_sorted_list.append(small_group.pop(0))
    
    while large_group:
        new_sorted_list.append(large_group.pop(0))

    return new_sorted_list


# general merge sort
def merge_sort(list):
    length = len(list)

    if length < 2:
        return list

    mid = length // 2
    first_group = list[:mid]
    second_group = list[mid:]

    merge_sort(first_group)
    merge_sort(second_group)

    first_group_index = 0
    second_group_index = 0
    index = 0

    while first_group_index < len(first_group) and second_group_index < len(second_group):

        if first_group[first_group_index] < second_group[second_group_index]:
            list[index] = first_group[first_group_index]
            first_group_index += 1
            index += 1

        else:
            list[index] = second_group[second_group_index]
            second_group_index += 1
            index += 1

    while first_group_index < len(first_group):
        list[index] = first_group[first_group_index]
        first_group_index += 1
        index += 1

    while second_group_index < len(second_group):
        list[index] = second_group[second_group_index]
        second_group_index += 1
        index += 1

    return list


def mergeSort(numbers) :
    size = len(numbers)
    if size == 1 :
        return numbers

    mid = size // 2
    leftNumbers = mergeSort(numbers[:mid])
    rightNumbers = mergeSort(numbers[mid:])

    return merge(leftNumbers, rightNumbers)


def merge(leftNumbers, rightNumbers) :
    p = 0 # current index of left
    q = 0 # current index of right
    leftSize = len(leftNumbers)
    rightSize = len(rightNumbers)

    result = []
    while p<leftSize and q<rightSize :
        if leftNumbers[p] < rightNumbers[q] :
            result.append(leftNumbers[p])
            p += 1
        else :
            result.append(rightNumbers[q])
            q += 1
    
    if p == leftSize :
        result += rightNumbers[q:]
    else :
        result += leftNumbers[p:]
    
    return result


list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(simple_merge_sort(list))
print(merge_sort(list))
print(mergeSort(list))


