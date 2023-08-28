<<<<<<< HEAD
#194

'''
Check if element exists in list in Python
'''

# Check if an element exists in the list using the in statement

lst = [1,6,3,5,3,4]

#checking if element 7 is present in the given list or not
i = 7

#if element present then return exist otherwise not exist
if i in lst:
    print("exist")
else:
    print("not exist")

#############################################################################################################

#195

'''
Find if an element exists in the list using a loop
'''

#Initializing list
test_list = [1,6,3,5,3,4]

#checking if 4 exists in list
for i in test_list:
    if (i==4):
        print("Element Exists")

############################################################################################################

#196

'''
Check if an element exists in the list using any() function
'''

# Initializing list
test_list = [1,6,3,5,3,4]

result = any(item in test_list for item in test_list)
print("Does string contain any list element: " + str(bool(result)))

###########################################################################################################

#197

'''
Find if any element exists in the list using the count() function
'''

#Initializing list
test_list = [10,15,20,7,46,2808]

print('Checking if 15 exists in list')

#number of times element exists in list
exist_count = test_list.count(15)

#checking if it is more than 0
if exist_count > 0:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")

########################################################################################################

#198

'''
Check if an element exists in the list using sort with bisect_left and set
'''

from bisect import bisect_left, bisect

#Initializing list
test_list_set = [1,6,3,5,3,4]
test_list_bisect = [1,6,3,5,3,4]

print("Checking if 4 exists in list (using set() + in): ")

# Checking if 4 exists in list using set() + in
test_list_set = set(test_list_set)
if 4 in test_list_set:
    print("Element Exists")

print("Checking if 4 exists in list (using sort() + bisect_left()): ")

# Checking if 4 exists in list using sort() + bisect_left()
test_list_bisect.sort()
if bisect_left(test_list_bisect, 4) != bisect(test_list_bisect,4):
    print("Element exist")
else:
    print("Elelement doesnt exist")

#############################################################################################################

#199

'''
Check if an element exists in list using find() method
'''

#Inititalizing list
test_list = [10,15,20,7,46,2808]

print("Checking if 15 exists in list")
x = list(map(str, test_list))
y = "-".join(x)

if y.find("15") != -1:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")

#########################################################################################################

#200

'''
Check if element exists in list using Counter() function
'''

from collections import Counter

test_list = [10,15,20,7,46,2808]

#calculating frequencies
frequency = Counter(test_list)

# If the element has frequency greater than 0 then it exist else it doesn't exist
if (frequency[15] > 0):
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")

############################################################################################################

#201

'''
Find if an element exists in list using try-except block
'''

def element_exists(lst, element):
    #try to get the index of the element in the list
    try:
        lst.index(element)
        # IF the element is found, return True
        return True
    except ValueError:
        #Return false in this case
        return False

#test the function
test_list = [1,6,3,5,3,4]

print(element_exists(test_list, 3)) #prints True
print(element_exists(test_list, 7)) #prints False

#########################################################################################################































































































































=======
#194

'''
Check if element exists in list in Python
'''

# Check if an element exists in the list using the in statement

lst = [1,6,3,5,3,4]

#checking if element 7 is present in the given list or not
i = 7

#if element present then return exist otherwise not exist
if i in lst:
    print("exist")
else:
    print("not exist")

#############################################################################################################

#195

'''
Find if an element exists in the list using a loop
'''

#Initializing list
test_list = [1,6,3,5,3,4]

#checking if 4 exists in list
for i in test_list:
    if (i==4):
        print("Element Exists")

############################################################################################################

#196

'''
Check if an element exists in the list using any() function
'''

# Initializing list
test_list = [1,6,3,5,3,4]

result = any(item in test_list for item in test_list)
print("Does string contain any list element: " + str(bool(result)))

###########################################################################################################

#197

'''
Find if any element exists in the list using the count() function
'''

#Initializing list
test_list = [10,15,20,7,46,2808]

print('Checking if 15 exists in list')

#number of times element exists in list
exist_count = test_list.count(15)

#checking if it is more than 0
if exist_count > 0:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")

########################################################################################################

#198

'''
Check if an element exists in the list using sort with bisect_left and set
'''

from bisect import bisect_left, bisect

#Initializing list
test_list_set = [1,6,3,5,3,4]
test_list_bisect = [1,6,3,5,3,4]

print("Checking if 4 exists in list (using set() + in): ")

# Checking if 4 exists in list using set() + in
test_list_set = set(test_list_set)
if 4 in test_list_set:
    print("Element Exists")

print("Checking if 4 exists in list (using sort() + bisect_left()): ")

# Checking if 4 exists in list using sort() + bisect_left()
test_list_bisect.sort()
if bisect_left(test_list_bisect, 4) != bisect(test_list_bisect,4):
    print("Element exist")
else:
    print("Elelement doesnt exist")

#############################################################################################################

#199

'''
Check if an element exists in list using find() method
'''

#Inititalizing list
test_list = [10,15,20,7,46,2808]

print("Checking if 15 exists in list")
x = list(map(str, test_list))
y = "-".join(x)

if y.find("15") != -1:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")

#########################################################################################################

#200

'''
Check if element exists in list using Counter() function
'''

from collections import Counter

test_list = [10,15,20,7,46,2808]

#calculating frequencies
frequency = Counter(test_list)

# If the element has frequency greater than 0 then it exist else it doesn't exist
if (frequency[15] > 0):
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")

############################################################################################################

#201

'''
Find if an element exists in list using try-except block
'''

def element_exists(lst, element):
    #try to get the index of the element in the list
    try:
        lst.index(element)
        # IF the element is found, return True
        return True
    except ValueError:
        #Return false in this case
        return False

#test the function
test_list = [1,6,3,5,3,4]

print(element_exists(test_list, 3)) #prints True
print(element_exists(test_list, 7)) #prints False

#########################################################################################################































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
