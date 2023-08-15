#498

'''
Python | Get Kth Column of Matrix
'''

# Using list comprehension

test_list = [[1,2,3],[4,5,6],[6,7,8]]

print("The original list is: " +str(test_list))

K = 2

res = [sub[K] for sub in test_list]

print("The Kth column of matrix is: " + str(res))

#########################################################################################################

#499

'''
Using zip
'''

test_list = [[1,2,3],[4,5,6],[6,7,8]]

print("The original list is: " +str(test_list))

K = 2

res = list(zip(*test_list)[K])

print("The Kth column of matrix is: " + str(res))

###############################################################################################################

#500

'''
Using Numpy
'''

import numpy as np

test_list = [[1,2,3],[4,5,6],[6,7,8]]

print("The original list is: " +str(test_list))

K = 2

res = np.array(test_list)[:,K]

print("The Kth column of matrix is: " + str(res))

#############################################################################################################

#501

'''
Using a for loop
'''

test_list = [[1,2,3],[4,5,6],[6,7,8]]

K = 2

res = []

for i in range(len(test_list)):
    res.append(test_list[i][K])

print("The Kth column of matrix is: " + str(res))

#############################################################################################################

#502

'''
Using the built-in function map()
'''

test_list = [[1,2,3],[4,5,6],[6,7,8]]

print("The original list is: " +str(test_list))

K = 2

res = list(map(lambda x: x[K], test_list))

print("The Kth column of matrix is: " + str(res))

#############################################################################################################

#503

'''
Using list slicing
'''

test_list = [[1,2,3],[4,5,6],[6,7,8]]

print("The original list is: " +str(test_list))

K = 2

res = [row[K] for row in test_list]

print("The Kth column of matrix is: " + str(res))

####################################################################################################























































































































































































