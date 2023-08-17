#572

'''
Python program to accept the strings which cotains all vowels
'''

# USing set() function

def check(string):
    string = string.lower()

    vowels = set("aeiou")
    s = set({})

    for char in string:

        if char in vowels:
            s.add(char)
        else:
            pass

    if len(s) == len(vowels):
        print("Accepted")
    else:
        print("Not accepted")

if __name__ == "__main__":
    string = "SEEquoial"
    check(string)

################################################################################################################

#573

'''
String which contains all vowels using builtin
'''

def check(string):
    string = string.replace(' ','')
    string = string.lower()
    vowel = [string.count('a'),string.count('e'),string.count('i'),string.count('o'),string.count('u')]

    if vowel.count(0) > 0:
        return ('not accepted')
    else:
        return ('accepted')

if __name__ == "__main__":
    string = "SEEquoiaL"
    print(check(string))

########################################################################################################

#574

def check(string):
    if len(set(string.lower()).intersection("aeiou")) >= 5:
        return ("accepted")
    else:
        return ("not accepted")

if __name__ == "__main__":
    string = "geekforgeeks"
    print(check(string))

#########################################################################################################

#575

'''
Using regular expressions
'''

import re

sampleInput = "aeiouAEiuioea"

c = re.compile('[^aeiouAEIOU]')

if (len(c.findall(sampleInput))):
    print("Not accepted")
else:
    print("Accepted")

################################################################################################################

#576

'''
Accept the strings which contains all vowelsusing data structures
'''

def all_vowels(str_value):
    new_list = [char for char in str_value.lower() if char in 'aeiou']

    if new_list:

        dic, lst = {}, []

        for char in new_list:
            dic['a'] = new_list.count('a')
            dic['e'] = new_list.count('e')
            dic['i'] = new_list.count('i')
            dic['o'] = new_list.count('o')
            dic['u'] = new_list.count('u')

        for i,j in dic.items():
            if j==0:
                lst.append(i)

        if lst:
            return f"All vowels except {','.join(lst)} are not present"
        else:
            return 'All vowels are present'

    else:
        return 'No vowels present'

str_value = "geeksforgeeks"
print(all_vowels(str_value))

str_value = "ABeeIghkjhadIOoiafd"
print(all_vowels(str_value))

################################################################################################################

#577

'''
Accept the strings which contains all vowels using set methods
'''

def check(string):
    if set("aeiou").issubset(set(string.lower())):
        return "Accepted"
    return "Not accepted"

if __name__ == "__main__":
    string = "SEEquoil"
    print(check(string))

################################################################################################################

#578

'''
Accept the strings which contains all vowels using collections
'''

import collections

def check(string):

    counter = collections.Counter(string.lower())

    vowels = set("aeiou")

    vowel_count = 0

    for vowel in vowels:
        if counter[vowel] > 0:
            vowel_count += 1

    if vowel_count == len(vowels):
        print("Accepted")
    else:
        print("Not accepted")

string = 'SEEquoial'
check(string)

#############################################################################################################

#579

'''
Accept the strings which contains all vowels using all() method
'''

def check(string):
    vowels = "aeiou"
    if all(vowel in string.lower() for vowel in vowels):
        return "Accepted"
    return "Not Accepted"

string = "SEEquoial"
print(check(string))

############################################################################################################

#580

'''
Accept the strings which contains all vowels using set.difference() method
'''

def check(s):
    A = {'a','e','i','o','u'}

    if len(A.difference(set(s.lower()))) == 0:
        print('accepted')

    else:
        print('not accepted')

s = 'SEEquoial'
check(s)

##################################################################################################################























































































































































































































































