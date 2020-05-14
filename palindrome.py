def is_palindrome(string):
    return True if string[::-1] == string else False


def is_palindrome_using_recursive(string):
    if len(string) == 0 or len(string) == 1:
        return True

    if string[0] == string[-1]:
        return is_palindrome_using_recursive(string[1:-1])
    else:
        return False


print("'Yes'" if is_palindrome('aba') else "'No'")
print("'Yes'" if is_palindrome_using_recursive('abba') else "'No'")


def reverse_list(lst):
    return lst[-1::-1]  # list[::-1]


def reverse_list_using_recursive(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        lst[0], lst[-1] = lst[-1], lst[0]
        return list(lst[0]) + reverse_list_using_recursive(lst[1:-1]) + list(lst[-1])


def reverse_string(string):
    return string[-1::-1]  # return string[::-1]


def reverse_string_using_loop(string):
    reversed_string = ''
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string


def reverse_string_using_recursive(string):
    lst = list(string)
    return ''.join(reverse_list_using_recursive(lst))


my_txt = 'I wonder how this text looks like backwards'
reversed_txt = reverse_string(my_txt)
reversed_txt = reverse_string_using_recursive(my_txt)
print(my_txt)
print(reversed_txt)
print(reverse_list(list(my_txt)))
