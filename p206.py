#967

'''
Read list of dictionaries from file in python
'''

import pickle

try:
    geeky_file = open('GFG.txt','r')
    dictionary_list = pickle.load(geeky_file)

    for d in dictionary_list:
        print(d)
    geeky_file.close()

except:
    print("Something unexpected occured!")

################################################################################################################

#968

'''
Reading from text file using read() method
'''

def parse(d):
    dictionary = dict()

    pairs = d.strip('{}').split(', ')
    for i in pairs:
        pair = i.split(': ')
        dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    return dictionary

try:
    geeky_file = open('geeky_file.txt','rt')
    lines = geeky_file.read().split('\n')
    for l in lines:
        if l != '':
            dictionary = parse(l)
            print(dictionary)
    geeky_file.close()

except:
    print("Something unexpected occured!")

#####################################################################################################################
