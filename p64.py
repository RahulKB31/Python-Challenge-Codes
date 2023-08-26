#486

'''
Adding and subtracting matrices in python
'''

import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[1,2],[3,4]])

print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)

print("Addition of two matrix")
print(np.add(A,B))

#############################################################################################################

#487

import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[1,2],[3,4]])

print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)

print("Subtraction of two matrix")
print(np.subtract(A,B))

####################################################################################################################

#488

'''
Using nested loops
'''

matrix1 = [[1,2],[3,4]]
matrix2 = [[1,2],[3,4]]

print("Printing elements of first matrix")
for row in matrix1:
    for element in row:
        print(element, end=" ")
    print()

print("Printing elements of second matrix")
for row in matrix2:
    for element in row:
        print(element, end = " ")
    print()

result = [[0,0],[0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]

print("Subtraction of two matrix")
for row in result:
    for element in row:
        print(element, end=" ")
    print()

##############################################################################################################












































































