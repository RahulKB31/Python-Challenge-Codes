#860

'''
Python program for binary insertion sort
'''

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    if start > end:
        return start

    mid = (start+end)/2
    if arr[mid] < val:
        return binary_search(arr,val,mid+1,end)
    elif arr[mid] > val:
        return binary_search(arr,val,start,mid-1)
    else:
        return mid

def insertion_sort(arr):
    for i in range(1,len(arr)):
        val = arr[i]
        j = binary_search(arr, val,0,i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

print("Sorted array:")
print(insertion_sort([37,23,4,23,466,76,56,345,76,5,45,33]))

##################################################################################################################

#861

'''
Implement using bisect module
'''

import bisect
def binary_search(arr,val,start,end):
    idx = bisect.bisect_left(arr[start:end+1],val)
    return start + idx

def insertion_sort(arr):
    for i in range(1,len(arr)):
        val = arr[i]
        j = binary_search(arr,val,0,i-1)
        arr = arr[:j] + [val] + arr[j:] + arr[i+1:]
    return arr

print("Sorted array:")
print(insertion_sort([37,23,4,23,466,76,56,345,76,5,45,33]))

##################################################################################################################






















