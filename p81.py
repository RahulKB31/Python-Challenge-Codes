#588

'''
Python - Least frequent character in string
'''

#Naive mthod + min()

test_str = "GeeksforGeeks"

print("The original string is: " + test_str)

#using naive method to get least frequent character in string
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key=all_freq.get)

#printing result
print("The minimum of all characters in GeeksForGeeks is :" + str(res))

###############################################################################################################

#589

'''
Using collections.counter() + min()
'''

from collections import Counter

test_str = "GeeksforGeeks"

print("The original string is: " + test_str)

res = Counter(test_str)
res = min(res, key = res.get)

print("The minimum of all characters in Geeksfor Geeks is: " + str(res))

#############################################################################################################

#590

'''
Using defaultdict and list comprehension
'''

from collections import defaultdict

def least_frequent_char(string):
    freq = defaultdict(int)
    for char in string:
        freq[char] += 1
    min_freq = min(freq.values())
    least_frequent_chars = [char for char in freq if freq[char] == min_freq]
    return ''.join(sorted(least_frequent_chars))[0]

test_str = "Geeksforeeks"
least_frequent = least_frequent_char(test_str)
print(f"The least frequent character in '{test_str}' is : {least_frequent}")

################################################################################################################

#591

'''
Using Numpy
'''

import numpy as np
def least_frequent_char(string):
    freq = {char: string.count(char) for char in set(string)}
    return list(freq.keys())[np.argmin(list(freq.values()))]

input_string = "GeeksforGeeks"
min_char = least_frequent_char(input_string)
print("The original string is:", input_string)
print("The minimum of all characters in", input_string, "is", min_char)

################################################################################################################

#592

'''
Using dictionary
'''

def least_frequent_char(input_str):
    freq_dict = {}

    for char in input_str:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    min_value = min(freq_dict.values())
    least_frequent_char = ''

    #Traversing the dictionary
    for key, value in freq_dict.items():
        if value == min_value:
            least_frequent_char = key
            break
    return least_frequent_char

input_string = "GeeksforGeeks"
print(least_frequent_char(input_string))

############################################################################################################





































































































































































































































































