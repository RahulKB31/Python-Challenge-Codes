#632

'''
Python - Replace duplicate Occurance in String
'''

# Using split() + enumerate() + loop

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

repl_dict = {'Gfg':'It', 'Classes':'They'}

test_list = test_str.split(' ')
res = set()
for idx, ele in enumerate(test_list):
    if ele in repl_dict:
        if ele in res:
            test_list[idx] = repl_dict[ele]
        else:
            res.add(ele)
res = ' '.join(test_list)

print("The string after replacing: " + str(res))

#################################################################################################################

#633

'''
Using keys() + index() + list comprehension
'''

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

repl_dict = {'Gfg':'It', 'Classes':'They'}

test_list = test_str.split(' ')
res = ' '.join([repl_dict.get(val) if val in repl_dict.keys() and test_list.index(val) != idx
                else val for idx, val in enumerate(test_list)])

print("The string after replacing: " + str(res))

#################################################################################################################

#634

'''
Using list comprehension + set + keys
'''

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

repl_dict = {'Gfg':'It', 'Classes':'They'}

words = test_str.split(' ')
seen = set()
res = [repl_dict[word] if word in repl_dict and word not in seen and not seen.add(word) else word for word in words]

res = ' '.join(res)

print("The string after replacing: " + str(res))

###############################################################################################################

#635

'''
Using regular expressions
'''

import re

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

repl_dict = {'Gfg':'It', 'Classes':'They'}

pattern = r'\b(' + '|'.join(repl_dict.keys()) + r')\b(?=.*\b\1\b'

res = re.sub(pattern, lambda match: repl_dict[match.group()], test_str)

print("The original string is: " + str(test_str))
print("The string after replacing: " + str(res))

###################################################################################################################

















































































































































































