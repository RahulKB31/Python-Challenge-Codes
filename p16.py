#76

'''
Python program to check armstrong number
'''

# Function to calculate x raised to the power y
def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)

    return x * power(x, y // 2) * power(x, y // 2)

# Function to calculate order of the number

def order(x):

    # variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10

    return n

# Function to check whether the given number is Armstrong number or not

def isArmstrong(x):

    n = order(x)
    temp = x
    sum1 = 0

    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10

    # If condition satisfies
    return (sum1 == x)

# Driver code
x = 153
print(isArmstrong(x))

x = 1253
print(isArmstrong(x))

##########################################################################################################

#77

'''
Python program to check if a number is an armstrong number without using the power function
'''

n = 153
s = n # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n!= 0:
    r = n % 10
    sum1 = sum1 + (r**b)
    n = n // 10

if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")

#########################################################################################################

#78

'''
Python program to check if a number is an Armstrong number string manipulation
'''

def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**n
    if sum == num:
        return True
    else:
        return  False

num = 153
print(is_armstrong(num))

##########################################################################################################

#79

'''
Digit by digit sum approach to check for Armstrong number
'''

import math

def isArmstrong(num):
    n = num
    numDigits = 0
    sum = 0

    # Find number of digits in num
    while n > 0:
        n //= 10
        numDigits += 1

    n = num

    # calculate sum of digits raised to the power of numDigits
    while n > 0:
        digit = n % 10
        sum += math.pow(digit, numDigits)
        n //= 10

    # Check if num is Armstrong number or not
    if sum == num:
        return True
    return False

#Example 1
num1 = 1634
if isArmstrong(num1):
    print(num1, "is an Armstrong number")
else:
    print(num1, "is not an Armstrong number")

# Example 2
num2 = 120
if isArmstrong(num2):
    print(num2, "is an Armstrong number")
else:
    print(num2, "is not an Armstrong number")

########################################################################################################

#80

'''
Python program to check if a number is an Armstrong number in return statement
'''

def is_armstrong_number(number):
    return  sum(int(digit) ** len(str(number)) for digit in str(number)) == number

num = 153
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

######################################################################################################








































































































