#307

'''
Python program to print odd numbers in a list
'''

# Using for loop

list1 = [10,21,4,45,66,93]

#iterating each number in list
for num in list1:

    #checking condition
    if num % 2 != 0:
        print(num, end= " ")

#############################################################################################################

#308

'''
Using while loop
'''

list1 = [10,21,4,45,66,93]
i = 0

#using while loop
while(i < len(list1)):

    #checking condition
    if list1[i] % 2 != 0:
        print(list1[i], end=" ")

    #increment i
    i += 1

#############################################################################################################

#309

'''
Using list comprehension
'''

list1 = [10,21,4,45,66,93]

only_odd = [num for num in list1 if num % 2 == 1]

print(only_odd)

############################################################################################################

#310

'''
Using lambda expressions
'''

list1 = [10,21,4,45,66,93,11]

#we can also print odd no's using lambda exp
odd_nos = lis(filter(lambda x: (x % 2 != 0), list1))

print("Odd numbers in the list:", odd_nos)

#############################################################################################################

#311

'''
Using pass
'''

lst = [10,21,4,45,66,93,11]
for i in lst:
    if 1 % 2 == 0:
        pass
    else:
        print(i, end=" ")

################################################################################################################

#312

'''
Using recursion
'''

def oddnumbers(list, n=0):
    #base case
    if n == len(list):
        exit()
    if list[n] % 2 != 0:
        print(list[n], end=" ")
    #calling function recursively
    oddnumbers(list, n+1)

list1 = [10,21,4,45,66,93,11]
print("Odd numbes in the list:", end=" ")
oddnumbers(list1)

###############################################################################################################

#313

'''
Using enumerate function
'''

list1 = [2,7,5,64,14]
for a,i in enumerate(list1):
    if i % 2 != 0:
        print(i, end=" ")

###############################################################################################################

#314

'''
Using numpy.array function
'''

import numpy as np

#list of numbers
list1 = np.array([10,21,4,45,66,93])

only_odd = list1[list1 % 2 == 1]

print(only_odd)

#################################################################################################################

#315

'''
Using bitwise and Operator
'''

list1 = [9,5,4,7,2]

for ele in list1:
    if ele & 1: #checking the element odd or not
        print(ele, end=" ")

#################################################################################################################

#316

'''
Using bitwise | operator
'''

list1 = [9,5,4,7,2]

for ele in list1:
    if ele | 1 == ele: #checking the element odd or not
        print(ele, end=" ")

###################################################################################################################

#317

'''
Using filter function
'''

def is_odd(number):
    return number % 2 == 1

def print_odd_numbers(numbers):
    odd_numbers = list(filter(is_odd, numbers))
    return odd_numbers

numbers = [1,2,3,4,5,6,7,8,9,10]
print(print_odd_numbers(numbers))

#################################################################################################################

#318

'''
Using numpy.where()
'''

import numpy as np

#list of numbers
list1 = [10,21,4,45,66,93]

#convert list to numpy array
arr = np.array(list1)

#find indices where elements are odd
idx = np.where(arr % 2 != 0)

#extract elements at odd indices
only_odd = arr[idx]

#print only odd elements
print(only_odd)

##############################################################################################################

#319

'''
Using functools.reduce method
'''

from functools import reduce

#list of numbers
list1 = [10,21,4,45,66,93]

#using reduce method in list
odd_list = reduce(lambda a, b: a + [b] if b % 2 else a, list1, [])

print(odd_list)

############################################################################################################















































































































































































































































































