#33

'''
Write a function that takes a 1D NumPy array as an argument and returns an array with the same elements,
but in the reverse order.
'''

import numpy as np

def ex1Fun(arr):
    # make a new array with the same length as arr
    # ii doesn't matter what the contents are, so initiate with 0s
    arr2 = np.array([0] * len(arr))
    # copy the elements one by one
    for i in range(len(arr)):
        arr2[i] = arr[-(i+1)]
    return arr2

a1 = np.array(range(20))
a1[5] = 99
a1[12] = 42
print("Original")
print(a1)
a2 = ex1Fun(a1)
print("reversed")
print(a2)

###################################################################################################

#34

'''
Write a function that takes two 1D NumPy arrays as arguments and prints all elements that occur in both
arrays
'''

import numpy as np

def ex2Fun(arr1, arr2):
    # avoid duplicate outputs by keeping a list of what's already been output
    outputs = []
    for n in arr1:
        if n not in outputs:
            for m in arr2:
                if n == m:
                    print(n)
                    outputs.append(n)
                    break

a1 = np.array([1,2,3,4,11,13,3,43,434,32])
a2 = np.array(range(5,15))
ex2Fun(a1,a2)

###########################################################################################################

#35

'''
Write a function that takes a 2D NumPy array as an argument and prints all elements that occur in both of
the first two rows of the array. The function should raise an exception if the array contains only one row.
'''

import numpy as np

#can make use of the function from ex2
def ex2Fun(arr1, arr2):
    # avoid duplicate outputs by keeping a list of whats already been output
    outputs = []
    for n in arr1:
        if n not in outputs:
            for m in arr2:
                if n==m:
                    print(n)
                    outputs.append(n)
                    break

def ex3Fun(arr2D):
    if len(arr2D) < 2:
        raise Exception
    ex2Fun(arr2D[0], arr2D[1])

a2D = np.array([1,2,3,4,5,7,8,9,0,11,23,34,34,45,1,2,34,35,3])
bad2D = np.array([[1,2,3]])  # has only one row

try:
    print("Testing with array with 2 rows")
    ex3Fun(a2D)
    print("Testing with array with 1 row")
    ex3Fun(bad2D)
except:
    print("Function raised exception")

##############################################################################################

#36

'''
Write a NumPy program to create a structured array using the student
data on the previous slide.
Sort the array by height.
Output the contents of the original array and the sorted array
Sample Output:
Original array:
[('James', 5, 48.5) (’Neil', 6, 52.5) ('Paul', 5, 42.1) (‘Pat', 5, 40.11)]
Sort by height
[(‘Pat', 5, 40.11) ('Paul', 5, 42.1) 'James', 5, 48.5) (’Neil', 6, 52.5 )]
Note that this output does not use the same data as the previous
example.
'''

import numpy as np
studType = [('name','S15'),('class',int),('height', float)]
students = [('James', 5, 48.5), ('Neil', 6, 52.5), ('Pau;ine', 5, 42.10)]

arr = np.array(students, dtype = studType)
newarr = np.sort(arr, order = 'height')

print("Original")
print(arr)
print("Sorted")
print(newarr)

#################################################################################################

#37

'''
Write a NumPy program to create a structured array from given student
names, heights, class and their data types.
Sort by class, then height if class are equal.
'''

import numpy as np
studType = [('name','S15'),('class',int),('height', float)]
students = [('James', 5, 48.5), ('Neil', 6, 52.5), ('Pau;ine', 5, 42.10)]

arr = np.array(students, dtype = studType)
newarr = np.sort(arr, order=['class','height'])

print("Original")
print(arr)
print("Sorted")
print(newarr)

#########################################################################################################













