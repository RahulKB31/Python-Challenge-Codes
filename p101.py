#682

'''
Python | Ways to remove a key from dictionary
'''

# Remove a key from a dictionary using the del

test_dict = {"Arushi":22,"Mani":21,"Haritha":21}

print("The dictionary before performing remove is: ", test_dict)

del test_dict['Mani']

print("The dictionary after remove is: ", test_dict)

del test_dict['Mani']

###############################################################################################################

#683

'''
Remove a key from a dictionary using pop()
'''

test_dict = {"Arushi":22,"Mani":21,"Haritha":21}

print("The dictionary before performing remove is: ", test_dict)

removed_value = test_dict.pop('Mani')

print("The dictionary after remove is: " + str(test_dict))
print("The removed key's value is: " + str(removed_value))

print('\r')

removed_value = test_dict.pop('Manjeet', 'No key found')

print("The dictionary after remove is: " + str(test_dict))
print("The removed key's value is: " + str(removed_value))

###############################################################################################################

#684

'''
Using items() + dict comprehension to remove a key from a dictionary
'''

test_dict = {"Arushi":22,"Mani":21,"Haritha":21}

print("The dictionary before performing remove is: " + str(test_dict))

new_dict = {key: val for key, val in test_dict.items() if key != 'Mani'}

print('The dictionary after remove is: ' + str(new_dict))

###############################################################################################################

#685

'''
Use a Python dictionary comprehension to remove a key from a dictionary
'''

test_dict = {"Arushi":22,"Mani":21,"Haritha":21}

print("The dictionary before performing remove is: " + str(test_dict))

a_dict = {key: test_dict[key] for key in test_dict if key != 'Mani'}

print("The dictionary after performing remove is: ", a_dict)

#################################################################################################################

#686

'''
Iterating and eliminating
'''

test_dict = {"Arushi":22,"Mani":21,"Haritha":21}

print(test_dict)

y = {}

for key, value in test_dict.items():
    if key != 'Arushi':
        y[key] = value

print(y)

###############################################################################################################

#687

'''
Delete all keys from a dictioary using the del
'''

test_dict = {"Arushi":22,"Mani":21,"Haritha":21}

print(test_dict)

del test_dict
try:
    print(test_dict)
except:
    print('Deleted!')

################################################################################################################

#688

'''
Delete all keys from a dictionary using dict.clear()
'''

test_dict = {"Arushi":22,"Mani":21,"Haritha":21}

print(test_dict)

test_dict.clear()
print("Length", len(test_dict))
print(test_dict)

################################################################################################################















































































































































































