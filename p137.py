#819

'''
Python - Order Tuples by List
'''

# Using dict() + list comprehension

test_list = [('Gfg', 3), ('best',9),('CS',10), ('Geeks',2)]

print("The original list is : " + str(test_list))

ord_list = ['Geeks','best','CS','Gfg']

temp = dict(test_list)
res = [(key, temp[key]) for key in ord_list]

print('The ordered tuple list: ' + str(res))

###############################################################################################################

#820

'''
Using setdefault() + sorted() + lambda
'''

test_list = [('Gfg', 3), ('best',9),('CS',10), ('Geeks',2)]

print("The original list is : " + str(test_list))

ord_list = ['Geeks','best','CS','Gfg']

temp = dict()
for key, ele in enumerate(ord_list):
    temp.setdefault(ele, []).append(key)

res = sorted(test_list, key = lambda ele: temp[ele[0]].pop())

print("The ordered tuple list: " + str(res))

##################################################################################################################

#821

'''
Using list and index() method
'''

test_list = [('Gfg', 3), ('best',9),('CS',10), ('Geeks',2)]

print("The original list is : " + str(test_list))

ord_list = ['Geeks','best','CS','Gfg']

res = []
x = []
for i in test_list:
    x.append(i[0])
for i in ord_list:
    if i in x:
        res.append(test_list[x.index(i)])

print("The ordered tuple list: " + str(res))

###################################################################################################################

#822

'''
Using lambda
'''

def order_tuples_by_list(test_list, ord_list):
    return sorted(test_list, key = lambda x: ord_list.index(x[0]))

test_list = [('Gfg', 3), ('best',9),('CS',10), ('Geeks',2)]
ord_list = ['Geeks','best','CS','Gfg']
print(order_tuples_by_list(test_list, ord_list))

##################################################################################################################

#823

'''
Using sorted() function with itemgetter() function
'''

from operator import itemgetter

original_list = [('Gfg', 3), ('best',9),('CS',10), ('Geeks',2)]

ordered_list = sorted(original_list, key=itemgetter(1))

print(ordered_list)

#################################################################################################################

#824

'''
Using reduce()
'''

from functools import reduce

test_list = [('Gfg', 3), ('best',9),('CS',10), ('Geeks',2)]

print()

print("The original list is : " + str(test_list))

ord_list = ['Geeks','best','CS','Gfg']

res = reduce(lambda acc, key: acc + [ele for ele in test_list if ele[0] == key], ord_list, [])

print("The ordered tuple list: " + str(res))

####################################################################################################################









































































































































































