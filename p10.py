#44

'''
Write a class called Point to represent a point in 2D space with x and y
coordinates as the attributes. Provide an __init__ method which takes
the coordinate values as arguments and a __str__ method that returns
a string of the form (30, 40).
Also provide methods to move the point horizontally by an amount
specified as an argument (i.e. changing the x coordinate) and to move
the point vertically.
Write a function that takes two points as arguments and calculates and
returns the distance between them (using Pythagoras theorem as in the
Heron’s formula example from lecture 3).
Write code to ask the user to supply two pairs of coordinates, create
Point objects from the supplied values and use these objects as
arguments in a call to the function.
'''

class Point:
    '''
    represents a point in 2D space
    attributes: x, y: int: x and y coordinates
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def moveHor(self, dist):
        self.x += dist

    def moveVert(self, dist):
        self.y += dist

import math

def distance(p1, p2):
    '''
    returns euclidean distance between 2 points
    arguments: p1, p2:point
    return value: float
    '''
    xdiff = p1.x - p2.x
    ydiff = p1.y - p2.y
    # use Pythagoras
    return math.sqrt(xdiff * xdiff + ydiff * ydiff)

print("Please supply coordinates of first point")
x1 = int(input('x: '))
x2 = int(input('y: '))
p1 = Point(x1, y1)

print("Please supply coordinates of second point")
x2 = int(input('x: '))
y2 = int(input('y: '))
p2 = Point(x2, y2)

print("distance between", p1, "and", p2, "is", round(distance(p1,p2),1))

#tests for move methods (not asked for in exercise)

print("move first point horizontally by 10")
print("old value", p1)
p1.moveHor(10)
print('new value', p1)

print('move second point vertically by 20')
print("Old value", p2)
p2.moveVert(20)
print('new value', p2)

############################################################################################

#45

'''
Write a class called Triangle which contains as its attributes three
Point objects, representing the vertices of a triangle. The __init__
method should take 3 Point objects as its arguments. Add to the class
methods to return the perimeter and the area of the triangle.
The perimeter can be calculated by using the function from the previous
exercise to calculate the lengths of each of the edges; the area can be
calculated using Heron’s formula (see lecture 3).
Write code to obtain three pairs of coordinates (representing the three
vertices of a triangle) from the user, use these to create 3 Point objects
to be supplied to a Triangle object, and print the results returned by
the area and perimeter methods.
'''

class Point:
    """
    represents a point in 2D space
    attributes: x,y: int: a and y coordinates
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

import math
def distance(p1, p2):
    '''
    returns euclidean distance between 2 points
    arguments: p1, p2: Point
    return value: float
    '''
    xdiff = p1.x - p2.x
    ydiff = p1.y - p2.y
    #use pythogoras
    return math.sqrt(xdiff * xdiff + ydiff * ydiff)

class Triangle:
    '''
    represents a triangle in 2D space
    attributes: a, b , c: Point: vertices of the triangle
    '''

    def __init__(self, p1, p2, p3):
        self.a = p1
        self.b = p2
        self.c = p3

    def perimeter(self):
        return distance(self.a, self.b) + distance(self.b,self.c) +\
               distance(self.c, self.a)

    def area(self):
        s1 = distance(self.a, self.b)
        s2 = distance(self.b, self.c)
        s3 = distance(self.c, self.a)
        s = 1/2 * (s1 + s2 + s3)
        return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

def getPoint():
    x = int(input('x: '))
    y = int(input('y: '))
    return Point(x,y)

print("Please supply coordinates of first vertex")
p1 = getPoint()

print("Please supply coordinates of second vertex")
p2 = getPoint()

print("Please supply coordinates of third vertex")
p3 = getPoint()

triangle = Triangle(p1, p2, p3)

print("Perimeter:", round(triangle.perimeter(), 1))
print("Area:", round(triangle.area(), 1))

###################################################################################################
































