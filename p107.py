#706

'''
Python | Check order of character in string using OrderedDict()
'''

from collections import OrderedDict

def checkOrder(input, pattern):
    dict = OrderedDict.fromkeys(input)

    ptrlen = 0
    for key,value in dict.items():
        if (key == pattern[ptrlen]):
            ptrlen = ptrlen + 1

        if (ptrlen == (len(pattern))):
            return 'true'

    return 'false'

if __name__ == "__main__":
    input = 'engineers rock'
    pattern = 'er'
    print(checkOrder(input, pattern))

#################################################################################################################

#707

'''
Check order of character in using two pointers
'''

def check_order(string, pattern):
    i, j = 0 , 0
    for char in string:
        if char == pattern[j]:
            j += 1
        if j == len(pattern):
            return True
        i += 1

    return False

string = 'engineers rock'
pattern = 'er'
print(checkOrder(string, pattern))

################################################################################################################

















































































