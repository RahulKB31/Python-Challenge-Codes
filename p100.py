#674

'''
Python program to find the sum of all items in a dictionary
'''

# Using inbuilt sum() function

def returnSum(myDict):

    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final

dict = {'a':100, 'b':200, 'c':300}
print("Sum: ", returnSum(dict))

#############################################################################################################

#675

'''
Using for loop to iterate through values using values() function
'''

def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i

    return sum

dict = {'a':100, 'b':200, 'c':300}
print('Sum: ', returnSum(dict))

################################################################################################################

#676

'''
Using for loop to iterate over each value in a dictionary
'''

def returnSum(dict):

    sum = 0
    for i in dict:
        sum = sum + dict[i]

    return sum

dict = {'a':100, 'b':200, 'c':300}
print('Sum: ', returnSum(dict))

###############################################################################################################

#677

'''
Using values() and sum() function
'''

def returnSum(dict):
    return sum(dict.values())

dict = {'a':100, 'b':200, 'c':300}
print('Sum: ', returnSum(dict))

#############################################################################################################

#678

'''
Using the lambda function
'''

import functools

dic = {'a':100, 'b':200, 'c':300}

sum_dic = functools.reduce(lambda ac,k: ac+dic[k], dic, 0)

print('Sum: ', sum_dic)

################################################################################################################

#679

def returnSum(myDict):
    return sum(myDict[key] for key in myDict)

dict = {'a':100, 'b':200, 'c':300}
print('Sum: ', returnSum(dict))

##################################################################################################################

#680

'''
Using the reduce() function
'''

import functools

def sum_dict_values(dict):
    return functools.reduce(lambda acc, x: acc + dict[x],dict,0)

dict = {'a':100, 'b':200, 'c':300}
print('Sum: ', sum_dict_values(dict))

###############################################################################################################

#681

'''
Using numpy
'''

import numpy as np

def returnSum(dict):
    values = np.array(list(dict.values()))
    return np.sum(values)

dict = {'a':100, 'b':200, 'c':300}
print('Sum: ', returnSum(dict))

###############################################################################################################











































































































































































































