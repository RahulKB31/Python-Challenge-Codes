#382

'''
Remove multiple elements from a list in Python
'''

list1 = [11,5,17,18,23,50]

#iterate each element in list and add them in variable total
for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)

#prinitng modified list
print("New list after removing all even numbers:", list1)

###########################################################################################################

#383

'''
using list comprehension
'''

list1 = [11,5,17,18,23,50]

#will create a new list excluding all even numbers
list1 = [elem for elem in list1 if elem % 2 != 0]

print(*list1)

###############################################################################################################

#384

'''
Remove adjacent elements using list splicing
'''

list1 = [11,5,17,18,23,50]

#remove elements from index 1 to 4 i.e, 5,17,18,23 will be deleted
del list1[1:5]

print(*list1)

###################################################################################################################

#385

'''
Using list comprehension
'''

list1 = [11,5,17,18,23,50]

#items to be removed
unwanted_num = {11,5}

list1 = [ele for ele in list1 if ele not in unwanted_num]

print("New list after removing unwanted numbers:", list1)

################################################################################################################

#386

'''
When index of elements is known
'''

list1 = [11,5,17,18,23,50]

#given index of elements removes 11,18,23
unwanted = [0,3,4]

for ele in sorted(unwanted, reverse=True):
    del list1[ele]

print(*list1)

################################################################################################################

#387

'''
Using enumerate function
'''

list1 = [11,5,17,18,23,50]

list1 = [elem for i,elem in enumerate(list1) if elem % 2 != 0]

print(list1)

###################################################################################################################

#388

'''
Approach using numpy.delete()
'''

import numpy as np

list1 = [12,15,3, 10]

#convert list to numpy array
arr = np.array(list1)

#indices of elements to be removed
remove_idx = [0,2]

#use numpy.delete() to remove elements
new_arr = np.delete(arr, remove_idx)

#convert numpy array back to list
new_list = new_arr.tolist()

#print the results
print("Removed =", [list1[i] for i in remove_idx],",New_List =", new_list)

####################################################################################################################

























































































































































































































