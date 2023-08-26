# Write a function that outputs all divisors of an integer supplied as an argument (i.e. all numbers n such
# that
# that when the argument is divided by n there is no remainder.
# Write a second function that takes as arguments two integers to use as the start and end values of a range and
# for each number in the range prints a message of the from “The divisors of 33 are:”, then calls the first
# function to output the divisors.
# Finally write code to ask the user to supply two numbers and use these as arguments to a call to the second
# function.

#7

def divisors(n):
    '''
    Outputs all the divisors of n
    argument n: int
    '''
    for i in range(1, n+1):
        if n % i ==0:
            print(i)

def rangeDivisors(x, y):
    '''
    outputs divisors of each number in a range
    arguments: x: int: start of range
               y: int: end of range
    I've assumed the range is inclusive
    '''
    for n in range(x, y+1):
        print("The divisors of", n, "are:")
        divisors(n)

#get inputs from user
start = int(input("Please enter start of range: "))
end = int(input("Please enter end of range: "))
rangeDivisors(start,end)

#########################Different Method####################################################

#8

#this solution includes validation that wasn't asked for in the question

def getDivisors(n):
    '''
    prints all the divisors of n
    '''
    if n<0:
        print("Sorry this function doesn't work for negative numbers")
    else:
        for i in range(1, n//2+1):
            if n % i == 0:
                print(i)

def getDivisorsForRange(a,b):
    '''
    prints all the divisors of all numbers in the range a..b
    (inclusive)
    uses descending order if a>b
    '''
    if a<b:
        for n in range(a, b+1):
            print("Divisors of", n, "are")
            getDivisors(n)
    else:
        for n in range(a, b-1, -1):
            print("Divisors of", n, "are")
            getDivisors(n)

start = int(input("Start of range: "))
end = int(input("End of range: "))
getDivisorsForRange(start, end)

#####################################################################################################

#9

# The Fibonacci sequence is 1, 1, 2, 3, 5, 8, 13, 21 …
# Write a function to print the first n numbers in the sequence where n is supplied as an argument.
# Write a second version of the function that also calculates and outputs the sum of the first n numbers.
# Write code to obtain input from the user to test your functions

def fib(n):
    '''
    prints the first n numbers in the fibonacci series
    arguments: n: int
    '''
    current = 1
    previous = 1
    if n > 0:
        print(1)
        if n>1:
            print(1)
    for i in range(2,n):
        new = current + previous
        previous = current
        current = new
        print(current)

def fibVersion2(n):
    '''
    prints the first n numbers in the fibonacci series
    also calculates the sum of the numbers that were output
    argument: n: int
    '''
    total = 0
    current = 1
    previous = 1
    if n >0:
        print(1)
        if n >1:
            print(1)
            total = 2
    for i in range (2,n):
        new = current + previous
        previous = current
        current = new
        print(current)
        total += current
    print("The sum of the first", n, "numbers in the fibonacci series is", total)

# get input from user
n = int(input("How many numbers do you want to see? "))
version = input("Do you want to see the total? (y/n) ")
if version == "n":
    fib(n)
elif version == "y":
    fibVersion2(n)
else:
    print("Please type y or n next time")

##########################################################################################################

#10

# Write a function that repeatedly generates random numbers between 1 and n, where n is an integer supplied
# as an argument. The function should finish when the total of the numbers generated is greater than or equal
# to 1000 and should return a count of how many numbers were generated.
# Write code that loops 10 times, each time asking the user to supply a positive integer, calling the function
# with the supplied value and outputting the result.
# [To generate a random number from 1 to n you should use import random and then call
# random.randint(1, n). (The range is inclusive, so you do not need to use n+1).]

import random

def getRandoms(n):
    '''
    generates random numbers in the range 1 to n until the total of the numbers
    generated is greater than or equal to 1000
    argument: n: int
    return: how many numbers that were generated
    '''
    total = 0
    counter = 0
    while total < 1000:
        r = random.randint(1,n)
        total += r
        counter += 1
    return counter

for i in range(10):
    # get input from user
    n = int(input("Please specify end of range: "))
    result = getRandoms(n)
    print(result, "random numbers were generated")