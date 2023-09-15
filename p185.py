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



















