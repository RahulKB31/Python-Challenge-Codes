#373

'''
Python program to print all negative numbers in a range
'''

def negativenumbers(a,b):
    #checking condition for negative numbers
    #single line solution
    out = [i for i in range(a,b+1) if i<0]

    #print the all negative numbers
    print(*out)

#driver code
a = -4
b =5
negativenumbers(a,b)

#################################################################################################################

#374

'''
Using for loop
'''

start, end = -4, 19

#iterating each number in list
for num in range(start, end + 1):

    #checking condition
    if num < 0:
        print(num, end = " ")

###########################################################################################################

#375

'''
Taking range limit from user input
'''

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#iterating each number in list
for num in range(start, end+1):

    #checking condition
    if num < 0:
        print(num,end = " ")

###############################################################################################################

#376

'''
Using lambda function
'''

a = -4
b = 5
li = []
for i in range(a, b):
    li.append(i)
#printing negative numbers using the lambda function
negative_num = list(filter(lambda x: (x<0), li))
print(negative_num)

###############################################################################################################

#377

'''
Using enumerate function
'''

a = -4
b = 5
l = []
for i in range(a,b+1):
    l.append(i)
print([a for j, a in enumerate(l) if a < 0])

########################################################################################################

#378

'''
Using list comprehension
'''

a = -4
b = 5
print([i for i in range(a, b+1) if i<0])

#######################################################################################################

#379

'''
Using pass()
'''

a = -4
b = 5
for i in range(a,b+1):
    if i>=0:
        pass
    else:
        print(i,end=" ")

#############################################################################################################

#380

'''
Using recursion
'''

def printNegative(itr,end):
    if itr == end:
        return
    if itr < 0:
        print(itr, end= " ")
    printNegative(itr+1, end)
    return

a = -5
b = 5
printNegative(a,b)

##############################################################################################################

#381

'''
Using numpy.arange() and numpy.where()
'''

import numpy as np

start = -4
end = 5

#creating an array using numpy.arange()
arr = np.arange(start, end+1)

#filtering negative numbers using numpy.where()
neg_arr = arr[np.where(arr<0)]

#printing the resulting array
print(neg_arr)

##############################################################################################################

















































































































































































































































