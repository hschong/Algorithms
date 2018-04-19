def binary_search(list, item):
    min_idx = 0
    max_idx = len(list) - 1

    while min_idx <= max_idx:

        mid_idx = (min_idx + max_idx) // 2
        guess = list[mid_idx]

        if guess == item:
            return guess
        elif guess > item:
            max_idx = mid_idx - 1
        else:
            min_idx = mid_idx + 1

    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))


