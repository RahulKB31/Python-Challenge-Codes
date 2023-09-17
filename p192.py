#933

'''
Check if email address valid or not in Python
'''

# Check for a valid email address using regular expression

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex,email)):
        print("Valid Email")
    else:
        print("Invalid Email")

if __name__ == '__main__':
    email = "ankitrai326@gmail.com"

    check(email)

    email = "my.ownsite@our-earth.org"
    check(email)

    email = "ankitrai326.com"
    check(email)

####################################################################################################################

#934

'''
Validate Email Address with Python using re.match
'''

import re

def check(s):
    pat = r'\b[A-Za-x0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat,s):
        print("Valid Email")
    else:
        print("Invalid Email")

if __name__ == '__main__':
    email = "ankitrai326@gmail.com"
    check(email)

    email = "my.ownsite@our-earth.org"
    check(email)

    email = "ankitrai326.com"
    check(email)

###################################################################################################################










































































