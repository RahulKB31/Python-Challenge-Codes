#691

'''
Python | Merging two Dictionaries
'''

# Using the method update()

def Merge(dict1, dict2):
    return (dict2.update(dict1))

dict1 = {'a':10,'b':8}
dict2 = {'d':6, 'c':4}

print(Merge(dict1, dict2))

print(dict2)

################################################################################################################

#692

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

dict1 = {'a':10,'b':8}
dict2 = {'d':6, 'c':4}

dict3 = Merge(dict1, dict2)
print(dict3)

#################################################################################################################

#693

def Merge(dict1, dict2):
    res = dict1 | dict2
    return res

dict1 = {'a':10,'b':8}
dict2 = {'d':6, 'c':4}

dict3 = Merge(dict1, dict2)
print(dict3)

##############################################################################################################

#694

'''
Using for loop and keys() method
'''

def Merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i] = dict2[i]
    return dict1

dict1 = {'a':10,'b':8}
dict2 = {'d':6, 'c':4}

dict3 = Merge(dict1, dict2)
print(dict3)

###############################################################################################################

#695

from collections import ChainMap

dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

merged_dict = ChainMap(dict1, dict2)

print(merged_dict['a'])
print(merged_dict['c'])
merged_dict['c'] = 5
print(merged_dict['c'])

merged_dict['e'] = 6
print(merged_dict['e'])

##############################################################################################################

#696

'''
Using dict constructor
'''

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {'x':10, 'y':8}
dict2 = {'a':6, 'b':4}

##############################################################################################################

#697

'''
Using the dict() constructor with the union operator(|)
'''

def Merge(dict1, dict2):
    merged_dict = dict(dict1.items() | dict2.items())
    return merged_dict

dict1 = {'a':10, 'b':8}
dict2 = {'d': 6, 'c':4}

merged_dict = Merge(dict1, dict2)

print(merged_dict)

##############################################################################################################

#698

'''
Using reduce()
'''

from functools import reduce

def merge_dictionaries(dict1, dict2):
    merge_dict = dict1.copy()
    merge_dict.update(dict2)
    return merged_dict

dict1 = {'a':10, 'b':8}
dict2 = {'d': 6, 'c':4}

dict_list = [dict1, dict2]

result_dict = reduce(merge_dictionaries, dict_list)

print(result_dict)

###############################################################################################################























































































































































































