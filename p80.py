#583

'''
Remove all duplicates from a given string in python
'''

from collections import OrderedDict

def removeDupWithoutOrder(str):
    return "".join(set(str))

def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))

if __name__ == "__main__":
    str = "geeksforgeeks"
    print("Without Order = ", removeDupWithoutOrder(str))
    print("With order =", removeDupWithOrder(str))

################################################################################################################

#584

def removeDuplicate(str):
    s = set(str)
    s = "".join(s)
    print("Without Order:",s)
    t = ""
    for i in str:
        if(i in t):
            pass
        else:
            t = t + i
        print("With order:",t)

str = "geeksforgeeks"
removeDuplicate(str)

#############################################################################################################

#585

from collections import OrderedDict

ordinary_dictionary = {}
ordinary_dictionary['a'] = 1
ordinary_dictionary['b'] = 2
ordinary_dictionary['c'] = 3
ordinary_dictionary['d'] = 4
ordinary_dictionary['e'] = 5

print(ordinary_dictionary)

ordered_dictionary = OrderedDict()
ordered_dictionary['a'] = 1
ordered_dictionary['b'] = 2
ordered_dictionary['c'] = 3
ordered_dictionary['d'] = 4
ordered_dictionary['e'] = 5

print(ordered_dictionary)

#############################################################################################################

#586

from collections import OrderedDict
seq = ('name','age','gender')
dict = OrderedDict.fromkeys(seq)

print(str(dict))
dict = OrderedDict.fromkeys(seq, 10)

print(str(dict))

#############################################################################################################

#587

import operator as op

def removeDuplicate(str):
    s = set(str)
    s = "".join(s)
    print("Without order: ",s)
    t = ""
    for i in str:
        if op.countOf(t, i) > 0:
            pass
        else:
            t = t + i
        print("With Order:", t)

str = "geeksforgeeks"
removeDuplicate(str)

#############################################################################################################


















































































































































































































