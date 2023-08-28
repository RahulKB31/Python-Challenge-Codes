<<<<<<< HEAD
#160

'''
Python program for reversal algorithm for array rotation
'''

def reverseArray(arr, d):
    c = (arr[d:]) + (arr[:d])
    return c

arr = [1,2,3,4,5,6,7]
d = 2
print(reverseArray(arr, d))

###########################################################################################################

#161

'''
Python program for reversal algorithm for array rotation
'''

# Function to reverse arr[] from index start to end
def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d-1)
    rverseArray(arr, d, n-1)
    rverseArray(arr, 0, n-1)
    # Function to print an arrray

def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])

# Driver function
arr = [1,2,3,4,5,6,7]
leftRotate(arr, 2)
printArray(arr)

############################################################################################################






























































































































































=======
#160

'''
Python program for reversal algorithm for array rotation
'''

def reverseArray(arr, d):
    c = (arr[d:]) + (arr[:d])
    return c

arr = [1,2,3,4,5,6,7]
d = 2
print(reverseArray(arr, d))

###########################################################################################################

#161

'''
Python program for reversal algorithm for array rotation
'''

# Function to reverse arr[] from index start to end
def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d-1)
    rverseArray(arr, d, n-1)
    rverseArray(arr, 0, n-1)
    # Function to print an arrray

def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])

# Driver function
arr = [1,2,3,4,5,6,7]
leftRotate(arr, 2)
printArray(arr)

############################################################################################################






























































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
