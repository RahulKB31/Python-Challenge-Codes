#355

'''
Python program to print negative numbers in a list
'''

#using for loop

list1 = [-10,21,-4,-45,-66,93]

#iterating each number in list
for num in list1:
    #checking condition
    if num < 0:
        print(num, end=" ")

###################################################################################################################

#356

'''
Using while loop
'''

list1 = [-10,21,-4,-45,-66,93]
num = 0

#using while loop
while (num < len(list1)):

    #checking condition
    if list1[num] < 0:
        print(list1[num], end=" ")

    #increment num
    num += 1

#############################################################################################################

#357

'''
Using list comprehension
'''

list1 = [-10,21,-4,-45,-66,93]

#using list comprehension
neg_nos = [num for num in list1 if num<0]

print("Negative numbers in the list:", *neg_nos)

#############################################################################################################

#358

'''
Using lambda expressions
'''

list1 = [-10,21,-4,-45,-66,93]

neg_nos = list(filter(lambda x : (x < 0), list1))

print("Negative numbers in the list: ",*neg_nos)

###########################################################################################################

#359

'''
Using enumerate function
'''

l = [12,-7,5,64,-14]
print([a for j,a in enumerate(l) if a<0])

##########################################################################################################

#360

'''
Using startswith() method
'''

list1 = [-10,21,-4,-45,-66,93]
res = []
list2 = list(map(str,list1))
for i in range(0, len(list2)):
    if(list2[i].startswith("-")):
        res.append(str(list1[i]))
res = " ".join(res)
print(res)

###############################################################################################################

#361

'''
Using numpy.array
'''

import numpy as np

list1 = [-10,21,-4,-45,-66,93]

temp = np.array(list1)
neg_nos = temp[temp <= 0]

print("Negative numbers in the list: ", *neg_nos)

#######################################################################################################################

#362

'''
Using recursion
'''

def PrintNegative(itr, list1):
    if itr == len(list1): #base condition
        return
    if list1[itr] < 0: #check negative numbers or not
        print(list1[itr], end=" ")
    PrintNegative(itr+1, list1) #recursive function call

list1 = [-1,8,9,-5,7]
PrintNegative(0,list1)

#######################################################################################################

#363

'''
Using numpy.array() and numpy.where()
'''

import numpy as np

#list of numbes
list1 = [-10,21,-4,-45,-66,93]

#converting list to numpy array
arr1 = np.array(list1)

#finding negative numbers in the array
neg_nums = arr1[np.where(arr1 < 0)]

#printing negative numbers
print("Negative numbers in the list: ", *neg_nums)

############################################################################################################

#364

'''
Using functools.reduce
'''

from functools import reduce

list1 = [-10,21,-4,-45,-66,93]

#using reduce method
neg_nos = reduce(lambda a, b : a + [b] if b < 0 else a, list1, [])

print("Negative numbers in the list: ", *neg_nos)

############################################################################################################































































































































































































































