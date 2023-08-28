<<<<<<< HEAD
#805

'''
Python - All pair combinations of 2 tuples
'''

# Using list comprehension

test_tuple1 = (4,5)
test_tuple2 = (7,8)

print("The original tuple 1: " + str(test_tuple1))
print("The original tuple 2: " + str(test_tuple2))

res = [(a,b) for a in test_tuple1 for b in test_tuple2]
res = res + [(a,b) for a in test_tuple2 for b in test_tuple1]

print("The filtered tuple: " + str(res))

#################################################################################################################

#806

'''
Using chain() + product()
'''

from itertools import chain, product

test_tuple1 = (4,5)
test_tuple2 = (7,8)

print("The original tuple 1: " + str(test_tuple1))
print("The original tuple 2: " + str(test_tuple2))

res = list(chain(product(test_tuple1, test_tuple2), product(test_tuple2, test_tuple1)))

print("The filtered tuple: " + str(res))

################################################################################################################

#807

'''
Using itertools.product()
'''

import itertools

test_tuple1 = (4,5)
test_tuple2 = (7,8)

print("The original tuple 1: " + str(test_tuple1))
print("The original tuple 2: " + str(test_tuple2))

res = [(a,b) for a in test_tuple1 for b in test_tuple2] + [(a,b) for a in test_tuple2 for b in test_tuple1]

print("All pair combinations of 2 tuples: " + str(res))

################################################################################################################

#808

'''
Using nested loops
'''

tuple1 = (4,5)
tuple2 = (7,8)

filtered_tuples = []

for element1 in tuple1:
    for element2 in tuple2:
        filtered_tuples.append((element1, element2))
        filtered_tuples.append((element2, element1))

print(filtered_tuples)

###############################################################################################################









































































































































































































=======
#805

'''
Python - All pair combinations of 2 tuples
'''

# Using list comprehension

test_tuple1 = (4,5)
test_tuple2 = (7,8)

print("The original tuple 1: " + str(test_tuple1))
print("The original tuple 2: " + str(test_tuple2))

res = [(a,b) for a in test_tuple1 for b in test_tuple2]
res = res + [(a,b) for a in test_tuple2 for b in test_tuple1]

print("The filtered tuple: " + str(res))

#################################################################################################################

#806

'''
Using chain() + product()
'''

from itertools import chain, product

test_tuple1 = (4,5)
test_tuple2 = (7,8)

print("The original tuple 1: " + str(test_tuple1))
print("The original tuple 2: " + str(test_tuple2))

res = list(chain(product(test_tuple1, test_tuple2), product(test_tuple2, test_tuple1)))

print("The filtered tuple: " + str(res))

################################################################################################################

#807

'''
Using itertools.product()
'''

import itertools

test_tuple1 = (4,5)
test_tuple2 = (7,8)

print("The original tuple 1: " + str(test_tuple1))
print("The original tuple 2: " + str(test_tuple2))

res = [(a,b) for a in test_tuple1 for b in test_tuple2] + [(a,b) for a in test_tuple2 for b in test_tuple1]

print("All pair combinations of 2 tuples: " + str(res))

################################################################################################################

#808

'''
Using nested loops
'''

tuple1 = (4,5)
tuple2 = (7,8)

filtered_tuples = []

for element1 in tuple1:
    for element2 in tuple2:
        filtered_tuples.append((element1, element2))
        filtered_tuples.append((element2, element1))

print(filtered_tuples)

###############################################################################################################









































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
