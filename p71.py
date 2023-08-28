<<<<<<< HEAD
#517

'''
Reverse words in a given string in python
'''

string = 'geeks quiz practice code'

s = string.split()[::-1]
l = []
for i in s:
    l.append(i)

print(" ".join(l))

#############################################################################################################

#518

def rev_sentence(sentence):

    words = sentence.split(' ')

    #then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))

    #finally return the joined string
    return reverse_sentence

if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(rev_sentence(input))

###############################################################################################################

#519

'''
reverse words using backward iteration
'''

import re

def rev_sentence(sentence):

    #find all the words in sentence
    words = re.findall('\w+',sentence)

    # backward iterate over list of words and join using space
    reverse_sentence = ' '.join(words[i] for i in range(len(words)-1, -1, -1))

    # finally return the joined string
    return reverse_sentence

if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(rev_sentence(input))

#############################################################################################################

#520

'''
Reverse words using stack
'''

string = 'geeks quiz practice code'

# creating an empty stack
stack = []

#pushing words onto the stack
for word in string.split():
    stack.append(word)

#creating empytylist to store the reverse words
reversed_words = []

#popping words off the stack and appending them to the list
while stack:
    reversed_words.append(stack.pop())

# joining the reversed words with a space
reversed_string = " ".join(reversed_words)

# printing the reversed string
print(reversed_string)

##################################################################################################################

#521

'''
using split() python
'''

def reverse_words(string):
    words = string.split()

    reversed_string = ''

    for i in range(len(words)-1, -1, -1):
        reversed_string += words[i] + ' '

    #remove the extra space at the end of the reversed string and reverse it
    return reversed_string.strip()

string = "geeks quiz practice code"
reversed_string = reverse_words(string)
print(reversed_string)

#############################################################################################################

#522

'''
Using two pointer approach
'''

def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

#function to reverse the string
def reverse_string(s):
    s = list(s)
    start, end = 0, len(s) - 1
    reverse_word(s, start, end)

    start = end = 0

    # iterate over the string s
    while end < len(s):
        if s[end] == " ":
            reverse_word(s, start, end - 1)
            start = end + 1
        end += 1

    #reverse the words
    reverse_word(s, start, end-1)
    return ''.join(s)

S = 'geeks quiz practice code'
print(reverse_string(S))

##################################################################################################################








































































































































































































































=======
#517

'''
Reverse words in a given string in python
'''

string = 'geeks quiz practice code'

s = string.split()[::-1]
l = []
for i in s:
    l.append(i)

print(" ".join(l))

#############################################################################################################

#518

def rev_sentence(sentence):

    words = sentence.split(' ')

    #then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))

    #finally return the joined string
    return reverse_sentence

if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(rev_sentence(input))

###############################################################################################################

#519

'''
reverse words using backward iteration
'''

import re

def rev_sentence(sentence):

    #find all the words in sentence
    words = re.findall('\w+',sentence)

    # backward iterate over list of words and join using space
    reverse_sentence = ' '.join(words[i] for i in range(len(words)-1, -1, -1))

    # finally return the joined string
    return reverse_sentence

if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(rev_sentence(input))

#############################################################################################################

#520

'''
Reverse words using stack
'''

string = 'geeks quiz practice code'

# creating an empty stack
stack = []

#pushing words onto the stack
for word in string.split():
    stack.append(word)

#creating empytylist to store the reverse words
reversed_words = []

#popping words off the stack and appending them to the list
while stack:
    reversed_words.append(stack.pop())

# joining the reversed words with a space
reversed_string = " ".join(reversed_words)

# printing the reversed string
print(reversed_string)

##################################################################################################################

#521

'''
using split() python
'''

def reverse_words(string):
    words = string.split()

    reversed_string = ''

    for i in range(len(words)-1, -1, -1):
        reversed_string += words[i] + ' '

    #remove the extra space at the end of the reversed string and reverse it
    return reversed_string.strip()

string = "geeks quiz practice code"
reversed_string = reverse_words(string)
print(reversed_string)

#############################################################################################################

#522

'''
Using two pointer approach
'''

def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

#function to reverse the string
def reverse_string(s):
    s = list(s)
    start, end = 0, len(s) - 1
    reverse_word(s, start, end)

    start = end = 0

    # iterate over the string s
    while end < len(s):
        if s[end] == " ":
            reverse_word(s, start, end - 1)
            start = end + 1
        end += 1

    #reverse the words
    reverse_word(s, start, end-1)
    return ''.join(s)

S = 'geeks quiz practice code'
print(reverse_string(S))

##################################################################################################################








































































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
