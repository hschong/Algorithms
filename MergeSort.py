from collections import deque
from typing import List
from typing import Deque
import itertools


def simple_merge_sort(lst: Deque[int]) -> Deque[int]:
    result = deque()
    length = len(lst)
    mid = length // 2

    if length < 2:
        return lst

    small_group = deque(itertools.islice(lst, 0, mid))
    large_group = deque(itertools.islice(lst, mid, len(lst)))
    small_group = simple_merge_sort(small_group)
    large_group = simple_merge_sort(large_group)

    while small_group and large_group:
        if small_group[0] < large_group[0]:
            result.append(small_group.popleft())
        else:
            result.append(large_group.popleft())

    while small_group:
        result.append(small_group.popleft())

    while large_group:
        result.append(large_group.popleft())

    return result


# general merge sort
def merge_sort(nums):
    size = len(nums)
    if size == 1:
        return nums

    mid = size // 2
    left_nums = merge_sort(nums[:mid])
    right_nums = merge_sort(nums[mid:])

    return merge(left_nums, right_nums)


def merge(left_nums, right_nums):
    result = []
    p = 0  # current index of left
    q = 0  # current index of right
    left_size = len(left_nums)
    right_size = len(right_nums)

    while p < left_size and q < right_size:
        if left_nums[p] < right_nums[q]:
            result.append(left_nums[p])
            p += 1
        else:
            result.append(right_nums[q])
            q += 1

    if p == left_size:
        result += right_nums[q:]
    else:
        result += left_nums[p:]

    return result


lst = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(list(simple_merge_sort(lst)))
print(merge_sort(lst))
