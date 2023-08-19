#618

'''
Python | Check if a given string is binary or not
'''

# Using set

def check(string):

    p = set(string)

    s = {'0','1'}

    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    string = "101010000111"
    check(string)

############################################################################################################

#619

'''
simple iteration
'''

def check2(string):
    t = '01'

    count = 0

    for char in string:
        if char not in t:
            count = 1
            break
        else:
            pass

    if count:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    string = "00012011101001010"

    check2(string)

#############################################################################################################

#620

'''
Regular expression
'''

import re

sampleInput = "1001010"

c = re.compile('[^01]')

if(len(c.findall(sampleInput))):
    print("No")
else:
    print("Yes")

##############################################################################################################

#621

'''
Using exception handling and int
'''

def check(string):
    try:
        int(string,2)

    except ValueError:
        return "No"
    return "Yes"

if __name__ == "__main__":
    string1 = "101011001111"
    string2 = "201000001"

    print(check(string1))
    print(check(string2))

##############################################################################################################

#622

'''
Using count() function
'''

string = "1010001010101"
if(string.count('0')+string.count('1')==len(string)):
    print("Yes")
else:
    print("No")

##############################################################################################################

#623

'''
Using replace() and len() methods
'''

string = '1010201010101'
binary = '01'
for i in binary:
    string = string.replace(i,"")
if(len(string) == 0):
    print("Yes")
else:
    print("No")

#################################################################################################################

#624

'''
Using all()
'''

def check(string):
    if all((letter in "01") for letter in string):
        return "Yes"
    return "No"


if __name__ == "__main__":
    string1 = "101011001111"
    string2 = "201000001"

    print(check(string1))
    print(check(string2))

#############################################################################################################

#625

'''
Using issubset() method
'''

def is_binary_string(s):
    unique_chars = {c for c in s}
    return unique_chars.issubset({'0','1'})


if __name__ == "__main__":
    string1 = "101011001111"
    string2 = "201000001"

    print(is_binary_string(string1))
    print(is_binary_string(string2))

###############################################################################################################

#626

'''
Using re.search()
'''

import re

def is_binary_string(str):
    regex = r"[^01]"

    if re.search(regex,str):
        return False
    else:
        return True

print(is_binary_string(string1))
print(is_binary_string(string2))

###############################################################################################################
























































































































































































































