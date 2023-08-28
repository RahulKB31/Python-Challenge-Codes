<<<<<<< HEAD
#489

'''
Transpose a matrix in single line in python
'''

#using nested list comprehension

m = [[1,2],[3,5],[6,7]]
for row in m:
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

print("\n")
for row in rez:
    print(row)

##########################################################################################################

#490

'''
Using zip
'''

matrix = [(1,2,4),(1,4,5),(5,6,7),(8,9,0)]
for row in matrix:
    print(row)
print("\n")
t_matrix = zip(*matrix)
for row in t_matrix:
    print(row)

#######################################################################################################

#491

'''
Using numpy
'''

import numpy
matrix = [[1,2,3],[4,5,6]]
print(matrix)
print("\n")
print(numpy.transpose(matrix))

#############################################################################################################

#492

import numpy as np
marix = np.array([[1,2,3],[4,5,6]])
print(matrix)
print("\n")
print(matrix.T)

##################################################################################################################







































































=======
#489

'''
Transpose a matrix in single line in python
'''

#using nested list comprehension

m = [[1,2],[3,5],[6,7]]
for row in m:
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

print("\n")
for row in rez:
    print(row)

##########################################################################################################

#490

'''
Using zip
'''

matrix = [(1,2,4),(1,4,5),(5,6,7),(8,9,0)]
for row in matrix:
    print(row)
print("\n")
t_matrix = zip(*matrix)
for row in t_matrix:
    print(row)

#######################################################################################################

#491

'''
Using numpy
'''

import numpy
matrix = [[1,2,3],[4,5,6]]
print(matrix)
print("\n")
print(numpy.transpose(matrix))

#############################################################################################################

#492

import numpy as np
marix = np.array([[1,2,3],[4,5,6]])
print(matrix)
print("\n")
print(matrix.T)

##################################################################################################################







































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
