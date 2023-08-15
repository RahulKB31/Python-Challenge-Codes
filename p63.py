#480

'''
Python | MAtrix Product
'''

# using list comprehension + loop

def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res

test_list = [[1,2,3],[4,5],[6],[7,8,9]]

print("The original list: " + str(test_list))

res = prod([ele for sub in test_list for ele in sub])

print("The total element product in lists is: " + str(res))

#################################################################################################################

#481

'''
Using chain() + loop
'''

from itertools import chain

def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res

test_list = [[1,2,3],[4,5],[6],[7,8,9]]

print("The original list: " + str(test_list))

res = prod(list(chain(*test_list)))

print("The total element product in lists in: " + str(res))

#############################################################################################################

#482

'''
Using extend() method
'''

test_list = [[1,2,3],[4,5],[6],[7,8,9]]

print("The original list: " + str(test_list))

x = []
for i in test_list:
    x.extend(i)
res = 1
for j in x:
    res *= j

print("The total element in lists is: " + str(res))

##############################################################################################################

#483

'''
Using extend(), functools.reduce() and operator.mul
'''

import operator
from functools import reduce
test_list = [[1,2,3],[4,5],[6],[7,8,9]]

print("The original list: " + str(test_list))

x = []
for i in test_list:
    x.extend(i)

res = reduce(operator.mul,x,1)

print("The total element product in lists is: " + str(res))

#########################################################################################################

#484

'''
Using nested loops
'''

test_list = [[1,2,3],[4,5],[6],[7,8,9]]

print("The original list : " + str(test_list))

res = 1
for i in test_list:
    for j in i:
        res *= j

print("The etotal element product in lists is: " + str(res))

########################################################################################################

#485

'''
Use recursion to traverse the nested list and multiply all the elements
'''

def multiply_nested_list(nested_list):
    res = 1
    for i in nested_list:
        if isinstance(i, list):
            res *= multiply_nested_list(i)
        else:
            res *= i
    return res

test_list = [[1,2,3],[4,5],[6],[7,8,9]]

print("The original list: " + str(test_list))

res = multiply_nested_list(test_list)

print("The total element product in lists is:" + str(res))

###############################################################################################################





































































































































































































