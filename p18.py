#86

'''
Python program to print all prime numbers in an interval
'''

def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

# Driver program
starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The rpime numbers in this range are: ", lst)

####################################################################################################

#87

'''
Optimized way to find a Prime number
'''

def prime(starting_range, ending_range):
    lst = []
    flag = 0
    for i in range(starting_range, ending_range):
        for j in range(2, i):
            if (i%j == 0):
                flag = 1
                break
            else:
                flag = 0
        if (flag == 0):
            lst.append(i)
    return lst

starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)

######################################################################################################

#88

'''
Sieve of Eratosthenes Method
'''

import math

def SieveOfEratosthenes(str, n):

    # create a boolean array prime[str to n] and
    # initialize all entries it as true. A value in
    # prime[i] will finally be false if i is Not a prime, else true
    prime = [True for i in range(n + 2 - str)]
    prime[0] = False
    prime[1] = True

    for p in range(str, int(math.sqrt(n)) + 1):
        # if prime[p] is not changed then it is a prime
        if prime[p] == True:
            # Update all multiples of p greater than or equal
            # to the square of it numbers which are
            # multiple of p and are less then p^2 are
            # already been marked
            for i in range(p*p, n+1, p):
                prime[i] = False

    # Print all prime numbers
    for p in range(str, n+1):
        if prime[p]:
            print(p, end = ' ')

# Driver code
if __name__ == "__main__":
    str = 1
    SieveOfEratosthenes(str, end)

######################################################################################################

#89

'''
Optimized Sieve of Eratosthenes Method
'''

def bitwiseSieve(srt,n):

    # prime[i] is going to store
    # true if if i*2 + 1 is composite
    prime = [0] * int(n / 2)

    # 2 is the only even prime so
    # we can ignore that. Loop
    # starts from 3
    if (srt%2 == 0):
        srt += 1
    if (srt <= 2):
        srt = 3
    i = srt
    while (i * i < n):
        # If i is prime, mark all its multiples as composite
        if (prime[int(i / 2)] == 0):
            j = i * i
            while (j < n):
                prime[int(j / 2)] = 1
                j += i * 2
        i += 2

    # writing 2 seperately
    print(2, end=" ")

    # printing other primes
    i = 3
    while (i < n):
        if (prime[int(i / 2)] == 0):
            print(i, end=" ")
        i += 2

if __name__ == "__main__":
    srt = 1
    end = 10
    bitwiseSieve(srt, end)

#####################################################################################################

#90

'''
Count numbers ina given range having prime and non-prime digits at prime and non-prime positions
respectively
'''

from math import ceil, sqrt

#function to check if a number is prime or not
def isPrime(n):
    # if n is less than or equal to 1
    if (n <= 1):
        return False

    # if n is less than or equal to 3
    if (n <= 3):
        return True

    # If n is a multiple of 2 or 3
    if (n % 2 == 0 or n % 3 == 0):
        return False

    # Iterate over the range [5, n]
    for i in range(5, ceil(sqrt(n)), 6):

        # if n is a multiple of i or (i + 2)
        if (n % i == 0 or n % (i + 2) == 0):
            return False

    return True

# Function to count the required numbers from the given range
def cntNum(pos, st, tight, prime):
    global dp, num

    if (pos == len(num)):
        return 1

    # If the subproblems already computed
    if (dp[pos][st][tight][prime] != -1):
        return dp[pos][st][tight][prime]

    res = 0

    # stores maximum possible at current digits

    for i in range(end + 1):
        # check if 1 is the maximum possible digit at current position or not
        ntight = 1 if (i < end) else tight

        # check if a number contains leading 0s or not
        nzero = 1 if (i != 0) else st

        # if number has only leading zeros and digit is non zero
        if ((nzero == 1) and isPrime(i) and isPrime(prime)):

            # Prime digit at prime positions
            res += cntNum(pos + 1, nzero, ntight, prime + 1)

        if ((nzero == 1) and isPrime(i) == False and isPrime(prime) == False):
            # Non prime digits at non prime positions

            res += cntNum(pos + 1, nzero, ntight, prime + 1)

        # If the number has only leading zeros and i is zero
        if (nzero == 0):
            res += cntNum(pos + 1, nzero, ntight, prime)


    dp[pos][st][tight][prime] = res

    return dp[pos][st][tight][prime]

# Function to find count of numbers in range [0,b] whose digits are prime at prime and non prime at non prime pos

def cntZeroRange(b):

    global num, dp

    num.clear()

    while (b > 0):
        num.append(b % 10)
        b //= 10

    # Reversing the digits in num
    num = num[::-1]

    #print
    dp = [[[[-1 for i in range(19)]
            for i in range(2)]
            for i in range(2)]
           for i in range(19)]

    res = cntNum(0, 0, 0 , 1)

    # Returning the value
    return res

# Driver code
if __name__ == "__main__":
    dp = [[[[-1 for i in range(19)]
            for i in range(2)]
           for i in range(2)]
          for i in range(19)]

    L, R, num = 5, 22, []

    # Function call
    res = cntZeroRange(R) - cntZeroRange(L-1)

    # print answer
    print(res)

#########################################################################################################

#91

'''
Print numbers such that no two consecutive numbers are co-prime and every
three consecutive numbers are co-prime
'''

limit = 10000000000
MAX_PRIME = 2000000
MAX = 1000000
I_MAX = 50000

mp = {}

b = [0] * MAX
p = [0] * MAX
j = 0
prime = [True] * (MAX_PRIME + 1)

# Function to generate Sieve of Eratosthenes
def SieveOfEratosthenes(n):
    global j
    p = 2
    while p * p <= n:
        # if prime[p] is not changed then it is a prime
        if (prime[p] == True):
            for i in range(p* p, n + 1, p):
                prime[i] = False

        p += 1

    # add the prime numbers to the array b
    for p in range(2, n + 1):
        if (prime[p]):
            b[j] = p
            j += 1

# Function to return the gcd of a and b
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

# Function to print the required sequence of integers
def printSeries(n):
    SieveOfEratosthenes(MAX_PRIME)

    ar = [0] * (I_MAX + 2)

    for i in range(j):
        if ((b[i] * b[i + 1]) > limit):
            break

        # Including the primes in a series of primes which will be later multiplied
        p[i] = b[i]

        # This is done to mark a product as existing
        mp[b[i] * b[i + 1]] = 1

    # Maximum number of primes that we consider

    d = 550
    flag = False

    # For Different interval
    k = 2
    while (k < d - 1) and not flag:
        # For different starting index of jump
        m = 2
        while (m < d) and not flag:
            for l in range(m + k, d, k):
                # Checking for occurances of a product. also checking for the same prime occuring consecutively
                if ((b[l] * b[l + k]) < limit) and (l + k) < d and p[i - 1] != b[l + k] and p[i - 1] != b[1] and ((b[l] * b[l + k] in mp) and mp[b[l] * b[l + k]] != 1):
                    if (mp[p[i - 1] * b[l]] != 1):
                        # Including the primes in a series of primes which will
                        # be later multiplied
                        p[i] = b[l]
                        mp[p[i - 1] * b[l]] = 1
                        i += 1

                if (i >= I_MAX):
                    flag = True
                    break
            m += 1

        k += 1

    for i in range(n):
        ar[i] = p[i] * p[i + 1]

    for i in range(n - 1):
        print(ar[i], end = " ")

    g = gcd(ar[n - 1], ar[n - 2])
    print(g * 2)

# Driver code
if __name__ == "__main__":
    n = 4
    printSeries(n)

#############################################################################################################





















































































































































































