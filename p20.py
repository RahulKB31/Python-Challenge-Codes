#101

'''
Python program for n-th Fibonacci number
'''

def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # False Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program
print(Fibonacci(10))

########################################################################################################

#102

'''
Python program for n-th Fibonacci number using Dynamic Programming
'''

FibArray = [0,1]

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n-1) + fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib

print(fibonacci(9))

######################################################################################################

#103

'''
n-th Fibonacci number using Dynamic Programming with space Optimization
'''

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect Input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(9))

######################################################################################################

#104

'''
Python program for n-th Fibonacci number using Arrays
'''

def fibonacci(n):
    if n <= 0:
        return "Incorrect Output"
    data = [0, 1]
    if n > 2:
        for i in range(2, n):
            data.append(data[i-1] + data[i-2])
    return data[n-1]

print(fibonacci(9))

#########################################################################################################

#105

'''
Python programming for n-th Fibonacci number using direct formula
'''

from math import sqrt

def nthFib(n):
    res = (((1 + sqrt(5))**n) - ((1-sqrt(5)))**n)/(2**n*sqrt(5))
    # compute the n-th fibonacci number
    print(int(res), "is", str(n) + "th fibonacci number")

nthFib(12)

##########################################################################################################

#106

'''
Python program for n-th Fibonacci number using power of the matrix {{1,1},{1,0}}
'''
def fib(n):
    F = [[1,1],
         [1,0]]
    if (n == 0):
        return 0
    power(F, n -1)
    return F[0][0]

def multiply(F,M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    M = [[1,1],[1,0]]
    for i in range(2, n+1):
        multiply(F,M)

# Driver code
if __name__ == "__main__":
    n = 9
    print(fib(n))

###########################################################################################################

#107

'''
Optimized power of the matrix method
'''

def fib(n):
    F = [[1,1],[1,0]]
    if (n == 0):
        return 0
    power(F, n-1)

    return F[0][0]

def multiply(F,M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F,n):
    if (n == 0 or n == 1):
        return
    M = [[1,1],
         [1,0]]

    power(F, n//2)
    multiply(F,F)

    if (n % 2 != 0):
        multiply(F,M)

if __name__ == "__main__":
    n = 5
    print(fib(n))

#######################################################################################################

#108

'''
Check if a M-th fibonacci number divides N-th fibonacci number
'''

def check(n,m):

    #exceptional case for F(2)
    if (n == 2 or m ==2 or n % m == 0):
        print("Yes")

    else:
        print("no")

m = 3
n = 9
check(n,m)

##############################################################################################################

#109

'''
Check if sum of Fibonacci elements in an array is a Fibonacci number or not
'''

MAX = 100005

fibonacci = set()

def createHash():
    global fibonacci

    # inserting the first two fibonacci numbers into the hash
    prev, curr = 0, 1
    fibonacci.add(prev)
    fibonacci.add(curr)

    # add the remaining fibonacci numbers based on the previous two numbers
    while (curr <= MAX):
        temp = curr + prev
        if temp <= MAX:
            fibonacci.add(temp)
        prev = curr
        curr = temp

# Function to check if the sum of fibonacci numbers is fibonacci or not

def checkArray(arr, n):

    sum = 0

    # iterating through the array
    for i in range(n):
        if (arr[i] in fibonacci):
            sum += arr[i]

    # if the sum is fibonacci then return true
    if (sum in fibonacci):
        return True

    return False

# Driver code
if __name__ == "__main__":
    arr = [1,2,4,8,2]
    n = len(arr)

    # creating a set containing all fibonacci numbers
    createHash()

    if (checkArray(arr, n)):
        print("Yes")
    else:
        print("No")

#########################################################################################################

#110

'''
Python program to check if a given number is fibonacci number
'''

import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):

    # n is fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

# a utility function to test above functions

for i in range(1,11):
    if (isFibonacci(i) == True):
        print(i, "is a Fibonacci number")
    else:
         print(i, "is not a fibonacci number")

#####################################################################################################

#111

'''
Python program for nth multiple of a number in fibonacci series
'''

def findPosition(k, n):
    f1 = 0
    f2 = 1
    i = 2
    while i != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if f2 % k == 0:
            return n*i

        i += 1

    return

#Multiple no
n = 5
# number of whose multiple we are finding
k = 4

print("Position of n\'th multiplr of k is in Fibonacci series is", isFibonacci(k,n))

#########################################################################################################

#112

'''
Program to find last two digits of nth fibonacci number
'''

def precomput(f):
    # oth and 1st number of the series are 0 and 1
    f.append(0)
    f.append(1)

    # aad the previous 2 numbers in the series in the series and store last two digits of result
    for i in range(2, 300):
        f.append((f[i-1] + f[i-2]) % 100)

# Returns last two digits of nth Fibonacci number
def findLastDigit(f, n):
    return f[n % 300]

# driver code
f = list()
precomput(f)
n = 1
print(findLastDigit(f,n))
n = 61
print(findLastDigit(f,n))
n = 7
print(findLastDigit(f,n))
n = 67
print(findLastDigit(f,n))

###############################################################################################################








































































































































































































