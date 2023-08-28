<<<<<<< HEAD
#809

'''
Python - Remove Tuples of length K
'''

test_list = [(4,5), (4,), (8,6,7), (1,), (3,4,6,7)]

print('The original list: ' + str(test_list))

K = 1

res = [ele for ele in test_list if len(ele) != K]
print("Filtered list: " + str(res))

################################################################################################################

#810

'''
Using filter() + lambda + len()
'''

test_list = [(4,5), (4,), (8,6,7), (1,), (3,4,6,7)]

print('The original list: ' + str(test_list))

K = 1

res = list(filter(lambda x: len(x) != K, test_list))

print("Filtered list: " + str(res))

 ###############################################################################################################

#811

'''
Using a loop
'''

test_list = [(4,5), (4,), (8,6,7), (1,), (3,4,6,7)]

print('The original list: ' + str(test_list))

K = 1

res = [ele for ele in test_list if len(ele) != K]

print("Filtered list: " + str(res))

################################################################################################################

#812

'''
Using map() and lambda function
'''

original_list = [(4,5), (4,), (8,6,7), (1,), (3,4,6,7)]
K = 1

filtered_list = list(map(lambda x: x, filter(lambda x: len(x) != K, original_list)))

print(filtered_list)

##################################################################################################################

#813

'''
Using heapq
'''

import heapq

test_list = [(4,5), (4,), (8,6,7), (1,), (3,4,6,7)]

print('The original list: ' + str(test_list))

K = 1

res = list(filter(lambda x: len(x) != K, test_list))

print(filtered_list)

#################################################################################################################



















































































































































































=======
#809

'''
Python - Remove Tuples of length K
'''

test_list = [(4,5), (4,), (8,6,7), (1,), (3,4,6,7)]

print('The original list: ' + str(test_list))

K = 1

res = [ele for ele in test_list if len(ele) != K]
print("Filtered list: " + str(res))

################################################################################################################

#810

'''
Using filter() + lambda + len()
'''

test_list = [(4,5), (4,), (8,6,7), (1,), (3,4,6,7)]

print('The original list: ' + str(test_list))

K = 1

res = list(filter(lambda x: len(x) != K, test_list))

print("Filtered list: " + str(res))

 ###############################################################################################################

#811

'''
Using a loop
'''

test_list = [(4,5), (4,), (8,6,7), (1,), (3,4,6,7)]

print('The original list: ' + str(test_list))

K = 1

res = [ele for ele in test_list if len(ele) != K]

print("Filtered list: " + str(res))

################################################################################################################

#812

'''
Using map() and lambda function
'''

original_list = [(4,5), (4,), (8,6,7), (1,), (3,4,6,7)]
K = 1

filtered_list = list(map(lambda x: x, filter(lambda x: len(x) != K, original_list)))

print(filtered_list)

##################################################################################################################

#813

'''
Using heapq
'''

import heapq

test_list = [(4,5), (4,), (8,6,7), (1,), (3,4,6,7)]

print('The original list: ' + str(test_list))

K = 1

res = list(filter(lambda x: len(x) != K, test_list))

print(filtered_list)

#################################################################################################################



















































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
