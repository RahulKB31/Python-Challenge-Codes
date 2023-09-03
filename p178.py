#909

'''
Python program to count Uppercase, Lowercase, special character and numeric values using Regex
'''

import re
string = "ThisIsGeeksforGeeks !, 123"

uppercase_characters = re.findall(r"[A-Z]",string)
lowercase_characters = re.findall(r"[a-z]",string)
numerical_characters = re.findall(r"[0-9]",string)
special_characters = re.findall(r"[, .!?]",string)

print("The no of uppercase characters is", len(uppercase_characters))
print("The no of lowercase characters is", len(lowercase_characters))
print("The no of numerical characters is", len(numerical_characters))
print("The no of special characters is", len(special_characters))

################################################################################################################

#910

import re

def count_characters(input_string):
    uppercase_count = len(re.findall(r'[A-Z]', input_string))
    lowercase_count = len(re.findall(r'[a-z]', input_string))
    special_char_count = len(re.findall(r'[!@#$%^&*(){}[]/\?><:"`~]', input_string))
    numeric_count = len(re.findall(r'[0-9]',input_string))

    return uppercase_count, lowercase_count, special_char_count, numeric_count

test_string = "Hello World! 123"
uppercase, lowercase, special_chars, numeric = count_characters(test_string)

print("Uppercase count:", uppercase)
print("Lowercase count:", lowercase)
print("Special character count:", special_chars)
print("Numeric count:", numeric)

###################################################################################################################

































