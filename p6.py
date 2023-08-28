<<<<<<< HEAD
#24

# Write a function that takes two sets as arguments and returns a set containing all elements that appear in
# exactly one of the two sets. (The result should not include elements that appear in both sets.) You should not
# make use of the difference method.
# Test with several calls to the function

def exlFun(s1, s2):
    result = set()
    for item in s1:
        if item not in s2: result.add(item)
    for item in s2:
        if item not in s1: result.add(item)
    return result

print(exlFun({'a','b','c','d','e','f'},{'a','c','e','g','i','k'}))

###############################################################################################################

#25

# Write a function that takes as an argument a list of words and creates and returns a dictionary that uses
# lengths of words as keys and the number of words of each length as values.
# Use this function in a program that first asks the user to input some words, storing them in a list and then
# asks the user to supply some lengths and produces output such as “There are 5 words of length 4 in the list”.
# If there are no words of that length the output should use “… no words …”. (Hint: use the two-argument
# version of get)

def getLengths(words):
    d = {}
    for word in words:
        length = len(word)
        if length in d:
            d[length] + 1
        else:
            d[length] = 1
    return d

wordList = []
print("Please input some words, one per line; use * to finish")
getting = True
while getting:
    word = input("> ")
    if word == "*":
        getting = False
    else:
        wordList.append(word)

myDict = getLengths(wordList)

print("Please input some lengths, one per line; use a negative number to finish")
looping = True
while looping:
    length = int(input("> "))
    if length < 0:
        looping = False
    elif myDict.get(length) == 1:
        print("There is 1 word of length", length, "in the list")
    else:
        print("There are", myDict.get(length, "no"), "words of length", length, "in the list")

#########################################################################################################

#26

'''
Suppose you have a dictionary containing an occurrence count
such as the one produced in exercise 1 e.g.
{ 'a':1, 'b' :2, 'c':3, 'd':4, 'e':1, 'f’:1 }
• Write a function that inverts the dictionary, i.e. maps numbers to
lists of letters. For the above example the result should be
{ 1:['a','e','f'], 2:['b'], 3:['c'], 4:['d'] }
'''

def invert(d):
    result = {}
    for key,val in d.items():
        if val in result:
            result[val] += key
        else:
            result[val] = [key]
    return result

print(invert({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 1}))

######################################################################################################

#27

'''
Write a function that takes as an argument a list of numbers, and
then returns the number that occurs the most frequently (the
mode).
• For example, if you pass as an argument [1, 2, 3, 3, 2, 5, 6, 2], your
function should return 2.
• If there is more than one equally most frequent number it is
acceptable to return any one of them.
'''

def countOccs(myList):
    result = {}
    for num in myList:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result

def mostFrequent(1):
    '''
    return most frequent number in 1
    argument: 1: list of numbers
    '''
    d = countOccs(1)
    mostFrequentSoFar = None
    occCount = 0
    for key, val in d.items():
        if val > occCount:
            occCount = val
            mostFrequentSoFar = key
    return mostFrequentSoFar

print(mostFrequent([1,2,3,3,2,4,5,657,8]))
print(mostFrequent(1,2,3,4,3))
print(mostFrequent([]))

#################################################################################################

#28

'''
Write a function that takes a sequence of characters as an
argument and outputs the five most frequent characters from
the sequence, together with their occurrence counts
'''

def countOccs(s):
    result = {}
    for c in s:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

def fiveMostFrequent(s):
    '''
    prints 5 most frequent characters in s together with there occurances counts
    arguments: s: list f characters
    '''
    d = countOccs(s)
    tuples = []
    for k,v in d.items():
        tuples.append((v,k))
    tuples.sort()
    # use value less than 5 if there aren't 5 tuples in the list
    if len(tuples) < 5:
        limit = len(tuples)
    else:
        limit = 5
    for i in range(-1, -(limit+1), -1):
        v,k = tuples[i]
        print(k, ':', v)

fiveMostFrequent("hello")
print()
fiveMostFrequent("dgfhsdgfhsdfsbvdfkjgndfnvoinvveryveryveryveryveryveryveryveryvery")

