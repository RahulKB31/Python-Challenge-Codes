#710

'''
Python - Append Dictionary Keys and Values (In Order) in dictionary
'''

# Using list() + keys() + values()

test_dict = {'Gfg':1, "is":3, "Best":2}

print("The Original dictionary is: " + str(test_dict))

res = list(test_dict.keys()) + list(test_dict.values())

print("The ordered keys and values: " + str(res))

#################################################################################################################

#711

'''
Using chain() + keys() + values()
'''

from itertools import chain

test_dict = {'Gfg':1, "is":3, "Best":2}

print("The Original dictionary is: " + str(test_dict))

res = list(chain(test_dict.keys(), test_dict.values()))

print("The ordered keys and values: " + str(res))

#################################################################################################################

#712

'''
Using list() + keys() + values() + extend()
'''

test_dict = {'Gfg':1, "is":3, "Best":2}

print("The Original dictionary is: " + str(test_dict))

a = list(test_dict.keys())
b = list(test_dict.values())
a.extend(b)
res = a

print("The ordered keys and values: " + str(res))

#################################################################################################################

#713

'''
Using zip() function and list comprehension
'''

test_dict = {'Gfg':1, "is":3, "Best":2}

print("The Original dictionary is: " + str(test_dict))

res = [val for val in zip(test_dict.values(), test_dict.keys())]

print("The ordered keys and values: " + str(res))

#################################################################################################################

#714

'''
Using sorted() function and list comprehension
'''

test_dict = {'Gfg':1, "is":3, "Best":2}

print("The Original dictionary is: " + str(test_dict))

keys = sorted(test_dict.keys())

values = [test_dict[key] for key in keys]

res = keys + values

print("The ordered keys and values: " + str(res))

#################################################################################################################






















































































































































































