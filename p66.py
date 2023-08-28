<<<<<<< HEAD
#493

'''
Python | Matrix creation of n*n
'''

# using list comprehension

N= 4

print("The dimension: " + str(N))

res = [list(range(1+N*i, 1+N * (i + 1))) for i in range(N)]

print("The created matrix of N*N: " + str(res))

#############################################################################################################

#494

'''
Using next() + itertool.count() 
'''

import itertools

N = 4

print("The dimension: " + str(N))

temp = itertools.count(1)
res = [[next(temp) for i in range(N)] for i in range(N)]

print("The created matrix of N*N:" + str(res))

###########################################################################################################

#495

'''
Using a list comprehension and the enumerate()
'''

n = 4

matrix = [[i*n+j for j in range(1, n+1)] for i, _ in enumerate(range(n))]

print("The created matrix of N*N: "+ str(matrix))

###########################################################################################################

#496

'''
Using for loop, while loop and slicing
'''

N = 4

print("The dimension: " + str(N))

x = N*N
y = []

for i in range(1,x+1):
    y.append(i)
res = []
i = 0
while (i<len(y)):
    a= y[i:i+N]
    res.append(a)
    i += N

print("The created matrix of N*N :" + str(res))

##############################################################################################################

#497

'''
Using nested for loop
'''

N = 4

print("The dimension: "+ str(N))

res = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(1+N * i+j)
    res.append(row)

print("The created matrix of N*N: " + str(res))

##############################################################################################################
















































































=======
#493

'''
Python | Matrix creation of n*n
'''

# using list comprehension

N= 4

print("The dimension: " + str(N))

res = [list(range(1+N*i, 1+N * (i + 1))) for i in range(N)]

print("The created matrix of N*N: " + str(res))

#############################################################################################################

#494

'''
Using next() + itertool.count() 
'''

import itertools

N = 4

print("The dimension: " + str(N))

temp = itertools.count(1)
res = [[next(temp) for i in range(N)] for i in range(N)]

print("The created matrix of N*N:" + str(res))

###########################################################################################################

#495

'''
Using a list comprehension and the enumerate()
'''

n = 4

matrix = [[i*n+j for j in range(1, n+1)] for i, _ in enumerate(range(n))]

print("The created matrix of N*N: "+ str(matrix))

###########################################################################################################

#496

'''
Using for loop, while loop and slicing
'''

N = 4

print("The dimension: " + str(N))

x = N*N
y = []

for i in range(1,x+1):
    y.append(i)
res = []
i = 0
while (i<len(y)):
    a= y[i:i+N]
    res.append(a)
    i += N

print("The created matrix of N*N :" + str(res))

##############################################################################################################

#497

'''
Using nested for loop
'''

N = 4

print("The dimension: "+ str(N))

res = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(1+N * i+j)
    res.append(row)

print("The created matrix of N*N: " + str(res))

##############################################################################################################
















































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
