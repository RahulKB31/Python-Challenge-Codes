<<<<<<< HEAD
#389

'''
Python - Remove empty list from list
'''

# using list comprehension

test_list = [5,6,[],3,[],[],9]

#printing original list
print("The original list is: "+ str(test_list))

#remove empty list from list using list comprehension
res = [ele for ele in test_list if ele != []]

#printing result
print("list after empty list removal:" + str(res))

###############################################################################################################

#390

'''
using filter() method
'''

test_list = [5,6,[],3,[],[],9]

#printing original list
print("The original list is: " + str(test_list))

#removing empty list from list using filter() method
res = list(filter(None, test_list))

#printing the resultant list
print("List after empty list removal: " + str(res))

##########################################################################################################

#391

'''
using function definition
'''

def empty_list_remove(input_list):
    new_list = []
    for ele in input_list:
        if ele:
            new_list.append(ele)
    return new_list

#input list values
input_list = [5,6,[],3,[],[],9]

#print initial list values
print(f"The original list is: {input_list}")

#function-call and print values
print(f"List after empty list removal: {empty_list_remove(input_list)}")

################################################################################################################

#392

'''
Using len() and type() methods if the length is zero then the list is empty
'''

test_list = [5,6,[],3,[],[],9]

#printing original list
print(f"The original list: "+ str(test_list))
new_list = []

#remove empty list from list
for i in test_list:
    x = str(type(i))
    if (x.find('list') != -1):
        if(len(i) != 0):
            new_list.append(i)
        else:
            new_list.append(i)

#printing result
print("List after empty list remval: " + str(new_list))

########################################################################################################

#393

'''
Using remove() method
'''

test_list = [5,6,[],3,[],[],9]

#printing original list
print(f"The riginal list is: " + str(test_list))

#remove empty list from list
while [] in test_list:
    test_list.remove([])

#printing result
print("List after empty list removal: " + str(test_list))

############################################################################################################

#394

'''
Using list(),map(),join() and replace() methods
'''

test_list = [5,6,[],3,[],[],9]

#printing original list
print("The original list is: " + str(test_list))
x = list(map(str,test_list))
y = "".join(x)
y = y.replace("[]","")
y = list(map(int,y))

#printing result
print("list after empty list removal: "+ str(y))

##############################################################################################################

#395

'''
Using enumerate function
'''

test_list = [5,6,[],3,[],[],9]

res = [ele for i,ele in enumerate(test_list) if ele != []]

print(res)

############################################################################################################

#396

'''
Using filter function
'''

test_list = [5,6,[],3,[],[],9]

#printing original list
print("The original list is: "+ str(test_list))

#remove empty list from list
res = filter(None, test_list)

#printing result
print("List after empty list removal: ", res)

#################################################################################################################

#397

'''
Using lambda function
'''

test_list = [5,6,[],3,[],[],9]

print("The origianl list is: " + str(test_list))

#removing an empty list from list using lambda function
res = list(filter(lambda x: x!= [], test_list))

#printing the resultant list
print("List after empty list removal: "+ str(res))

#####################################################################################################################

#398

'''
Using recursion method
'''

def remove_empty(start, oldlist, newlist):
    if start == len(oldlist):
        return newlist
    if oldlist[start] == []:
        pass
    else:
        newlist.append(oldlist[start]) #appending non empty list element to newlist
    return remove_empty(start+1,oldlist,newlist)

test_list = [5,6,[],3,[],[],9]

print("The original list is: " + str(test_list))

result = remove_empty(0, test_list,[])
print("List after emty list removal: ",result)

###################################################################################################################

#399

'''
Using itertools.filterfalse()
'''

import itertools

test_list = [5,6,[],3,[],[],9]

print("The original list is: "+ str(test_list))

#removing empty list from list using lambda function
res = list(itertools.filterfalse(lambda x: x == [], test_list))

print("List after empty list removal: " + str(res))

################################################################################################################

#400

'''
using the map() function
'''

test_list = [5,6,[],3,[],[],9]

print("The original list is: " + str(test_list))

#remove empty list from list using map() function
res = list(map(lambda x: x if x != [] else None, test_list))

res = [x for x in res if x != None]

print("List after empty list removal: "+ str(res))

##############################################################################################################

#401

'''
Using re module
'''

import re

input_list = [5,6,[],3,[],[],9]

print(f"The original list is: {input_list}")

res = list(filter(None, [x for x in input_list if not re.match('\[\]',str(x))]))
print(f"List after empty list removal: {res}")

#################################################################################################################

#402

'''
Using the pop()
'''

test_list = [5,6,[],3,[],[],9]

print("The original list is: " + str(test_list))

i = 0

while i < len(test_list):
    if test_list[i] == []
        test_list.pop(i)
    else:
        i+=1

res = test_list

print("List after empty list removal: "+ str(res))

