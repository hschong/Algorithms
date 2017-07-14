# simple merge sort
def m_sort(list):
    result = []
    length = len(list)
    mid = length // 2

    if length <= 1:
        return list

    first_group = m_sort(list[:mid])
    second_group = m_sort(list[mid:])

    while first_group and second_group:
        if first_group[0] < second_group[0]:
            result.append(first_group.pop(0))
        else:
            result.append(second_group.pop(0))

    while first_group:
        result.append(first_group.pop(0))

    while second_group:
        result.append(second_group.pop(0))

    return result


# general merge sort
def merge_sort(list):
    length = len(list)

    if length <= 1:
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


list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(m_sort(list))
print(merge_sort(list))


