<<<<<<< HEAD
#869

'''
Python program for BogoSort or Permutation Sort
'''

import random

def bogoSort(a):
    n = len(a)
    while (is_sorted(a) == False):
        shuffle(a)

def is_sorted(a):
    n = len(a)
    for i in range(0,n-1):
        if (a[i] > a[i+1]):
            return False
    return True

def shuffle(a):
    n = len(a)
    for i in range(0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]

a = [3,4,5,6,7,8,2]
bogoSort(a)
print("Sorted array: ")
for i in range(len(a)):
    print("%d" %a[i])

###############################################################################################################

#870

'''
Bogosort implementation using builtin shuffle() and sorted() function
'''

import random

def bogosort(a):
    n = len(a)
    while not sorted(a) == a:
        random,shuffle(a)

a = [3, 4, 5, 6, 7, 8, 2]
bogoSort(a)
print("Sorted array: ")
for i in range(len(a)):
    print("%d" % a[i])

###############################################################################################################




















































=======
#869

'''
Python program for BogoSort or Permutation Sort
'''

import random

def bogoSort(a):
    n = len(a)
    while (is_sorted(a) == False):
        shuffle(a)

def is_sorted(a):
    n = len(a)
    for i in range(0,n-1):
        if (a[i] > a[i+1]):
            return False
    return True

def shuffle(a):
    n = len(a)
    for i in range(0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]

a = [3,4,5,6,7,8,2]
bogoSort(a)
print("Sorted array: ")
for i in range(len(a)):
    print("%d" %a[i])

###############################################################################################################

#870

'''
Bogosort implementation using builtin shuffle() and sorted() function
'''

import random

def bogosort(a):
    n = len(a)
    while not sorted(a) == a:
        random,shuffle(a)

a = [3, 4, 5, 6, 7, 8, 2]
bogoSort(a)
print("Sorted array: ")
for i in range(len(a)):
    print("%d" % a[i])

###############################################################################################################




















































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
