<<<<<<< HEAD
#235

'''
Python program to find smallest number in a list
'''

#Sorting the list to find smallest number in a list in ascending order

list1 = [10,20,4,45,99]

#sorting the list
list1.sort()

#printing the first element
print("Smallest element is: ",list1[0])

###########################################################################################################

#236

'''
In descending order
'''

list1 = [10,20,4,45,99]

#sorting the list
list1.sort(reverse=True)

#printing the first element
print("Smallest element is:", list1[-1])

#############################################################################################################

#237

'''
Using min() method to find smallest number in a list
'''

list1 = [10,20,1,45,99]

#printing the minimum element
print("Smallest element is:", min(list1))

#######################################################################################################

#238

'''
Find minimum list element for a user defined list
'''

#creating empty list
list1 = []

#asking number of elements to put in list
num = int(input("Enter number of elements in list:"))

#iterating till num tp a[[end elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

#print minimum element
print("Smallest element is: ", min(list1))

################################################################################################################

#239

'''
Find the smallest element element in list comparing every element
'''

l = [int(l) for l in input("List:").split(",")]
print("The list is", l)

#Assign first element as a minimum
min1 = l[0]

for i in range(len(l)):
    # if the other element is min than first element
    if l[i] < min1:
        min1 = l[i] #it will change

print("The smallest element in the list is", min1)

##########################################################################################################

#240

'''
Using the lambda function to find smallest number in a list
'''

lst = [20,10,20,1,100]
print(min(lst, key=lambda value: int(value)))

###########################################################################################################

#241

'''
Using the enumerate function to find smallest number in a list
'''

lst = [20,10,20,1,100]
a,i = min((a,i) for (i,a) in enumerate(lst))
print(a)

############################################################################################################

#242

'''
Using reduce function to find the smallest number in a list
'''

from functools import reduce
lst = [20,10,20,15,100]
print(reduce(min,lst))

############################################################################################################

#243

'''
Using heap
'''

import heapq

def find_smallest(numbers):
    # build a min heap using the elements in the list
    heap = [(x,x) for x in numbers]
    heapq.heapify(heap)

    #return the root element (smallest element)
    _, smallest = heapq.heappop(heap)

    return smallest

#test the function
numbers = [10,20,4,45,99]
print(find_smallest(numbers))

############################################################################################################

#244

'''
Using recursion
'''

def Findsmall(itr,ele,list1): # recursive function to find the smallest number
    if itr == len(list1):
        print("The smallest number in the list is", ele)
        return
    if list1[itr] < ele: #check the current element less than minimum or not
        ele = list1[itr]
    Findsmall(itr+1,ele,list1) # recursive function call
    return

#driver code
lis = [5,7,2,8,9]
ele = lis[0]
Findsmall(0,ele,lis)

####################################################################################################

#245

'''
Using numpy module
'''

#importing module
import numpy as np

#initializing list
lis = [5,7,2,8,9]

#finding minimum value
minimum = np.min(lis)

#printing output
print("The smallest number in the list is", minimum)

################################################################################################

#246

'''
Finding the minimum element in a list that consists of duplicate elements
'''

#defining the list
arr = [5,2,3,2,5,4,7,9,7,10,15,68]

#converting the list into set
set_arr = set(arr)

#Now using the min function to get the minimum value from the set
print(min(set_arr))

#######################################################################################################

#247

'''
Find all the positions of the minimum value in a list that consists of duplicate elements
'''

arr = [2,6,8,4,9,7,52,3,6,2,4,5,6,8,2]

min_val = min(arr)   #finding the minimum value

values = {}

# print item with position
for pos,val in enumerate(arr):
    if val==min_val:
        values.update({pos:val})  # pos - Index of the smallest element
                                  # val - The value of the smallest element

# get all min values
print(values)

#############################################################################################################




























































































































































































=======
#235

'''
Python program to find smallest number in a list
'''

#Sorting the list to find smallest number in a list in ascending order

list1 = [10,20,4,45,99]

#sorting the list
list1.sort()

#printing the first element
print("Smallest element is: ",list1[0])

###########################################################################################################

#236

'''
In descending order
'''

list1 = [10,20,4,45,99]

#sorting the list
list1.sort(reverse=True)

#printing the first element
print("Smallest element is:", list1[-1])

#############################################################################################################

#237

'''
Using min() method to find smallest number in a list
'''

list1 = [10,20,1,45,99]

#printing the minimum element
print("Smallest element is:", min(list1))

#######################################################################################################

#238

'''
Find minimum list element for a user defined list
'''

#creating empty list
list1 = []

#asking number of elements to put in list
num = int(input("Enter number of elements in list:"))

#iterating till num tp a[[end elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

#print minimum element
print("Smallest element is: ", min(list1))

################################################################################################################

#239

'''
Find the smallest element element in list comparing every element
'''

l = [int(l) for l in input("List:").split(",")]
print("The list is", l)

#Assign first element as a minimum
min1 = l[0]

for i in range(len(l)):
    # if the other element is min than first element
    if l[i] < min1:
        min1 = l[i] #it will change

print("The smallest element in the list is", min1)

##########################################################################################################

#240

'''
Using the lambda function to find smallest number in a list
'''

lst = [20,10,20,1,100]
print(min(lst, key=lambda value: int(value)))

###########################################################################################################

#241

'''
Using the enumerate function to find smallest number in a list
'''

lst = [20,10,20,1,100]
a,i = min((a,i) for (i,a) in enumerate(lst))
print(a)

############################################################################################################

#242

'''
Using reduce function to find the smallest number in a list
'''

from functools import reduce
lst = [20,10,20,15,100]
print(reduce(min,lst))

############################################################################################################

#243

'''
Using heap
'''

import heapq

def find_smallest(numbers):
    # build a min heap using the elements in the list
    heap = [(x,x) for x in numbers]
    heapq.heapify(heap)

    #return the root element (smallest element)
    _, smallest = heapq.heappop(heap)

    return smallest

#test the function
numbers = [10,20,4,45,99]
print(find_smallest(numbers))

############################################################################################################

#244

'''
Using recursion
'''

def Findsmall(itr,ele,list1): # recursive function to find the smallest number
    if itr == len(list1):
        print("The smallest number in the list is", ele)
        return
    if list1[itr] < ele: #check the current element less than minimum or not
        ele = list1[itr]
    Findsmall(itr+1,ele,list1) # recursive function call
    return

#driver code
lis = [5,7,2,8,9]
ele = lis[0]
Findsmall(0,ele,lis)

####################################################################################################

#245

'''
Using numpy module
'''

#importing module
import numpy as np

#initializing list
lis = [5,7,2,8,9]

#finding minimum value
minimum = np.min(lis)

#printing output
print("The smallest number in the list is", minimum)

################################################################################################

#246

'''
Finding the minimum element in a list that consists of duplicate elements
'''

#defining the list
arr = [5,2,3,2,5,4,7,9,7,10,15,68]

#converting the list into set
set_arr = set(arr)

#Now using the min function to get the minimum value from the set
print(min(set_arr))

#######################################################################################################

#247

'''
Find all the positions of the minimum value in a list that consists of duplicate elements
'''

arr = [2,6,8,4,9,7,52,3,6,2,4,5,6,8,2]

min_val = min(arr)   #finding the minimum value

values = {}

# print item with position
for pos,val in enumerate(arr):
    if val==min_val:
        values.update({pos:val})  # pos - Index of the smallest element
                                  # val - The value of the smallest element

# get all min values
print(values)

#############################################################################################################




























































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
