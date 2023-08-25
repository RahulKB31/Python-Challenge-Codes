#799

'''
Python - Extract digits from Tuple list
'''

# Using map() + chain.from_iterable() + set() + loop

from itertools import chain

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

temp = map(lambda ele: str(ele), chain.from_iterable(test_list))

res = set()
for sub in temp:
    for ele in sub:
        res.add(ele)

print("The extracted digits: " + str(res))

################################################################################################################

#800

# Using Regex Expression

import re

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

temp = re.sub(r'[\[\]\(\), ]', '', str(test_list))
res = [int(ele) for ele in set(temp)]

print("The extracted digits: " + str(res))

#################################################################################################################

#801

'''
Using list(), str(), map(), set() methods
'''

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

x = ""

for i in test_list:
    for j in i:
        x += str(j)
res = list(map(int,set(x)))

print("The extracted digits: " + str(res))

#################################################################################################################

#802

'''
Using list comprehension
'''

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

temp = ''.join([str(i) for sublist in test_list for i in sublist])

result = set(temp)
result = [int(i) for i in result]

print("The extracted digits: " + str(list(result)))

#################################################################################################################

#803

'''
Using reduce and set
'''

from functools import reduce

tup_list = [(15,3),(3,9),(1,10),(99,2)]

digit_list = set(reduce(lambda a,b: str(a) + str(b), tup) for tup in tup_list)
digit_list = set(digit for string in digit_list for digit in string)

print("The original list is:", tup_list)
print("The extracted digits:", digit_list)

#################################################################################################################

#804

'''
Using heapq
'''

import heapq

test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]

print("The original list is: " + str(test_list))

result = []
for tpl in test_list:
    result.extend(list(tpl))

heapq.heapify(result)

unique_digits = set()
while result:
    digits = str(heapq.heapify(result))
    for digit in digits:
        unique_digits.add(int(digit))

print('The extracted digits: ' + str(list(unique_digits)))

##############################################################################################################






























































































































































