#403

'''
Python cloning or copying a list
'''

#using the slicing technique

def cloning(li1):
    li_copy = li1[:]
    return li_copy

li1 = [4,5,6,7,8,34]
li2 = cloning(li1)
print("Original List: ", li1)
print("After cloning:", li2)

##################################################################################################################

#404

'''
Using the extend() method
'''

def cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy

li1 = [4,5,6,7,8,34]
li2 = cloning(li1)
print("Original List: ", li1)
print("After cloning:", li2)

################################################################################################################

#405

'''
LIst copy using assignment operator
'''

def cloning(li1):
    li_copy = li1
    return li_copy

li1 = [4,5,6,7,8,34]
li2 = cloning(li1)
print("Original List: ", li1)
print("After cloning:" ,li2)

########################################################################################################

#406

'''
Using the method of shallow copy
'''

import copy
li1 = [1,2,[3,5],4]

#using copy for shallow copy
li2 = copy.copy(li1)
print(li2)

##########################################################################################################

#407

'''
Using list comprehension
'''

def cloning(li1):
    li_copy = [i for i in li1]
    return li_copy

li1 = [4,5,6,7,8,34]
li2 = cloning(li1)
print("Original List: ", li1)
print("After cloning:" ,li2)

################################################################################################################

#408

'''
Using the append() method
'''

def cloning(li1):
    li_copy = []
    for item in li1:
        li_copy.append(item)
    return li_copy

li1 = [4,5,6,7,8,34]
li2 = cloning(li1)
print("Original List: ", li1)
print("After cloning:", li2)

###############################################################################################################

#409

'''
Using the copy() method
'''

def cloning(li1):
    li_copy = []
    li_copy = li1.copy()
    return li_copy

li1 = [4,5,6,7,8,34]
li2 = cloning(li1)
print("Original List: ", li1)
print("After cloning:", li2)

###########################################################################################################

#410

'''
Using the method of deep copy
'''

import copy

li1 = [1,2,[3,5], 4]

li3 = copy.deepcopy(li1)
print(li3)

##############################################################################################################

#411

'''
Using enumerate function
'''

lst = [4,8,9,45,34,3]

li_copy = [i for a,i in enumerate(lst)]
print("Original List:", lst)
print("After cloning:",li_copy)

#############################################################################################################

#412

'''
Using map function
'''

lst = [4,8,9,45,34,3]
li_copy = map(int,lst)
print("Original list:",lst)
print("After cloning:",*li_copy)

################################################################################################################

#413

'''
Using slice() function
'''

lst = [4,8,9,45,34,3]
li_copy = lst[slice(len(lst))]
print("Original list:", lst)
print("After cloning:", li_copy)

###########################################################################################################

#414

'''
Using the deque() function
'''

from collections import deque

original_list = [4,8,2,10,15,18]

copied_list = deque(original_list)
copied_list = list(copied_list)

print("Original list:", original_list)
print("After cloning:", copied_list)

#######################################################################################################

#415

'''
Using reduce method()
'''

from functools import reduce

def clone_list(li1):
    return reduce(lambda x, y: x + [y], li1, [])

li1 = [4,8,2,10,15,18]
li2 = clone_list(li1)
print("Original list:",li1)
print("After cloning:", li2)

############################################################################################################


























































































































































































































