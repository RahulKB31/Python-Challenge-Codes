#664

'''
Python - Replace all occurances of a substring in a string
'''

input_string = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
input_string = input_string.replace(s1,s2)
print(input_string)

###########################################################################################################

#665

'''
Splitting the string by substring and then replacing with the new string.split() function is used
'''

test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"

s = test_str.split(s1)
new_str = ""

for i in s:
    if(i==""):
        new_str += s2
    else:
        new_str += i

print(new_str)

#############################################################################################################

#666

'''
Using the re.sub() function
'''

import re

def replace_substring(test_str, s1, s2):
    test_str = re.sub(s1,s2,test_str)
    return test_str

test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
print(replace_substring(test_str,s1,s2))

#########################################################################################################

#667

'''
Using simple iteration
'''

def replace_substring(test_str,s1,s2):
    result = ""
    i = 0

    while i < len(test_str):
        if test_str[i:i+len(s1)] == s1:
            result += s2
            i += len(s1)
        else:
            result += test_str[i]
            i += 1

    return result

test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
print(replace_substring(test_str,s1,s2))

###############################################################################################################



































































































