#986

'''
Python program for efficient program to print all prime factors of a given number
'''

import math

# A function to print all prime factors of a given number n
def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n // 2

    # n must be odd at this point so a skip of 2 (i=i+2) can be used
    for i in range(3,int(math.sqrt(n))+1, 2):

        # while i divides n, print i and divide n
        while n % i == 0:
            print(i)
            n = n // i

        # condition if n is a prime number greater than 2
        if n > 2:
            print(n)

n =315
primeFactors(n)

#####################################################################################################################

#987

def primeFactors(n):
    spf = [o for i in range(n+1)]
    spf[1] = 1
    for i in range(2, n+1):
        spf[i] = i
    for i in range(4, n+1, 2):
        spf[i] = 2

    for i in range(3, int(n**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i

    while n != 1:
        print(spf[n], end = " ")
        n = n // spf(n)

n = 315
primeFactors(n)

#######################################################################################################################