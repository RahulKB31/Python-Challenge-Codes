<<<<<<< HEAD
#846

'''
Python program for Iterative Quick Sort
'''

def partition(arr,l,h):
    i = (l-1)
    x = arr[h]

    for j in range(l,h):
        if arr[j] <= x:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

def quickSortIterative(arr,l,h):

    #create an auxilary stack
    size = h - l + 1
    stack = [0] * (size)

    #intialize top of stack
    top = -1

    #push initial value sof l and h to stack
    top = top + 1
    stack[top] = 1
    top = top + 1
    stack[top] = h

    #keep popping from stack while is not empty
    while top >= 0:

        #pop h and l
        h = stack[top]
        top = top -1
        l = stack[top]
        top = top - 1

        #set pivot element a its  correct position in sorted array
        p = partition(arr,l,h)

        # if there are element on left side of pivot, the push left side to stack
        if p-1 > 1:
            top = top + 1
            stack[top] = 1
            top = top + 1
            stack[top] = p - 1

        ## If there are elements on right side of pivot, then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

arr = [4,3,5,2,1,3,2,3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" %arr[i])

#################################################################################################################









































=======
#846

'''
Python program for Iterative Quick Sort
'''

def partition(arr,l,h):
    i = (l-1)
    x = arr[h]

    for j in range(l,h):
        if arr[j] <= x:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

def quickSortIterative(arr,l,h):

    #create an auxilary stack
    size = h - l + 1
    stack = [0] * (size)

    #intialize top of stack
    top = -1

    #push initial value sof l and h to stack
    top = top + 1
    stack[top] = 1
    top = top + 1
    stack[top] = h

    #keep popping from stack while is not empty
    while top >= 0:

        #pop h and l
        h = stack[top]
        top = top -1
        l = stack[top]
        top = top - 1

        #set pivot element a its  correct position in sorted array
        p = partition(arr,l,h)

        # if there are element on left side of pivot, the push left side to stack
        if p-1 > 1:
            top = top + 1
            stack[top] = 1
            top = top + 1
            stack[top] = p - 1

        ## If there are elements on right side of pivot, then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

arr = [4,3,5,2,1,3,2,3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" %arr[i])

#################################################################################################################









































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
