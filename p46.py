<<<<<<< HEAD
#331

'''
Python program to print all odd numbers in a range
'''

# using for loop

start, end = 4,19

#iterating eaach number in list
for num in range(start, end+1):

    #checking condition
    if num % 2 != 0:
        print(num, end=" ")

#################################################################################################################

#332

'''
Taking range limit from user input
'''

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range:"))

#iterating each number in list
for num in range(start,end+1):

    #checking condition
    if num % 2 != 0:
        print(num)

##############################################################################################################

#333

'''
Taking range limit from user input or with static inputs to reduce code execution 
time and to increase code performance
'''

start = 5
end = 20

if start % 2 != 0:

    for num in range(start, end+1, 2):
        print(num, end=" ")
else:
    for num in range(start+1, end+1, 2):
        print(num,end=" ")

###############################################################################################################

#334

'''
Taking range limit from user
'''

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#create a list that contains only even numbers in given range
even_list = range(start,end+1)[start%2::2]

for num in even_list:
    print(num, end=" ")

#############################################################################################################

#335

'''
Using the lambda function
'''

a=3
b=11
li=[]
for in range(a,b+1):
    li.append(i)
#printing odd numbers using the lambda function
odd_num = list(filter(lambda x: (x%2 !=0),li))
print(odd_num)

################################################################################################################

#336

'''
Using recursion
'''

def odd(num1,num2):
    if num1 > num2:
        return
    if num1 & 1:
        print(num1,end=" ")
        return odd(num1+2,num2)
    else:
        return odd(num1+1,num2)

num1=5
num2=15
odd(num1,num2)

##################################################################################################################

#337

'''
Using list comprehension
'''

x = [i for in range(4,15+1) if i%2 !=0]
print(*x)

###############################################################################################################

#338

'''
Using the enumerate function
'''

a=4
b=15
l=[]
for i in range(a,b+1):
    l.append(i)
print([a for j,a in enumerate(l) if a%2 != 0])

###############################################################################################################

#339

'''
Using pass
'''

a=4
b=15
for i in range(a,b+1):
    if i%2 == 0:
        pass
    else:
        print(i,end=" ")

##############################################################################################################

#340

'''
Using filter method
'''

a=4
b=15

#create a list that contains only even numbers in given range
l=filter(lambda a: a%2, range(a,b+1))
print(*l)

############################################################################################################

#341

'''
Using bitwise & operator
'''

start,end = 4,19

#iterating each number in list
for num in range(start,end+1):

    #checking condition
    if num&1 != 0:
        print(num, end=" ")

############################################################################################################

#342

'''
Using bitwise | operator
'''

start,end = 4,19

#iterating each number in list
for num in range(start,end+1):

    #checking condition
    if num | 1 == num:
        print(num, end=" ")

##############################################################################################################

#343

'''
Using numpy module
'''

import numpy as np

#range declaration
a = 3
b = 15

#create an array containing numbers in the range
arr = np.arange(a,b+1)

#create a new array containing only even numbers
evens = arr[arr % 2 != 0]

#print the array of even numbers
print(*evens)

##########################################################################################################

#344

'''
Using continue key
'''

a = 4
b = 15

for i in range(a,b+1):
    if i % 2 == 0:
        continue
    else:
        print(i, end=" ")

##############################################################################################################

#345

'''
Using filter false method
'''

import itertools

a = 3
b =15

#using filterfalse function
evens = list(itertools.filterfalse(lambda x: x%2 == 0, range(a,b+1)))

print(*evens)

###############################################################################################################













































































































































































































=======
#331

'''
Python program to print all odd numbers in a range
'''

# using for loop

start, end = 4,19

#iterating eaach number in list
for num in range(start, end+1):

    #checking condition
    if num % 2 != 0:
        print(num, end=" ")

#################################################################################################################

#332

'''
Taking range limit from user input
'''

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range:"))

#iterating each number in list
for num in range(start,end+1):

    #checking condition
    if num % 2 != 0:
        print(num)

##############################################################################################################

#333

'''
Taking range limit from user input or with static inputs to reduce code execution 
time and to increase code performance
'''

start = 5
end = 20

if start % 2 != 0:

    for num in range(start, end+1, 2):
        print(num, end=" ")
else:
    for num in range(start+1, end+1, 2):
        print(num,end=" ")

###############################################################################################################

#334

'''
Taking range limit from user
'''

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#create a list that contains only even numbers in given range
even_list = range(start,end+1)[start%2::2]

for num in even_list:
    print(num, end=" ")

#############################################################################################################

#335

'''
Using the lambda function
'''

a=3
b=11
li=[]
for in range(a,b+1):
    li.append(i)
#printing odd numbers using the lambda function
odd_num = list(filter(lambda x: (x%2 !=0),li))
print(odd_num)

################################################################################################################

#336

'''
Using recursion
'''

def odd(num1,num2):
    if num1 > num2:
        return
    if num1 & 1:
        print(num1,end=" ")
        return odd(num1+2,num2)
    else:
        return odd(num1+1,num2)

num1=5
num2=15
odd(num1,num2)

##################################################################################################################

#337

'''
Using list comprehension
'''

x = [i for in range(4,15+1) if i%2 !=0]
print(*x)

###############################################################################################################

#338

'''
Using the enumerate function
'''

a=4
b=15
l=[]
for i in range(a,b+1):
    l.append(i)
print([a for j,a in enumerate(l) if a%2 != 0])

###############################################################################################################

#339

'''
Using pass
'''

a=4
b=15
for i in range(a,b+1):
    if i%2 == 0:
        pass
    else:
        print(i,end=" ")

##############################################################################################################

#340

'''
Using filter method
'''

a=4
b=15

#create a list that contains only even numbers in given range
l=filter(lambda a: a%2, range(a,b+1))
print(*l)

############################################################################################################

#341

'''
Using bitwise & operator
'''

start,end = 4,19

#iterating each number in list
for num in range(start,end+1):

    #checking condition
    if num&1 != 0:
        print(num, end=" ")

############################################################################################################

#342

'''
Using bitwise | operator
'''

start,end = 4,19

#iterating each number in list
for num in range(start,end+1):

    #checking condition
    if num | 1 == num:
        print(num, end=" ")

##############################################################################################################

#343

'''
Using numpy module
'''

import numpy as np

#range declaration
a = 3
b = 15

#create an array containing numbers in the range
arr = np.arange(a,b+1)

#create a new array containing only even numbers
evens = arr[arr % 2 != 0]

#print the array of even numbers
print(*evens)

##########################################################################################################

#344

'''
Using continue key
'''

a = 4
b = 15

for i in range(a,b+1):
    if i % 2 == 0:
        continue
    else:
        print(i, end=" ")

##############################################################################################################

#345

'''
Using filter false method
'''

import itertools

a = 3
b =15

#using filterfalse function
evens = list(itertools.filterfalse(lambda x: x%2 == 0, range(a,b+1)))

print(*evens)

###############################################################################################################













































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
