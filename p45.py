<<<<<<< HEAD
#320

'''
Python program to print all even numbers in a range
'''

for even_numbers in range(4,15,2):
    print(even_numbers, end=" ")

################################################################################################################

#321

'''
Taking range limit from user input
'''

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#iterating each number in list
for num in range(start,end+1):

    #checking condition
if num % 2 == 0:
    print(num, end=" ")

#############################################################################################################

#322

'''
Taking range limit user input and using skip sequence number in range function which
generates the all even number
'''

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#creating even starting range
start = start +1 if start&1 else start

#creating a list and printing element
#contains even numbers in range
[print(x) for x in range(start,end+1,2)]

#############################################################################################################

#323

'''
Using recursion
'''

def even(num1,num2):
    if num1 > num2:
        return
    print(nm1, end=" ")
    return even(num1+2, num2)

num1=4, num2=15
even(num1,num2)

##############################################################################################################

#324

'''
Using the lambda function
'''

a=4
b=15
li=[]
for i in range(a,b+1):
    li.append(i)

#printing odd numbers using the lambda function
even_num = list(filter(lambda x: (x%2==0),li))
print(even_num)

###############################################################################################################

#325

'''
Using list comprehension
'''

x = [i for i in range(4,15+1) if i%2==0]
print(*x)

#############################################################################################################

#326

'''
Using enumerate function
'''

a = 4
b = 15
l = []
for i in range(a,b+1):
    l.append(i)
print([a for j,a in enumerate(l) if a%2==0])

###############################################################################################################

#327

'''
Using pass
'''

a=4
b=15
for i in range(a,b+1):
    if i%2 != 0:
        pass
    else:
        print(i, end=" ")

################################################################################################################

#328

'''
Using numpy.array
'''

import numpy as np

a=4
b=15
li = np.array(range(a,b+1))

#printing odd numbers using numpy array
even_num = li[li%2==0]
print(even_num)

#################################################################################################################

#329

'''
Using bitwise and operator
'''

start,end = 4,19

#iterating each number in list
for num in range(start, end+1):

    #checking condition
    if not (num & 1):
        print(num, end=" ")

##################################################################################################################

#330

'''
Using bitwise or operator
'''

start, end = 4,19

#iterating each number in list
for num in range(start, end+1):

    #checking condition
    if not (num|1) == num:
        print(num, end=" ")

##################################################################################################################

















































































































































































































































=======
#320

'''
Python program to print all even numbers in a range
'''

for even_numbers in range(4,15,2):
    print(even_numbers, end=" ")

################################################################################################################

#321

'''
Taking range limit from user input
'''

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#iterating each number in list
for num in range(start,end+1):

    #checking condition
if num % 2 == 0:
    print(num, end=" ")

#############################################################################################################

#322

'''
Taking range limit user input and using skip sequence number in range function which
generates the all even number
'''

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#creating even starting range
start = start +1 if start&1 else start

#creating a list and printing element
#contains even numbers in range
[print(x) for x in range(start,end+1,2)]

#############################################################################################################

#323

'''
Using recursion
'''

def even(num1,num2):
    if num1 > num2:
        return
    print(nm1, end=" ")
    return even(num1+2, num2)

num1=4, num2=15
even(num1,num2)

##############################################################################################################

#324

'''
Using the lambda function
'''

a=4
b=15
li=[]
for i in range(a,b+1):
    li.append(i)

#printing odd numbers using the lambda function
even_num = list(filter(lambda x: (x%2==0),li))
print(even_num)

###############################################################################################################

#325

'''
Using list comprehension
'''

x = [i for i in range(4,15+1) if i%2==0]
print(*x)

#############################################################################################################

#326

'''
Using enumerate function
'''

a = 4
b = 15
l = []
for i in range(a,b+1):
    l.append(i)
print([a for j,a in enumerate(l) if a%2==0])

###############################################################################################################

#327

'''
Using pass
'''

a=4
b=15
for i in range(a,b+1):
    if i%2 != 0:
        pass
    else:
        print(i, end=" ")

################################################################################################################

#328

'''
Using numpy.array
'''

import numpy as np

a=4
b=15
li = np.array(range(a,b+1))

#printing odd numbers using numpy array
even_num = li[li%2==0]
print(even_num)

#################################################################################################################

#329

'''
Using bitwise and operator
'''

start,end = 4,19

#iterating each number in list
for num in range(start, end+1):

    #checking condition
    if not (num & 1):
        print(num, end=" ")

##################################################################################################################

#330

'''
Using bitwise or operator
'''

start, end = 4,19

#iterating each number in list
for num in range(start, end+1):

    #checking condition
    if not (num|1) == num:
        print(num, end=" ")

##################################################################################################################

















































































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
