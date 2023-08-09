#149

'''
Python program to find largest element in an array
'''

# Find largest element in an array using Native Approach

def largest(arr, n):

    # Initialize maximum element
    max = arr[0]

    # traverse array elements from second and compare every element with current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

# Driver code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array", Ans)

#################################################################################################################

#150

'''
Find largest element in an array using built in function max()
'''

def largest(arr, n):
    ans = max(arr)
    return ans

# Driver code
if __name__ == "__main__":
    arr = [10, 324, 45, 90, 9808]
    n = len(arr)
    print('Largest in given array', largest(arr,n))

####################################################################################################################

#151

'''
Find largest element in an array using sort() function
'''

def largest(arr, n):
    # sort the array
    arr.sort()

    # the last element of the array is the largest element
    return arr[n-1]

arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array", Ans)

#######################################################################################################

#152

'''
Find largest element in an array using reduce() function
'''

from functools import reduce

def largest(arr):

    # sort the array
    ans = reduce(max, arr)

    return ans

# Driver code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr)
print("Largest in given array", Ans)

############################################################################################################

#153

'''
Find largest element in an array using operator.gt()
'''

import operator

# Initializing the list
arr = [2, 1, 7, 3, 0]
max = 0

# printing the original list
print("The given array is:", arr)

# checking for large element
for i in arr:
    if operator.gt(i, max):
        max = i

print("The biggest number in the given array is:",max)

###########################################################################################################

#154

'''
Find largest element with Python lambda
'''

array = [10, 5, 20, 8, 15]

largest_element = max(array, key = lambda x: x)
print("Largest element in the array:", largest_element)

###############################################################################################################

































