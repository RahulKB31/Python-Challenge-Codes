#127

'''
Python program for SUM of squares of first n natural numbers
'''

def squaresum(n):

    # iterate i from l and n finding square of i and add to sum
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i*i)

    return sm

# Driver Program
n = 4
print(squaresum(n))

#################################################################################################

#128

def squaresum(n):
    return (n * (n+1) * (2*n+1)) // 6

# Driven Program
n = 4
print(squaresum(n))

#######################################################################################################

#129

'''
Python program to find sum of squares of first n natural numbers. This program avoids overflow upto
some extent for large value of n.y
'''

def squaresum(n):
    return (n * (n+1) / 2 * (2* n+1)/3)

n = 4
print(squaresum(n))

##########################################################################################################

#130

N = 5

# USe list comprehension to create list of squares
squares_list = [i*i for i in range(1, N+1)]

# find sum of squares using sum() function
sum_of_squares = sum(squares_list)

# print the result
print("Sum of squares of first", N, "natral numbers is", sum_of_squares)

###########################################################################################################

#131

'''
Iterative approach
'''

n = 4
sum = 0
for i in range(1, n+1):
    sum += i**2

print("The sum of squares of first",n, "natural numbers is", sum)

#################################################################################################################

#132

def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n*n + sum_of_squares(n-1)

N = 4
sum_of_squares = sum_of_squares(N)

print("Sum of squares of first", N, "natural numbers:", sum_of_squares)

###################################################################################################################

#133

'''
Difference between sum of the squares of first n natural natural numbers and square of sum
'''

import math

def square_diff(n):

    '''
    Calculate the absoute difference between between the sum of squares and
    the square of sum of the first n natural numbers
    '''

    sum_of_squares = 0
    sum_ = 0
    for i in range(1, n+1):
        sum_of_squares += math.pow(i,2)
        sum_ += i

    square_of_sum = math.pow(sum_, 2)
    abs_difference = abs(sum_of_squares - square_of_sum)
    return int(abs_difference)

n = 10
print(square_diff(n))

######################################################################################################

#134

'''
Sum of squares of first n natural numbers
'''

def summation(n):
    return sum([i**2 for i in range(1, n+1)])

if __name__ == "__main__":
    n = 2
    print(summation(n))

####################################################################################################

#135

'''
Sum of squares of first n natural numbers
'''

def squaresum(n):
    # iterate i from 1 and n finding square of i and add to sum
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i*i)

    return sm

n = 4
print(squaresum(n))

#########################################################################################################

#136

'''
Check if factorial of N is divisible by the sum of squares of first N natural numbers
'''

from math import sqrt

# functon to count number of times prime p divide factorial N
def checkfact(n, countprime, prime):
    countfact = 0
    if (prime == 2 or prime == 3):
        countfact += 1
    divide = prime

    # Lengendre Formula
    while (int(N / divide) != 0):
        countfact += int(N / divide)
        divide = divide * divide

    if (countfact >= countprime):
        return True
    else:
        return False

# Function to find count number of times all prime P divide summation

def check(N):

    # Formula for summation of square after removing n and constant 6
    sumsquares = (N + 1) * (2 * N+1)
    countprime = 0

    # Loop to traverse over all prime p which divide summation
    for i in range(2, int(sqrt(sumsquares)) + 1, 1):
        flag = 0

        while (sumsquares % i == 0):
            flag = 1
            countprime += 1
            sumsquares /= i

        if (flag):
            if (checkfact(N-1, countprime, i) == False):
                return False
            countprime = 0

    # If Number itself is a prime number
    if (sumsquares != 1):
        if (checkfact(N-1,1, sumsquares) == False):
            return False

    return True

#Driver code
if __name__ == "__main__":
    N = 5
    if (check(N)):
        print("Yes")
    else:
        print("No")

##########################################################################################################

#137

'''
Sum of alternating sign of squares of first N natural numbers
'''

def summation(n):

    # variable to store the sum
    sum = 0

    # Loop to iterate each number from 1 to N
    for i in range(1, n+1):
        # the alternating sign is put by checking if the number is even or odd
        if (i % 2 == 1):
            # add the square with the sign
            sum += (i * i)

        else:
            # add the square with the sign
            sum -= (i * i)

    return sum

if __name__ == "__main__":
    N = 2
    print(summation(N))

##########################################################################################################

#138

'''

'''



































