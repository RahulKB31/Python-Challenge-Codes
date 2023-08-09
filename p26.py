#155

'''
Python program for array rotation
'''

# Function reverse the given array by swapping first and last numbers

def reverse(start, end, arr):

    # No of iterartions needed for reversing the list
    no_of_reverse = end - start + 1

    # by incrementing count value swapping of first and last elements is done
    count = 0
    while ((no_of_reverse) // 2 != count):
        arr[start + count], arr[end - count] = arr[end - count], arr[start + count]
        count += 1
    return arr

# Function takes array, length of array and no of rotations as input

def left_rotate_array(arr, size, d):

    # Reverse the entire list
    start = 0
    end = size - 1
    arr = reverse(start, end, arr)

    # Divide array into two sub-array based on no of rotations.
    # Divide first sub-array
    # Reverse the first sub-array
    start = 0
    end = size - d - 1
    arr = reverse(start,end,arr)

    # Divide second sub array
    # Reverse the second sub arry
    start = size - d
    end = size - 1
    arr = reverse(start, end, arr)
    return arr

arr = [1,2,3,4,5,6,7,8]
size = 8
d = 1
print("Original survey:", arr)

# Finding all the symmetrc rotation number
if (d <= size):
    print("Rotated array:", left_rotate_array(arr,size,d))

else:
    d = d % size
    print("Rotated array:", left_rotate_array(arr,size,d))

#############################################################################################################

#156

'''
Python program for array rotation using temp array
'''

# function to rotate array by d elements using temp array

def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i += 1

    i=0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[:i] + temp
    return arr

arr = [1,2,3,4,5,6,7,8,9]
print("Array after left rotation is", end = ' ')
print(rotateArray(arr, len(arr), 2))

#########################################################################################################

#157

'''
Python program for array rotation using rotate one by one
'''

# Function to left rotate arr[] of size n by d*/
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

# Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

# Utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print("%d"% arr[i], end= " ")

arr = [1,2,3,4,5,6,7]
leftRotate(arr, 2, 7)
printArray(arr, 7)

#######################################################################################################

#158

'''
Python program for array rotation using 4 juggling algorithm
'''

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d, n):
    for i in range(gcd(d, n)):

        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k -n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

# Utility function to print an array
def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end = " ")

# Function to get gcd of a and b
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

arr = [1,2,3,4,5,6,7]
leftRotate(arr, 2, 7)
printArray(arr, 7)

#####################################################################################################

#159

'''
Using list slicing
'''

def rotateList(arr, d, n):
    arr[:] = arr[d:n] + arr[0:d]
    return arr

arr = [1,2,3,4,5,6]
print(arr)
print("Rotated list is")
print(rotateList(arr, 2, len(arr)))

##########################################################################################################
































































































































































































































































































































