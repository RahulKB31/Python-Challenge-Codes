<<<<<<< HEAD
#731

'''
Python dictionary with keys having multiple inputs
'''

import random as rn

dict = {}

x,y,z = 10,20,30
dict[x,y,z] = x+y-z

x,y,z = 5,2,4
dict[x,y,z] = x+y-z

print(dict)

##############################################################################################################

#732

'''
Python dictionary with keys having multiple inputs to get access to the keys
'''

places = {("19.07'53.2", "72.54'51.0"): "Mumbai", ("19.07'53.2", "72.54'51.0"): "Delhi" }

print(places)
print("\n")

lat = []
long = []
plc = []
for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0],i[1]])

print(lat)
print(long)
print(plc)

###############################################################################################################

#733

'''
Python dictionary with keys having multiple inputs
'''





































































































































=======
#731

'''
Python dictionary with keys having multiple inputs
'''

import random as rn

dict = {}

x,y,z = 10,20,30
dict[x,y,z] = x+y-z

x,y,z = 5,2,4
dict[x,y,z] = x+y-z

print(dict)

##############################################################################################################

#732

'''
Python dictionary with keys having multiple inputs to get access to the keys
'''

places = {("19.07'53.2", "72.54'51.0"): "Mumbai", ("19.07'53.2", "72.54'51.0"): "Delhi" }

print(places)
print("\n")

lat = []
long = []
plc = []
for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0],i[1]])

print(lat)
print(long)
print(plc)

###############################################################################################################

#733

'''
Python dictionary with keys having multiple inputs
'''





































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
