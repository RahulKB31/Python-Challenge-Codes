# Also try some variations, such as a version of the circle exercise where the user is asked
# to supply the radius,
# and a version of the currency-conversion exercise where the user is asked to supply the exchange rate and
# the cost in dollars of three items in turn, outputting the equivalent cost in pounds and then calculating the
# total and displaying it in both pounds and dollars.
# To input an integer you need to use something like
# radius = int(input("Please enter the radius"))
# and to input a real number you should use something like
# exchangeRate = float(input("Please enter the exchange rate"))
# Run the programs with various different inputs, including some invalid ones, to observe what happens.
#1

import math
radius = float(input("Enter the radius "))
area = math.pi * radius * radius
circum = 2 * math.pi * radius

print("Area is", area, " Circumference is ",circum)

############################################################################################################

#2

rate = float(input("Please input the exchange rate (pounds per dollar) "))
firstCost = float(input("cost of first item in dollars "))
secondCost = float(input("Cost of second item in dollars "))
thirdCost = float(input("Cost of thrid item in dollars "))
print("Costs in pounds")
print(firstCost * rate)
print(secondCost * rate)
print(thirdCost * rate)
totalCost = firstCost + secondCost + thirdCost
print("Total in dollars", totalCost)
print("Total in pounds", totalCost * rate)