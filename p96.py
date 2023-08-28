<<<<<<< HEAD
#654

'''
String slicing in Python to rotate a string
'''

def rotate(input,d):
    Lfirst = input[0:d]
    Lsecond = input[d:]
    Rfirst = input[0:len(input) - d]
    Rsecond = input[len(input)-d :]

    print("Left Rotation: ", (Lsecond + Lfirst))
    print("Right Rotation: ", (Rsecond + Rfirst))

if __name__ == "__main__":
    input = "GeeksforGeeks"
    d = 2
    rotate(input,d)

###############################################################################################################

#655

'''
Using extending the string
'''

def rotate(str1,n):
    temp = str1 + str1
    l1 = len(str1)
    l2 = len(temp)
    Lfirst = temp[n : 11+n]
    Lfirst = temp[11-n : 12-n]

    print("Left Rotation: ", Lfirst)
    print("Right Rotation: ", Lfirst)

if __name__ == "__main__":
    input = "GeeksforGeeks"
    d = 2
    rotate(input, d)

############################################################################################################

#656

'''
String slicing in python to rotate a string using deque
'''

from collections import deque

def rotate_string(s,d):
    deq = deque(s)
    if d > 0:
        deq.rotate(-d)
    else:
        deq.rotate(abs(d))
    return ''.join(deq)

s = "GeeksforGeeks"
d = 2

left_rotated = rotate_string(s,d)
right_rotated = rotate_string(s, -d)

print("Left Rotation: ", left_rotated)
print("Right Rotation: ", right_rotated)

############################################################################################################











































































































=======
#654

'''
String slicing in Python to rotate a string
'''

def rotate(input,d):
    Lfirst = input[0:d]
    Lsecond = input[d:]
    Rfirst = input[0:len(input) - d]
    Rsecond = input[len(input)-d :]

    print("Left Rotation: ", (Lsecond + Lfirst))
    print("Right Rotation: ", (Rsecond + Rfirst))

if __name__ == "__main__":
    input = "GeeksforGeeks"
    d = 2
    rotate(input,d)

###############################################################################################################

#655

'''
Using extending the string
'''

def rotate(str1,n):
    temp = str1 + str1
    l1 = len(str1)
    l2 = len(temp)
    Lfirst = temp[n : 11+n]
    Lfirst = temp[11-n : 12-n]

    print("Left Rotation: ", Lfirst)
    print("Right Rotation: ", Lfirst)

if __name__ == "__main__":
    input = "GeeksforGeeks"
    d = 2
    rotate(input, d)

############################################################################################################

#656

'''
String slicing in python to rotate a string using deque
'''

from collections import deque

def rotate_string(s,d):
    deq = deque(s)
    if d > 0:
        deq.rotate(-d)
    else:
        deq.rotate(abs(d))
    return ''.join(deq)

s = "GeeksforGeeks"
d = 2

left_rotated = rotate_string(s,d)
right_rotated = rotate_string(s, -d)

print("Left Rotation: ", left_rotated)
print("Right Rotation: ", right_rotated)

############################################################################################################











































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
