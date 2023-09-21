#961

'''
How to remove lines starting with any prefix using Python
'''

file1 = open('GeeksforGeeks.txt','r')

file2 = open('GeeksforGeeksUpdated.txt','w')

for line in file1.readlines():
    if not (line.startswith('TextGenerator')):
        print(line)
        file2.write(line)

file2.close()
file1.close()

##################################################################################################################

#962

# Remove lines starting with a prefix using Regex model

import re

file1 = open('GeeksforGeeks.txt','r')

file2 = open('GeeksforGeeksUpdated.txt','w')

for line in file1.readlines():
    x = re.findall("^Geeks",line)
    if not x:
        print(line)

        file2.write(line)

file1.close()
file2.close()

##################################################################################################################

#963

# Remove lines starting with a prefix using find() method

file1 = open('GeeksforGeeks.txt','r')

file2 = open('GeeksforGeeksUpdated.txt','w')

for line in file1.readlines():
    if not (line.find('TextGenerator')==0):
        print(line)
        file2.write(line)

file2.close()
file1.close()

###################################################################################################################