<<<<<<< HEAD
#636

'''
Python - Replace multiple words with K
'''

# Using join() + split() + list comprehension

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

word_list = ['best','CS','for']

repl_wrd = 'gfg'

res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()])

print("String after multiple replace: " + str(res))

##############################################################################################################

#637

'''
Using regex + join()
'''

import re

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

word_list = ['best','CS','for']

repl_wrd = 'gfg'

res = re.sub("|".join(sorted(word_list, key = len, reverse=True)), repl_wrd, test_str)

print("String after multiple replace: " + str(res))

################################################################################################################

#638

'''
Using for loop + replace() methods
'''

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

word_list = ['best','CS','for']

repl_wrd = 'gfg'

for i in word_list:
    test_str = test_str.replace(i,repl_wrd)

print("String after multiple replace: " + str(test_str))

##################################################################################################################

#639

'''
Using dictionary and re.sub()
'''

import re

def multiple_replace(text, word_dict):

    pattern = re.compile("|".join(map(re.escape, word_dict.keys())))

    return pattern.sub(lambda x: word_dict[x.group(0)], text)

text = 'GeeksforGeeks is bet for geeks and CS'
word_dict = {'best':'gfg','CS':'gfg','for':'gfg'}

result = multiple_replace(text, word_dict)

print("String after multiple replace: " + str(result))

################################################################################################################

#640

'''
Using a lambda function with reduce() method
'''

from functools import reduce

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

word_list = ['best','CS','for']

repl_wrd = 'gfg'

replace_func = lambda s, w: s.replace(w, repl_wrd)
test_str = reduce(replace_func, word_list,test_str)

print("String after multiple replace: " + str(test_str))

##########################################################################################################

#641

'''
Using heapq
'''

import heapq

text = 'Geeksforgeeks is best for geeks and CS'
word_list = ['best','CS','for']
repl_wrd = 'gfg'

print("The original string is: " + str(text))

heap = [(-len(word), word, repl_wrd) for word in word_list]
heapq.heapify(heap)

while heap:
    _, word, repl = heapq.heappop(heap)
    text = text.replace(word, repl)

print("String after multiple replace: " + str(test_str))

################################################################################################################











































































































































































































=======
#636

'''
Python - Replace multiple words with K
'''

# Using join() + split() + list comprehension

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

word_list = ['best','CS','for']

repl_wrd = 'gfg'

res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()])

print("String after multiple replace: " + str(res))

##############################################################################################################

#637

'''
Using regex + join()
'''

import re

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

word_list = ['best','CS','for']

repl_wrd = 'gfg'

res = re.sub("|".join(sorted(word_list, key = len, reverse=True)), repl_wrd, test_str)

print("String after multiple replace: " + str(res))

################################################################################################################

#638

'''
Using for loop + replace() methods
'''

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

word_list = ['best','CS','for']

repl_wrd = 'gfg'

for i in word_list:
    test_str = test_str.replace(i,repl_wrd)

print("String after multiple replace: " + str(test_str))

##################################################################################################################

#639

'''
Using dictionary and re.sub()
'''

import re

def multiple_replace(text, word_dict):

    pattern = re.compile("|".join(map(re.escape, word_dict.keys())))

    return pattern.sub(lambda x: word_dict[x.group(0)], text)

text = 'GeeksforGeeks is bet for geeks and CS'
word_dict = {'best':'gfg','CS':'gfg','for':'gfg'}

result = multiple_replace(text, word_dict)

print("String after multiple replace: " + str(result))

################################################################################################################

#640

'''
Using a lambda function with reduce() method
'''

from functools import reduce

test_str = 'Gfg is best. Gfg also has Classes now, Classes help understand better'

print("The original string is: " + str(test_str))

word_list = ['best','CS','for']

repl_wrd = 'gfg'

replace_func = lambda s, w: s.replace(w, repl_wrd)
test_str = reduce(replace_func, word_list,test_str)

print("String after multiple replace: " + str(test_str))

##########################################################################################################

#641

'''
Using heapq
'''

import heapq

text = 'Geeksforgeeks is best for geeks and CS'
word_list = ['best','CS','for']
repl_wrd = 'gfg'

print("The original string is: " + str(text))

heap = [(-len(word), word, repl_wrd) for word in word_list]
heapq.heapify(heap)

while heap:
    _, word, repl = heapq.heappop(heap)
    text = text.replace(word, repl)

print("String after multiple replace: " + str(test_str))

################################################################################################################











































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
