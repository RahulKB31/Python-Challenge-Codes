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