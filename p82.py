#593

'''
Python | Maximum frequency character in string
'''

# Naive method + max()

test_str = "GeeksforGeeks"

#printing original string
print("The original string is:" + test_str)

#using naive method to get maximum frequency character in string
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = max(all_freq, key= all_freq.get)

print("The maximum of all characters in GeeksforGeeks is: " + str(res))

#############################################################################################################

#594

'''
Using collections.Counter() + max()
'''

from collections import Counter

test_str = "GeeksforGeeks"

print("The original string is: "+ test_str)

res = Counter(test_str)
res = max(res, key = res.get)

print("The maximum of all characters in GeeksforGeeks is: "+ str(res))

#################################################################################################################

#595

'''
Using a dictionary
'''

test_str = "GeeksforGeeks"

print("The original string is: " + test_str)

freq = {}

for char in test_str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

max_char = max(freq, key=freq.get)

print("The maximum of all characters in GeeksforGeeks is: " + str(max_char))

##############################################################################################################

#596

'''
Using a generator expression
'''

test_str = "GeeksforGeeks"
res = max(test_str, key = lambda x: test_str.count(x))
print(res)

##############################################################################################################




































































































































































