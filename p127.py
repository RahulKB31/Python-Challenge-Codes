#770

'''
Find the size of a Tuple in Python
'''

# Using getsizeof() function

import sys

Tuple1 = ('A',1,'B',2,'C',3)
Tuple2 = ('Geek1','Raju','Geeks','Nikhil','Geek3','Deepanshu')
Tuple3 = ((1,'Lion'),(2,'Tiger'),(3,'Fox'),(4,'Wolf'))

print('Size of Tuple1: ' + str(sys.getsizeof(Tuple1)) + 'bytes')
print('Size of Tuple2: ' + str(sys.getsizeof(Tuple2)) + 'bytes')
print('Size of Tuple3: ' + str(sys.getsizeof(Tuple3)) + 'bytes')

##################################################################################################################

#771

#Using inbuilt __sizeof__() method

Tuple1 = ('A',1,'B',2,'C',3)
Tuple2 = ('Geek1','Raju','Geeks','Nikhil','Geek3','Deepanshu')
Tuple3 = ((1,'Lion'),(2,'Tiger'),(3,'Fox'),(4,'Wolf'))

print('Size of Tuple1: ' + str(Tuple1.__sizeof__()) + 'bytes')
print('Size of Tuple2: ' + str(Tuple2.__sizeof__()) + 'bytes')
print('Size of Tuple3: ' + str(Tuple3.__sizeof__()) + 'bytes')

##################################################################################################################
















































































































