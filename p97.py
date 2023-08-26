#658

'''
Python - Find all duplicate characters in string
'''

#Naive approach

def duplicate_characters(string):
    chars = {}

    for char in string:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    duplicates = []

    for char,count in chars.items():
        if count > 1:
            duplicates.append(char)

    return duplicates

print(duplicate_characters("geeksforgeeks"))

################################################################################################################

#659

from collections import Counter

def find_dup_char(input):
    WC = Counter(input)

    for letter,count in WC.items():
        if (count > 1):
            print(letter)

if __name__ == "__main__":
    input = "geeksforgeeks"
    find_dup_char(input)

###########################################################################################################

#660

'''
Using count() method
'''

def find_dup_char(input):
    x = []
    for i in input:
        if i not in x and input.count(i) >1:
            x.append(i)
    print(" ".join(x))

if __name__ == "__main__":
    input = "geeksforgeeks"
    find_dup_char(input)

#################################################################################################################

#661

'''
Using filter() method
'''

def find_dup_char(input):
    x = filter(lambda x: input.count(x) >= 2,input)
    print(' '.join(set(x)))

if __name__ == "__main__":
    input = "geeksforgeeks"
    find_dup_char(input)

#############################################################################################################

#662

'''
Using sets
'''

def find_duplicate_chars(string):
    unique_chars = set()
    duplicate_chars = set()

    for char in string:
        if char in unique_chars:
            duplicate_chars.add(char)

        else:
            unique_chars.add(char)
    return duplicate_chars

print(find_duplicate_chars("geeksforgeeks"))

#################################################################################################################

#663

'''
Using functools.reduce method
'''

from functools import reduce

def find_dup_char(input):
    x = reduce(lambda x,b: x+b if input.rindex(b) != input.index(b) and b not in x else x, input, "")
    print(x)

if __name__ == "__main__":
    input = "geeksforgeeks"
    find_dup_char(input)

#############################################################################################################










































































