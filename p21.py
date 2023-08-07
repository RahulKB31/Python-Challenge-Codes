#113

'''
Python program to for nth multiple of a number in Fibonacci Series
'''

# Iterative approach using a list to store Fibonacci series

def nth_fib_multiple(n, k):
    fibonacci = [0, 1]
    counter = 0
    for i in range(2, 10000):
        current = fibonacci[i-1] + fibonacci[i-2]
        if current % k == 0:
            counter += 1
            if counter == n:
                return i
        fibonacci.append(current)

print(nth_fib_multiple(3, 2))

#########################################################################################################

#114

'''
Recursive Fibonacci series with memoization
'''

def fib(n, memo):
    if n == 1 or n == 2:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Function to find the nth multiple of k in the Fibonacci Series

def fib_multiple(k, n):
    memo = [0] * 100
    count = 0
    for i in range(1, 100):
        if fib(i, memo) % k == 0:
            count += 1
            if count == n:
                return i
    return -1

k = 2
n = 3
result = fib_multiple(k, n)
print(f"The {n}th multiple of {k} in the Fibonacci series is at position {result}")

#########################################################################################################


















