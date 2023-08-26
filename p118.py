#741

'''
Python | Remove all duplicates words from a given sentence
'''

from collections import Counter

def remov_duplicates(input):
    input = input.split(" ")

    UniqW = Counter(input)

    s = " ".join(UniqW.keys())
    print(s)

if __name__ == "__main__":
    input = 'Python is great and java is also great'
    remov_duplicates(input)

################################################################################################################

#742

s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:
    if (s.count(i) >= 1 and (i not in k)):
        k.append(i)
print(' '.join(k))

################################################################################################################

#743

string = "Python is great and Java is also great"

print(' '.join(dict.fromkeys(string.split())))

###############################################################################################################

#744

'''
Using set()
'''

string = "Python is great and Java is also great"
print(' '.join(set(string.split())))

###############################################################################################################

#745

'''
Using operator.countOf()
'''

import operator as op

s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:
    if (op.countOf(l,i) >= 1 and (i not in k)):
        k.append(i)
print(' '.join(k))

################################################################################################################

#746

def remove_duplicates(sentence):
    words = sentence.split(" ")
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    return " ".join(result)

sentence = "Python is great and Java is also great"
print(remove_duplicates(sentence))

#################################################################################################################

#747

'''
Using recursive method
'''

def remove_duplicates(sentence):
    words = sentence.split(" ")

    if len(words) == 1:
        return words[0]
    if words[0] in words[1:]:
        return remove_duplicates(" ".join(words[1:]))
    else:
        return words[0] + " " + remove_duplicates(" ".join(words[1:]))

sentence = "Python is great and Java is also great"
print(remove_duplicates(sentence))

#########################################################################################################

#748

'''
Using reduce
'''

from functools import reduce

def remove_duplicates(input_str):
    words = input_str.split()
    unique_words = reduce(lambda x,y: x if y in x else x + [y], [[], ] + words)
    return ' '.join(unique_words)

input_str = "Python is great and Java is also great"
print(remove_duplicates(input_str))

################################################################################################################











































































































































































































































