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
Python program to print squares of first 'n' natural numbers without using *, / and -
'''

def printSquares(n):
    # Initialize square and previous value of x
    square = 0
    prev_x = 0

    # calculate and print squares
    for x in range(0, n):
        # update value of square using previos values
        square = (square + x + prev_x)

        # print square and update prev for next iteration
        print(square, end = " ")
        prev_x = x

# Driver code
n = 5
printSquares(n)

##########################################################################################################

#139

'''
Split squares of first N natural numbers into two sets with minimum absolute difference of their sums
'''

def minimumSubsetDifference(N):

    # store the count of block of size 8
    blockOfSize8 = N // 8

    # Partition of block of 8 elements
    str = "ABBABAAB"

    # Store the minimum subset difference
    subsetDifference = 0

    # Partition of N elements to minimize their subset sum difference
    partition = ""

    while blockOfSize8 != 0:
        partition = partition + str
        blockOfSize8 = blockOfSize8 - 1

    # store elements of subset A and B
    A = []
    B = []

    for i in range(N):

        # If element is of type A
        if partition[i] == "A":
            A.append((i+1) * (i+1))

        # If the elements is of type B
        else:
            B.append((i+1) * (i+1))

    # Print the minimum subset difference
    print(subsetDifference)

    # Print the first subset
    for i in A:
        print(i, end = " ")
    print()

    # Print the second subset
    for i in B:
        print(i, end = " ")

# Driver code
N = 8

# Function call
minimumSubsetDifference(N)

#####################################################################################################

#140

'''
Kth elel=ment in permutation of first N natural numbers having all even numbers 
placed before odd numbers in incresing order 
'''

# Function to find the k-th element in the required permutation
def findKthElement(N, K):

    # store the required permutation
    v = []

    # Insert all the even numbers less than or equal to N
    for i in range(1, N+1):
        if (i % 2 == 0):
            v.append(i)

    # Now insert all odd numbers less than or equal to N
    for i in range(1, N+1):
        if (i % 2 != 0):
            v.append(i)

    # print the kth element
    print(v[K - 1])

# Driver code
if __name__ == "__main__":
    N = 10
    K = 3
    findKthElement(N, K)

######################################################################################################

#141

'''
Python program for cube sum of first n natural numbers
'''

def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum += pow(i,3)

    return sum

# Driver Function
n = 5
print(sumOfSeries(n))

#########################################################################################################

#142

'''
Minimize sum of numbers required to convert an array into a permutation of first n natural numbers
'''

# Function to find the minimum additions required to convert the array into a permutation of 1 to N

def minimumAdditions(a, n):

    # sort the array in increasing order
    a = sorted(a)
    ans = 0

    # Traverse the array
    for i in range(n):

        # If a[i] > i + 1, then return -1
        if ((i+1) - a[i] < 0):
            return -1

        if ((i+1) - a[i] > 0):

            # update answer
            ans += (i + 1 - a[i])

    # Return the required result
    return ans

# Driver code
if __name__ == "__main__":

    # Given input
    A = [1,1,1,1,1]
    n = len(A)

    print(minimumAdditions(A, n))

######################################################################################################
































