#58

'''
Python program to find the factorial of a number
'''

# Find the factorial of a number using recursive approach

'''
This python program uses a recursive function to calculate the factorial of a given number.
The factorial is computed by mutiplying the number with the factorial of its preceding number.
'''

# factorial of a given number

def factorial(n):

    # single line to find factorial
    return 1 if(n==1 or n==0) else n * factorial(n-1)

# Driver code
num = 5
print("Factorial of", num, "is", factorial(num))

##################################################################################################

#59

'''
Find the factorial of number using iterative approach
'''

# Factorial of a given number

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact

# Driver code
num = 5
print("Factorial of", num, "is", factorial(num))

##########################################################################################################

#60

# Function to find the factorial of a given number

def factorial(n):
    res = 1

    for i in range(2, n+1):
        res *= i
    return res

#Driver code
num = 5
print("Factorial of", num, "is", factorial(num))

##########################################################################################################

#61

'''
Find the factorial of a number using one line solution (Using ternary operator):
'''

def factorial(n):

    #single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n-1)

#Driver code
num = 5
print("Factorial of", num, "is", factorial(num))

########################################################################################################

#62

'''
Find the factorial of a number using in-built function
'''

import math
def factorial(n):
    return (math.factorial(n))

#Driver code
num = 5
print("Factorial of", num, "is", factorial(n))

#############################################################################################

#63

'''
Find the factorial of a number using numpy.prod
'''

import numpy
n = 5
x = numpy.prod([i for i in range(1, n+1)])
print(x)

###################################################################################################

#64

'''
Prime factorization method to find factorial
'''

def primeFactors(n):
    factors = {}
    i =2
    while i*i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    return factors

# Function to find factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n+1):
        factors = primeFactors(i)
        for p in factors:
            result *= p **factors(p)
    return result

#Driver code
num = 5
print("Factorial of", num, "is", factorial(num))

########################################################################################################

#65

'''
Find the last digit when factorial of A divides factorial of B
'''

def computeLastDigit(A,B):
    variable = 1
    if (A == B):
        return 1

    # if difference (B-A) >= 5, answer = 0
    elif ((B-A) >= 5):
        return 0

    else:
        for i in range(A+1, B+1):
            variable = (variable * (i % 10)) % 10

        return variable % 10

#driver function

print(computeLastDigit(2632, 2634))

###################################################################################################

#66

'''
This approach calculates the factorial of A 
using recursion and divides the factorial of B with it to get the last digit
'''

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def last_digit(A, B):
    fact_A = factorial(A)
    fact_B = factorial(B)
    return fact_B // fact_A % 10

print(last_digit(2, 4))
print(last_digit(107, 109))

#################################################################################################

#67

"""
Recursive program to find factorial of large number
"""

def multiply(n, digits):

    #Initialize carry
    carry = 0

    #one by one multiply n with individual digits of res[]
    for i in range(len(digits)):
        result = digits[i] * n + carry

        # store last digit of prod in res[]
        digits[i] = result % 10

        #put rest in carry
        carry = result//10

    # put carry in res and increase result size
    while (carry):
        digits.append(carry % 10)
        carry = carry // 10

    return digits

# Function to recursively calculate the factorial of a large number
def factorialRecursiveAlgorithm(n):
    if (n <= 2):
        return multiply(n, [1])

    return multiply(n, factorialRecursiveAlgorithm(n-1))

if __name__ == "__main__":
    n = 50

    result = factorialRecursiveAlgorithm(n)

    for i in range(len(result) - 1, -1, -1):
        print(result[i], end="")

################################################################################################

#68

'''
Python program to count trailing zeros in factorial of a number
'''

def findTrailingZeros(n):

    #Initializing result
    count = 0

    #keep dividing n by powers of 5 and update count
    i = 5
    while (n/i >= 1):
        count += int(n/i)
        i *= 5

    return int(count)

# Driver program
n = 100
print("Count of trailing Os" + "in 100! is", findTrailingZeros(n))

##################################################################################################




















































































