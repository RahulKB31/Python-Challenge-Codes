#513

'''
Python program to check whether the string is Symmetrical or Palindrome
'''

def palindrome(a):

    # finding the mi, start and last index of the string
    mid = (len(a)-1)//2
    start = 0
    last = len(a) - 1
    flag = 0

    while(start <= mid):

        #comparing letters from right from the letters from left
        if (a[start] == a[last]):

            start += 1
            last -= 1

        else:
            flag = 1
            break

    #checking the flag variable to check if the string is palindrome or not
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")

#function to check whether the string is symmetrical or not
def symmetry(a):

    n = len(a)
    flag = 0

    #check if the strings length is odd or even
    if n%2:
        mid = n//2 + 1
    else:
        mid = n//2

    start1 = 0
    start2 = mid

    while(start1 < mid and start2 < n):

        if (a[start1] == a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break

    #checking the flag variable to check if the string is symmetrical or not
    if flag == 0:
        print("The enterred string is symmetrical")
    else:
        print("The entered string is not symmetrical")

string = 'amaama'
palindrome(string)
symmetry(string)

####################################################################################################################

#514

'''
Use slicing in this method
'''

string = 'amaama'
half = int(len(string) / 2)

first_str = string[:half]
second_str = string[half:]

if first_str == second_str:
    print(string, 'string is symmetrical')
else:
    print(string, 'string is not symmetrical')

#palindrome
if first_str == second_str[::-1]:
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')

############################################################################################################

#515

'''
Using re module
'''

import re

input_str = "amaama"
reversed_str = input_str[::-1]

if input_str == reversed_str:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")

if re.match("^(\w+)\z", input_str) and input_str == input_str[::-1]:
    print("The entered string is palindrome")

else:
    ("The entered string is not palindrome")

###########################################################################################################

#516

'''
Using the reversed()
'''

string = 'malayalam'
print("The string is palindrome" if string == reversed(string) else 'the string is not palindrome')

##############################################################################################################















































































































































































































