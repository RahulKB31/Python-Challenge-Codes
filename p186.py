#924

'''
Python Regex | Program to accept string ending with alphanumeric character
'''

# re module provides support for regular expressions

import re

# make a regular expression to accept string ending with alphanumeric character
regex = '[a-zA-Z0-9]$'

def check(string):
    if(re.search(regex, string)):
        print("Accept")
    else:
        print("Discard")

if __name__ == '__main__':
    string = "ankirai@"
    check(string)

    string = "ankitrai326"
    check(string)

    string = "ankit."
    check(string)

    string = "geeksforgeeks"
    check(string)

###################################################################################################################