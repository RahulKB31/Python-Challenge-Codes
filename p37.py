<<<<<<< HEAD
#216

'''
Python program to find sum of elements in list
'''

total = 0

#creating a list
list1 = [11,5,17,18,23]

#iterate each element in list and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]

#printing total value
print("Sum of all elements in given list: ", total)

##############################################################################################################

#217

'''
Using while() loop
'''

total = 0
ele = 0

#creating a list
list1 = [11,5,17,18,23]

#iterate each element in list and add them in variable total
while(ele < len(list1)):
    total = total + list1[ele]
    ele += 1

#printing total value
print("Sum of all elements in given list: ", total)

##############################################################################################################

#218

'''
Recursive way
'''

#creating a list
list1 = [11,5,17,18,23]

#creating sum_list function

def sumOfList(list,size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)

#Driver code
total = sumOfList(list1, len(list1))

print("Sum of all elements in given lisst: ", total)

##############################################################################################################

#219

'''
Using sum() method
'''

#creating a list
list1 = [11,5,17,18,23]

#using sum() function
total = sum(list1)

#printing total value
print("Sum of all elements in given list :", total)

############################################################################################################

#220

'''
Using add() function of operator module
'''

from operator import*
list1 = [12,15,3,10]
result = 0
for i in list1:
    # adding elements in the list using add function of operator module
    result = add(i, result)
#printing the result
print(result)

#############################################################################################################

#221

'''
Using enumerate function
'''

list1 = [12,15,3,10]
s = 0
for i,a in enumerate(list1):
    s+=a
print(s)

################################################################################################################

#222

'''
Using list comprehension
'''

list1 = [12,15,3,10]
s = [i for i in list1]
print(sum(s))

############################################################################################################

#223

'''
Using lambda function
'''

list1 = [12,15,3,10]
print(sum(list(filter(lambda x: (x), list1))))

###########################################################################################################

#224

'''
Using add operator
'''

import operator
list1 = [12,15,3,10]
s=0
for i in list1:
    s = s+operator.add(0,i)
print(s)

#########################################################################################################

#225

'''
Using add() + while loop
'''

import operator

#initializing the values
lst = [0,4,1,6,8]
sum = 0
i = 0

# Traversing the list using while loop finding the sum using add()
while i < len(lst):
    sum = sum + operator.add(0,lst[i])
    i = i + 1

#printing the sum of list elements
print("The sum of elements in the given list is:", sum)

#####################################################################################################





































































































































































=======
#216

'''
Python program to find sum of elements in list
'''

total = 0

#creating a list
list1 = [11,5,17,18,23]

#iterate each element in list and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]

#printing total value
print("Sum of all elements in given list: ", total)

##############################################################################################################

#217

'''
Using while() loop
'''

total = 0
ele = 0

#creating a list
list1 = [11,5,17,18,23]

#iterate each element in list and add them in variable total
while(ele < len(list1)):
    total = total + list1[ele]
    ele += 1

#printing total value
print("Sum of all elements in given list: ", total)

##############################################################################################################

#218

'''
Recursive way
'''

#creating a list
list1 = [11,5,17,18,23]

#creating sum_list function

def sumOfList(list,size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)

#Driver code
total = sumOfList(list1, len(list1))

print("Sum of all elements in given lisst: ", total)

##############################################################################################################

#219

'''
Using sum() method
'''

#creating a list
list1 = [11,5,17,18,23]

#using sum() function
total = sum(list1)

#printing total value
print("Sum of all elements in given list :", total)

############################################################################################################

#220

'''
Using add() function of operator module
'''

from operator import*
list1 = [12,15,3,10]
result = 0
for i in list1:
    # adding elements in the list using add function of operator module
    result = add(i, result)
#printing the result
print(result)

#############################################################################################################

#221

'''
Using enumerate function
'''

list1 = [12,15,3,10]
s = 0
for i,a in enumerate(list1):
    s+=a
print(s)

################################################################################################################

#222

'''
Using list comprehension
'''

list1 = [12,15,3,10]
s = [i for i in list1]
print(sum(s))

############################################################################################################

#223

'''
Using lambda function
'''

list1 = [12,15,3,10]
print(sum(list(filter(lambda x: (x), list1))))

###########################################################################################################

#224

'''
Using add operator
'''

import operator
list1 = [12,15,3,10]
s=0
for i in list1:
    s = s+operator.add(0,i)
print(s)

#########################################################################################################

#225

'''
Using add() + while loop
'''

import operator

#initializing the values
lst = [0,4,1,6,8]
sum = 0
i = 0

# Traversing the list using while loop finding the sum using add()
while i < len(lst):
    sum = sum + operator.add(0,lst[i])
    i = i + 1

#printing the sum of list elements
print("The sum of elements in the given list is:", sum)

#####################################################################################################





































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
