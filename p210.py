#978

'''
Python program to reverse a single line of a text file
'''

f = open('GF.txt','r')

lines = f.readlines()
f.close()
choice = 1

line = lines[choice].split()
Reversed = " ".join(line[::-1])
lines.pop(choice)
lines.insert(choice, Reversed)

u = open('GFG.txt','w')
u.writelines(lines)
u.close()

#####################################################################################################################