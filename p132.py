#792

'''
Python - Join Tuples if similar initial element
'''

# Using loop

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

res = []
for sub in test_list:
    if res and res[-1][0] == sub[0]:
        res[-1].extend(sub[1:])
    else:
        res.append([ele for ele in sub])
res = list(map(tuple, res))

print("The extracted elements: " + str(res))

################################################################################################################

#793

'''
Using defaultdict() + loop
'''

from collections import defaultdict

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

mapp = defaultdict(list)

for key,val in test_list:
    mapp[key].append(val)
res = [(key, *val) for key, val in map.items()]

print("The extracted elements: " + str(res))

################################################################################################################

#794

'''
Using for loop
'''

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

res = []
x = []
for i in test_list:
    if i[0] not in x:
        x.append(i[0])
for i in x:
    p = []
    p.append(i)
    for j in test_list:
        if i == j[0]:
            p.append(j[1])
    res.append(p)

print("The extracted elements: " + str(res))

#################################################################################################################

#795

'''
Using dictionary and list comprehension
'''

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

temp_dict = {}
for x in test_list:
    temp_dict[x[0]] = temp_dict.get(x[0], []) + list(x[1:])

res = [(k,) + tuple(v) for k,v in temp_dict.items()]

print("The extracted elements: " + str(res))

#################################################################################################################

#796

'''
Using itertools.groupby()
'''

from itertools import groupby

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

res = []

for k,g in groupby(test_list, key=lambda x: x[0]):
    values = [v for _,v in g]
    res.append((k, *values))

print("The extracted elements: " + str(res))

###############################################################################################################

#797

'''
Using pandas
'''

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

import pandas as pd

df = pd.Dataframe(test_list, columns = ["A","B"])

grouped = df.groupby("A")["B"].apply(list)

res = [tuple([k] + v) for k,v in grouped.items()]

print("The extracted elements: " + str(res))

##################################################################################################################

#798

'''
Using recursion
'''

def join_tuples(test_list, index):
    if index == len(test_list) - 1:
        return test_list
    elif test_list[index][0] == test_list[index + 1][0]:
        test_list[index] += test_list[index+1][1:]
        test_list.pop(index + 1)
        return join_tuples(test_list, index)
    else:
        return join_tuples(test_list, index + 1)

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

res = join_tuples(test_list, 0)

print("The extracted elements: " + str(res))

################################################################################################################
























































































































































































































