#416

'''
Python | count occurances of an element in a list
'''

#using a loop

def count(lst,x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

lst = [8,6,8,10,8,20,10,8,8]
x = 8
print('{} has occured {} times'.format(x, count(lst,x)))

####################################################################################################################

#417

'''
Using count()
'''

def countX(lst, x):
    return lst.count(x)

lst = [8,6,8,10,8,20,10,8,8]
x = 8
print('{} has occured {} times'.format(x, count(lst,x)))

##########################################################################################################

#418

'''
Using counter()
'''

from collections import Counter

l = [1,1,2,2,3,3,4,4,5,5,6,6]

x = 3
d = Counter(l)
print('{} has occured {} times'.format(x,d[x]))

############################################################################################################

#419

'''
Using countof()
'''

import operator as op

l = [1,1,2,2,3,3,4,4,5,5,6,6]

x = 2
print(f"{x} has occured {op.countOf(1, x)} times")

##########################################################################################################


#420

'''
Count occurances of an element in a list using dictionary comprehension
'''

lis = ['a','b','d', 'c','a','c','b']

occurances = {item: lis.count(item) for item in lis}
print(occurances.get("a"))

##########################################################################################################

#421

'''
Using the pandas library
'''

import pandas as pd

l = [1,1,2,2,3,3,4,4,5,5,6,6]

count = pd.Series(l).value_counts()
print("Element count")
print(count)

########################################################################################################

#422

'''
Using list comprehension
'''

l = [1,1,2,2,3,3,4,4,5,5,6,6]
ele = 1
x = [i for i in l if i==ele]
print("The element",ele,"occurs",len(x),"times")

###########################################################################################################

#423

'''
Using enumerate function
'''

l = [1,1,2,2,3,3,4,4,5,5,6,6]
ele = 1
x = [i for j,i in enumerate(l) if i==ele]
print("The element",ele,"occurs",len(x),"times")

###############################################################################################################


















































































































































































































