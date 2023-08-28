<<<<<<< HEAD
#726

'''
Handling missing keys in Python Dictionaries
'''

d = {'a':1, 'b':2}

print("The value associated with 'c' is: ")
print(d['c'])

################################################################################################################

#727

'''
Using get()
'''

country_code = {'India':'0091', 'Australia':'0025', 'Nepal':'00977'}

print(country_code.get('India','Not Found'))

print(country_code.get('Japan', 'Not found'))

#################################################################################################################

#728

'''
Using setdefault()
'''

country_code = {'India':'0091', 'Australia':'0025', 'Nepal':'00977'}

country_code.setdefault('Japan', 'Not Present')

print(country_code['India'])

print(country_code['Japan'])

###############################################################################################################

#729

'''
Using default dict
'''

import collections

defd = collections.defaultdict(lambda: 'Key Not Found')

defd['a'] = 1

defd['b'] = 2

print("The value associated with 'a' is: ", end = "")
print(defd['a'])

print('The value associated with "c" is: ', end= "")
print(defd['c'])

###################################################################################################################

#730

'''
Using the try-except block
'''

country_code = {'India':'0091', 'Australia':'0025', 'Nepal':'00977'}

try:
    print(country_code['India'])
    print(country_code['USA'])
except KeyError:
    print('Not Found')

################################################################################################################
























































































































































































=======
#726

'''
Handling missing keys in Python Dictionaries
'''

d = {'a':1, 'b':2}

print("The value associated with 'c' is: ")
print(d['c'])

################################################################################################################

#727

'''
Using get()
'''

country_code = {'India':'0091', 'Australia':'0025', 'Nepal':'00977'}

print(country_code.get('India','Not Found'))

print(country_code.get('Japan', 'Not found'))

#################################################################################################################

#728

'''
Using setdefault()
'''

country_code = {'India':'0091', 'Australia':'0025', 'Nepal':'00977'}

country_code.setdefault('Japan', 'Not Present')

print(country_code['India'])

print(country_code['Japan'])

###############################################################################################################

#729

'''
Using default dict
'''

import collections

defd = collections.defaultdict(lambda: 'Key Not Found')

defd['a'] = 1

defd['b'] = 2

print("The value associated with 'a' is: ", end = "")
print(defd['a'])

print('The value associated with "c" is: ', end= "")
print(defd['c'])

###################################################################################################################

#730

'''
Using the try-except block
'''

country_code = {'India':'0091', 'Australia':'0025', 'Nepal':'00977'}

try:
    print(country_code['India'])
    print(country_code['USA'])
except KeyError:
    print('Not Found')

################################################################################################################
























































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
