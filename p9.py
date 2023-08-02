#38

'''
Write a recursive function called sum which takes a positive integer n as an argument and calculates the sum
of all the integers from 1 to n.
The recursive definition will be:
 Base case: The sum of all the digits from 1 to 0 is 0.
 Recursive case: When n>0 the sum of all the digits from 1 to n is n plus the sum of all the digits from 1 to
n-1
[ There is of course a more efficient way of obtaining the result using a formula.]
Also provide code that obtains a value from the keyboard and supplies this as an argument to the sum function
then prints the result.
'''

def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)

print(sum(20))
#should do more testing

#################################################################################################\

#39

'''
The binomial coefficient of n and m is the number of different possible ways of selecting m items from a
collection of n items. We will use bc(n, m) as an abbreviation. It can be calculated using a formula that
involves factorials, but if you do not happen to know that formula an approach using recursion can be used.
Assume we wish to find the number of ways of selecting m lottery balls for a collection of n. Paint one of
the balls red. It can either be selected or not selected. The number of possible ways of selecting m balls
from the collection if the red ball is not selected is the number of possible ways of selecting m balls from the
remaining n-1 balls, i.e. bc(n-1, m). If the red ball is selected the number of ways of selecting m balls is the
number of ways of selecting another m-1 balls from the remaining n-1, i.e. bc(n-1, m-1). The total number
of possible ways is the number of ways that include the red ball plus the number of ways that do not include
the red ball so
 bc(n,m) = bc(n-1,m) + bc(n-1, m-1)
The are some special cases to use as the base for the recursion, If n is less than m the binomial coefficient is
0, if m is equal to n the BC is 1, if m is equal to 1 the BC is n.
Use this to write a recursive function to calculate the binomial coefficient of two positive integers m and n.
A wrapper function should be used to check for negative arguments and the n less than m cases to avoid
having to do this in every recursive call.
Make some calls to your function (avoid using large values of m since the function may be come rather
efficient); for example determine how many different combinations of balls are possible in the UK National
Lottery where 6 are chosen from 59.
'''

def bc(n, m):
    if m==n:
        return 1
    elif m == 1:
        return n
    else:
        return bc(n-1, m) + bc(n-1, m-1)

def binCoeff(n, m):
    if n<=0 or m<=0:
        print("Need positive numbers")
        return 0
    elif m>n:
        print("Need m <= n")
        return 0
    else:
        return bc(n, m)

print(binCoeff(6,4))
print(binCoeff(59,6))

############################################################################################################

#40

'''
Although recursion can be a powerful tool it can be very inefficient if used inappropriately.
The Fibonacci series is a sequence of numbers in which each number (other than the first two) is the sum of
the two previous numbers in the sequence.
The first two numbers (the 0th and the 1st ) are defined to be 0 and 1 respectively. The resulting series of
numbers is as follows:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 ......
We can use the following recursive function to calculate the nth number in the series
def fib(n) :
 """
 calculates nth number in fibonacci series
 argument: n: int
 returns: fib(n): int
 """
 if n==0 or n==1 : return n
 else : return fib(n-1)+fib(n-2)
Write a program that asks the user for a non-negative integer, checks that the input is valid, calls the fib
function with the input number and prints the result that is returned.
Supply as input some values less than 30 - you'll notice that the result appears almost instantaneously. Now
try an input value of 35. You'll notice that you have to wait a few seconds for the result. Now try 40 - this
time you'll probably need to wait for about a minute. (Don't try any larger values - it will probably take
about half an hour with an input value of 45.)
Enhance the program by adding a call to print at the beginning of the function as follows:
 print("entering fib with parameter", n)
Run the enhanced version.
How many function calls are made when evaluating fib(4)?
How many times is fib(1) evaluated?
'''

def fib(n):
    # enhancement line; looking at the output you may observe that the number
    # times fib(1) is called is exactly equal to the final value of fib(n)
    # so if you tried fib(35) it would have been called 9227365 times
    print("Entering fib with parameter", n)
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)

try:
    i = int(input("Enter a non-negative integer: "))
    if i<0:
        raise ValueError
    else:
        print("Value", i, "in the Fibonacci series is", fib(i))
except:
    print("Invalid input")

# the following non-recursive function will be much more efficient when n is large

def fib2(n):
    if n==0 or n==1:
        return n
    else:
        current = 1
        previous = 0
        for i in range(2, n+1):
            new = current + previous
            previous = current
            current = new
        return current

try:
    print("Non recursive version")
    i = int(input("Enter a non-negative integer: "))
    if i<0:
        raise ValueError
    else:
        print("value", i, "in the Fibonacci series is", fib2(i))
except:
    print("Invalid input")

####################################################################################################
















