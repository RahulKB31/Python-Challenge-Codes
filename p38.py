<<<<<<< HEAD
#226

'''
Python | Multiply all numbers in the list
'''

# Multiply all numbers in the list using Traversal

def multiplyList(myList):

    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

#Driver code
list1 = [1,2,3]
list2 = [3,2,4]
print(multiplyList(list1))
print(multiplyList(list2))

######################################################################################################

#227

# Multiply all numbers in the list using numpy.prod()

import numpy
list1 = [1,2,3]
list2 = [3,2,4]

#using numpy.prod() to get the multiplication
result1 = numpy.prod(list1)
result2 = numpy.prod(list2)
print(result1)
print(result2)

########################################################################################################

#228

'''
Multiply all numbers in the list using lambda function
'''

from functools import reduce
list1 = [1,2,3]
list2 = [3,2,4]

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)

###########################################################################################################

#229

'''
Multiply all numbers in the list using prod function of math library
'''

import math

list1 = [1,2,3]
list2 = [3,2,4]

result1 = math.prod(list1)
result2 = math.prod(list2)
print(result1)
print(result2)

#########################################################################################################

#230

'''
Multiply all numbers in the list using mul() function of operator module
'''

from operator import *
list1 = [1,2,3]
m = 1
for i in list1:
    # multiply all elements in the given list
    # using mul function of operator module
    m = mul(i, m)
# printing the result
print(m)

############################################################################################################

#231

'''
Multiply all numbers in the list using traversal by index
'''

def multiplyList(myList):

    #Multiply elements one by one
    result = 1
    for i in range(0, len(myList)):
        result = result * myList[i]
    return result

# Driver code
list1 = [1,2,3]
list2 = [3,2,4]
print(multiplyList(list1))
print(multiplyList(list2))

############################################################################################################

#232

'''
Multiply all numbers in the list using itertools.accumulate
'''

from itertools import accumulate

list1 = [1,2,3]
list2 = [3,2,4]

result1 = list(accumulate(list1, (lambda x, y: x * y)))
result2 = list(accumulate(list2, (lambda x, y: x * y)))
print(result1[-1])
print(result2[-1])

###########################################################################################################

#233

'''
Multiply all numbers in the list using the recursive function
'''

def product_recursive(numbers):
    # base case: list is empty
    if not numbers:
        return 1
    # recursive case: Multiply first element by product of the rest of the list
    return numbers[0] * product_recursive(numbers[1:])
list1 = [1,2,3]
product = product_recursive(list1)
print(product)

list2 = [3,2,4]
product = product_recursive(list2)
print(product)

############################################################################################################

#234

'''
Multiply all numbers in the list using reduce() and the mul() functions
'''

from functools import reduce
from operator import mul

list1 = [1,2,3]
result = reduce(mul, list1)

print(result)

##########################################################################################################























































































































































































=======
#226

'''
Python | Multiply all numbers in the list
'''

# Multiply all numbers in the list using Traversal

def multiplyList(myList):

    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

#Driver code
list1 = [1,2,3]
list2 = [3,2,4]
print(multiplyList(list1))
print(multiplyList(list2))

######################################################################################################

#227

# Multiply all numbers in the list using numpy.prod()

import numpy
list1 = [1,2,3]
list2 = [3,2,4]

#using numpy.prod() to get the multiplication
result1 = numpy.prod(list1)
result2 = numpy.prod(list2)
print(result1)
print(result2)

########################################################################################################

#228

'''
Multiply all numbers in the list using lambda function
'''

from functools import reduce
list1 = [1,2,3]
list2 = [3,2,4]

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)

###########################################################################################################

#229

'''
Multiply all numbers in the list using prod function of math library
'''

import math

list1 = [1,2,3]
list2 = [3,2,4]

result1 = math.prod(list1)
result2 = math.prod(list2)
print(result1)
print(result2)

#########################################################################################################

#230

'''
Multiply all numbers in the list using mul() function of operator module
'''

from operator import *
list1 = [1,2,3]
m = 1
for i in list1:
    # multiply all elements in the given list
    # using mul function of operator module
    m = mul(i, m)
# printing the result
print(m)

############################################################################################################

#231

'''
Multiply all numbers in the list using traversal by index
'''

def multiplyList(myList):

    #Multiply elements one by one
    result = 1
    for i in range(0, len(myList)):
        result = result * myList[i]
    return result

# Driver code
list1 = [1,2,3]
list2 = [3,2,4]
print(multiplyList(list1))
print(multiplyList(list2))

############################################################################################################

#232

'''
Multiply all numbers in the list using itertools.accumulate
'''

from itertools import accumulate

list1 = [1,2,3]
list2 = [3,2,4]

result1 = list(accumulate(list1, (lambda x, y: x * y)))
result2 = list(accumulate(list2, (lambda x, y: x * y)))
print(result1[-1])
print(result2[-1])

###########################################################################################################

#233

'''
Multiply all numbers in the list using the recursive function
'''

def product_recursive(numbers):
    # base case: list is empty
    if not numbers:
        return 1
    # recursive case: Multiply first element by product of the rest of the list
    return numbers[0] * product_recursive(numbers[1:])
list1 = [1,2,3]
product = product_recursive(list1)
print(product)

list2 = [3,2,4]
product = product_recursive(list2)
print(product)

############################################################################################################

#234

'''
Multiply all numbers in the list using reduce() and the mul() functions
'''

from functools import reduce
from operator import mul

list1 = [1,2,3]
result = reduce(mul, list1)

print(result)

##########################################################################################################























































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
