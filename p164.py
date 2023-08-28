<<<<<<< HEAD
#872

'''
Python program for stooge sort
'''

def stoogesort(arr,l,h):
    if l >= h:
        return

    if arr[l]>arr[h]:
        t = arr[l]

    arr[l] = arr[h]
    arr[h] = test

    if  h-l+1 >2:
        t = (int)((h-l+1)/3)

        stoogesort(arr,l,(h-t))
        stoogesort(arr, l+t,(h))
        stoogesort(arr,l,(h-t))

arr = [2,4,5,3,1]
n = len(arr)

stoogesort(arr,0,n-1)
for i in range(0,n):
    print(arr[i],end = ' ')

=======
#872

'''
Python program for stooge sort
'''

def stoogesort(arr,l,h):
    if l >= h:
        return

    if arr[l]>arr[h]:
        t = arr[l]

    arr[l] = arr[h]
    arr[h] = t

    if  h-l+1 >2:
        t = (int)((h-l+1)/3)

        stoogesort(arr,l,(h-t))
        stoogesort(arr, l+t,(h))
        stoogesort(arr,l,(h-t))

arr = [2,4,5,3,1]
n = len(arr)

stoogesort(arr,0,n-1)
for i in range(0,n):
    print(arr[i],end = ' ')

>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
##################################################################################################################