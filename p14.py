#69

'''
Python program for simple Interest
'''

def simple_interest(p, t, r):
    print("The principle is", p)
    print("The time period is", t)
    print("The rate of interest is", r)

    si = (p * t * r)/100

    print("The simple Interest is", si)
    return si

# Driver code
simple_interest(8, 6, 8)

#################################################################################################

#70

'''
program for simple interest with taking input from the user
'''

def simple_interest(p, t, r):
    print("The principle is", p)
    print("The time period is", t)
    print("The rate of interest is", r)

    si = (p * t * r)/100

    print("The simple interest is", si)

# Driver code
P = int(input("Enter the principle amount: "))
T = int(input("Enter the time period: "))
R = int(input("Enter the rate of interest: "))
simple_interest(P, T, R)

############################################################################################