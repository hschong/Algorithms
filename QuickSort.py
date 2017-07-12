def q_sort(list):
    n = len(list)

    if n <= 1:
        return list

    pivot = list[-1]
    small_group  = []
    large_group = []

    for i in range(0, n-1):
        if list[i] <= pivot:
            small_group.append(list[i])
        else:
            large_group.append(list[i])

    return q_sort(small_group) + [pivot] + q_sort(large_group)


def quick_sort(list, start, end):
    if end - start < 1:
        return

    pivot = list[end]
    i = start

    for j in range(start, end):
        if list[j] <= pivot:
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[end] = list[end], list[i]

    quick_sort(list, start, i-1)
    quick_sort(list, i+1, end)



data = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]


print(q_sort(data))
print(data)
quick_sort(data, 0, len(data)-1)
print(data)
