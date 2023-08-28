<<<<<<< HEAD
#554

'''
Find length of string in python (6 ways)
'''

# Using the built in function len

str = "geeks"
print(len(str))

########################################################################################################

#555

#Using for loop and in operator

def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter

str = "geeks"
print(findLen(str))

#################################################################################################################

#556

'''
Using while loop and slicing
'''

def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

str = "geeks"
print(findLen(str))

################################################################################################################

#557

'''
Using string methods join and count
'''

def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1

str = "geeks"
print(findLen(str))

###############################################################################################################

#558

'''
Using reduce method
'''

import functools

def findLen(string):
    return functools.reduce(lambda x,y: x+1, string, 0)

string = "geeks"
print(findLen(string))

###############################################################################################################

#559

'''
Using sum(0 and list comprehension function
'''

def findLen(string):
    return sum(1 for i in string)

string = 'geeks'
print(findLen(string))

###########################################################################################################

























































































































=======
#554

'''
Find length of string in python (6 ways)
'''

# Using the built in function len

str = "geeks"
print(len(str))

########################################################################################################

#555

#Using for loop and in operator

def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter

str = "geeks"
print(findLen(str))

#################################################################################################################

#556

'''
Using while loop and slicing
'''

def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

str = "geeks"
print(findLen(str))

################################################################################################################

#557

'''
Using string methods join and count
'''

def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1

str = "geeks"
print(findLen(str))

###############################################################################################################

#558

'''
Using reduce method
'''

import functools

def findLen(string):
    return functools.reduce(lambda x,y: x+1, string, 0)

string = "geeks"
print(findLen(string))

###############################################################################################################

#559

'''
Using sum(0 and list comprehension function
'''

def findLen(string):
    return sum(1 for i in string)

string = 'geeks'
print(findLen(string))

###########################################################################################################

























































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
