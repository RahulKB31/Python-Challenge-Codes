#19

'''
Write a function that outputs a square pattern of the form
+0+0+0+0+0+
0+0+0+0+0+0
+0+0+0+0+0+
0+0+0+0+0+0
+0+0+0+0+0+
0+0+0+0+0+0
+0+0+0+0+0+
0+0+0+0+0+0
+0+0+0+0+0+
0+0+0+0+0+0
+0+0+0+0+0+
The function should take 3 arguments, the size of the square (which should be odd) and the two characters to
be used in the display.
You should first generate the two strings for odd and even rows (create a string comprising 2 characters, use
the * operator to generate strings of appropriate lengths containing multiple copies of the 2-character string,
then concatenate with an extra copy of the first character.
Then use a loop to output pairs or lines, and output the final line at the end.
Test with several calls to the function to generate squares of different sizes
'''

def pattern(firstChar, secondChar, size):
    '''
    displays a square pattern with alternating characters
    arguments: firsChar, secondChar: two different characters to use in pattern
    size: size of square (should be odd)
    '''
    if size%2 ==0:
        print("Size argument should be odd")
    elif size < 0:
        print("Size cannot be negative")
    elif firstChar==secondChar:
        print("have to use 2 different characters")
    else:
        firstPair = firstChar + secondChar
        secondPair = secondChar + firstChar
        nPairs = size//2
        firstString = firstPair * nPairs + firstChar
        secondString = secondPair * nPairs + secondChar
        for i in range(0,size-1,2):
            print(firstString)
            print(secondString)
        print(firstString)
    print() # to give blank lines between calls

pattern('*','+',15)
pattern('0','#',7)
pattern("0","#",6)
pattern("0","#",-5)
pattern("x","x",3)

####################################################################################################

#20

"""
Modify your solution to exercise 1 so the output is a triangle of the form
+0+0+0+0+0+
0+0+0+0+0+
+0+0+0+0+
0+0+0+0+
+0+0+0+
0+0+0+
+0+0+
0+0+
+0+
0+
+
"""

def pattern(firstChar, secondChar, size):
    '''
    displays a triangle pattern with alternating characters
    arguments: firstChar, secondChar: two different characters to use in pattern
    Size; size of triangle (should be odd)
    '''

    if size%2 == 0:
        print("Size argument should be odd")
    elif size<0:
        print("Size cannot be negative")
    elif firstChar==secondChar:
        print("Have to use 2 different characterrs")
    else:
        firstPair = firstChar + secondChar
        secondPair = secondChar + firstChar
        nPairs = size//2
        firstString = firstPair * nPairs + firstChar
        secondString = secondPair * nPairs # dont need to add extra copy ofsecondChar this time
        for i in range(size,1, -2):
            print(firstString[:i])
            print(secondString[:i-1])
        print(firstString[0])
    print() #to give blank lines between calls

pattern("^","0",15)
pattern("-","#",9)

#######################################################################################################

#21

# Write a function that takes as an argument a list of strings and returns a list of the characters (if any) that
# occur in all of the strings.

def commonChars(strings):
    '''
    returns a list of characters that occur in all of the strings
    argument: strings: list of strings
    return: list of single-character strings
    '''

    # deal with special cases first
    if len(strings) == 0:
        return []
    elif len(strings) == 1:
        result = []
        for ch in strings[0]:
            # avoid duplicate chars in result
            if ch not in result:
                result.append(ch)
        return result

    result = []
    for ch in strings[0]:
        # again avoid duplicate chars in result
        if ch not in result:
            occurs = True
            for s in strings[1:]: # check if ch occurs in all other strings
                # if it's missing from any string it's not in all of them
                if ch not in s:
                    occurs = False
            if occurs:
                result.append(ch)
    return result

s1 = "Python"
s2 = "Monty"
s3 = "Hello world"
s4 = "Goodbye world"
s5 = "Cruel world"

print(commonChars([s1,s2,s3,s4,s5]))
print(commonChars([s3,s4,s5]))
print(commonChars([s1,s2]))
print(commonChars([s1]))
print(commonChars([s1,'x']))
print(commonChars([]))

#########################################Deplicate version############################################

#22

def commonChars(strings):
    '''
    returns a list of characters that occur in all of the strings
    argument: strings: list of strings
    return: list of single character strings
    '''

    #deal with special cases first
    if len(strings) == 0:
        return []
    elif len(strings) == 1:
        result = []
        for ch in strings[0]:
            # avoid duplicate chars in result
            if ch not in result:
                result.append(ch)
        return result

    result = []
    for ch in strings[0]:
        # again avoid duplicate chars in result
        if ch not in result:
            for s in strings[1:]: # check if ch occurs in all other strings
                # if it's missing from any string it's not in all of them
                if ch not in s:
                    break
            else: # get here only if we did not break, ch is in all strings
                result.append(ch)
    return result

s1 = "Python"
s2 = "Monty"
s3 = "Hello world"
s4 = "Goodbye world"
s5 = "Cruel world"

print(commonChars([s1,s2,s3,s4,s5]))
print(commonChars([s3,s4,s5]))
print(commonChars([s1,s2]))
print(commonChars([s1]))
print(commonChars([s1,'x']))
print(commonChars([]))

################################################################################################

#23

# this exercises was in the slides before the use of the in operator
# with strings was covered
# hence I've compared individual pairs of characters to see if letters
# in the first string also appear in the second one

def commonChars(str1, str2):
    '''
    prints all characters that appear in both strings
    arguments: str1, str2: strings
    return: nothing
    '''
    checkedchars = []
    foundOne = False
    for char in str1:
        # skip if we've already checked it
        if char not in checkedchars:  # can use not in as an operator
            for ch in str2:
                if char==ch:
                    foundOne = True
                    if char == ' ':
                        print("A space apppears in both strings")
                    else:
                        print(char, "appears in both strings")
                    break
            checkedchars += char
    if not foundOne:
        print("There were no common characters")

commonChars("Hello world", "Python is Hot")
print("----------------------------------------")
commonChars("abcdefghijklm", "zyzyzksdkjfhskj")
print("----------------------------------------")
commonChars("abcdefghijklm", "ABC")

#################################################################################################

