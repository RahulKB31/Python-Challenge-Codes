<<<<<<< HEAD
#546

'''
Python - convert snake case to pascal case
'''

# using title() + replace()

test_str = "geeksforgeeks_is_best"

print("The original string is: "+ test_str)

res = test_str.replace("_"," ").title().replace(" ","")

print("The string after changing case: " + str(res))

###############################################################################################################

#547

'''
Using capwords()
'''

import string

test_str = "geeksforgeeks_is_best"

print("The original string is: "+ test_str)

res = string.capwords(test_str.replace("_"," ").title().replace(" ",""))

print("The string after changing case: " + str(res))

###############################################################################################################

#548

'''
Using split().title() and join() methods
'''

test_str = "geeksforgeeks_is_best"

print("The original string is: "+ test_str)

x = test_str.split("_")
res = []
for i in x:
    i = i.title()
    res.append(i)
res="".join(res)

print("The string after changing case: " + str(res))

###############################################################################################################

#549

'''
Using capitalize
'''

def snake_to_pascal_1(snake_str):
    words = snake_str.split("_")
    pascal_str = "".join([word.capitalize() for word in words])
    return pascal_str
snake_str = 'geeksforgeeks_is_best'
print(snake_to_pascal_1(snake_str))

#############################################################################################################

#550

'''
Using the split() method
'''

string = 'geeksforgeeks_is_best'

words = string.split('_')
capitalized_words = [word.title() for word in words]
result = ''.join(capitalized_words)

print(result)

##################################################################################################################

#551

'''
Using reduce()
'''

from functools import reduce

test_str = 'geeksforgeeks_is_best'

print("The original string is: " + test_str)

res = reduce(lambda a, b: a+b.title(), test_str.split("_"),"")

print("The string after changing case: " + str(res))

##################################################################################################################

#552

def snake_to_pascal(input_str):
    result = ""
    capitalize_next_word = True

    for char in input_str:
        if char == "_":
            capitalize_next_word = True
        elif capitalize_next_word:
            result += char.upper()
            capitalize_next_word = False
        else:
            result += char

    return result

print(snake_to_pascal("geeks_for_geeks"))
print(snake_to_pascal("left_index"))

##################################################################################################################

#553

'''
Using regular expressions
'''

import re

def snake_to_pascal_case_2(snake_str):

    return re.sub(r"(^|_)([a-z])", lambda match: match.group(2).upper(), snake_str)

snake_str = 'geeksforgeeks_is_best'
print(snake_to_pascal_case_2(snake_str))

##################################################################################################################






















































































































































=======
#546

'''
Python - convert snake case to pascal case
'''

# using title() + replace()

test_str = "geeksforgeeks_is_best"

print("The original string is: "+ test_str)

res = test_str.replace("_"," ").title().replace(" ","")

print("The string after changing case: " + str(res))

###############################################################################################################

#547

'''
Using capwords()
'''

import string

test_str = "geeksforgeeks_is_best"

print("The original string is: "+ test_str)

res = string.capwords(test_str.replace("_"," ").title().replace(" ",""))

print("The string after changing case: " + str(res))

###############################################################################################################

#548

'''
Using split().title() and join() methods
'''

test_str = "geeksforgeeks_is_best"

print("The original string is: "+ test_str)

x = test_str.split("_")
res = []
for i in x:
    i = i.title()
    res.append(i)
res="".join(res)

print("The string after changing case: " + str(res))

###############################################################################################################

#549

'''
Using capitalize
'''

def snake_to_pascal_1(snake_str):
    words = snake_str.split("_")
    pascal_str = "".join([word.capitalize() for word in words])
    return pascal_str
snake_str = 'geeksforgeeks_is_best'
print(snake_to_pascal_1(snake_str))

#############################################################################################################

#550

'''
Using the split() method
'''

string = 'geeksforgeeks_is_best'

words = string.split('_')
capitalized_words = [word.title() for word in words]
result = ''.join(capitalized_words)

print(result)

##################################################################################################################

#551

'''
Using reduce()
'''

from functools import reduce

test_str = 'geeksforgeeks_is_best'

print("The original string is: " + test_str)

res = reduce(lambda a, b: a+b.title(), test_str.split("_"),"")

print("The string after changing case: " + str(res))

##################################################################################################################

#552

def snake_to_pascal(input_str):
    result = ""
    capitalize_next_word = True

    for char in input_str:
        if char == "_":
            capitalize_next_word = True
        elif capitalize_next_word:
            result += char.upper()
            capitalize_next_word = False
        else:
            result += char

    return result

print(snake_to_pascal("geeks_for_geeks"))
print(snake_to_pascal("left_index"))

##################################################################################################################

#553

'''
Using regular expressions
'''

import re

def snake_to_pascal_case_2(snake_str):

    return re.sub(r"(^|_)([a-z])", lambda match: match.group(2).upper(), snake_str)

snake_str = 'geeksforgeeks_is_best'
print(snake_to_pascal_case_2(snake_str))

##################################################################################################################






















































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
