<<<<<<< HEAD
#523

'''
How to remove letters from a string in python
'''

#using replace()

string = "Geek123For123Geeks"
character = '123'

count = len(string) - len(string.replace(character,''))
print(count)

#########################################################################################################

#524

'''
Using translate()
'''

str = "Geek123For123Geeks"

print(str.translate({ord(i): None for i in '123'}))

############################################################################################################

#525

'''
Using recursion()
'''

def remove_ith_character(s,i):

    # return string with first character removed
    if i == 0:
        return s[1:]

    # recursive case: return first character
    # contenated with result of calling function
    # on string with index decremented by 1
    return s[0] + remove_ith_character(s[1:],i-1)

test_str = "GeeksForGeeks"
new_str = remove_ith_character(test_str, 2)
print("The string after removal of ith character:", new_str)

#################################################################################################################

#526

'''
Using the naive method
'''

test_str = "GeeksForGeeks"

#removing char at pos 3
new_str = ""

for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

#printing string after removal
print("The string after removal of ith character: " + new_str)

###############################################################################################################

# 527

'''
Using str.replace()
'''

test_str = "GeeksForGeeks"

# removing char at pos 3 using replace
new_str = test_str.replace('e','')

#printing string after removal removes all occurances of 'e'
print("The string after removal of i th character (doesn't work): " + new_str)

#removing 1st occurances of s, i.e, 5th pos if we wish to remove it
new_str = test_str.replace('s','',1)

#printing string after removal removes first occurances of s
print("The stirng after removal of ith character(works): " + new_str)

###############################################################################################################

#528

'''
Using sice + concatenation
'''

test_str = "GeeksForGeeks"

new_str = test_str[:2] + test_str[3:]

print("The string after removal of ith character: " + new_str)

###############################################################################################################

#529

'''
Using str.join() and list comprehension
'''

test_str = "GeeksForGeeks"

new_str = ''.join([test_str[i] for i in range(len(test_str)) if i != 2])

print("The string after removal of ith character: " + new_str)

###############################################################################################################

#530

'''
Using bytearray
'''

def remove_char(s, i):
    b = bytearray(s, 'utf-8')
    del b[i]
    return b.decode()

s = "hello world"
i = 4
s = remove_char(s, i)
print(s)

#############################################################################################################











































































































































































































































=======
#523

'''
How to remove letters from a string in python
'''

#using replace()

string = "Geek123For123Geeks"
character = '123'

count = len(string) - len(string.replace(character,''))
print(count)

#########################################################################################################

#524

'''
Using translate()
'''

str = "Geek123For123Geeks"

print(str.translate({ord(i): None for i in '123'}))

############################################################################################################

#525

'''
Using recursion()
'''

def remove_ith_character(s,i):

    # return string with first character removed
    if i == 0:
        return s[1:]

    # recursive case: return first character
    # contenated with result of calling function
    # on string with index decremented by 1
    return s[0] + remove_ith_character(s[1:],i-1)

test_str = "GeeksForGeeks"
new_str = remove_ith_character(test_str, 2)
print("The string after removal of ith character:", new_str)

#################################################################################################################

#526

'''
Using the naive method
'''

test_str = "GeeksForGeeks"

#removing char at pos 3
new_str = ""

for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

#printing string after removal
print("The string after removal of ith character: " + new_str)

###############################################################################################################

# 527

'''
Using str.replace()
'''

test_str = "GeeksForGeeks"

# removing char at pos 3 using replace
new_str = test_str.replace('e','')

#printing string after removal removes all occurances of 'e'
print("The string after removal of i th character (doesn't work): " + new_str)

#removing 1st occurances of s, i.e, 5th pos if we wish to remove it
new_str = test_str.replace('s','',1)

#printing string after removal removes first occurances of s
print("The stirng after removal of ith character(works): " + new_str)

###############################################################################################################

#528

'''
Using sice + concatenation
'''

test_str = "GeeksForGeeks"

new_str = test_str[:2] + test_str[3:]

print("The string after removal of ith character: " + new_str)

###############################################################################################################

#529

'''
Using str.join() and list comprehension
'''

test_str = "GeeksForGeeks"

new_str = ''.join([test_str[i] for i in range(len(test_str)) if i != 2])

print("The string after removal of ith character: " + new_str)

###############################################################################################################

#530

'''
Using bytearray
'''

def remove_char(s, i):
    b = bytearray(s, 'utf-8')
    del b[i]
    return b.decode()

s = "hello world"
i = 4
s = remove_char(s, i)
print(s)

#############################################################################################################











































































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
