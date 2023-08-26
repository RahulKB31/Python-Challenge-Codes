#850

'''
Python Program for merge sort
'''

def merge(arr,l,m,r):
    n1 = m-1+1
    n2 = r - m

    #create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    #copy data to temp arrays L[] and R[]
    for i in range(0,n1):
        L[i] = arr[l+i]

    for j in range(0,n2):
        R[j] = arr[m+1+j]

    #merge temp array back into arr
    i = 0
    j = 0
    k = 1

    while i<n1 and j<n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    #Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copy the remaining elements of R[] if there are any
    while j<n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the subarray of arr to be sorted
def mergeSort(arr,l,r):
    if l>r:
        m = l+(r-l)//2

        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)

arr = [12,11,13,5,6,7]
n = len(arr)
print('Given array is')
for i in range(n):
    print("%d" %arr[i], end=" ")

mergeSort(arr,0,n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" %arr[i], end= " ")

#################################################################################################################






































































