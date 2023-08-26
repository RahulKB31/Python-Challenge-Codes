#642

'''
Python | Permutation of a given string using inbuilt function
'''

from itertools import permutations

def allPermutations(str):
    permList = permutations(str)
    for perm in list(permList):
        print(''.join(perm))

if __name__ == "__main__":
    str = 'ABC'
    allPermutations(str)

#################################################################################################################

#643

from itertools import permutations

import string

s = 'GEEK'
a = string.ascii_letters
p = permutations(s)

d = []
for i in list(p):
    if(i not in d):
        d.append(i)
        print(''.join(i))

################################################################################################################

#644

'''
Using recursion
'''

def generate_permutations(string):
    if len(string) == 1:
        return [string]

    permutations = []

    for i in range(len(string)):
        fixed_char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        for perm in generate_permutations(remaining_chars):
            permutations.append(fixed_char + perm)

    return permutations

string = 'GEEK'

permutations_list = generate_permutations(string)
z = set(permutations_list)

for perm in z:
    print(perm)

##############################################################################################################












































































































