<<<<<<< HEAD
#854

'''
Python program for counting sort
'''

def countSort(arr):
    output = [0 for i in range(256)]

    count = [0 for i in range(256)]

    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i-1]

    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

arr = "geeksforgeeks"
ans = countSort(arr)
print("Sorted character array is %s" %("".join(ans)))

#################################################################################################################

#855

from collections import Counter

def counting_sort(arr):
    count = Counter(arr)
    output = []
    for c in sorted(count.keys()):
        output += count
    return output

arr = "geeksforgeeks"
arr = list(arr)
arr = counting_sort(arr)
output = ''.join(arr)
print("Sorted character array is", output)

################################################################################################################

#856

'''
Using sorted() and reduce()
'''

from functools import reduce

string = "geeksforgeeks"

sorted_str = reduce(lambda x,y: x+y, sorted(string))

print("Sorted String:", sorted_str)

##############################################################################################################















































































































































=======
#854

'''
Python program for counting sort
'''

def countSort(arr):
    output = [0 for i in range(256)]

    count = [0 for i in range(256)]

    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i-1]

    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

arr = "geeksforgeeks"
ans = countSort(arr)
print("Sorted character array is %s" %("".join(ans)))

#################################################################################################################

#855

from collections import Counter

def counting_sort(arr):
    count = Counter(arr)
    output = []
    for c in sorted(count.keys()):
        output += count
    return output

arr = "geeksforgeeks"
arr = list(arr)
arr = counting_sort(arr)
output = ''.join(arr)
print("Sorted character array is", output)

################################################################################################################

#856

'''
Using sorted() and reduce()
'''

from functools import reduce

string = "geeksforgeeks"

sorted_str = reduce(lambda x,y: x+y, sorted(string))

print("Sorted String:", sorted_str)

##############################################################################################################















































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
