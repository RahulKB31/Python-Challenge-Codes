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

#935

'''
Test if the email address is valid or not in Python using email_validator
'''

from email_validator import validate_email, EmailNotValidError

def check(email):
    try:
        # validate and get info
        v = validate_email(email)

        # replace with normalized form
        email = v["email"]
        print("True")
    except EmailNotValidError as e:
        # email is not valid, exception message is human_readable
        print(str(e))

check("my.ownsite@our-earth.org")
check("ankitrai326.com")

###################################################################################################################

#936

'''
Validate Emails from a Text file using Python
'''

import re
a = open("a.text","r")
b = a.read()
c = b.split("\n")
for d in c:
    obj = re.search(r'[\w.]+\@[\w.]+',d)
    if obj:
        print("Valid Email")
    else:
        print("Invalid Email")

###################################################################################################################






































































