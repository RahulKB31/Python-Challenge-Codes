#715

'''
Python | Sort Python Dictionaries by Key or Value
'''

# Sort Dictionary by Key in Python

myDict = {'ravi':10, 'rajnish':9, 'sanjeev':15, 'yash':2, 'suraj':32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict =  {i: myDict[i] for i in myKeys}

print(sorted_dict)

################################################################################################################

#716

'''
Displaying the keys in sorted order
'''

def dictionary():
    key_value = {}

    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 1:-\n")

    print("key_value", key_value)

    for i in sorted(key_value.keys()):
        print(i, end = " ")

def main():
    dictionary()

if __name__ == "__main__":
    main()

##############################################################################################################

#717

'''
Sort the dictionary by key
'''

from collections import OrderedDict

dict = {'ravi':10, 'rajnish':9, 'sanjeev':15, 'yash':2, 'suraj':32}

dict1 = OrderedDict(sorted(dict.items()))
print(dict1)

############################################################################################################

#718

'''
Sorting the keys and values in alphabetical order using the key
'''


def dictionary():
    key_value = {}

    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("key_value", key_value)

    print("Task 2:-\nKeys and Values sorted in","alphabetical order by the key")

    for i in sorted(key_value):
        print((i, key_value[i]), end = " ")

def main():
    dictionary()

if __name__ == "__main__":
    main()

##################################################################################################################

#719

'''
Sorting the keys and values alphabetically using the value
'''


def dictionary():
    key_value = {}

    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("key_value", key_value)

    print("Task 3:-\nKeys and Values sorted in", "alphabetical order by the value")

    print(sorted(key_value.items(), key=lambda kv: (kv[1],kv[0])))

def main():
    dictionary()

if __name__ == "__main__":
    main()

################################################################################################################

#720

'''
Sort dictionary by value in Python
'''

from collections import OrderedDict

import numpy as np

myDict = {'ravi':10, 'rajnish':9, 'sanjeev':15, 'yash':2, 'suraj':32}

print(myDict)

keys = list(dict.keys())
values = list(dict.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)

###############################################################################################################






















































































































































































