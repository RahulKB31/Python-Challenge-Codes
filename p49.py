#365

'''
Python program to print all positive numbers in a range
'''

start, end = -4, 19

#iterating each number in list
for num in range(start, end+1):

    #checking condition
    if num >= 0:
        print(num, end=" ")

#################################################################################################################

#366

'''
Taking range limit from user input
'''

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of the range: "))

#iterating each number in list
for num in range(start, end+1):

    #checking condition
    if num >= 0:
        print(num, end=" ")

##################################################################################################################

#367

'''
Using the lambda function
'''

a = -4
b = 5
li = []
for i in range(a,b+1):
    li.append(i)
#printing positive numbers using the lambda function
positive_num = list(filter(lambda x: (x >= 0), li))

##########################################################################################################

#368

'''
Using the list comprehension
'''

a = -4
b = 5
out = [i for i in range(a,b+1) if i>0]
print(*out)

###############################################################################################################

#369

'''
Using enumerate function
'''

a = -4
b = 5
l = []
for i in range(a, b+1):
    l.append(i)
print([a for j,a in enumerate(l) if a>=0])

###############################################################################################################

#370

'''
Using pass()
'''

a = -4
b = 5
for i in range(a, b+1):
    if i<0:
        pass
    else:
        print(i,end=" ")

###############################################################################################################

#371

'''
Using recursion
'''

def printPositives(start,end):
    if start == end:
        return
    if start > 0:
        print(start, end= " ")
    printPositives(start+1,end)
a, b = -5, 10
printPositives(a, b)

###############################################################################################################

#372

'''
Using filter() function
'''

a = -4
b = 5

positive_nums = list(filter(lambda x: x>= 0, range(a, b+1)))
print(positive_nums)

###################################################################################################################















































































































































































































