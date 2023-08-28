<<<<<<< HEAD
#170

'''
Python program to check if given array Monotonic
'''

# using extend() and sort()

def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if (x==A or y==A):
        return True
    return False

A = [6,5,4,4]
print(isMonotonic(A))

###########################################################################################################

#171

def isMonotonic(A):
    return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i+1] for i in range(len(A) - 1)))


A = [6,5,4,4]
print(isMonotonic(A))

###########################################################################################################

#172

'''
By checking length of the array
'''

def isMonotonic(arr):
    if len(arr) <= 2:
        return True
    direction = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if direction == 0:
            direction = arr[i] - arr[i-1]
            continue
        if (direction > 0 and arr[i] < arr[i-1]) or (direction < 0 and arr[i] > arr[i-1]):
            return False
    return True

arr1 = [1,2,3,4,5]
arr2 = [5,4,3,2,1]
arr3 = [1,2,2,3,4]
arr4 = [1,2,3,4,5,4]

print(isMonotonic(arr1))
print(isMonotonic(arr2))
print(isMonotonic(arr3))
print(isMonotonic(arr4))

##############################################################################################################

=======
#170

'''
Python program to check if given array Monotonic
'''

# using extend() and sort()

def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if (x==A or y==A):
        return True
    return False

A = [6,5,4,4]
print(isMonotonic(A))

###########################################################################################################

#171

def isMonotonic(A):
    return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i+1] for i in range(len(A) - 1)))


A = [6,5,4,4]
print(isMonotonic(A))

###########################################################################################################

#172

'''
By checking length of the array
'''

def isMonotonic(arr):
    if len(arr) <= 2:
        return True
    direction = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if direction == 0:
            direction = arr[i] - arr[i-1]
            continue
        if (direction > 0 and arr[i] < arr[i-1]) or (direction < 0 and arr[i] > arr[i-1]):
            return False
    return True

arr1 = [1,2,3,4,5]
arr2 = [5,4,3,2,1]
arr3 = [1,2,2,3,4]
arr4 = [1,2,3,4,5,4]

print(isMonotonic(arr1))
print(isMonotonic(arr2))
print(isMonotonic(arr3))
print(isMonotonic(arr4))

##############################################################################################################

>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
