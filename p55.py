#424

'''
Python | Remove empty tuples from a list
'''

# Using the concept of list comprehension

def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(Remove(tuples))

###########################################################################################################

#425

'''
Using the filter() method
'''

def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(Remove(tuples))

############################################################################################################

#426

'''
using len() method
'''

def Remove(tuples):
    for i in tuples:
        if (len(i) == 0):
            tuples.remove(i)
    return tuples

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(Remove(tuples))

############################################################################################################

#427

'''
Using == operator
'''

def Remove(tuples):
    for i in tuples:
        if (i==()):
            tuples.remove(i)
    return tuples

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(Remove(tuples))

################################################################################################################

#428

'''
using enumerate function
'''

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]

res = [t for i,t in enumerate(tuples) if t]
print(res)

#################################################################################################################

#429

'''
Using while and in operator
'''

def Remove(tuples):
    while () in tuples:
        tuples.remove(())
    return tuples

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(Remove(tuples))

###################################################################################################################

#430

'''
Using str(0,len() and find() method
'''

def Remove(tuples):
    for i in tuples:
        if(str(i).find("()") != -1 and len(str(i)) == 2):
            tuples.remove(i)
    return tuples

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(Remove(tuples))

#######################################################################################################

#431

'''
Using lambda function
'''

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]

tuples = list(filter(lambda x : len(x) > 0, tuples))
print(tuples)

############################################################################################################

#432

'''
Using list comprehension, len() method
'''

def Remove(tuples):
    return [t for t in tuples if len(t) > 0]

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(Remove(tuples))

#############################################################################################################

#433

'''
Using recursion method
'''

def remove_empty_tuples(start,oldlist,newlist):
    if start == len(oldlist):
        return newlist
    if oldlist[start]==():
        pass
    else:
        newlist.append(oldlist[start])
    return remove_empty_tuples(start+1,oldlist,newlist)

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(remove_empty_tuples(0,tuples,[]))

##############################################################################################################

#434

'''
Using itertools.filterflase()
'''

import itertools

def Remove(tuples):
    #remove empty tuples using filterfalse from itertools
    tuples = list(itertools.filterfalse(lambda x: x == (), tuples))
    return tuples

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(Remove(tuples))

#############################################################################################################

#435

'''
Using reduce
'''

from functools import reduce

#defining lambda function to remove empty tuples
remove_empty = lambda lst, val: lst + [val] if val!= () else lst

tuples = [(), ('ram','15','8'),(), ('laxman','sita'),('krishna','akbar','45'),('',''),()]

#using reduce to remove empty tuples
result = reduce(remove_empty, tuples, [])

#printing final result
print("The original list is:", +str(tuples))
print("The list after removing empty tuples: " + str(result))

################################################################################################################












































































































































































































