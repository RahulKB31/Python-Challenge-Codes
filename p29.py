<<<<<<< HEAD
#167

'''
Python program for find remainder of array multiplication divided by n
'''

# to use reduce function import reduce from functools

from functools import reduce

def find_remainder(arr, n):
    sum_1 = reduce(lambda x, y: x*y, arr)
    remainder = sum_1 % n
    print(remainder)

arr = [100, 10, 5, 25, 35, 14]
n =11
find_remainder(arr, n)

############################################################################################################

#168

'''
without using inbuilt functions
'''

arr = [100, 10, 5, 25, 35, 14]; lens = len(arr); n=11
mul = 1
for i in range(lens):
    mul = (mul * (arr[i] % n)) % n
print(mul * n)

##############################################################################################################

#169

'''
Using logarithmic operations
'''

import math

def find_remainder(arr, n):
    # calculating the sum of logarithms of array elements
    # and storing them in the variable below
    log_sum = 0
    for i in arr:
        log_sum += math.log10(i)

    # take exponential of the sum and return remainder
    remainder = int(pow(10, log_sum)) % n
    return remainder

arr = [100, 10, 5,25, 35, 14]
ele = 11
rem = find_remainder(arr, ele)
print(rem)

=======
#167

'''
Python program for find remainder of array multiplication divided by n
'''

# to use reduce function import reduce from functools

from functools import reduce

def find_remainder(arr, n):
    sum_1 = reduce(lambda x, y: x*y, arr)
    remainder = sum_1 % n
    print(remainder)

arr = [100, 10, 5, 25, 35, 14]
n =11
find_remainder(arr, n)

############################################################################################################

#168

'''
without using inbuilt functions
'''

arr = [100, 10, 5, 25, 35, 14]; lens = len(arr); n=11
mul = 1
for i in range(lens):
    mul = (mul * (arr[i] % n)) % n
print(mul * n)

##############################################################################################################

#169

'''
Using logarithmic operations
'''

import math

def find_remainder(arr, n):
    # calculating the sum of logarithms of array elements
    # and storing them in the variable below
    log_sum = 0
    for i in arr:
        log_sum += math.log10(i)

    # take exponential of the sum and return remainder
    remainder = int(pow(10, log_sum)) % n
    return remainder

arr = [100, 10, 5,25, 35, 14]
ele = 11
rem = find_remainder(arr, ele)
print(rem)

>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
##########################################################################################################