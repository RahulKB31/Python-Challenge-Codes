#612

'''
Python program to split and join a string
'''

def split_string(string):
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    string = "-".join(list_string)
    return string

if __name__ == "__main__":
    string = "Geek for Geeks"
    list_string = split_string(string)
    print(list_string)

    new_string = join_string(list_string)
    print(new_string)

############################################################################################################

#613

s = "Geeks for Geeks"

print(s.split(" "))

print("-".join(s.split()))

############################################################################################################

#614

import re

def split_and_join(string):

    split_string = re.split(r'[^a-zA-Z]', string)

    join_string = ''

    for i,s in enumerate(split_string):
        if i > 0:
            join_string += '-'
        join_string += s

    return split_string, join_string

string = "Geeks for Geeks"
split_string, join_string = split_and_join(string)
print(split_string)
print(join_string)

##############################################################################################################

#615

'''
Using regex.findall() method
'''

import re

s = "Geeks for Geeks"

print(re.findall(r'[a-zA-Z]+', s))

print("-".join(re.findall(r'[a-zA-Z]+',s)))

##############################################################################################################

#616

'''
Using re.split()
'''

import re

def split_string(string):
    list_string = re.split('\s+',string)
    return list_string

def join_string(list_string):
    new_string = "-".join(list_string)
    return new_string


if __name__ == "__main__":
    string = "Geek for Geeks"
    list_string = split_string(string)
    print(list_string)

    new_string = join_string(list_string)
    print(new_string)

###############################################################################################################

#617

'''
Using the find() method
'''

s = 'Geeks for Geeks'

words = []

while True:
    space_index = s.find(' ')
    if space_index == -1:
        words.append(s)
        break

    words.append(s[:space_index])
    s = s[space_index+1:]

join_string = '-'.join(words)
print(join_string)

###############################################################################################################































































































































































































































