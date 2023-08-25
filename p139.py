#832

'''
Python - Convert Nested Tuple to custom key Dictionary
'''

# Using list comprehension + dictionary

test_tuple = ((4,'Gfg',10),(3,'is',8),(6,'Best',10))

print("The original tuple: " + str(test_tuple))

res = [{'key':sub[0], 'value':sub[1], 'id':sub[2]} for sub in test_tuple]

print("The converted dictionary: " + str(res))

#################################################################################################################

#833

'''
Using zip() + list comprehension
'''

test_tuple = ((4,'Gfg',10),(3,'is',8),(6,'Best',10))

print("The original tuple: " + str(test_tuple))

keys = ['key','value','id']

res = [{key: val for key, val in zip(keys, sub)} for sub in test_tuple]

print("The converted dictionary: " + str(res))

#################################################################################################################

#834

'''
Using a for loop
'''

test_tuple = ((4,'Gfg',10),(3,'is',8),(6,'Best',10))

keys = ['key','value','id']

res = []

for sub in test_tuple:
    sub_dict = {}
    for i in range(len(keys)):
        sub_dict[keys[i]] = sub[i]
    res.append(sub_dict)

print("The converted dictionary: " + str(res))

#################################################################################################################



































































































