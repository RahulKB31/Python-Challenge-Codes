#914

'''
Python check whether a string starts and ends with same character or not (Using regular expression)
'''

import re
regex = r'^[a-z]$|^([A-Z]).8\1$'

def check(string):

    if(re.search(regex, string)):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    sample1 = 'abba'
    sample2 = 'a'
    sample3 = 'abcd'

    check(sample1)
    check(sample2)
    check(sample3)

################################################################################################################





























