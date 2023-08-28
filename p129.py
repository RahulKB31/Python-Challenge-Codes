<<<<<<< HEAD
#778

'''
Python program to create a list of tuples from given list having number and its cube in each tuple
'''

# Using pow() function

list1 = [1,2,5,6]

res = [(val, pow(val,3)) for val in list1]
print(res)

##################################################################################################################

#779

'''
Using ** operator
'''

val = [1,2,5,6]

res = [(val, val**3) for val in list1]
print(res)

##################################################################################################################

#780

'''
Using map() and lambda function
'''

list1 = [1,2,5,6]
res = list(map(lambda x: (x,x**3), list1))
print(res)

###############################################################################################################

#781

'''
Using a for loop to iterate through the values in the list and create a tuple of each value and its cube
'''

list1 = [1,2,5,6]
res = []

for val in list1:
    tup = (val, val**3)
    res.append(tup)

print(res)

#################################################################################################################

#782

'''
Using re method
'''

import re

lst_str = "1,2,5,6"
lst = [int(num) for num in re.findall(r'\d+', lst_str)]
result = [(num, num**3) for num in lst]
print(result)

##################################################################################################################

























































































































































=======
#778

'''
Python program to create a list of tuples from given list having number and its cube in each tuple
'''

# Using pow() function

list1 = [1,2,5,6]

res = [(val, pow(val,3)) for val in list1]
print(res)

##################################################################################################################

#779

'''
Using ** operator
'''

val = [1,2,5,6]

res = [(val, val**3) for val in list1]
print(res)

##################################################################################################################

#780

'''
Using map() and lambda function
'''

list1 = [1,2,5,6]
res = list(map(lambda x: (x,x**3), list1))
print(res)

###############################################################################################################

#781

'''
Using a for loop to iterate through the values in the list and create a tuple of each value and its cube
'''

list1 = [1,2,5,6]
res = []

for val in list1:
    tup = (val, val**3)
    res.append(tup)

print(res)

#################################################################################################################

#782

'''
Using re method
'''

import re

lst_str = "1,2,5,6"
lst = [int(num) for num in re.findall(r'\d+', lst_str)]
result = [(num, num**3) for num in lst]
print(result)

##################################################################################################################

























































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
