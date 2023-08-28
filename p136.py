<<<<<<< HEAD
#814

'''
Python programs to sort a list of tuples by second item
'''

# Using the bubble sort

def Sort_Tuple(tup):

    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j+1][1]):
                temp = tup[j]
                tup[j] = tup[j+1]
                tup[j+1] = temp
    return tup

tup = [('for', 24),('is',10),('Geeks',28),('Geeksforgeeks',5),('portal',20), ('a',15)]

print(Sort_Tuple(tup))

################################################################################################################

#815

'''
Using sort() method
'''

def Sort_Tuple(tup):
    tup.sort(key = lambda x: x[1])
    return tup

tup = [('rishav',10), ('akash',5),('ram',20),('gaurav',15)]

print(Sort_Tuple(tup))

#################################################################################################################

#816

'''
Using sorted() method
'''

def Sort_Tuple(tup):

    return(sorted(tup, key = lambda x:x[1]))

tup = [('rishav',10), ('akash',5),('ram',20),('gaurav',15)]

print(Sort_Tuple(tup))

#################################################################################################################

#817

'''
Using the itemgetter function from the operator module
'''

from operator import itemgetter

def sort_tuples(tuples):
    return sorted(tuples, key=itemgetter(1))

tuples = [('rishav',10), ('akash',5),('ram',20),('gaurav',15)]

print(sort_tuples(tuples))

################################################################################################################

#818

'''
Using numpy.argsort() function
'''

import numpy as np

def sort_tuple(tup):
    arr = np.array(tup, dtype=[('col1',object),('col2', int)])
    indices = np.argsort(arr['col2'])
    sorted_arr = arr[indices]
    sorted_tup = [(row['col1'], row['col2']) for row in sorted_arr]

    return sorted_tup

tup = [('rishav',10), ('akash',5),('ram',20),('gaurav',15)]

print(sort_tuple(tup))

#################################################################################################################



































































































































































































=======
#814

'''
Python programs to sort a list of tuples by second item
'''

# Using the bubble sort

def Sort_Tuple(tup):

    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j+1][1]):
                temp = tup[j]
                tup[j] = tup[j+1]
                tup[j+1] = temp
    return tup

tup = [('for', 24),('is',10),('Geeks',28),('Geeksforgeeks',5),('portal',20), ('a',15)]

print(Sort_Tuple(tup))

################################################################################################################

#815

'''
Using sort() method
'''

def Sort_Tuple(tup):
    tup.sort(key = lambda x: x[1])
    return tup

tup = [('rishav',10), ('akash',5),('ram',20),('gaurav',15)]

print(Sort_Tuple(tup))

#################################################################################################################

#816

'''
Using sorted() method
'''

def Sort_Tuple(tup):

    return(sorted(tup, key = lambda x:x[1]))

tup = [('rishav',10), ('akash',5),('ram',20),('gaurav',15)]

print(Sort_Tuple(tup))

#################################################################################################################

#817

'''
Using the itemgetter function from the operator module
'''

from operator import itemgetter

def sort_tuples(tuples):
    return sorted(tuples, key=itemgetter(1))

tuples = [('rishav',10), ('akash',5),('ram',20),('gaurav',15)]

print(sort_tuples(tuples))

################################################################################################################

#818

'''
Using numpy.argsort() function
'''

import numpy as np

def sort_tuple(tup):
    arr = np.array(tup, dtype=[('col1',object),('col2', int)])
    indices = np.argsort(arr['col2'])
    sorted_arr = arr[indices]
    sorted_tup = [(row['col1'], row['col2']) for row in sorted_arr]

    return sorted_tup

tup = [('rishav',10), ('akash',5),('ram',20),('gaurav',15)]

print(sort_tuple(tup))

#################################################################################################################



































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
