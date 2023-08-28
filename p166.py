#874

'''
Python | Print an Inverted Star pattern
'''

n = 11

for i in range(n,0,-1):
    print((n-i) * ' ' + i * '*')

#################################################################################################################

#875

'''
Using Recursion
'''

def inverted_star_pattern_recursive(height):
    if height > 0:
        print("*" * height)
        inverted_star_pattern_recursive(height - 1)

height = 5
inverted_star_pattern_recursive(height)

#################################################################################################################















