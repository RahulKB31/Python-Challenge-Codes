#185

'''
How to find the length of a list in Python
'''

# Get the length of a list in Python using len()

li = [10,20,30]
n = len(li)
print("The length of list is:",n)

####################################################################################################

#186

'''
Find the length of a list in Python Naive Method
'''

# Initializing list
test_list = [1,4,5,7,8]

# Printing test_list
print("The list is:" + str(test_list))

# Finding length of list using loop
# Intializing counter
counter = 0
for i in test_list:
    # incrementing counter
    counter = counter + 1

# printing length of list
print("Length of list using naive method is: " + str(counter))

#########################################################################################################

#187

'''
Find the length of a list in Python using length_hint()
'''

# Using len() and length_hint
from operator import length_hint

# Initializing list
test_list = [1,4,5,7,8]

# Printing test_list
print("The list is: " + str(test_list))

# Finding length of list using len()
list_len = len(test_list)

# Finding length of list using length_hint()
list_len_hint = length_hint(test_list)

#printing length of list
print("Length of list using len() is: " + str(list_len))
print("Length of list using length_hint() is: " + str(list_len_hint))

########################################################################################################

#188

























































