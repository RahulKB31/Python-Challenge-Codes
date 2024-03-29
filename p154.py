<<<<<<< HEAD
#859

'''
Python program for Radix Sort
'''

def countingSort(arr, expl):
    n = len(arr)

    output = [0] * (n)

    count = [0] * (10)

    for i in range (0,n):
        index = (arr[i]/expl)
        count[int((index)%10)] += 1

    for i in range(0,n):
        index = (arr[i]/expl)
        count[int((index)%10)] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n - 1
    while i>=0:
        index = arr([i]/expl)
        output[count[int((index)%10)] -1] = arr[i]
        count[int((index)%10)] -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        countingSort(arr,exp)
        exp *= 10

arr = [170,45,75,90,802,24,2,66]
radixSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")

##################################################################################################################


=======
#859

'''
Python program for Radix Sort
'''

def countingSort(arr, expl):
    n = len(arr)

    output = [0] * (n)

    count = [0] * (10)

    for i in range (0,n):
        index = (arr[i]/expl)
        count[int((index)%10)] += 1

    for i in range(0,n):
        index = (arr[i]/expl)
        count[int((index)%10)] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n - 1
    while i>=0:
        index = arr([i]/expl)
        output[count[int((index)%10)] -1] = arr[i]
        count[int((index)%10)] -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        countingSort(arr,exp)
        exp *= 10

arr = [170,45,75,90,802,24,2,66]
radixSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")

##################################################################################################################


>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
