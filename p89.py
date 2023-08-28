<<<<<<< HEAD
#627

'''
Python program to find uncommon words from two strings
'''

def UncommonWords(A,B):
    count = {}

    for word in A.split():
        count[word] = count.get(word, 0) + 1

    for word in B.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] == 1]

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A,B))

#################################################################################################################

#628

'''
Using split(), list(), set(), in and not in operators
'''

def UncommonWords(A,B):
    A = A.split()
    B = B.split()
    x = []
    for i in A:
        if i not in B:
            x.append(i)
    for i in B:
        if i not in A:
            x.append(i)
    x = list(set(x))
    return x

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A,B))

################################################################################################################

#629

'''
Using counter() function
'''

from collections import Counter

def UncommonWords(A,B):
    A = A.split()
    B = B.split()
    frequency_arr1 = Counter(A)
    frequency_arr2 = Counter(B)
    result = []

    for key in frequency_arr1:
        if key not in frequency_arr2:
            result.append(key)
    for key in frequency_arr2:
        if key not in frequency_arr1:
            result.append(key)

    return result

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A,B))

################################################################################################################

#630

'''
Using operator.countOf() method
'''

import operator as op

def UncommonWords(A,B):
    A = A.split()
    B = B.split()
    x = []
    for i in A:
        if op.countOf(B,i) == 0:
            x.append(i)
    for i in B:
        if op.countOf(A, i) == 0:
            x.append(i)
    x = list(set(x))
    return x

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A,B))

################################################################################################################

#631

'''
Using the set() and difference() method to find the difference of two sets
'''

def UncommonWords(A,B):
    setA = set(A.split())
    setB = set(B.split())

    uncoomonWords = setA.difference(setB).union(setB.difference(setA))

    return list(uncoomonWords)

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A,B))

###############################################################################################################

















































































































































































































=======
#627

'''
Python program to find uncommon words from two strings
'''

def UncommonWords(A,B):
    count = {}

    for word in A.split():
        count[word] = count.get(word, 0) + 1

    for word in B.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] == 1]

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A,B))

#################################################################################################################

#628

'''
Using split(), list(), set(), in and not in operators
'''

def UncommonWords(A,B):
    A = A.split()
    B = B.split()
    x = []
    for i in A:
        if i not in B:
            x.append(i)
    for i in B:
        if i not in A:
            x.append(i)
    x = list(set(x))
    return x

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A,B))

################################################################################################################

#629

'''
Using counter() function
'''

from collections import Counter

def UncommonWords(A,B):
    A = A.split()
    B = B.split()
    frequency_arr1 = Counter(A)
    frequency_arr2 = Counter(B)
    result = []

    for key in frequency_arr1:
        if key not in frequency_arr2:
            result.append(key)
    for key in frequency_arr2:
        if key not in frequency_arr1:
            result.append(key)

    return result

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A,B))

################################################################################################################

#630

'''
Using operator.countOf() method
'''

import operator as op

def UncommonWords(A,B):
    A = A.split()
    B = B.split()
    x = []
    for i in A:
        if op.countOf(B,i) == 0:
            x.append(i)
    for i in B:
        if op.countOf(A, i) == 0:
            x.append(i)
    x = list(set(x))
    return x

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A,B))

################################################################################################################

#631

'''
Using the set() and difference() method to find the difference of two sets
'''

def UncommonWords(A,B):
    setA = set(A.split())
    setB = set(B.split())

    uncoomonWords = setA.difference(setB).union(setB.difference(setA))

    return list(uncoomonWords)

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A,B))

###############################################################################################################

















































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
