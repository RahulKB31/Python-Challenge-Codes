#753

'''
Python | Convert a list of Tuples into dictionary
'''

# Use of setdefault()

def Convert(tup, di):
    for a,b in tup:
        di.setdefault(a, []).append(b)
    return di

tups = [('akash',10),('gaurav',12),('anand',14),('suraj',20),('akhil',25),('ashish',30)]

dictionary = {}
print(Convert(tups, dictionary))

##################################################################################################################

#754

list_1 = [('akash',10),('gaurav',12),('anand',14),('suraj',20),('akhil',25),('ashish',30)]

dict_1 = dict()

for student, score in list_1:
    dict_1.setdefault(student, []).append(score)
print(dict_1)

##################################################################################################################

#755

'''
Use of dict() method
'''

def Convert(tup, di):
    di = dict(tup)
    return di

tups = [('akash',10),('gaurav',12),('anand',14),('suraj',20),('akhil',25),('ashish',30)]
dictionary = {}
print(Convert(tups, dictionary))

################################################################################################################

#756

print(dict([('akash',10),('gaurav',12),('anand',14),('suraj',20),('akhil',25),('ashish',30)]))

################################################################################################################

#757

from itertools import groupby

def convert_to_dict(tuple_list):
    groups = groupby(tuple_list, key=lambda x: x[0])

    dictionary = {}

    for key, group in groups:
        dictionary[key] = [tuple[1] for tuple in group]

    return dictionary

tuple_list = [('akash',10),('gaurav',12),('anand',14),('suraj',20),('akhil',25),('ashish',30)]

print(convert_to_dict(tuple_list))

####################################################################################################################

#758

'''
Using the setdefault() method
'''

tups = [('akash',10),('gaurav',12),('anand',14),('suraj',20),('akhil',25),('ashish',30)]

dictionary = {}
for key, val in tups:
    dictionary.setdefault(key,val)
print(dictionary)

###################################################################################################################

#759

'''
Using a loop to add tuples to the dictionary
'''

def convert_to_dict(tuple_list):
    dictionary = {}

    for tuple in tuple_list:
        if tuple[0] in dictionary:
            dictionary[tuple[0]].append(tuple[1])
        else:
            dictionary[tuple[0]] = [tuple[1]]

    return dictionary


tuple_list = [('akash', 10), ('gaurav', 12), ('anand', 14), ('suraj', 20), ('akhil', 25), ('ashish', 30)]

print(convert_to_dict(tuple_list))

#################################################################################################################

#760

'''
Using the dict() constructor and a list comprehension
'''

def convert_to_dict(tuple_list):
    dictionary = dict((key,value) for key,value in tuple_list)

    return dictionary

tuple_list = [('akash', 10), ('gaurav', 12), ('anand', 14), ('suraj', 20), ('akhil', 25), ('ashish', 30)]

print(convert_to_dict(tuple_list))

#################################################################################################################
















































































































































































































