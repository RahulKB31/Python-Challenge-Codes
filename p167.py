<<<<<<< HEAD
#876

'''
Program to print double sided stair case pattern
'''

def pattern(n):
    for i in range(1,n+1):
        k = i+1 if (i%2 != 0) else i

        for g in range(k,n):
            if g>=k:
                print(end=" ")

        for j in range(0,k):
            if j == k - 1:
                print(" * ")
            else:
                print(" * ", end = " ")

n = 10
pattern(n)

################################################################################################################

#877

def print_double_sided_staircase(height):
    for i in range(1,height+1):
        for j in range(i):
            print("*",end="")

        #adding spacing between the two sides
        print(" " * (2 * height -2 * i), end = "")

        #print right side steps
        for j in range(i):
            print("*",end = "")

        print()

height = int(input("Enter the of double sided stairs:"))
print_double_sided_staircase(height)

###################################################################################################################




















=======
#876

'''
Program to print double sided stair case pattern
'''

def pattern(n):
    for i in range(1,n+1):
        k = i+1 if (i%2 != 0) else i

        for g in range(k,n):
            if g>=k:
                print(end=" ")

        for j in range(0,k):
            if j == k - 1:
                print(" * ")
            else:
                print(" * ", end = " ")

n = 10
pattern(n)

################################################################################################################

#877

def print_double_sided_staircase(height):
    for i in range(1,height+1):
        for j in range(i):
            print("*",end="")

        #adding spacing between the two sides
        print(" " * (2 * height -2 * i), end = "")

        #print right side steps
        for j in range(i):
            print("*",end = "")

        print()

height = int(input("Enter the of double sided stairs:"))
print_double_sided_staircase(height)

###################################################################################################################




















>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
