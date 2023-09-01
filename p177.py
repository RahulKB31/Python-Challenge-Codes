#908

'''
Python - check if string contain only defined characters using regex
'''

import re

def check(str, pattern):

    #matching the strings
    if re.search(pattern, str):
        print("Valid String")
    else:
        print("Invalid String")

pattern = re.compile('^[1234]+$')
check('2134', pattern)
check('349',pattern)