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
