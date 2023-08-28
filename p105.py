<<<<<<< HEAD
#699

'''
Python - Convert key-values list to flat dictionary
'''

# Convert key-values list to flat dictionary using zip() + dict()

from itertools import product

test_dict = {'month':[1,2,3],
             'name': {'Jan','Feb','March'}}

print("The original dictionary is: " + str(test_dict))

res = dict(zip(test_dict['month'], test_dict['name']))

print("Flattened dictionary: " + str(res))

################################################################################################################

#700

'''
Convert key-values list to flat dictionary using values() and dict() methods
'''

test_dict = {'month':[1,2,3],
             'name': {'Jan','Feb','March'}}

print("The original dictionary is: " + str(test_dict))

x = list(test_dict.values())
a = x[0]
b = x[1]
d = dict()
for i in range(0, len(a)):
    d[a[i]] = b[i]

print("FLattened dictionary: " + str(d))

###################################################################################################################

#701

'''
Convert key-values list to flat dictionary using a dictionary comprehension
'''

test_dict = {'month':[1,2,3],
             'name': {'Jan','Feb','March'}}

res = {test_dict['month'][i]: test_dict['name'][i] for i in range(len(test_dict['month']))}
print("Flatterned dictionary: ", res)

################################################################################################################

#702

'''
Use for loop to iterate over the keys and values and create a new dictionary by assigning each key-value pair
to the new dictionary
'''

test_dict = {'month':[1,2,3],
             'name': {'Jan','Feb','March'}}

print("The original dictionary is: " + str(test_dict))

res = {}
for i in range(len(test_dict['month'])):
    res[test_dict['month'][i]] = test_dict['name'][i]

print("Flattened dictionary: " + str(res))

###################################################################################################################















































































































































































=======
#699

'''
Python - Convert key-values list to flat dictionary
'''

# Convert key-values list to flat dictionary using zip() + dict()

from itertools import product

test_dict = {'month':[1,2,3],
             'name': {'Jan','Feb','March'}}

print("The original dictionary is: " + str(test_dict))

res = dict(zip(test_dict['month'], test_dict['name']))

print("Flattened dictionary: " + str(res))

################################################################################################################

#700

'''
Convert key-values list to flat dictionary using values() and dict() methods
'''

test_dict = {'month':[1,2,3],
             'name': {'Jan','Feb','March'}}

print("The original dictionary is: " + str(test_dict))

x = list(test_dict.values())
a = x[0]
b = x[1]
d = dict()
for i in range(0, len(a)):
    d[a[i]] = b[i]

print("FLattened dictionary: " + str(d))

###################################################################################################################

#701

'''
Convert key-values list to flat dictionary using a dictionary comprehension
'''

test_dict = {'month':[1,2,3],
             'name': {'Jan','Feb','March'}}

res = {test_dict['month'][i]: test_dict['name'][i] for i in range(len(test_dict['month']))}
print("Flatterned dictionary: ", res)

################################################################################################################

#702

'''
Use for loop to iterate over the keys and values and create a new dictionary by assigning each key-value pair
to the new dictionary
'''

test_dict = {'month':[1,2,3],
             'name': {'Jan','Feb','March'}}

print("The original dictionary is: " + str(test_dict))

res = {}
for i in range(len(test_dict['month'])):
    res[test_dict['month'][i]] = test_dict['name'][i]

print("Flattened dictionary: " + str(res))

###################################################################################################################















































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
