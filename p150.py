#852

'''
Python program for heap sort
'''

def heapify(arr,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    #see if left child of root exists and is greater than root
    if l<n and arr[i] < arr[l]:
        largest = l

    #see if right child of root exists and is greater than root
    if r<n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr,n,largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2-1, -1,-1):
        heapify(arr,n,i)

        for i in range(n-1,0,-1):
            (arr[i],arr[0]) = (arr[0], arr[i])
            heapify(arr,i,0)

arr = [12,11,13,5,6,7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print(arr[i])

##############################################################################################################

#853

import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr))
    return result

arr = [60,20,40,70,30,10]
print("Input Array: ", arr)
print('Sorted Array: ', heap_sort(arr))

################################################################################################################














































































































































