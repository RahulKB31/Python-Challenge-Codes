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