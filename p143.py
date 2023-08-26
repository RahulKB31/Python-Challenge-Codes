#842

'''
Python program for recursive Insertion Sort
'''

def insertionSortRecursive(arr, n):
    if n <= 1:
        return

    insertionSortRecursive(arr, n-1)

    last = arr[n-1]
    j = n -2

    while (j >= 0 and arr[j] > last):
        arr[j+1] = arr[j]
        j = j - 1
    arr[j + 1] = last

if __name__ == "__main__":
    A = [-7,11,6,0,-3,5,10,2]
    n = len(A)
    insertionSortRecursive(A,n)
    print(A)

###############################################################################################################

#843

'''
Using a divide and conquer
'''

def insertion_sort_recursive(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = insertion_sort_recursive(arr[:mid])

    right_half = insertion_sort_recursive(arr[mid:])

    i,j = 0,0
    sorted_arr = []
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1

        else:
            sorted_arr.append(right_half[j])
            j += 1

    sorted_arr += left_half[i:]
    sorted_arr += right_half[j:]

    return sorted_arr

arr = [5,2,4,6,1,3]
sorted_arr = insertion_sort_recursive(arr)
print(sorted_arr)

#############################################################################################################


















































































































