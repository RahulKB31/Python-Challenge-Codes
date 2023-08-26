#867

'''
Python Program for odd-Even sort/Brick Sort
'''

def oddEvenSort(arr,n):
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1,2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
                isSorted = 0

        for i in range(0,n-1,2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0

        return

arr = [34,3,10,-2]
n = len(arr)

oddEvenSort(arr,n)
for i in range(0,n):
    print(arr[i], end=" ")

#################################################################################################################

#868

'''
Using the sorted() function
'''

def oddEvenSort(arr,n):
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        arr[1::2], arr[2::2] = sorted(arr[1::2]), sorted(arr[2::2])

        for i in range(0,n-1,2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
                isSorted = 0

    return

arr = [34,3,10,-2]
n = len(arr)

oddEvenSort(arr,n)
for i in range(0,n):
    print(arr[i], end=" ")

##################################################################################################################
































































































