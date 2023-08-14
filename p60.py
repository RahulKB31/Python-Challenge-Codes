#467

'''
Sort the values of first list using second list in python
'''

def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)

    z = [x for _, x in sorted(zipped_pairs)]

    return z

x = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
y = [0,1,2,3,4,5,6,7,8,1,1]

print(sort_list(x,y))

x = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
y = [0,1,2,3,4,5,6,7,8,1,1]

print(sort_list(x,y))

#########################################################################################################

#468

'''
Using dictionary, list comprehension, lambda function
'''

def sorting_of_elements(list1, list2):

    f_1 = {}

    final_list = []

    f_1 = {list1[i]: list2[i] for i in range(len(list2))}

    f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}

    for i in f_lst.keys():
        final_list.append(i)
    return final_list

list1 = ['a','b','c','d','e','f','g','h']
list2 = [0,1,1,0,1,2,2,0,1]

list3 = sorting_of_elements(list1,list2)
print(list3)

################################################################################################################

#469

'''
Using sort(),list() and set() methods
'''

list1 = ['a','b','c','d','e','f','g','h']
list2 = [0,1,1,0,1,2,2,0,1]

a = list(set(list2))
a.sort()
res = []
for i in a:
    for j in range(0, len(list2)):
        if(list2[j] == i):
            res.append(list1[j])
print(res)

###########################################################################################################

#470

'''
Using collections.orderedDict()
'''

from collections import OrderedDict
list1 = ['a','b','c','d','e','f','g','h']
list2 = [0,1,1,0,1,2,2,0,1]
d = OrderedDict(zip(list1,list2))
res = list(OrderedDict(sorted(d.items(), key=lambda x: x[1])))
print(res)

#################################################################################################################

#471

'''
using numpy.argsort() function with fancy indexing
'''

import numpy as np

def sort_list(list1, list2):
    idx = np.argsort(list2)
    return np.array(list1)[idx]

x = ['a','b','c','d','e','f','g','h']
y = [0,1,1,0,1,2,2,0,1]

print(sort_list(x,y))

x = ['a','b','c','d','e','f','g','h']
y = [0,1,1,0,1,2,2,0,1]

print(sort_list(x,y))

################################################################################################################







































































































































































