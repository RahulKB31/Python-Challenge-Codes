#984

'''
Python program for find largest prime factor of a number
'''

import math

# A function to find largest prime factor
def maxPrimeFactors(n):
    # Intitialize the maximum prime factor
    # variab;e with the lowest one
    maxPrime = -1

    # print the number of 2s that divide n
    while n%2 == 0:
        maxPrime = 2
        n >>= 1

    # n must be odd at this point, thus skip the even numbers and iterate only for odd integers
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            maxPrime = i
            n = n/i

    # This condition is to handle the case when n is a prime number greater than 2
    if n > 2:
        maxPrime = n

    return int(maxPrime)

# Driver code to tst above function
n = 15
print(maxPrimeFactors(n))

n = 2565476834721
print(maxPrimeFactors(n))

#######################################################################################################################

#985

def largest_prime_factor(n):
    largest_prime = -1
    i = 2
    while i*i <= n:
        while n % i == 0:
            largest_prime = i
            n = n//i
        i = i + 1
    if n > 1:
        largest_prime = n
    return largest_prime

n = 15
print(largest_prime_factor(n))

n = 23413742894357
print(largest_prime_factor(n))

#####################################################################################################################

