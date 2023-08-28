<<<<<<< HEAD
#346

'''
Python program to print positive numbers in a list
'''

list1 = [11,-21,0,45,66,-93]

#iterating each number in list
for num in list1:

    #checking condition
    if num == 0:
        print(num, end=" ")

####################################################################################################################

#347

'''
Using while loop
'''

list1 = [-10,21,-4,-45,-66,93]
num = 0

#using while loop
while(num< len(list1)):

    #checking condition
    if list1[num] >= 0:
        print(list1[num], end=" ")

    #increment num
    num += 1

################################################################################################################

#348

'''
Using list comprehension
'''

list1 = [-10,21,-4,-45,-66,93]

#using list comprehension
pos_nos = [num for num in list1 if num >= 0]

print("Positive numbers in the list: ", *pos_nos)

################################################################################################################

#349

'''
Using lambda expressions
'''

list1 = [-10,21,-4,-45,-66,93]

#we can also print positive no's using lambda expressions
pos_nos = list(filter(lambda x: (x>= 0),list1))

print("Positive numbers in the list: ",*pos_nos)

##############################################################################################################

#350

'''
Using enumerate function
'''

l = [12,-7,5,64,-14]
print([a for j,a in enumerate(l) if a>=0])

#############################################################################################################

#351

'''
Using startswith() method
'''

list1 = [-10,21,-4,-45,-66,93]
res = []
list2 = list(map(str,list1))
for i in range(0,len(list2)):
    if (not list2[i].startswith("-") and list2[i] != "0"):
        res.append(str(list1[i]))
    res = " ".join(res)
    print(res)

##############################################################################################################

#352

'''
Using numpy array
'''

import numpy as np

list1 = np.array([-10,21,-4,-45,-66,93])

#using numpy array
pos_nos = list1[list1 >=0]

print("Positive numbers in the list: ", *pos_nos)

##########################################################################################################

#353

'''
Using recursion
'''

def PrintEVen(itr,list1):
    if itr == len(list1): #base condition
        return
    if list1[itr] >= 0:
        print(list1[itr], end=" ")
    PrintEVen(itr+1, list1)
    return

list1 = [-5,7,-19,10,9]
PrintEVen(0,list1)

##################################################################################################################

#354

'''
Using operator.ge()
'''

list1 = [-10,21,4,-45,-66,93,11]

import operator
pos_nos = []
for i in list1:
    if operator.ge(i,0):
        pos_nos.append(i)

print("Positive numbers in the list:", pos_nos)

###################################################################################################################






























































































































































































































=======
#346

'''
Python program to print positive numbers in a list
'''

list1 = [11,-21,0,45,66,-93]

#iterating each number in list
for num in list1:

    #checking condition
    if num == 0:
        print(num, end=" ")

####################################################################################################################

#347

'''
Using while loop
'''

list1 = [-10,21,-4,-45,-66,93]
num = 0

#using while loop
while(num< len(list1)):

    #checking condition
    if list1[num] >= 0:
        print(list1[num], end=" ")

    #increment num
    num += 1

################################################################################################################

#348

'''
Using list comprehension
'''

list1 = [-10,21,-4,-45,-66,93]

#using list comprehension
pos_nos = [num for num in list1 if num >= 0]

print("Positive numbers in the list: ", *pos_nos)

################################################################################################################

#349

'''
Using lambda expressions
'''

list1 = [-10,21,-4,-45,-66,93]

#we can also print positive no's using lambda expressions
pos_nos = list(filter(lambda x: (x>= 0),list1))

print("Positive numbers in the list: ",*pos_nos)

##############################################################################################################

#350

'''
Using enumerate function
'''

l = [12,-7,5,64,-14]
print([a for j,a in enumerate(l) if a>=0])

#############################################################################################################

#351

'''
Using startswith() method
'''

list1 = [-10,21,-4,-45,-66,93]
res = []
list2 = list(map(str,list1))
for i in range(0,len(list2)):
    if (not list2[i].startswith("-") and list2[i] != "0"):
        res.append(str(list1[i]))
    res = " ".join(res)
    print(res)

##############################################################################################################

#352

'''
Using numpy array
'''

import numpy as np

list1 = np.array([-10,21,-4,-45,-66,93])

#using numpy array
pos_nos = list1[list1 >=0]

print("Positive numbers in the list: ", *pos_nos)

##########################################################################################################

#353

'''
Using recursion
'''

def PrintEVen(itr,list1):
    if itr == len(list1): #base condition
        return
    if list1[itr] >= 0:
        print(list1[itr], end=" ")
    PrintEVen(itr+1, list1)
    return

list1 = [-5,7,-19,10,9]
PrintEVen(0,list1)

##################################################################################################################

#354

'''
Using operator.ge()
'''

list1 = [-10,21,4,-45,-66,93,11]

import operator
pos_nos = []
for i in list1:
    if operator.ge(i,0):
        pos_nos.append(i)

print("Positive numbers in the list:", pos_nos)

###################################################################################################################






























































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
