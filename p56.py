#436

'''
Python | program to print duplicates from a list of integers
'''

# Using the Brute Force approach

def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])

    return repeated

list1 = [10,20,30,20,20,30,40,50,-20,60,60,-20,-20]
print(Repeat(list1))

##############################################################################################################

#437

'''
Using a single for loop
'''

lis = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]

uniqueList = []
duplicateList = []

for i in lis:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)

print(duplicateList)

################################################################################################################

#438

'''
Using counter() function from collection module
'''

from collections import Counter

l1 = [1,2,1,2,3,4,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)

new_list = list([item for item in d if d[item] > 1])
print(new_list)

#############################################################################################################

#439

'''
Using count() method
'''

list = [1,2,1,2,3,4,1,1,2,5,6,7,8,9,9]

new = []

for a in list:
    n = list.count(a)
    if n > 1:
        if new.count(a) == 0:
            new.append(a)

print(new)

##############################################################################################################

#440

'''
Using list comprehension method
'''

def duplicate(input_list):
    return list(set([x for x in input_list if input_list.count(x) > 1]))

if __name__ == "__main__":
    input_list = [1,2,1,2,3,4,1,1,2,5,6,7,8,9,9]
    print(duplicate(input_list))

#################################################################################################################

#441

'''
Using list-dictionary approach (without any inbuild count function)
'''

def duplicate(input_list):
    new_dict, new_list = {},[]

    for i in input_list:
        if not i in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    for key, values in new_dict.items():
        if values > 1:
            new_list.append(key)

    return new_list

if __name__ == "__main__":
    input_list = [1,2,1,2,3,4,1,1,2,5,6,7,8,9,9]
    print(duplicate(input_list))

############################################################################################################

#442

'''
Using in, not in operators and count() method
'''

lis = [1,2,1,2,3,4,1,1,2,5,6,7,8,9,9]
x = []
y = []
for i in lis:
    if i not in x:
        x.append(i)
for i in x:
    if lis.count(i) > 1:
        y.append(i)
print(y)

#############################################################################################################

#443

'''
Using enumerate function
'''

input_list = [1,2,1,2,3,4,1,1,2,5,6,7,8,9,9]

print(list(set([x for i,x in enumerate(input_list) if input_list.count(x) > 1])))

##########################################################################################################

#444

'''
Using operator.countOf() method
'''

import operator as op

list = [1,2,1,2,3,4,1,1,2,5,6,7,8,9,9]

new = []

for a in list:
    #checking the occurances of elements
    n = op.countOf(list,a)

    #if the occurances is more than one we add it to the output list
    if n > 1:
        if op.countOf(new, a) == 0:
            new.append(a)

print(new)

###################################################################################################

#445

'''
Using operator.countOf().in and not in operators
'''

lis = [1,2,1,2,3,4,1,1,2,5,6,7,8,9,9]

x = []
y = []
import operator
for i in lis:
    if i not in x:
        x.append(i)
for i in x:
    if operator.countOf(lis,i) > 1:
        y.append(i)
print(y)

##############################################################################################################

#446

'''
Using numpy
'''

import numpy as np

l1 = [1,2,1,2,3,4,1,1,2,5,6,7,8,9,9]

unique, counts = np.unique(l1, return_counts = True)
new_list = unique[np.where(counts > 1)]
print(new_list)

##################################################################################################################










































































































































































