#459

'''
Break a list into chunks of size N in Python
'''

#using yield

my_list = ['geeks', 'for','geeks', 'like','geeky','nerdy','geek','love','questions','words','life']

def divide_chunks(l,n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = 5
x = list(divide_chunks(my_list,n))
print(x)

#####################################################################################################

#460

'''
Using a loop
'''

my_list = [1,2,3,4,5,6,7,8,9]

start = 0
end = len(my_list)
step = 3
for i in range(start, end, step):
    x = i
    print(my_list[x:x+step])

#########################################################################################################

#461

'''
Using list comprehension
'''

my_list = [1,2,3,4,5,6,7,8,9]

n = 4

final = [my_list[i * n:(i+1) * n] for i in range((len(my_list) + n -1) // n)]

####################################################################################################

#462

l = [1,2,3,4,5,6,7,8,9]

n = 4

x = [l[i:i + n] for i in range(0, len(l), n)]
print(x)

###########################################################################################################

#463

'''
Using numpy
'''

import numpy as np

arr = range(30)
np.array_split(arr, 6)

##########################################################################################################

#464

'''
User itertool
'''

from itertools import islice

def chunk(arr_range, arr_size):
    arr_range = iter(arr_range)
    return iter(lambda: tuple(islice(arr_range,arr_size)), ())

list(chunk(range(30), 5))

##########################################################################################################

#465

'''
Collections
'''

from collections import deque

def split_list(input_list, chunk_size):
    deque_obj = deque(input_list)

    while deque_obj:
        chunk = []

        for _ in range(chunk_size):
            if deque_obj:
                chunk.append(deque_obj.popleft())

        yield chunk

input_list = [1,2,3,4,5,6,7,8,9]
chunk_size = 3
chunks = list(split_list(input_list, chunk_size))
print(chunks)

#######################################################################################################

#466

'''
Partial assignment
'''

my_list = list(range(10))
chunk_size = 3
while my_list:
    chunk, my_list = my_list[:chunk_size],my_list[chunk_size:]
    print(chunk)

############################################################################################################
























































































































































































