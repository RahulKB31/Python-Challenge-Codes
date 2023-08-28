<<<<<<< HEAD
#294

'''
Python program to print even numbers in a list
'''

# Using for loop

list1 = [10,21,4,45,66,93]

#iterating each number in list
for num in list1:

    #checking condition
    if num % 2 == 0:
        print(num, end = " ")

################################################################################################################

#295

'''
Using while loop
'''

list1 = [10,24,4,45,66,93]
num = 0

#using while loop
while(num < len(list1)):

    #checking condition
    if list1[num] % 2 == 0:
        print(list1[num], end=" ")

    #increment num
    num += 1

###########################################################################################################

#296

'''
Using list comprehension
'''

list1 = [10,21,4,45,66,93]

#using list comprehension
even_nos = [num for num in list1 if num % 2 == 0]

print("Even numbers in the list:", even_nos)

#########################################################################################################

#297

'''
Using lambda expressions
'''

list1 = [10,21,4,45,66,93]

# we can also print ven no's using lambda exp
even_nos = list(filter(lambda x: (x % 2 == 0), list1))

print("Even numbers in the list:", even_nos)

#########################################################################################################

#298

'''
Using recursion
'''

def evennumbers(list, n =0):

    #base case
    if n == len(list):
        exit()
    if list[n] % 2 == 0:
        print(list[n], end=" ")

    #calling function recursively
    evennumbers(list, n+1)

#Initializing list
list1 = [10,21,4,45,66,93]

print("Even numbers in the list:", end=" ")
evennumbers(list1)

###########################################################################################################

#299

'''
Using enumerate function
'''

list1 = [2,7,5,64,14]
for a,i in enumerate(list1):
    if i % 2 == 0:
        print(i, end=" ")

################################################################################################################

#300

'''
Uisng pass
'''

list1 = [2,7,5,64,14]
for i in list1:
    if (i % 2 != 0):
        pass
    else:
        print(i, end=" ")

#################################################################################################################

#301

'''
Using numpy.array
'''

import numpy as np

#declaring range
temp = [2,7,5,64,14]
li = np.array(temp)

#printing even numbers using numpy array
even_num = li[li % 2 == 0]
print(even_num)

###################################################################################################################

#302

'''
Using not and Bitwise & Operator
'''

list1 = [39,28,19,45,33,74,56]

#traversing list using for loop
for element in list1:
    if not element&1:   #condition to check even or not
        print(element, end=" ")

#########################################################################################################

#303

'''
Using bitwise | operator
'''

list1 = [39,28,19,45,33,74,56]

#traversing list using for loop
for element in list1:

    # condition to check even or not
    if element|1 != element:
        print(element, end=" ")

#####################################################################################################################

#304

'''
Using reduce method
'''

from functools import reduce
list1 = [39,28,19,45,33,74,56]
even_numbers = reduce(lambda x, y: x + [y] if y % 2 == 0 else x, list1, [])
for num in even_numbers:
    print(num, end=" ")

################################################################################################################

#305

'''
Using numpy.where method
'''

import numpy as np

list1 = [2,7,5,64,14]

#converting list to numpy array
arr = np.array(list1)

#finding even numbers using where() method
even_num = arr[np.where(arr % 2 == 0)]

#printing even numbers
print(even_num)

############################################################################################################

#306

'''
Using itertools.filterflase method
'''

from itertools import filterfalse

#test list1
list1 = [39, 28,19,45,33,74,56]

#filtering even number
even_numbers = filterfalse(lambda y: y % 2, list1)

#printing result
for num in even_numbers:
    print(num, end = " ")

##############################################################################################################






























































































































































































































=======
#294

'''
Python program to print even numbers in a list
'''

# Using for loop

list1 = [10,21,4,45,66,93]

#iterating each number in list
for num in list1:

    #checking condition
    if num % 2 == 0:
        print(num, end = " ")

################################################################################################################

#295

'''
Using while loop
'''

list1 = [10,24,4,45,66,93]
num = 0

#using while loop
while(num < len(list1)):

    #checking condition
    if list1[num] % 2 == 0:
        print(list1[num], end=" ")

    #increment num
    num += 1

###########################################################################################################

#296

'''
Using list comprehension
'''

list1 = [10,21,4,45,66,93]

#using list comprehension
even_nos = [num for num in list1 if num % 2 == 0]

print("Even numbers in the list:", even_nos)

#########################################################################################################

#297

'''
Using lambda expressions
'''

list1 = [10,21,4,45,66,93]

# we can also print ven no's using lambda exp
even_nos = list(filter(lambda x: (x % 2 == 0), list1))

print("Even numbers in the list:", even_nos)

#########################################################################################################

#298

'''
Using recursion
'''

def evennumbers(list, n =0):

    #base case
    if n == len(list):
        exit()
    if list[n] % 2 == 0:
        print(list[n], end=" ")

    #calling function recursively
    evennumbers(list, n+1)

#Initializing list
list1 = [10,21,4,45,66,93]

print("Even numbers in the list:", end=" ")
evennumbers(list1)

###########################################################################################################

#299

'''
Using enumerate function
'''

list1 = [2,7,5,64,14]
for a,i in enumerate(list1):
    if i % 2 == 0:
        print(i, end=" ")

################################################################################################################

#300

'''
Uisng pass
'''

list1 = [2,7,5,64,14]
for i in list1:
    if (i % 2 != 0):
        pass
    else:
        print(i, end=" ")

#################################################################################################################

#301

'''
Using numpy.array
'''

import numpy as np

#declaring range
temp = [2,7,5,64,14]
li = np.array(temp)

#printing even numbers using numpy array
even_num = li[li % 2 == 0]
print(even_num)

###################################################################################################################

#302

'''
Using not and Bitwise & Operator
'''

list1 = [39,28,19,45,33,74,56]

#traversing list using for loop
for element in list1:
    if not element&1:   #condition to check even or not
        print(element, end=" ")

#########################################################################################################

#303

'''
Using bitwise | operator
'''

list1 = [39,28,19,45,33,74,56]

#traversing list using for loop
for element in list1:

    # condition to check even or not
    if element|1 != element:
        print(element, end=" ")

#####################################################################################################################

#304

'''
Using reduce method
'''

from functools import reduce
list1 = [39,28,19,45,33,74,56]
even_numbers = reduce(lambda x, y: x + [y] if y % 2 == 0 else x, list1, [])
for num in even_numbers:
    print(num, end=" ")

################################################################################################################

#305

'''
Using numpy.where method
'''

import numpy as np

list1 = [2,7,5,64,14]

#converting list to numpy array
arr = np.array(list1)

#finding even numbers using where() method
even_num = arr[np.where(arr % 2 == 0)]

#printing even numbers
print(even_num)

############################################################################################################

#306

'''
Using itertools.filterflase method
'''

from itertools import filterfalse

#test list1
list1 = [39, 28,19,45,33,74,56]

#filtering even number
even_numbers = filterfalse(lambda y: y % 2, list1)

#printing result
for num in even_numbers:
    print(num, end = " ")

##############################################################################################################






























































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
