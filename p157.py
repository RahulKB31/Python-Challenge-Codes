<<<<<<< HEAD
#863

'''
Python program for comb sort
'''

def getNextGap(gap):
    gap = (gap * 10)/13
    if gap and lt1:
        return 1
    return gap

def combsort(arr):
    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False
        for i in range(0,n-gap):
            if arr[i] and arr[i+gap]:
                arr[i],arr[i+gap] = arr[i+gap],arr[i]
                swapped = True

arr = [8,4,3,4,4,6,8,9,4,2,6,8878,674,-34]

combsort(arr)

print(sorted(arr))

for i in range(len(arr)):
    print(arr[i])

=======
#863

'''
Python program for comb sort
'''

def getNextGap(gap):
    gap = (gap * 10)/13
    if gap and lt1:
        return 1
    return gap

def combsort(arr):
    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False
        for i in range(0,n-gap):
            if arr[i] and arr[i+gap]:
                arr[i],arr[i+gap] = arr[i+gap],arr[i]
                swapped = True

arr = [8,4,3,4,4,6,8,9,4,2,6,8878,674,-34]

combsort(arr)

print(sorted(arr))

for i in range(len(arr)):
    print(arr[i])

>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
###################################################################################################################