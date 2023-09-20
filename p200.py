#949

'''
Python program to count the number of occurences of key-value pair in a text file
'''

f = open("file.txt",'r')
d = dict()

for res in f:
    res = res.strip()
    res = res.lower()
    lines = res.split()
    for line in lines:
        if line in d:
            d[line] = d[line] + 1
        else:
            d[line] = 1

f.close()

for key in list(d.keys()):
    print("The count of {} is {}".format(key,d[key]))

##################################################################################################################

#950

'''
Count occurances of a value in a python dictionary using collections.counter
'''

from collections import Counter

def count_key_value_pairs(file_path,key,value):
    with open(file_path,'r') as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        line_key, line_value = line.strip().split('=')
        if line_key == key and line_value == value:
            count += 1

    return count

if __name__ == '__main__':
    file_path = 'textfile.txt'
    key_to_find = "your_key"
    value_to_find = "your_value"

    occurances = count_key_value_pairs(file_path, key_to_find, value_to_find)
    print(f"Number of occurances of '{key_to_find}={value_to_find}':{occurances}")

##################################################################################################################

#951

'''
Count Occurances of a value in a Python Dictionary using RegEx
'''

import re

def count_key_value_pairs(file_path,key,value):
    with open(file_path,'r') as file:
        data = file.read()

    pattern = r'\b{}={}\b'.format(re.escape(key), re.escape(value))
    occurances = len(re.findall(pattern,data))

    return occurances

if __name__ == "__main__":
    file_path = "text_file.txt"
    key_to_find = "your_key"
    value_to_find = "your_value"

    occurances = count_key_value_pairs(file_path, key_to_find, value_to_find)
    print(f"Number of occurances of '{key_to_find}={value_to_find}':{occurances}")

#################################################################################################################