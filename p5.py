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
























