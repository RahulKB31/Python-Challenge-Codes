def fib(n):
    # Base case
    if n <= 0:
        return "Invalid input"  # Fibonacci numbers are for positive integers
    elif n == 1 or n == 2:
        return 1

    # Initialize the first two Fibonacci numbers
    a, b = 1, 1

    # Calculate Fibonacci numbers iteratively
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b
print(fib(1))  # Output: 1
print(fib(2))  # Output: 1
print(fib(3))  # Output: 2
print(fib(4))  # Output: 3
print(fib(5))  # Output: 5
print(fib(6))  # Output: 8
print(fib(7))  # Output: 13
