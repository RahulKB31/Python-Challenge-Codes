<<<<<<< HEAD
#783

'''
Python - Adding Tuple to list and vice-versa
'''

# Using += operator[list + tuple]

test_list = [5,6,7]

print('The original list is: ' + str(test_list))

test_tup = (9,10)
test_list += test_tup

print("The container after addition: " + str(test_list))

#################################################################################################################

#784

'''
Using tuple(), data type conversion[tuple + list]
'''
test_list = [5,6,7]

print("The original list is: " + str(test_list))

test_tup = (9,10)

res = tuple(list(test_tup) + test_list)

print("The container after addition: " + str(res))

#################################################################################################################

#785

'''
Using tuple().list() and extend() methods
'''

test_list = [5,6,7]
test_tup = (9,10)

print('The original list is: ' + str(test_list))

test_list.extend(list(test_tup))

print("The container after addition: " + str(test_list))

test_list = [1,2,3,4]
test_tup = (5,6)

print("The original tuple is: " + str(test_tup))

test_tup = list(test_tup)
test_tup.extend(test_list)
test_tup = tuple(test_tup)

print("The container after addition: " + str(test_tup))

################################################################################################################

#786

'''
Using the insert() method
'''

my_list = [5,6,7]
my_tuple = (9,10)

index = 3
my_list.insert(index, my_tuple)

print("List after addition: ", my_list)

###############################################################################################################

























































































































































































=======
#783

'''
Python - Adding Tuple to list and vice-versa
'''

# Using += operator[list + tuple]

test_list = [5,6,7]

print('The original list is: ' + str(test_list))

test_tup = (9,10)
test_list += test_tup

print("The container after addition: " + str(test_list))

#################################################################################################################

#784

'''
Using tuple(), data type conversion[tuple + list]
'''
test_list = [5,6,7]

print("The original list is: " + str(test_list))

test_tup = (9,10)

res = tuple(list(test_tup) + test_list)

print("The container after addition: " + str(res))

#################################################################################################################

#785

'''
Using tuple().list() and extend() methods
'''

test_list = [5,6,7]
test_tup = (9,10)

print('The original list is: ' + str(test_list))

test_list.extend(list(test_tup))

print("The container after addition: " + str(test_list))

test_list = [1,2,3,4]
test_tup = (5,6)

print("The original tuple is: " + str(test_tup))

test_tup = list(test_tup)
test_tup.extend(test_list)
test_tup = tuple(test_tup)

print("The container after addition: " + str(test_tup))

################################################################################################################

#786

'''
Using the insert() method
'''

my_list = [5,6,7]
my_tuple = (9,10)

index = 3
my_list.insert(index, my_tuple)

print("List after addition: ", my_list)

###############################################################################################################

























































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
