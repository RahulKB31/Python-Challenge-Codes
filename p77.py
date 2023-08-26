#560

'''
Python program to print even length words in a string
'''

n = "This is a python language"

s = n.split(" ")
for i in s:
    if len(i)%2 == 0:
        print(i)

###############################################################################################################

#561

'''
Using split() function
'''

def printWords(s):

    s = s.split(' ')

    for word in s:
        if len(word)%2 == 0:
            print(word)

s = 'I am muskan'
printWords(s)

################################################################################################################

#562

'''
Using the lambda function
'''

n = 'geeks for geek'

s = n.split(" ")
l = list(filter(lambda x: (len(x)%2 == 0),s))
print(l)

###############################################################################################################

#563

'''
Using list comprehension
'''

n = 'geeks for geek'
a = n.split(" ")
print([x for x in s if len(x)%2 == 0])

#############################################################################################################

#564

'''
Using the enumerate function
'''

n = 'geeks for geek'
a = n.split(" ")
print([x for i,x in enumerate(s) if len(x)%2 == 0])

#############################################################################################################

#565

'''
Using recursion
'''

def PrintEvenLengthWord(itr, list1):
    if itr == len(list1):
        return
    if len(list1[itr])%2 == 0:
        print(list1[itr])
    PrintEvenLengthWord(itr+1,list1)
    return

str = 'geeks for geek'
l = [i for i in str.split()]
PrintEvenLengthWord(0,1)

################################################################################################################

#566

'''
Using the filter function and lambda function
'''

s = 'geeks for geek'

words = s.split(" ")

even_length_words = list(filter(lambda x: len(x)%2 == 0, words))

print(even_length_words)

################################################################################################################

#567

'''
Using the itertools.filterfalse() function
'''

import itertools
s = 'geeks for geek'

words = s.split(" ")

even_length_words = list(itertools.filterfalse(lambda x: len(x)%2 != 0, words))

print(even_length_words)

################################################################################################################

#568

'''
Using replace() function
'''

def print_even_length_words(s):
    words = s.replace(',',' ').replace('.',' ').split()
    for word in words:
        if len(word)%2 == 0:
            print(word, end=' ')

s = 'geeks for geek'
print_even_length_words(s)

################################################################################################################

#569

'''
Iterative character by character parsing
'''

s = 'This is a python language'

word = ''

for i in s:
    if i == ' ':
        if len(word)%2 == 0 and len(word) != 0:
            print(word, end=' ')
        word = ''

    else:
        word += i

if len(word)%2 == 0 and len(word) != 0:
    print(word, end = ' ')

################################################################################################################

#570

'''
Using itertools.compress() function
'''

from itertools import compress

n = "This is a python language"
s = n.split(" ")
even_len_bool = [len(word)%2 == 0 for word in s]
even_len_words = list(compress(s, even_len_bool))
print(even_len_words)

################################################################################################################

#571

'''
Word-by-word parsing
'''

s = "I am omkhar"

word_start = 0
even_words = []

for i in range(len(s)):
    if s[i] == " ":
        word_end = i
        word_length = word_end - word_start
        if word_length %2 == 0:
            even_word.append(s[word_start:word_end])
        word_start = i+1

word_length = len(s) - word_start
if word_length % 2 == 0:
    even_words.append(s[word_start:])

for w in even_words:
    print(w)

################################################################################################################





















































































































































































