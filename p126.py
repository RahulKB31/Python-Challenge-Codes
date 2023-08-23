#767

'''
Python - Keys associated with values in Dictionary
'''

# Using defaultdict() + loop

from collections import defaultdict

test_dict = {'gfg':[1,2,3], 'is':[1,4], 'best':[4,2]}

print("The original dictionary is: " + str(test_dict))

res = defaultdict(list)

for key,val in test_dict.items():
    for ele in val:
        res[ele].append(key)

print("The value associated dictionary: " + str(dict(res)))

###############################################################################################################

#768

'''
Using dict comprehension + loop
'''

test_dict = {'gfg':[1,2,3], 'is':[1,4], 'best':[4,2]}

print("The original dictionary is: " + str(test_dict))

result_dict = {}
for key,val in test_dict.items():
    for ele in val:
        if ele in result_dict:
            result_dict[ele].append(key)
        else:
            result_dict[ele] = [key]

print("The value associated dictionary: " + str(dict(res)))

#########################################################################################################

#769

'''
Using the setdefault() method of dictionary
'''

test_dict = {'gfg':[1,2,3], 'is':[1,4], 'best':[4,2]}

print("The original dictionary is: " + str(test_dict))

result_dict = {}
for key, val in test_dict.items():
    for ele in val:
        result_dict.setdefault(ele, []).append(key)

print("The value associated dictionary: " + str(dict(res)))

#########################################################################################################s





























































































































































