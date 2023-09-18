#943

'''
Python program to read file word by word
'''

with open('GFG.txt','r') as file:
    for line in file:
        for word in line.split():
            print(word)

####################################################################################################################

#944

with open('GFG.txt','r') as file:
    for line in file:
        for word in line.split():
            print(word)

##################################################################################################################