############################################################################################################



















































































































































































































=======
#389

'''
Python - Remove empty list from list
'''

# using list comprehension

test_list = [5,6,[],3,[],[],9]

#printing original list
print("The original list is: "+ str(test_list))

#remove empty list from list using list comprehension
res = [ele for ele in test_list if ele != []]

#printing result
print("list after empty list removal:" + str(res))

###############################################################################################################

#390

'''
using filter() method
'''

test_list = [5,6,[],3,[],[],9]

#printing original list
print("The original list is: " + str(test_list))

#removing empty list from list using filter() method
res = list(filter(None, test_list))

#printing the resultant list
print("List after empty list removal: " + str(res))

##########################################################################################################

#391

'''
using function definition
'''

def empty_list_remove(input_list):
    new_list = []
    for ele in input_list:
        if ele:
            new_list.append(ele)
    return new_list

#input list values
input_list = [5,6,[],3,[],[],9]

#print initial list values
print(f"The original list is: {input_list}")

#function-call and print values
print(f"List after empty list removal: {empty_list_remove(input_list)}")

################################################################################################################

#392

'''
Using len() and type() methods if the length is zero then the list is empty
'''

test_list = [5,6,[],3,[],[],9]

#printing original list
print(f"The original list: "+ str(test_list))
new_list = []

#remove empty list from list
for i in test_list:
    x = str(type(i))
    if (x.find('list') != -1):
        if(len(i) != 0):
            new_list.append(i)
        else:
            new_list.append(i)

#printing result
print("List after empty list remval: " + str(new_list))

########################################################################################################

#393

'''
Using remove() method
'''

test_list = [5,6,[],3,[],[],9]

#printing original list
print(f"The riginal list is: " + str(test_list))

#remove empty list from list
while [] in test_list:
    test_list.remove([])

#printing result
print("List after empty list removal: " + str(test_list))

############################################################################################################

#394

'''
Using list(),map(),join() and replace() methods
'''

test_list = [5,6,[],3,[],[],9]

#printing original list
print("The original list is: " + str(test_list))
x = list(map(str,test_list))
y = "".join(x)
y = y.replace("[]","")
y = list(map(int,y))

#printing result
print("list after empty list removal: "+ str(y))

##############################################################################################################

#395

'''
Using enumerate function
'''

test_list = [5,6,[],3,[],[],9]

res = [ele for i,ele in enumerate(test_list) if ele != []]

print(res)

############################################################################################################

#396

'''
Using filter function
'''

test_list = [5,6,[],3,[],[],9]

#printing original list
print("The original list is: "+ str(test_list))

#remove empty list from list
res = filter(None, test_list)

#printing result
print("List after empty list removal: ", res)

#################################################################################################################

#397

'''
Using lambda function
'''

test_list = [5,6,[],3,[],[],9]

print("The origianl list is: " + str(test_list))

#removing an empty list from list using lambda function
res = list(filter(lambda x: x!= [], test_list))

#printing the resultant list
print("List after empty list removal: "+ str(res))

#####################################################################################################################

#398

'''
Using recursion method
'''

def remove_empty(start, oldlist, newlist):
    if start == len(oldlist):
        return newlist
    if oldlist[start] == []:
        pass
    else:
        newlist.append(oldlist[start]) #appending non empty list element to newlist
    return remove_empty(start+1,oldlist,newlist)

test_list = [5,6,[],3,[],[],9]

print("The original list is: " + str(test_list))

result = remove_empty(0, test_list,[])
print("List after emty list removal: ",result)

###################################################################################################################

#399

'''
Using itertools.filterfalse()
'''

import itertools

test_list = [5,6,[],3,[],[],9]

print("The original list is: "+ str(test_list))

#removing empty list from list using lambda function
res = list(itertools.filterfalse(lambda x: x == [], test_list))

print("List after empty list removal: " + str(res))

################################################################################################################

#400

'''
using the map() function
'''

test_list = [5,6,[],3,[],[],9]

print("The original list is: " + str(test_list))

#remove empty list from list using map() function
res = list(map(lambda x: x if x != [] else None, test_list))

res = [x for x in res if x != None]

print("List after empty list removal: "+ str(res))

##############################################################################################################

#401

'''
Using re module
'''

import re

input_list = [5,6,[],3,[],[],9]

print(f"The original list is: {input_list}")

res = list(filter(None, [x for x in input_list if not re.match('\[\]',str(x))]))
print(f"List after empty list removal: {res}")

#################################################################################################################

#402

'''
Using the pop()
'''

test_list = [5,6,[],3,[],[],9]

print("The original list is: " + str(test_list))

i = 0

while i < len(test_list):
    if test_list[i] == []
        test_list.pop(i)
    else:
        i+=1

res = test_list

print("List after empty list removal: "+ str(res))

############################################################################################################



















































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
