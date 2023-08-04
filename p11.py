#46

'''
Python programming to add two numbers
'''

# Simple program to add two numbers
num1 = 15
num2 = 12

sum = num1 + num2

print("Sum of", num1, "and", num2, "is", sum)

##########################################################################################

#47

# Adding two numbers with user input

number1 = input("First number: ")
number2 = input("\nSecond NUmber: ")

# Adding two numbers
# User might also enter float numbers
sum = float(number1) + float(number2)

#Display the sum
# will print value in float

print("The sum of {0} and {1} is {2}".format(number1, number2, sum))


##################################################################################################

#48

# Defining add function and returning the result

def add(a, b):
    return a+b

# Initializing the variables
num1 = 10
num2 = 5

# function calling and store the result into the sum of two numbers
sum_of_twonumbers = add(num1, num2)

# To print the result
print("Sum of {0} and {1} is {2};".format(num1, num2, sum_of_twonumbers))

###################################################################################################

#49

'''
Add two numbers in python using operator.add() method
'''

num1 = 15
num2 = 12

# Adding two numbers
import operator
su = operator.add(num1, num2)

# printing values
print("Sum of {0} and {1} is {2}".format(num1, num2, su))

##########################################################################################

#50

'''
Adding two number using lambda function
'''

add_numbers = lambda x, y: x + y

# Take input from the user
num1 = 1
num2 = 2

# Call the lambda function to add the two numbers
result = add_numbers(num1, num2)

#Print the result
print("The sum of", num1, "and",num2, "is", result)

#############################################################################################

#51

'''
Python prgram to add two numbers with recursive function
(This code defines a recursive function to add two numbers by incrementing one numbers and decrementing the other.
User inputs two numbers and the sum id calculated and displayed
'''

def add_numbers_recursive(x, y):
    if y==0:
        return x
    else:
        return add_numbers_recursive(x+1, y-1)

# Take input from the user
num1 = 1
num2 = 2

# CAll the recursive function to add the two numbers

result = add_numbers_recursive(num1, num2)

#print the result
print("The sum of", num1, "and", num2, "is", result)

############################################################################################








































































