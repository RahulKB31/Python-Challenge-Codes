<<<<<<< HEAD
#71

'''
Python program for Compund Interest
'''

def compund_interest(principal, rate, time):

    #calculate compund interest
    Amount = principal * (pow((1 + rate/100), time))
    CI = Amount - principal
    print("Compound interest is", CI)

# Driver Code
compund_interest(10000, 10.25, 5)

####################################################################################################

#72

'''
Compund interest with input from user
'''

def compound_interest(principal, rate, time):

    # calculates compound interest
    Amount = principal * (pow((1 + rate/100), time))
    CI = Amount - principal
    print("Compound Interest is", CI)

# Driver code
# Taking input from user
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))

#Function call
compound_interest(principal, rate, time)

#####################################################################################################

#73

'''
Finding compound interest of given values without using pow() function.
'''

p = 1200
t = 2
r = 5.4

# calculates the compund interest
a = p*(1 + (r/100)) ** t
ci = a - p
print(ci)

#######################################################################################################

#74

'''
Compund interest using for loop
'''

def compound_interest(principal, rate, time):
    Amount = principal
    for i in range(time):
        Amount = Amount * (1 + rate/100)
    CI = Amount - principal
    print("Compund interest is", CI)

#Driver code
compund_interest(1200, 5.4, 2)

######################################################################################################

#75

'''
Program to find the rate percentage from compound interest of consecutive years
'''

def Rate(N1, N2):
    rate = (N2 - N1) * 100 // (N1)
    return rate

# Driver code
if __name__ == "__main__":
    N1 = 100
    N2 = 120

    print(Rate(N1, N2)," %")

######################################################################################################





































=======
#71

'''
Python program for Compund Interest
'''

def compund_interest(principal, rate, time):

    #calculate compund interest
    Amount = principal * (pow((1 + rate/100), time))
    CI = Amount - principal
    print("Compound interest is", CI)

# Driver Code
compund_interest(10000, 10.25, 5)

####################################################################################################

#72

'''
Compund interest with input from user
'''

def compound_interest(principal, rate, time):

    # calculates compound interest
    Amount = principal * (pow((1 + rate/100), time))
    CI = Amount - principal
    print("Compound Interest is", CI)

# Driver code
# Taking input from user
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))

#Function call
compound_interest(principal, rate, time)

#####################################################################################################

#73

'''
Finding compound interest of given values without using pow() function.
'''

p = 1200
t = 2
r = 5.4

# calculates the compund interest
a = p*(1 + (r/100)) ** t
ci = a - p
print(ci)

#######################################################################################################

#74

'''
Compund interest using for loop
'''

def compound_interest(principal, rate, time):
    Amount = principal
    for i in range(time):
        Amount = Amount * (1 + rate/100)
    CI = Amount - principal
    print("Compund interest is", CI)

#Driver code
compund_interest(1200, 5.4, 2)

######################################################################################################

#75

'''
Program to find the rate percentage from compound interest of consecutive years
'''

def Rate(N1, N2):
    rate = (N2 - N1) * 100 // (N1)
    return rate

# Driver code
if __name__ == "__main__":
    N1 = 100
    N2 = 120

    print(Rate(N1, N2)," %")

######################################################################################################





































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
