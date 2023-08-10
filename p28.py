#162

'''
Python program to split the array and add the first part to the end
'''

def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]

        arr[n-1] = x

# main
arr = [12,10, 5, 6, 52, 36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
    print(arr[i], end = ' ')

############################################################################################################

#163

def splitArr(a, n, k):
    b = a[:k]
    return (a[k::] + b[::])

arr = [12,10, 5, 6,52, 36]
n = len(arr)
position = 2
arr = splitArr(arr, n, position)
for i in range(0, n):
    print(arr[i], end = ' ')

############################################################################################################

#164

'''
Using slicing and extend() method
'''

arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
x = arr[:position]
y = arr[position:]
y.extend(x)
for i in y:
    print(i, end = " ")

##########################################################################################################

#165

'''
Using list comprehension and modulo
'''

def split_and_add(arr, n):
    return [arr[(i + n) % len(arr)] for i in range(len(arr))]

arr = [12,10, 5, 6,52, 36]
n = 2
result = split_and_add(arr, n)
print(*result)

###########################################################################################################

#166

'''
Using deque module from the collection
'''

from collections import deque

def splitArr(a, n, k):
    q = deque(a)
    q.rotate(-k)
    return list(q)

arr = [12,10, 5, 6,52, 36]
n = len(arr)
position = 2
arr = splitArr(arr, n, position)
for i in range(0, n):
    print(arr[i], end = ' ')

#############################################################################################################










































































































































