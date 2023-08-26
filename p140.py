#835

'''
Python program for Binary search (Recursive and Iterative)
'''

def binaary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binaary_search(arr, low, mid-1, x)

        else:
            return binaary_search(arr, mid+1, high, x)

    else:
        return -1

arr = [2,3,4,10,40]
x = 10

result = binaary_search(arr, 0 , len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

###############################################################################################################

#836

def binary_search(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

arr = [2,3,4,10,40]
x = 10

result = binary_search(arr,x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

###############################################################################################################

#837

'''
Using the built in bisect module in python
'''

import bisect

def binary_search_bisect(arr, x):
    i = bisect.bisect_left(arr,x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1

arr = [2,3,4,10,40]
x = 10

result = binary_search_bisect(arr,x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

###############################################################################################################





























































































































































































