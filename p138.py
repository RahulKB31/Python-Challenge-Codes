#825

'''
Python - Flatten tuple of list to tuple
'''

# Using sum() + tuple()

test_tuple = ([5,6],[6,7,8,9],[3])

print("The original tuple: " + str(test_tuple))

res = tuple(sum(test_tuple, []))

print("The flattend tuple: " + str(res))

##################################################################################################################

#826

'''
Using tuple() + chain.from_iterable()
'''

from itertools import chain

test_tuple = ([5,6],[6,7,8,9],[3])

print("The original tuple: " + str(test_tuple))

res = tuple(chain.from_iterable(test_tuple))

print("The flattened tuple: " + str(res))

################################################################################################################

#827

'''
Using extend() and tuple() methods
'''

test_tuple = ([5,6],[6,7,8,9],[3])

print("The original tuple: " + str(test_tuple))

res = []
for i in test_tuple:
    res.extend(i)
res = tuple(res)

print("The flattend tuple: " + str(res))

##################################################################################################################

#828

'''
Using Nested loops
'''

test_tuple = ([5,6],[6,7,8,9],[3])

print("The original tuple: " + str(test_tuple))

res = []

for i in test_tuple:
    for j in i:
        res.append(j)

res = tuple(res)

print("The flattend tuple: " + str(res))

####################################################################################################################

#829

'''
Using list comprehension and extend()
'''

test_tuple = ([5,6],[6,7,8,9],[3])

print("The original tuple: " + str(test_tuple))

res_list = []
[res_list.extend(sublist) for sublist in test_tuple]

res = tuple(res_list)

print("The flattened tuple: " + str(res))

###################################################################################################################

#830

'''
Using the itertools.chain()
'''

import itertools

test_tuple = ([5,6],[6,7,8,9],[3])

print("The original tuple: " + str(test_tuple))

res = tuple(itertools.chain(*test_tuple))

print("The flattened tuple: " + str(res))

##################################################################################################################

#831

'''
Using Recursive method
'''

def flatten_tuple(tup):
    if not tup:
        return()
    elif isinstance(tup[0],list):
        return flatten_tuple(tup[0]) + flatten_tuple(tup[1:])

    else:
        return (tup[0],) + flatten_tuple(tup[1:])

test_tuple = ([5,6],[6,7,8,9],[3])

print("The original tuple: " + str(test_tuple))

res = flatten_tuple(test_tuple)

print("The flattened tuple: " + str(res))

##################################################################################################################

















































































































































































































