def is_palindrome(lst):
    # Compare the list with its reversed version
    return lst == lst[::-1]

print(is_palindrome([3]))  # Output: True
print(is_palindrome([1, 2, 2, 1]))  # Output: True
print(is_palindrome([1, 2, 3, 2, 1]))  # Output: True
print(is_palindrome([2, 2, 3, 2, 1]))  # Output: False
