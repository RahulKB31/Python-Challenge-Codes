#52

'''
Find maximum of two numbers in python

(This is the naive approach where we will compare two numbers
using if-else statement ad will print the output accordingly
'''


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


# Driver code
a = 2
b = 3
print(maximum(a, b))

###############################################################################################

#53

'''
Find maximum of two numbers using max() function
'''

a = 2
b = 4

maximum = max(a, b)
print(maximum)

########################################################################################

#54

'''
Maximum of two numbers using ternary operator

This operator is also knwon as conditional expression are operators that evaluate something 
based on a condition being true or flase. It simply allows testing a condition in a single line
'''

# Driver code
a = 2
b =4

# Use of ternary operator
print(a if a>=b else b)

################################################################################################

#55

'''
Maximum of two numbers using lambda function
'''

a = 2; b=4
maximum = lambda a,b: a if a > b else b
print(f'{maximum(a,b)} is a maximum number')

#######################################################################################

#56

'''
Maximum of two numbers using list comprehension
'''

a = 2; b=4
x = [a if a > b else b]
print("maximum number is:", x)

##########################################################################################

#57

'''
Maximum of two numbers using sort() method
'''

a = 2
b = 4

x = [a,b]
x.sort()
print(x[-1])

#############################################################################################















































































