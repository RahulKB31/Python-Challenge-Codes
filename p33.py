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

'''
Find the length of a list in Python using sum()
'''

# Initializing list

test_list = [1,4,5,7,8]

#printing test_list
print("The list is: " + str(test_list))

#finding length of list using sum()
list_len = sum(1 for i in test_list)

#printing length of list
print("Length of list using len() is: " + str(list_len))
print("Length of list using length_hint() is: " + str(list_len))

###############################################################################################################

#189

'''
Find the length of a list in Python using a list comprehension
'''

#Define the list to be used for the demonstration
test_list = [1,4,5,7,8]

#calculate the length of the list using a list comprehension and the sum function
#The list comprehension generates a sequence of ones for each element in the list
#The sum function then sums all the ones to give the length of the list

length = sum(1 for _ in test_list)

#print the length of the list
print("Length of list using list comprehension is: ", length)

################################################################################################################

#190

'''
Find the length of a list in python using recursion
'''

#define a function to count the number of elements in a list using recursion
def count_elements_recursion(lst):
    # base case: if the list is empty, return 0
    if not lst:
        return 0
    #recursive case: add 1 to the count of the remaining elements in the list
    return 1 + count_elements_recursion(lst[1:])

#test the function with a sample list
lst = [1,2,3,4,5]
print("The length of the list is: ", count_elements_recursion(lst))

###########################################################################################################

#191

'''
Find the length of a list in python using enumerate function
'''

list1 = [1,4,5,7,8]
s = 0
for i,a in enumerate(list1):
    s += 1
print(s)

################################################################################################################

#192

'''
Find the length of a list in python using collections
'''

from collections import Counter

#Initializing list
test_list = [1,4,5,7,8]

#Finding length of list using counter()
list_len = sum(Counter(test_list).values())

print("Length of list using Counter() is:", list_len)

#########################################################################################################

#193

'''
Naive vs Python len() vs Python length_hint()
'''

from operator import length_hint
import time

#Initializing list
test_list = [1,4,5,7,8]

#printing test_list
print("The lis is:" + str(test_list))

#finding length of list using loop
#Initializing counter
start_time_naive = time.time()
counter = 0
for i in test_list:
    # Incrementing counter
    counter = counter + 1
end_time_naive = str(time.time() - start_time_naive)

# Finding length of list using len()
start_time_len = time.time()
list_len = len(test_list)
end_time_len = str(time.time() - start_time_len)

# finding length of list using length_hint()
start_time_hint = time.time()
list_len_hint = length_hint(test_list)
end_time_hint = str(time.time() - start_time_hint)

#printing times of each
print("Time taken using naive method is: " + end_time_naive)
print("Time taken using len() is: " + end_time_len)
print("Time taken using length_hint() is: " + end_time_hint)

#######################################################################################################


















