#####################################################################################################









=======
#24

# Write a function that takes two sets as arguments and returns a set containing all elements that appear in
# exactly one of the two sets. (The result should not include elements that appear in both sets.) You should not
# make use of the difference method.
# Test with several calls to the function

def exlFun(s1, s2):
    result = set()
    for item in s1:
        if item not in s2: result.add(item)
    for item in s2:
        if item not in s1: result.add(item)
    return result

print(exlFun({'a','b','c','d','e','f'},{'a','c','e','g','i','k'}))

###############################################################################################################

#25

# Write a function that takes as an argument a list of words and creates and returns a dictionary that uses
# lengths of words as keys and the number of words of each length as values.
# Use this function in a program that first asks the user to input some words, storing them in a list and then
# asks the user to supply some lengths and produces output such as “There are 5 words of length 4 in the list”.
# If there are no words of that length the output should use “… no words …”. (Hint: use the two-argument
# version of get)

def getLengths(words):
    d = {}
    for word in words:
        length = len(word)
        if length in d:
            d[length] + 1
        else:
            d[length] = 1
    return d

wordList = []
print("Please input some words, one per line; use * to finish")
getting = True
while getting:
    word = input("> ")
    if word == "*":
        getting = False
    else:
        wordList.append(word)

myDict = getLengths(wordList)

print("Please input some lengths, one per line; use a negative number to finish")
looping = True
while looping:
    length = int(input("> "))
    if length < 0:
        looping = False
    elif myDict.get(length) == 1:
        print("There is 1 word of length", length, "in the list")
    else:
        print("There are", myDict.get(length, "no"), "words of length", length, "in the list")

#########################################################################################################

#26

'''
Suppose you have a dictionary containing an occurrence count
such as the one produced in exercise 1 e.g.
{ 'a':1, 'b' :2, 'c':3, 'd':4, 'e':1, 'f’:1 }
• Write a function that inverts the dictionary, i.e. maps numbers to
lists of letters. For the above example the result should be
{ 1:['a','e','f'], 2:['b'], 3:['c'], 4:['d'] }
'''

def invert(d):
    result = {}
    for key,val in d.items():
        if val in result:
            result[val] += key
        else:
            result[val] = [key]
    return result

print(invert({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 1}))

######################################################################################################

#27

'''
Write a function that takes as an argument a list of numbers, and
then returns the number that occurs the most frequently (the
mode).
• For example, if you pass as an argument [1, 2, 3, 3, 2, 5, 6, 2], your
function should return 2.
• If there is more than one equally most frequent number it is
acceptable to return any one of them.
'''

def countOccs(myList):
    result = {}
    for num in myList:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result

def mostFrequent(1):
    '''
    return most frequent number in 1
    argument: 1: list of numbers
    '''
    d = countOccs(1)
    mostFrequentSoFar = None
    occCount = 0
    for key, val in d.items():
        if val > occCount:
            occCount = val
            mostFrequentSoFar = key
    return mostFrequentSoFar

print(mostFrequent([1,2,3,3,2,4,5,657,8]))
print(mostFrequent(1,2,3,4,3))
print(mostFrequent([]))

#################################################################################################

#28

'''
Write a function that takes a sequence of characters as an
argument and outputs the five most frequent characters from
the sequence, together with their occurrence counts
'''

def countOccs(s):
    result = {}
    for c in s:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

def fiveMostFrequent(s):
    '''
    prints 5 most frequent characters in s together with there occurances counts
    arguments: s: list f characters
    '''
    d = countOccs(s)
    tuples = []
    for k,v in d.items():
        tuples.append((v,k))
    tuples.sort()
    # use value less than 5 if there aren't 5 tuples in the list
    if len(tuples) < 5:
        limit = len(tuples)
    else:
        limit = 5
    for i in range(-1, -(limit+1), -1):
        v,k = tuples[i]
        print(k, ':', v)

fiveMostFrequent("hello")
print()
fiveMostFrequent("dgfhsdgfhsdfsbvdfkjgndfnvoinvveryveryveryveryveryveryveryveryvery")

#####################################################################################################









>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
