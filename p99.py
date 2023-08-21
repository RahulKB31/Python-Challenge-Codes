#668

'''
Python -Extract Unique values dictionary values
'''

test_dict = { 'gfg' : [5,6,7,8],
              'is' : [10,11,7,5],
              'best' : [6,12,10,8],
              'for' : [1,2,5]
}

print("the oroginal dictionary is: " + str(test_dict))

res = list(sorted({ele for val in test_dict.values() for ele in val}))

print("The unique value list is: " + str(res))

###############################################################################################################

#669

'''
Extract unique values dictionary values using chain() + sorted() + values()
'''

from itertools import chain

test_dict = { 'gfg' : [5,6,7,8],
              'is' : [10,11,7,5],
              'best' : [6,12,10,8],
              'for' : [1,2,5]
}

print("the original dictionary is: " + str(test_dict))

res = list(sorted(set(chain(*test_dict.values()))))

print("The unique value list is: " + str(res))

##############################################################################################################

#670

'''
Extract unique values dictionary values using extend() and sort() methods
'''

test_dict = { 'gfg' : [5,6,7,8],
              'is' : [10,11,7,5],
              'best' : [6,12,10,8],
              'for' : [1,2,5]
}

print("the original dictionary is: " + str(test_dict))

x = list(test_dict.values())
y = []
res = []
for i in x:
    y.extend(i)
for i in y:
    if i not in res:
        res.append(i)
res.sort()

print("The unique values list is: " + str(res))

#################################################################################################################

#671

'''
Extarct unique values dictionary values using counter(),append() and sort() methods
'''

from collections import Counter

test_dict = { 'gfg' : [5,6,7,8],
              'is' : [10,11,7,5],
              'best' : [6,12,10,8],
              'for' : [1,2,5]
}

print("the original dictionary is: " + str(test_dict))

valuesList = []
for key, values in test_dict.items():
    for value in values:
        valuesList.append(value)
freq = Counter(valuesList)
uniqueValues = list(freq.keys())
uniqueValues.sort()

print("The unique values list is: " + str(uniqueValues))

#############################################################################################################

#672

'''
Extract unique values dictionary values operator.countOf() method
'''

import operator as op

test_dict = { 'gfg' : [5,6,7,8],
              'is' : [10,11,7,5],
              'best' : [6,12,10,8],
              'for' : [1,2,5]
}

print("the original dictionary is: " + str(test_dict))

x = list(test_dict.values())
y = []
res = []
for i in x:
    y.extend(i)
for i in y:
    if op.countOf(res,i) == 0:
        res.append(i)
res.sort()

print("The unique values list is: " + str(res))

###################################################################################################################

#673

'''
Extract unique values dictionary values using set() + sum()
'''

test_dict = { 'gfg' : [5,6,7,8],
              'is' : [10,11,7,5],
              'best' : [6,12,10,8],
              'for' : [1,2,5]
}

print("the original dictionary is: " + str(test_dict))

result = list(set(sum(test_dict.values(), [])))

print("The unique values list is: " + str(result))

####################################################################################################################






















































































































































