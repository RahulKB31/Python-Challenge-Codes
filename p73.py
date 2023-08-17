#531

'''
Check if string contains substring in python
'''

# Using the if-else

MyString1 = "A geek in need is a geek indeed"

if 'need' in MyString1:
    print("Yes it is present in the string")
else:
    print("No it is not present")

#################################################################################################################

#532

'''
Using in operator
'''

text = "Geeks welcome to the Geek Kingdom"

if "Geek" in text:
    print("Substring found")
else:
    print("Substring not found")

if "For" in text:
    print("Substring found")
else:
    print("Substring not found")

################################################################################################################

#533

'''
Using split() method
'''

string = "geeks for geeks"
substring = "geeks"

s = string.split()

if substring in s:
    print("yes")
else:
    print("no")

#################################################################################################################

#532

'''
Using find() method
'''

def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")

string = "geeks for geeks"
sub_str = "geek"
check(string,sub_str)

################################################################################################################

#533

'''
Using count() method
'''

def check(s2,s1):
    if (s2.count(s1) > 0):
        print("YES")
    else:
        print("NO")

s2 = "A geek in nned is a geek indeed"
s1 = "geeks"
check(s2,s1)

################################################################################################################

#534

'''
Using index() method
'''

any_string = "Geeks for Geeks substring"
start = 0
end = 1000
print(any_string.index('substring', start, end))

##############################################################################################################

#535

'''
Using list comprehension
'''

s = "geeks for geeks"
s2 = "geeks"
print(["yes" if s2 in s else "no"])

#################################################################################################################

#536

'''
Using lambda function
'''

s = "geeks for geeks"
s2 = "geeks"
x = list(filter(lambda x: (s2 in s), s.split()))
print(["yes" if x else "no"])

##############################################################################################################

#537

'''
using the "__contains__" magic class
'''

a = ['Geeks-13', 'for-56','Geeks-78','xyz-46']
for i in a:
    if i.__contains__("Geeks"):
        print(f"Yes {i} is containing")

################################################################################################################

#538

'''
Using slicing
'''

def is_substring(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return True
    return False

string = "A geek in nned is a geek indeed"
substring = "geeks"
print(is_substring(string, substring))

################################################################################################################

#539

'''
Using regular expression
'''

import re

MyString1 = "A geek in nned is a geek indeed"

if re.search("need", MyString1):
    print("Yes it is present in the string")
else:
    print("No it is not present")

#################################################################################################################

#540

'''
Using operator.contains() method
'''

import operator as op
s = "geeks for geeks"
s2 = "geeks"
if(op.contains(s,s2)):
    print("yes")
else:
    print("no")

###############################################################################################################
























































































































































































































































