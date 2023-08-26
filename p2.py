#3
# Write a script that asks the user to input a positive integer, n, and calculates and outputs the sum of the
# squares of all numbers from 1 to n. (For example if the input was 5 the answer would be 1^2 + 2^2 + 3^2 + 4^2 +
# 5^2.)
# The script should output a message if the input value is less than 1. You will need to keep track of the total
# so far when building the result, so you should initialise a variable (to hold this running total) to 0 before
# using a for loop to perform the calculation. The output of the result should be performed after the loop

n = int(input("Enter a positive integer value for n: "))
if n<1:
    print("Input was less than 1; no squares to sum")
else:
    sum = 0
    for i in range(1, n+1): #end value not included in range
                            # so need n+1 to ensure n is included
        sum += i*i
    print("The sum of the squares of numbers from 1 to", n, "is", sum)

#####################################################################################################

#4

# Write a script that asks the user to input a series of numbers, one at a time. An input of 0 should be used to
# indicate that the series is complete.
# The script should calculate and display (i) the sum of all of the numbers that were input, (ii) the smallest
# input and (iii) the largest input.
# Since the number of inputs is not known you should use a while loop. Three variables will be needed to keep
# track of the sum so far, the smallest number so far and the largest number so far. The first number should be
# input before entering the loop, and used to initialise all 3 variables. Inside the loop you will need to check if
# the new input is 0, and if it is not, add it to the sum and check whether it is smallest than the smallest so far
# or larger than the largest so far (using if and elif)
# Once again the results should be output after leaving the loop.

print("Enter a series of numbers, one at a time")
print("use 0 to finish")
first = float(input("First number: "))
sum = first
smallest = first
largest = first
next = float(input("Next number: "))
while next!=0:
    sum += next
    if next < smallest:
        smallest = next
    elif next > largest:
        largest = next
    next = float(input("Next number: "))

print("The sum of the inputs is", sum)
print("The smallest value is", smallest, "and the largest is", largest)

#########################Different method#################################################################

#5

print("Enter a series of numbers, one at a time")
print("use 0 to finish")
first = float(input("First number: "))
sum = first
smallest = first
largest = first
looping = True
while looping:
    next = float(input("Next number: "))
    if next==0:
        looping = False
    else:
        sum += next
        if next < smallest:
            smallest = next
        elif next > largest:
            largest = next

print("The sum of the inputs is", sum)
print("The smallest value is", smallest, "and the largest value is", largest)

########################################Different method#########################################

#6

n = int(input("Enter first number: "))
smallest = n
largest = n
total = n

while n!= 0:
    n = int(input("Enter next number (use 0 to finish)"))
    if n!=0:
        #update value of total
        total += n
    #update smallest or largest if necessary
    if n < smallest:
        smallest = n
    elif n > largest:
        largest = n

#Output results
print("Smallest:", smallest)
print("Largest:", largest)
print("Total:", total)