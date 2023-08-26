#504

'''
Python - Vertical Concatination in Matrix
'''

test_list = [['gfg','good'],['is','for'],['Best']]

print("The original list: " + str(test_list))

res = []
N = 0
while N != len(test_list):
    temp = ''
    for idx in test_list:

        #checking for valid index/column
        try: temp = temp + idx[N]
        except IndexError: pass
    res.append(temp)
    N = N+1

res = [ele for ele in res if ele]

print("List after column  Concatination: " + str(res))

################################################################################################################

#505

'''
Using join() + list_comprehension + zip_longest()
'''

from itertools import zip_longest

test_list = [['gfg','good'],['is','for'],['Best']]

print("The original list: " + str(test_list))

res = ["".join(ele) for ele in zip_longest(*test_list, fillvalue="")]

print("List after column concatination: " + str(res))

###########################################################################################################

#506

'''
Using numpy.transpose() and numpy.ravel()
'''

import numpy as np

test_list = [['gfg','good'],['is','for'],['Best']]

max_len = max(len(sublist) for sublist in test_list)

#pad the list with empty strings to make them the same length
padded_list = [sublist + [''] * (max_len - len(sublist)) for sublist in test_list]

#convert the list tp numpy array
arr = np.array(padded_list)

#use the transpose to switch rows and columns
arr_t = arr.T

#use join to concatinate the strings in each row
res = [''.join(row) for row in arr_t]

print("List after column concatination: " + str(res))

##############################################################################################################






































































































