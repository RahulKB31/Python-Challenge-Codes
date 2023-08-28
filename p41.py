<<<<<<< HEAD
#257

'''
Python program to find second largest number in a list
'''

# Sorting is an easier but less optimal method. Given below is an O(n) algorithm to do the same

# list of numbers - length of list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2,n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and mx != list1[i]:
        secondmax = list1[i]
    elif mx == secondmax and secondmax != list1[i]:
        secondmax = list1[i]

print("Second highest number is:",str(secondmax))

##########################################################################################################

#258

'''
Sort the list in ascending order and print the second last element in the list
'''

#List of numbers
list1 = [10,20,20,4,45,45,99,99]

#Removing duplicates from the list
list2 = list(set(list1))

#sorting the list
list2.sort()

#Printing the second last element
print("Second largest element is:", list2[-2])

##########################################################################################################

#259

'''
By removing the max element from the list
'''

#list of numbers
list1 = [10,20,4,45,99]

#new_list is a set of list1
new_list = set(list1)

#Removing the largest element from temp list
new_list.remove(max(new_list))

#Elements in original list are not changed
print(max(new_list))

##########################################################################################################

#260

'''
Find the max list element on inputs provided by the user
'''

#creating list of integer type
list1 = [10,20,4,45,99]

#print second maximum element using sorted() method
print("Second largest element is:", sorted(list1)[-2])

##################################################################################################

#261

'''
Traverse once to find the largest and then once again to find the second largest
'''

def findLargest(arr):
    secondLargest = 0
    largest = min(arr)

    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        else:
            secondLargest = max(secondLargest, arr[i])

    # Returning second largest element
    return secondLargest

#calling above method over this array set
print(findLargest([10,20,4,45,99]))

##########################################################################################################

#262

'''
Using list comprehension
'''

def secondmax(arr):
    sublist = [x for x in arr if x < max(arr)]
    return max(sublist)

if __name__ == "__main__":
    arr = [10,20,4,45,99]
    print(secondmax(arr))

#############################################################################################################

#263

'''
Using lambda function
'''

lst = [10,20,4,45,99]
maximum1 = max(lst)
maximum2 = max(lst, key=lambda x: min(lst)-1 if (x == maximum1) else x)
print(maximum2)

################################################################################################################

#264

'''
Using enumerate function
'''

lst = [10,20,4,45,99]
m = max(lst)
x = [a for i,a in enumerate(lst) if a<m]
print(max(x))

##################################################################################################################

#265

'''
Using heap
'''

import heapq

def find_second_largest(numbers):
    #build a max heap using the elements in the list
    heap = [(-x,x) for x in numbers]
    heapq.heapify(heap)

    #remove the root element (largest element)
    heapq.heappop(heap)

    #the new root element is the second largest element
    _, second_largest = heapq.heappop(heap)

    return second_largest

#test the function
numbers = [10,20,4,45,99]
print(find_second_largest(numbers))

############################################################################################################

#266

'''
Using numpy.argsort() function
'''

import numpy as np

def find_second_largest(arr):
    #creating numpy array
    np_arr = np.array(arr)

    #getting sorted indices
    sorted_indices = np.argsort(np_arr)

    #finding the second last index from sorted indices
    second_last_index = sorted_indices[-2]

    # returning the element at the second last index from original array
    return np_arr[second_last_index]

#exampple usage
arr = [10,20,4,45,99]
print(find_second_largest(arr))

#########################################################################################################

#277

'''
Using sorted()
'''

list = [2,1,8,7,3,0]

#printing the original list
print('The given list is;', list)

#using sorted()
list1 = []
list1 = sorted(list,reverse=True)

#list after sorting
print('The sorted list is:', list1)

#printing the second largest number in the list
print("The econd largest number in the given list is:",list1[1])

##############################################################################################################













































































































































































































































=======
#257

'''
Python program to find second largest number in a list
'''

# Sorting is an easier but less optimal method. Given below is an O(n) algorithm to do the same

# list of numbers - length of list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2,n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and mx != list1[i]:
        secondmax = list1[i]
    elif mx == secondmax and secondmax != list1[i]:
        secondmax = list1[i]

print("Second highest number is:",str(secondmax))

##########################################################################################################

#258

'''
Sort the list in ascending order and print the second last element in the list
'''

#List of numbers
list1 = [10,20,20,4,45,45,99,99]

#Removing duplicates from the list
list2 = list(set(list1))

#sorting the list
list2.sort()

#Printing the second last element
print("Second largest element is:", list2[-2])

##########################################################################################################

#259

'''
By removing the max element from the list
'''

#list of numbers
list1 = [10,20,4,45,99]

#new_list is a set of list1
new_list = set(list1)

#Removing the largest element from temp list
new_list.remove(max(new_list))

#Elements in original list are not changed
print(max(new_list))

##########################################################################################################

#260

'''
Find the max list element on inputs provided by the user
'''

#creating list of integer type
list1 = [10,20,4,45,99]

#print second maximum element using sorted() method
print("Second largest element is:", sorted(list1)[-2])

##################################################################################################

#261

'''
Traverse once to find the largest and then once again to find the second largest
'''

def findLargest(arr):
    secondLargest = 0
    largest = min(arr)

    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        else:
            secondLargest = max(secondLargest, arr[i])

    # Returning second largest element
    return secondLargest

#calling above method over this array set
print(findLargest([10,20,4,45,99]))

##########################################################################################################

#262

'''
Using list comprehension
'''

def secondmax(arr):
    sublist = [x for x in arr if x < max(arr)]
    return max(sublist)

if __name__ == "__main__":
    arr = [10,20,4,45,99]
    print(secondmax(arr))

#############################################################################################################

#263

'''
Using lambda function
'''

lst = [10,20,4,45,99]
maximum1 = max(lst)
maximum2 = max(lst, key=lambda x: min(lst)-1 if (x == maximum1) else x)
print(maximum2)

################################################################################################################

#264

'''
Using enumerate function
'''

lst = [10,20,4,45,99]
m = max(lst)
x = [a for i,a in enumerate(lst) if a<m]
print(max(x))

##################################################################################################################

#265

'''
Using heap
'''

import heapq

def find_second_largest(numbers):
    #build a max heap using the elements in the list
    heap = [(-x,x) for x in numbers]
    heapq.heapify(heap)

    #remove the root element (largest element)
    heapq.heappop(heap)

    #the new root element is the second largest element
    _, second_largest = heapq.heappop(heap)

    return second_largest

#test the function
numbers = [10,20,4,45,99]
print(find_second_largest(numbers))

############################################################################################################

#266

'''
Using numpy.argsort() function
'''

import numpy as np

def find_second_largest(arr):
    #creating numpy array
    np_arr = np.array(arr)

    #getting sorted indices
    sorted_indices = np.argsort(np_arr)

    #finding the second last index from sorted indices
    second_last_index = sorted_indices[-2]

    # returning the element at the second last index from original array
    return np_arr[second_last_index]

#exampple usage
arr = [10,20,4,45,99]
print(find_second_largest(arr))

#########################################################################################################

#277

'''
Using sorted()
'''

list = [2,1,8,7,3,0]

#printing the original list
print('The given list is;', list)

#using sorted()
list1 = []
list1 = sorted(list,reverse=True)

#list after sorting
print('The sorted list is:', list1)

#printing the second largest number in the list
print("The econd largest number in the given list is:",list1[1])

##############################################################################################################













































































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
