#945

'''
Python program to read character by character from a file
'''

file = open('file.txt','r')

while 1:
    char = file.read(1)
    if not char:
        break

    print(char)

file.close()

#############################################################################################################

#946

with open('file.txt') as f:
    while True:
        c = f.read(5)
        if not c:
            break

        print(c)

###############################################################################################################