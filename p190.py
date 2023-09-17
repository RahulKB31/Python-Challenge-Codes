#929

'''
Parsing and Processing URL using Python - Regex
'''

import re

# url link
s = 'https://www.geeksforgeeks.org/'

# finding the protocol
obj1 = re.findall('(\w+)://',s)

print(obj1)

# finding the host name which may contain dash or dots
obj2 = re.findall('://www.([\w\-\.]+)',s)
print(obj2)

#################################################################################################################

#930

import re

# url link
s = 'file://localhost:4040/abc_file'

# finding the file capture group
obj1 = re.findall('(\w+)://',s)
print(obj1)

# finding the hostname which may contain dash or dots
obj2 = re.findall('://([\w\_\.]+)',s)
print(obj2)

# finding the hostname which may contain dash or dots or port number
obj3 = re.findall('://([\w\_\.]+)(:(\d+))?',s)
print(obj3)

###################################################################################################################

#931

'''
For a general URL, this can be used, where the path elements can also be constructed
'''

import re

# url
s = 'http://www.example.com/index.html'

# searching for all the capture groups
obj = re.findall('(\w+)://([\w\_\.]+)/(\w+).(\w+)',s)
print(obj)

################################################################################################################



























































































