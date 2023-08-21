#703

'''
Python - Insertion at the beginning in OrderedDict
'''

# Using OrderedDict.move_to_end()

from collections import OrderedDict

iniordered_dict = OrderedDict([('akshat','1'),('nikhil','2')])

iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last=False)

print("Resultant Dictionary: " + str(iniordered_dict))

################################################################################################################

#704

'''
Using Naive approach
'''

from collections import OrderedDict

ini_dict1 = OrderedDict([('akshat','1'),('nikhil','2')])
ini_dict2 = OrderedDict([('manjeet','4'),('akash','4')])
both = OrderedDict(list(ini_dict2.items()) + list(ini_dict1.items()))

print("Resultant Dictionary: " + str(both))

################################################################################################################

#705

'''
Using OrderedDict.popitem()
'''

from collections import OrderedDict

ini_dict = OrderedDict([('akshat','1'),('nikhil','2')])

iniordered_dict = OrderedDict()

iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last = False)

while ini_dict:
    iniordered_dict.update({ini_dict.popitem(last = False)})

print("Resultant Dictionary: " + str(iniordered_dict))

##################################################################################################################
































































































