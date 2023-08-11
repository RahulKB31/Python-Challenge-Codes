#202

'''
Different ways to clear a list in Python
'''

# Using clear() method

#creating list
GEEK = [6,0,4,1]
print("GEEK before clear:", GEEK)

#clearing list
GEEK.clear()
print("GEEK after clear:", GEEK)

################################################################################################################

#203

'''
Reinitializing the list
'''

#Initializing lists
list1 = [1,2,3]
list2 = [5,6,7]

#Printing list1 before deleting
print("List1 before deleting is: "+ str(list1))

#Deleting list using clear()
list1.clear()

#printing list1 after clearing
print("List1 after clearing using clear(): " + str(list1))

#printing list2 before deleting
print("List2 before deleting is: " + str(list2))

#deleting list using reinitialization
print("Lists after clearing using reinitialization : " + str(list2))

######################################################################################################

#204

'''
Using "*=0": This is a lesser known method but this method removes all elements of the list and makes it empty
'''

# Initializing lists
list1 = [1,2,3]
list2 = [5,6,7]

#printing list1 before deleting
print("List1 before deleting is: " + str(list1))

#deleting list using clear()
list1.clear()

#printing list1 after clearing
print("List1 after clearing using clear(): " + str(list1))

#printing list2 before deleting
print("List2 before deleting is: "+ str(list2))

#deleting list using reinitialization
list2 = []

#Printing list2 after reinitialization
print("List2 after clearing using reinitialization: " + str(list2))

#######################################################################################################

#205

'''
Using del
'''

#Initializing lists
list1 = [1,2,3]
list2 = [5,6,7]

#printing list1 before deleting
print("List1 before deleting is: " + str(list1))

#Deleting list1 using del
del list1[:]
print("List1 after clearing using del: " + str(list1))

#Printing list2 before deleting
print("List2 before deleting is: " + str(list2))

#deleting list using del
del list2[:]
print("List2 after clearing using del: " + str(list2))

###########################################################################################################

#206

'''
Using pop() method
'''

#Initializing lists
list1 = [1,2,3]

#printing list1 before deleting
print("List1 before deleting is: " + str(list1))

#deleting list1
while (len(list1) != 0):
    list1.pop()
print("List1 after clearing using del: " + str(list1))

###########################################################################################################

#207

'''
Using slicing
'''

#Initializing list
lst = [1,2,3,4,5]

#clearing list using slicing
lst = lst[:0]
print(lst)  #Output: []

#########################################################################################################

#208

'''
Assigning an empty list to clear a list
'''

#Initializing lists
list1 = [1,2,3]

#printing list1 before deleting
print("List1 before deleting is: " + str(list1))

#clearing list1 by assigning an empty list
list1 = []
print("List1 after clearing using an empty list: " + str(list1))

############################################################################################################







































































































































































































































































































