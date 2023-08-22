#721

'''
Python - Sort Dictionary key and values list
'''

test_dict = {'gfg':[7,6,3], 'is':[2,10,3], 'best':[19,4]}

print("The original dictionary is: " + str(test_dict))

res = dict()
for key in sorted(test_dict):
    res[key] = sorted(test_dict[key])

print("The sorted dictionary: " + str(res))

################################################################################################################

#722

'''
Sort dictionary key and values list using dictionary comprehension + sorted()
'''

test_dict = {'gfg':[7,6,3], 'is':[2,10,3], 'best':[19,4]}

print("The original dictionary is: " + str(test_dict))

res = {key: sorted(test_dict[key]) for key in sorted(test_dict)}

print("The sorted ditionary: " + str(res))

##############################################################################################################

#723

'''
Sort dictionary key and values list using lambda function with sorted()
'''

test_dict = {'gfg':[7,6,3], 'is':[2,10,3], 'best':[19,4]}

print("The original dictionary is: " + str(test_dict))

res = dict(sorted(test_dict.items(), key = lambda x: x[0]))

for key in res:
    res[key] = sorted(res[key])

print("The sorted dictionary: " + str(res))

#################################################################################################################

#724

'''
Sort dictionary key and values list using the zip() function with sorted() function
'''

test_dict = {'gfg':[7,6,3], 'is':[2,10,3], 'best':[19,4]}

print("The original dictionary is: " + str(test_dict))

keys = list(test_dict.keys())
values = list(test_dict.values())
sorted_tuples = sorted(zip(keys, values), key = lambda x: x[0])
res = {k: sorted(v) for k, v in sorted_tuples}

print("The sorted dictionary: "  + str(res))

###################################################################################################################

#725

'''
Sort Dictionary key and values list using recursive method
'''

def sort_dict_recursive(test_dict):
    if not test_dict:
        return {}
    min_key = min(test_dict.keys())
    sorted_values = sorted(test_dict[min_key])
    rest_dict = {k:v for k,v in test_dict.items() if k!= min_key}
    sorted_res_dict = sort_dict_recursive(rest_dict)
    return {min_key: sorted_values, **sorted_res_dict}

test_dict = {'gfg':[7,6,3], 'is':[2,10,3], 'best':[19,4]}
res = sort_dict_recursive(test_dict)
print("The original dictionary is: " + str(test_dict))
print("The sorted dictionary: " + str(res))

##############################################################################################################





















































































