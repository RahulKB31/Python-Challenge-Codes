#92

'''
Python programs to check if the number is Prime or not in Python
'''

num = 11
# if the given number is greater than 1
if num > 1:
    # Iterate from 2 to n/2
    for i in range(2, int(num/2) + 1):
        # if num is divisible by any number between 2 and n/2, is is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")

#######################################################################################################

#93

'''
Find prime numbers with a flag variable
'''

from math import sqrt
# n is the number to be check whether it is prime or not
n = 1

# this flag maintains status whether the n is prime or not
prime_flag = 0

if (n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("True")
    else:
        print("False")
else:
    print("False")

#####################################################################################################

#94

'''
Check prime numbers using recursion
'''

from math import sqrt

def Prime(number, itr): # prime function to check given number prime or not
    if itr == 1: # base condition
        return True
    if number % itr == 0: # if given number divided by itr or not
        return False
    if Prime(number, itr-1) == False: # recursive function call
        return False

    return True

num = 13

itr = int(sqrt(num) + 1)

print(Prime(num,itr))

#####################################################################################################

#95

'''
Check the prime trial division method
'''

def is_prime_trial_division(n):
    # check if the number is less than or equal to 1, return False if it is
    if n <= 1:
        return False
    # loop through all numbers from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # if n is divisible by any of these numbers, return False
        if n % i == 0:
            return False
    # if n is not divisible by any of these numbers, return True
    return True

# test the function with n = 11
print(is_prime_trial_division(11))

######################################################################################################

#96

'''
Python program to check prime number using a while loop to check divisibility
'''

import math

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(11))
print(is_prime(1))

########################################################################################################

#97

'''
Python program to check prime number using math module 
'''

import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = 11
print(is_prime(n))

#########################################################################################################

#98

'''
Python program to check prime number using sympy.isprime() method
'''

from sympy import *

# calling isprimefunction on different numbers
geek1 = is_prime(30)
geek2 = is_prime(13)
geek3 = is_prime(2)

print(geek1) # check for 30 is prime or not
print(geek2) # check for 13 is prime or not
print(geek3) # check for 2 is prime or not

########################################################################################################

#99

'''
CHeck if a number is prime, semi prime or composite for very large numbers
'''

def prime(n):
    flag = 0

    # checking divisibility by 6
    if ((n + 1) % 6 != 0 and (n - 1) % 6 != 0):
        print("Not Prime")
    else:
        # breakout if number is perfect square
        s = pow(n, 1/2)
        if ((s * s) == n):
            print("Semi-Prime")
        else:
            f = int(s)
            l = int(f * f)

            # iterating over to get the closest average value
            for i in range(f + 1, l):
                # 1st factor
                p = i - (pow(((i * i) - (n)), 1/2))

                #2nd factor
                q = n // p

                # to avoid convergence
                if (p < 2 or q < 2):
                    break

                # checking semi-prime condition
                if ((p * q) == n):
                    flag = 1
                    break

                # if convergence found then number is semi-prime
                else:
                    # convergence not found then number is prime
                    flag = 2

            if (flag == 1):
                print("Semi-Prime")
            elif (flag == 2):
                print("Prime")

# Driver code
if __name__ == "__main__":
    # Entered number should be greater than 300 to avoid convergence of second factor to 1
    prime(8179)
    prime(7884793)
    prime(90000000000)
    prime(841)
    prime(22553)
    prime(1187)

###########################################################################################################

#100

'''
Check if a prime number can be expressed as a sum of two prime numbers
'''

import math

# function to check whether a number is prime or not
def isPrime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n%2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n%i == 0:
            return False

    return True

# Function to check if a prime number can be expressed as sum of two Prime numbers

def isPossible(n):

    # if the number is prime and number-2 is also prime
    if isPrime(n) and isPrime(n - 2):
        return True
    else:
        return False

# Driver code
n = 13
if isPossible(n) == True:
    print("Yes")
else:
    print("No")

######################################################################################################


























































































































































































































































































































































