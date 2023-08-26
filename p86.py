#607

'''
Python program for removing i-th character from a string
'''

def remove(string, i):
    a = string[:i]
    b = string[i + 1:]
    return a + b

if __name__ == "__main__":
    string = "geeksforgeeks"
    i = 5
    print(remove(string,i))

##################################################################################################################

#608

'''
Use string replace in python
'''

def remove(string, i):
    for j in range(len(string)):
        if j == i:
            string = string.replace(string[i], "", 1)
    return string


if __name__ == "__main__":
    string = "geeksforgeeks"
    i = 5
    print(remove(string, i))

##################################################################################################################

#609

'''
Using list().pop() and join() methods
'''

def remove(string, i):
    if i > len(string):
        return string
    a = list(string)
    a.pop(i)
    return "".join(a)

if __name__ == "__main__":
    string = "geeksforgeeks"
    i = 5
    print(remove(string, i))

##################################################################################################################

#610

'''
Using enumerate, join
'''

def remove(string, i):
    return "".join()

print(remove("geeksforgeeks",2))

##################################################################################################################

#611

'''
Using the remodule and f string
'''

import re

def remove(string, i):
    pattern = f"(^.{{{i}}})(.)"
    return re.sub(pattern, r"\1", string)

if __name__ == "__main__":
    string = "geeksforgeeks"
    i = 5
    print(remove(string, i))

##################################################################################################################



















































































































































































































