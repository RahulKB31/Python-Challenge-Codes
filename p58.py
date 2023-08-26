#452

'''
Python | Sum of number digits in list
'''

test_list = [12,67,98,34]

print("The original list is: " + str(test_list))

#sum of number digits in list
#using loop + str()
res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)

print("List integer summation: " + str(res))

################################################################################################################

#453

'''
Using sum() + list comprehension
'''

test_list = [12,67,98,34]

print("The original list is: " + str(test_list))

res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))

print("List integer summation: " + str(res))

##############################################################################################################

#454

'''
Using sum() + reduce()
'''

from functools import reduce

test_list = [12,67,98,34]

print("The original list is: " + str(test_list))

res = [reduce(lambda x, y: int(x) + int(y), list(str(i))) for i in test_list]

print("List integer summation: "+ str(res))

#################################################################################################################

#455

'''
Using numpy
'''

import numpy as np

test_list = [12,67,98,34]

print("The original list is: " + str(test_list))

res = np.sum([list(map(int, str(ele))) for ele in test_list], axis = 1)

print("List integer summation: " + str(list(res)))

#################################################################################################################

#456

'''
Using itertools library
'''

import itertools

test_list = [12,67,98,34]

print("The original list is: " + str(test_list))

res = [sum(map(int, list(itertools.chain(*str(ele))))) for ele in test_list]

print("List inteer summation: " + str(res))

############################################################################################################

#457

'''
Using map() function and modulo operator
'''

lst = [12,67,98,34]
def digit_sum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

def sum_of_digits_list(lst):
    return list(map(digit_sum, lst))

print(sum_of_digits_list(lst))

############################################################################################################

#458

'''
Creating a expression without changing to a string
'''

test_list = [12,67,98,34]

print("The original list is: " + str(test_list))

res = list(sum(int(digit) for digit in str(num)) for num in test_list)

print("List integer summation: " + str(list(res)))

###########################################################################################################































































































































































