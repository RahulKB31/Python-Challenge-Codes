<<<<<<< HEAD
#787

'''
Python closest pair to kth index element in tuple
'''

# Using enumerate() + loop

test_list = [(3,4),(78,76),(2,3),(9,8),(19,23)]

print("Te original list is: " + str(test_list))

tup = (17,23)

K = 1

min_diff, res = 999999999, None
for idx,val in enumerate(test_list):
    dif = abs(tup[K-1] - val[K-1])
    if dif < min_diff:
        min_diff, res = dif, idx

print("The nearest tuple to Kth index element is: " + str(test_list[res]))

#################################################################################################################

#788

'''
Using min() + lambda
'''

test_list = [(3,4),(78,76),(2,3),(9,8),(19,23)]

print("The original list is: " + str(test_list))

tup = (17,23)

K = 1

res = min(range(len(test_list)), key = lambda sub: abs(test_list[sub][K-1] - tup[K-1]))

print("The nearest tuple to kth index element is: " + str(test_list[res]))

##################################################################################################################

#789

'''
Using a lambda function and the min() function
'''

test_list = [(3,4),(78,76),(2,3),(9,8),(19,23)]

print("The original list is: " + str(test_list))

tup = (17,23)

K = 1

res = min(test_list, key=lambda x: abs(x[K-1] - tup[K-1]))

print("The nearest tuple to kth index element is: " + str(res))

###############################################################################################################

#790

'''
Using the heapq.nsmallest() function
'''

import heapq

test_list = [(3,4),(78,76),(2,3),(9,8),(19,23)]

tup = (17,23)

K = 1

res = heapq.nsmallest(1, test_list, key=lambda x: abs(x[K-1] - tup[K-1]))[0]

print("The nearest tuple to kth index element is: " + str(res))

###############################################################################################################

#791

'''
Using the sorted() function with a custom key
'''

test_list = [(3,4),(78,76),(2,3),(9,8),(19,23)]

tup = (17,23)

K = 1

def key_func(t):
    return abs(t[K-1] - tup[K-1])

sorted_list = sorted(test_list, key = key_func)

res = sorted_list[0]

print("The nearest tuple to kth index element is: " + str(res))

###############################################################################################################
























































































































































































=======
#787

'''
Python closest pair to kth index element in tuple
'''

# Using enumerate() + loop

test_list = [(3,4),(78,76),(2,3),(9,8),(19,23)]

print("Te original list is: " + str(test_list))

tup = (17,23)

K = 1

min_diff, res = 999999999, None
for idx,val in enumerate(test_list):
    dif = abs(tup[K-1] - val[K-1])
    if dif < min_diff:
        min_diff, res = dif, idx

print("The nearest tuple to Kth index element is: " + str(test_list[res]))

#################################################################################################################

#788

'''
Using min() + lambda
'''

test_list = [(3,4),(78,76),(2,3),(9,8),(19,23)]

print("The original list is: " + str(test_list))

tup = (17,23)

K = 1

res = min(range(len(test_list)), key = lambda sub: abs(test_list[sub][K-1] - tup[K-1]))

print("The nearest tuple to kth index element is: " + str(test_list[res]))

##################################################################################################################

#789

'''
Using a lambda function and the min() function
'''

test_list = [(3,4),(78,76),(2,3),(9,8),(19,23)]

print("The original list is: " + str(test_list))

tup = (17,23)

K = 1

res = min(test_list, key=lambda x: abs(x[K-1] - tup[K-1]))

print("The nearest tuple to kth index element is: " + str(res))

###############################################################################################################

#790

'''
Using the heapq.nsmallest() function
'''

import heapq

test_list = [(3,4),(78,76),(2,3),(9,8),(19,23)]

tup = (17,23)

K = 1

res = heapq.nsmallest(1, test_list, key=lambda x: abs(x[K-1] - tup[K-1]))[0]

print("The nearest tuple to kth index element is: " + str(res))

###############################################################################################################

#791

'''
Using the sorted() function with a custom key
'''

test_list = [(3,4),(78,76),(2,3),(9,8),(19,23)]

tup = (17,23)

K = 1

def key_func(t):
    return abs(t[K-1] - tup[K-1])

sorted_list = sorted(test_list, key = key_func)

res = sorted_list[0]

print("The nearest tuple to kth index element is: " + str(res))

###############################################################################################################
























































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
