<<<<<<< HEAD
#844

'''
Pythn proram for quicksort
'''

def partition(array, low, high):
    pivot = array(high)

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i+1], array[high]) = (array[high], array[i+1])

    return i + 1

def quickSort(array, low, high):
    if low < high:

        pi = partition(array,low,high)
        quickSort(array, low, pi-1)

        quickSort(array, pi+1,high)

data = [1,7,4,1,10,9,-2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0 , size-1)

print("Sorted Array in ascending Order")
print(data)

##############################################################################################################

#845

'''
QuickSort using list comprehension
'''

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

arr = [1,7,4,1,10,9,-2]
sorted_arr = quicksort(arr)
print("Sorted Array in ascending order:")
print(sorted_arr)

################################################################################################################




































































































=======
#844

'''
Pythn proram for quicksort
'''

def partition(array, low, high):
    pivot = array(high)

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i+1], array[high]) = (array[high], array[i+1])

    return i + 1

def quickSort(array, low, high):
    if low < high:

        pi = partition(array,low,high)
        quickSort(array, low, pi-1)

        quickSort(array, pi+1,high)

data = [1,7,4,1,10,9,-2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0 , size-1)

print("Sorted Array in ascending Order")
print(data)

##############################################################################################################

#845

'''
QuickSort using list comprehension
'''

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

arr = [1,7,4,1,10,9,-2]
sorted_arr = quicksort(arr)
print("Sorted Array in ascending order:")
print(sorted_arr)

################################################################################################################




































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
