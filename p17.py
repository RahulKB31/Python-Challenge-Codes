#81

'''
Python program to find the area of a circle
'''

def findArea(r):
    PI = 3.142
    return PI * (r*r)

#Driver method
print("Area is %.6f" % findArea(5))

##################################################################################################

#82

'''
Python program to Find Area of a circle with math library
'''

import math
def area(r):
    area = math.pi * pow(r,2)
    return print("Area of circle is:", area)
area(4)

##################################################################################################

#83

'''
Python code to find the volume of a tetrahedron
'''

import math
def vol_tetra(side):
    volume = (side ** 3 / (6 * math.sqrt(2)))
    return round(volume, 2)

# Driver code
side = 3
vol = vol_tetra(side)
print(vol)

##################################################################################################

#84

import math

def calculate_tetrahedron_area(side):
    area = math.sqrt(3) * side ** 2 / 4
    return round(area, 2)

#Example usage
side = 3
area = calculate_tetrahedron_area(side)
print("The area of a tetrahedron with side", side, "is", area)

####################################################################################################

#85

'''
Python program to find volumne, surface area and space diagonal of a cuboid
'''

import math

# function to calculate surface area

def find_surface_area(l, b, h):

    #formula of surface area = 2 (lb + bh + hl)
    Surface_area = 2 * (l * b + b * h + h * l)

    #Display surface area
    print(Surface_area)

# Function to find the volumne of rectangular prism

def find_volumne(l, b, h):
    # formula to calculate volumne (l*b*h)
    volumne = (l * b * h)

    #display of volumne
    print(volumne)

def find_space_diagonal(l, b, h):

    #formula to calculate space diagonal  = square_root(l**2 + b**2 + h**2)
    Space_diagonal = math.sqrt(l**2 + b**2 + h**2)

    # display space diagonal
    print(Space_diagonal)

# Driver code
l = 9
b = 6
h = 10

# surface area function call
find_surface_area(l, b , h)

# volumne function call
find_volumne(l, b , h)

# space diagonal function call
find_space_diagonal(l, b , h)

#######################################################################################################


































































































