#477

'''
Python program to multiply two matrices
'''

# Matrix multiplication using nested list

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = [[sum(a*b for a,b in zip(x_row, y_col))
           for y_col in zip(*y)]
          for y_row in x]

for r in result:
    print(r)

###########################################################################################################

#478

'''
MAtrix multiplcation
'''

import numpy as np

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

result = np.dot(x,y)

for r in result:
    print(r)

##############################################################################################################

#479

'''
Using recursive matrix multiplication
'''

def matrix_multiply_recursive(A,B):
    if len(A[0]) != len(B):
        raise ValueError("invalid matrix dimension")

    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

    def multiply(A,B,result,i,j,k):
        if i >= len(A):
            return
        if j >= len(B[0]):
            return multiply(A,B, result, i+1,0,0)
        if k >= len(B):
            return multiply(A,B,result,i,j+1,0)
        result[i][j] += A[i][k] * B[k][j]
        multiply(A,B,result,i,j,k+1)

    multiply(A,B,result,0,0,0)
    return result

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3,4],[5,6,7,8],[9,1,2,3]]

result = matrix_multiply_recursive(A,B)
for row in result:
    print(row)

#################################################################################################################




























































































































































































































