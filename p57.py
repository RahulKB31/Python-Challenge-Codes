#447

'''
Python program to find cumulative sum of a list
'''

def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]

lists = [10,20,30,40,50]
print(Cumulative(lists))

#############################################################################################################

#448

list = [10,20,30,40,50]
new_list = []
j = 0
for i in range(0, len(list)):
    j += list[i]
    new_list.append(i)

print(new_list)

############################################################################################################

#449

'''
Using itertools module
'''

from itertools import accumulate

import operator

def cumulative_sum(input_list):
    #use accumulate() function to perform a cumulative sum of the elements in the list
    cumulative_sum_iter = accumulate(input_list, operator.add)
    #convert the iterator to a list and return it
    return list(cumulative_sum_iter)

input_list = [10,20,30,40,50]
output_list = cumulative_sum(input_list)
print(output_list)

############################################################################################################

#450

'''
Using numpy.cumsum()
'''

import numpy as np

def cumulative_sum(input_list):
    #convert the list to a NumPy array
    input_array = np.array(input_list)
    #compute the cumulative sum along the first axis of the array
    cumulative_sum_array = np.cumsum(input_array)
    #convert the NumP array back to a list and return it
    return cumulative_sum_array.tolist()

input_list = [10,20,30,40,50]
output_list = cumulative_sum(input_list)
print(output_list)

###############################################################################################################

#451

'''
Using counter method
'''

from collections import Counter

def cumulative_sum(lst):
    cnt = Counter(lst)
    cum_sum = [lst[0]]
    for i in range(1, len(lst)):
        cum_sum.append(cum_sum[i-1] + lst[i])
    return cum_sum

lst = [10,20,30,40,50]
result = cumulative_sum(lst)
print(result)

##############################################################################################################







































































































