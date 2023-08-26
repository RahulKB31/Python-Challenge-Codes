#541

'''
Python - Words Frequency in string shorthands
'''

# Using dictionary comprehension + count() + split()

test_str = "Gfg is best, Geeks are good and Geeks like Gfg"

print("The original string is: "+ str(test_str))

res = {key: test_str.count(key) for key in test_str.split()}

print("The words frequency: " + str(res))

###########################################################################################################

#542

'''
Using counter() + split()
'''

from collections import Counter

test_str = "Gfg is best, Geeks are good and Geeks like Gfg"

print("The original string is: "+ str(test_str))

res = Counter(test_str.split())

print("The words frequency: " + str(res))

################################################################################################################

#543

'''
Using dictionary comprehension + operator.countOf() + split()
'''

import operator as op

test_str = "Gfg is best, Geeks are good and Geeks like Gfg"

print("The original string is: "+ str(test_str))
listString = test_str.split()

res = {key: op.countOf(listString, key) for key in listString}

print("The words frequency: " + str(res))

###############################################################################################################

#544

'''
Using defaultdict
'''

from collections import defaultdict

test_str = "Gfg is best, Geeks are good and Geeks like Gfg"

print("The original string is: "+ str(test_str))
listString = test_str.split()

freq = defaultdict(int)

for word in listString:
    freq[word] += 1

res = dict(freq)

print("The words frequency: " + str(res))

##############################################################################################################

#545

'''
Using set() and list comprehension
'''

test_str = "Gfg is best, Geeks are good and Geeks like Gfg"

print("The original string is: "+ str(test_str))

listString = test_str.split()

freq = {word: listString.count(word) for word in set(listString)}

print("The words frequency: " + str(freq))

###############################################################################################################


















































































































































































