<<<<<<< HEAD
#851

'''
Python program for iterative merge sort
'''

def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i,j = 0,0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        if i == len(left) or j==len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

def mergesort(list):
    if len(list) < 2:
        return list

    middle = len(list)/2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)

seq = [12,11,13,5,6,7]
print("GIven array is")
print(seq)
print("\n")
print("Sorted array is")
print(mergesort(seq))

##################################################################################################################
























































































=======
#851

'''
Python program for iterative merge sort
'''

def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i,j = 0,0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        if i == len(left) or j==len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

def mergesort(list):
    if len(list) < 2:
        return list

    middle = len(list)/2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)

seq = [12,11,13,5,6,7]
print("GIven array is")
print(seq)
print("\n")
print("Sorted array is")
print(mergesort(seq))

##################################################################################################################
























































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
