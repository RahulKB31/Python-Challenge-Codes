<<<<<<< HEAD
#597

'''
Program to check if a string contains any special character
'''

# Using regular expression

import re

def run(string):
    regex = re.compile('[@_!@#$%^&*()_<>?:"{}~]')

    if (regex.search(string) == None):
        print("Strinfg is accepted")
    else:
        print("String is not accepted")

if __name__ == "__main__":
    string = "GeeksforGeeks"
    run(string)

############################################################################################################

#598

n = "GeeksforGeeks"
n.split()
c = 0
s = '[@_!@#$%^&*()_<>?:"{}~]'
for i in range(len(n)):
    if n[i] in s:
        c += 1

if c:
    print("String is not accepted")
else:
    print("String accepted")

##########################################################################################################

#599

'''
Using inbuilt methods
'''

def has_special_char(s):
    for c in s:
        if not (c.isalpha() or c.isdigit() or c == " "):
            return True
        return False

s = "Hello World"
if has_special_char(s):
    print("The string contains special characters")
else:
    print("The string does not contain special characters")

###########################################################################################################

#600

'''
Using string.punctuation
'''

import string

def check_string(s):
    for c in s:
        if c in string.punctuation:
            print("String is not accepted")
            return
    print("String is accepted")

check_string("Geeks$For$Geeks")
check_string("Geeks for Geeks")

############################################################################################################

#601

'''
Using ASCII values
'''

def check_specal_char_ascii(string):
    for char in string:
        if ord(char) < 48 or (57 < ord(char < 65) or (90 < ord(char) < 97) or ord(char) > 122):
            return "String is not accepted"
        return "String is accepted"

string = "Geeks$For$Geeks"
print(check_specal_char_ascii(string))

#############################################################################################################







































































































































































































































=======
#597

'''
Program to check if a string contains any special character
'''

# Using regular expression

import re

def run(string):
    regex = re.compile('[@_!@#$%^&*()_<>?:"{}~]')

    if (regex.search(string) == None):
        print("Strinfg is accepted")
    else:
        print("String is not accepted")

if __name__ == "__main__":
    string = "GeeksforGeeks"
    run(string)

############################################################################################################

#598

n = "GeeksforGeeks"
n.split()
c = 0
s = '[@_!@#$%^&*()_<>?:"{}~]'
for i in range(len(n)):
    if n[i] in s:
        c += 1

if c:
    print("String is not accepted")
else:
    print("String accepted")

##########################################################################################################

#599

'''
Using inbuilt methods
'''

def has_special_char(s):
    for c in s:
        if not (c.isalpha() or c.isdigit() or c == " "):
            return True
        return False

s = "Hello World"
if has_special_char(s):
    print("The string contains special characters")
else:
    print("The string does not contain special characters")

###########################################################################################################

#600

'''
Using string.punctuation
'''

import string

def check_string(s):
    for c in s:
        if c in string.punctuation:
            print("String is not accepted")
            return
    print("String is accepted")

check_string("Geeks$For$Geeks")
check_string("Geeks for Geeks")

############################################################################################################

#601

'''
Using ASCII values
'''

def check_specal_char_ascii(string):
    for char in string:
        if ord(char) < 48 or (57 < ord(char < 65) or (90 < ord(char) < 97) or ord(char) > 122):
            return "String is not accepted"
        return "String is accepted"

string = "Geeks$For$Geeks"
print(check_specal_char_ascii(string))

#############################################################################################################







































































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
