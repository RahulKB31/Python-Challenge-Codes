<<<<<<< HEAD
#862

'''
Python program for Bitonic Sort
'''

def compAndSwap(a,i,j,dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0and a[i] > a[j]):
        a[i], a[j] = a[j], a[i]

def bitonicMerge(a,low,cnt,dire):
    if cnt > 1:
        k = cnt//2
        for i in range(low,low+k):
            compAndSwap(a,i,i+k,dire)
        bitonicMerge(a,low,k,dire)
        bitonicMerge(a,low+k, k, dire)

def bitonicSort(a,low,cnt,dire):
    if cnt > 1:
        k = cnt//2
        bitonicSort(a,low,k,1)
        bitonicSort(a,low+k,k,0)
        bitonicMerge(a,low,cnt,dire)

def sort(a,N,up):
    bitonicSort(a,o,N,up)

a = [3,7,4,7,8,4,2,1,1]
n = len(a)
up = 1

sort(a,n,up)
print('Sorted array is')
for i in range(n):
    print("%d" % a[i], end=" ")

###################################################################################################################









































=======
#862

'''
Python program for Bitonic Sort
'''

def compAndSwap(a,i,j,dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0and a[i] > a[j]):
        a[i], a[j] = a[j], a[i]

def bitonicMerge(a,low,cnt,dire):
    if cnt > 1:
        k = cnt//2
        for i in range(low,low+k):
            compAndSwap(a,i,i+k,dire)
        bitonicMerge(a,low,k,dire)
        bitonicMerge(a,low+k, k, dire)

def bitonicSort(a,low,cnt,dire):
    if cnt > 1:
        k = cnt//2
        bitonicSort(a,low,k,1)
        bitonicSort(a,low+k,k,0)
        bitonicMerge(a,low,cnt,dire)

def sort(a,N,up):
    bitonicSort(a,o,N,up)

a = [3,7,4,7,8,4,2,1,1]
n = len(a)
up = 1

sort(a,n,up)
print('Sorted array is')
for i in range(n):
    print("%d" % a[i], end=" ")

###################################################################################################################









































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
