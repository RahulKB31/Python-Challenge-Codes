#143

'''
Python program to find sum of array
'''

def _sum(arr):
    # Initialize a variable to store the sum while iterating through the array later
    sum = 0

    # iterate through the array and add each element to the sum of variable one at a time
    for i in arr:
        sum = sum + i

    return(sum)

# main function
if __name__ == "__main__":
    # input values to list
    arr = [12, 3, 4, 15]

    #calculating length of array
    n = len(arr)

    # calling function ans store the sum in ans
    ans = _sum(arr)

    print('Sum of the array is', ans)

###########################################################################################################

#144

'''
Python program to find sum of array using sum()
'''

arr = [12, 3, 4,15]

# sum() is an inbuilt function in python that adds all the elements in list, sets and tuples and
# returns the value

ans = sum(arr)

# display sum
print("Sum of the array is", ans)

#############################################################################################################

#145

'''
Python program to find sum of array using reduce method
'''

from functools import reduce

def _sum(arr):
    # iterate over array using reduce and get sum on accumulator
    sum = reduce(lambda a, b: a + b, arr)

    return (sum)

# driver function
arr = []

# input values to list
arr = [12,3,4,15]

# calculating length of array
n = len(arr)

ans = _sum(arr)

# display sum
print("Sum of the array is", ans)

######################################################################################################

#146

'''
Python program to find sum of array using enumerate function
'''

list1 = [12, 3, 4,15]
s = 0
for i,a in enumerate(list1):
    s = s + a
    print(s)

#########################################################################################################

#147

'''
Python program to find sum of array using Divide and conquer
'''

def sum_of_array(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_sum = sum_of_array(arr, low, mid)
    right_sum = sum_of_array(arr, mid+1, high)
    return left_sum + right_sum

arr = [1,2,3]
print(sum_of_array(arr, 0, len(arr) - 1))

arr = [15, 12, 13, 10]
print(sum_of_array(arr, 0, len(arr) - 1))

##########################################################################################################

#148

'''
Python program to find sum of array using counter method
'''

from collections import Counter

arr = [12, 3, 4, 15]
c = Counter(arr)
sum = 0

for key, value in c.items():
    sum 6= key * value

print("Sum of the array is", sum)

########################################################################################################


















































































































































































































