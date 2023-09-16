#917

'''
Python | Remove all characters except letters and numbers
'''

import re

#initializing string
ini_string = "abcdjw:, -@! eiw"

#printing initial string
print("initial string: ", ini_string)

result = re.sub('[\W_]+','',ini_string)

#printing final string
print('final string', result)

#################################################################################################################

#918

'''
Remove all characters except letters and numbers using isalpha() and isnumeric()
'''

import re

#initializing the string
ini_string = "123abcjw:, .@! eiw"

# printing intial string
print("Intial string: ", ini_string)

getVals = list([val for val in ini_string if val.isalpha() or val.isnumeric()])

result = "".join(getVals)

# printing final string
print("Final string", result)

###################################################################################################################

#919

'''
Remove all characters except letters using alnum()
'''

ini_string = "123:,  .@!  "

# printing initial string
print("Initial string: ", ini_string)

getVals = list([val for val in ini_string if val.isalnum()])
result = "".join(getVals)

# printing final string
print("final string", result)

###################################################################################################################

#920

'''
Remove all characters except letters and numbers usning a filter and in
'''

ini_string = "123abcjw:,  .@! eiw"

# printing initial string
print("Initial string: ", ini_string)

k = "1223324543534589asdfghjnbgkndksjfksgjJKSDLJFKLSDJBASDSDAF"

getVals = list(filter(lambda x: x in k, ini_string))

print("Final string", result)

#################################################################################################################

#921

'''
Remove all characters except letters and numbers using ord() function
'''

ini_string = "123abcjw:,  .@! eiw"

print("initial string: ", ini_string)
s=""
for i in ini_string:
    if ord(i) in range(48,58) or ord(i) in range(65,91) or ord(i) in range(97,123):
        s+=i

print("final string",s)

##################################################################################################################

#922

'''
Remove all characters except letters and numbers using operator.countOf() method
'''

import operator as op

# create a string of allowed characters
allowed_chars = "231829438498asdamnsfbdflkdjfsdlgjriejs"

ini_string = "123abcjw:,  .@! eiw"

print("initial string:", ini_string)
s=""
for i in ini_string:
    if op.countOf(allowed_chars,i) > 0:
        s += i

print("final string",s)

###################################################################################################################

#923

'''
Remove all characters except letters and numbers using numpy
'''

import numpy as np

ini_string = "123abcjw:,  .@! eiw"

print("initial string:", ini_string)

# create a char array from input string
char_array = np.fromiter(ini_string, dtype='U1',count=len(ini_string))

# extract alphanumeric characters
alphanumeric_chars = char_array[np.char.isalnum(char_array)]

# join alphanumeric characters into a string
result = ''.join(alphanumeric_chars)

print("final string", result)

##################################################################################################################
















