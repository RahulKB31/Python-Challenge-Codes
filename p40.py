#248

'''
Python program to find largest number in a list
'''

# Find largest number in a list with naive example

list1 = [10,20,4,45,99]

#sorting the list
list1.sort()

#printing the last element
print("Largest element is:", list[-1])

#####################################################################################################

#249

'''
Find largest number in a list using max() method
'''

list1 = [10,20,4,45,99]

#printing the maximum element
print("Largest element is:", max(list1))

#########################################################################################################

#250

'''
Find the max list element on inputs provided by user
'''

#creating an empty list
list1 = []

#asking number of elements to put in list
num = int(input("ENter number of elements in list: "))

#Iterating till num to append elements in list
for i in range(1, num+1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

#printing maximum element
print("Largest element is:", max(list1))

###########################################################################################################

#251

'''
Find largest number in a list without using built-in functions
'''

def myMax(list1):

    # assume first number in list is largest
    # initially and assign it to variable max
    max = list1[0]

    # Now traverse through th list and compare
    # each number with max value. WHichever is largest assign that value to max
    for x in list1:
        if x > max:
            max = x

    #after complete traversing the list
    # return the max value
    return max

#driver code
list1 = [10,20,4,45,99]
print("Largest element is:", myMax(list1))

############################################################################################################

#252

'''
Find largest number in a list using the lambda function
'''

lst = [10,20,4,45,99]
print(max(lst, key=lambda value: int(value)))

############################################################################################################

#253

'''
Find largest number in a list using reduce function 
'''

from functools import reduce
lst = [10,20,4,45,99]
largest_elem = reduce(max, lst)
print(largest_elem)

##############################################################################################################

#254

'''
Find largest number in a list using recursion
'''

def FindLargest(itr, ele, list1):

    #base condition
    if itr == len(list1):
        print("Largest element in the list is: ", ele)
        return

    #Check max condition
    if ele < list1[itr]:
        ele = list1[itr]

    #recursive solution
    FindLargest(itr+1, ele, list1)

    return

# input list
list1 = [2,1,7,9,5,4]

FindLargest(0, list1[0], list1)

###########################################################################################################

#255

'''
Find largest number in a list using heapq.nlargest()
'''

import heapq

#list of numbers
list1 = [10,20,4,45,99]

# finding the largest element using heapq.nlargest()
largest_element = heapq.nlargest(1, list1)[0]

#printing the largest element
print("Largest element is:", largest_element)

###########################################################################################################

#256

'''
Find largest number in a list using np.max() method
'''

import numpy as np

#given list
list1 = [2,7,5,64,14]

#converting list to numpy array
arr = np.array(list1)

#finding largest numbers using np.max() method
num = arr.max()

#printing largest number
print(num)

########################################################################################################






















































































































































































































