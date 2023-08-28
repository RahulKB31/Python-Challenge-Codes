<<<<<<< HEAD
#472

'''
Python program to add two matrices
'''

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for r in result:
    print(r)

###########################################################################################################

#473

'''
Add two matrices using list comprehension
'''

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]

for r in result:
    print(r)

#######################################################################################################

#474

'''
Add two matrices using zip() function
'''

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = [map(sum, zip(*t)) for t in zip(x,y)]
print(result)

###############################################################################################################

#475

'''
Add two matrices using Numpy
'''

import numpy as np

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = np.array(x) + np.array(y)
print(result)

################################################################################################################

#476

'''
Add two matrices using SymPy
'''

from sympy import Matrix

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

matrix_x = Matrix(x)
matrix_y = Matrix(y)

result = matrix_x + matrix_y

print(result)

################################################################################################################












































































































































=======
#472

'''
Python program to add two matrices
'''

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for r in result:
    print(r)

###########################################################################################################

#473

'''
Add two matrices using list comprehension
'''

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]

for r in result:
    print(r)

#######################################################################################################

#474

'''
Add two matrices using zip() function
'''

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = [map(sum, zip(*t)) for t in zip(x,y)]
print(result)

###############################################################################################################

#475

'''
Add two matrices using Numpy
'''

import numpy as np

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = np.array(x) + np.array(y)
print(result)

################################################################################################################

#476

'''
Add two matrices using SymPy
'''

from sympy import Matrix

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

matrix_x = Matrix(x)
matrix_y = Matrix(y)

result = matrix_x + matrix_y

print(result)

################################################################################################################












































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
