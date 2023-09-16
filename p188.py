#926

'''
How to check if a string starts with a substring using regex in python
'''

import re
def find(string, sample):
    if (sample in string):
        y = "^" + sample

        # check if string starts with the substring
        x = re.search(y,string)

        if x:
            print("String starts with the given substring")
        else:
            print("String doesn't start with the given substring")
    else:
        print("Entered string isn't a substring")

string = "geeks for geeks makes learning fun"
sample = "geeks"

find(string, sample)

sample = "makes"

find(string, sample)

###################################################################################################################

#927

'''
if a string starts with a substring
'''

import re


def find(string, sample):
    if (sample in string):
        y = "\A" + sample

        # check if string starts with the substring
        x = re.search(y, string)

        if x:
            print("String starts with the given substring")
        else:
            print("String doesn't start with the given substring")
    else:
        print("Entered string isn't a substring")


string = "geeks for geeks makes learning fun"
sample = "geeks"

find(string, sample)

sample = "makes"

find(string, sample)

#####################################################################################################################

















