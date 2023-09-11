#916

'''
Remove duplicate words from sentence using regular expression
'''

import re

def removeDuplicateWords(input):

    #regex to matching repeated words
    regex = r'\b(\w+)(?:\w+\1\b)+'

    return re.sub(regex, r'\1', input, flags=re.IGNORECASE)

#Test case 1:
str1 = 'Good bye bye world world'
print(removeDuplicateWords(str1))

str2 = 'Ram went went to to his home'
print(removeDuplicateWords(str2))

str3 = "Hello hello world world"
print(removeDuplicateWords(str3))