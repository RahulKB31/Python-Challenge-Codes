#957

'''
Count number of lines in a text file in python
'''

# Python count the number of lines in a string using readlines()

with open(r"myfile.txt",'r') as fp:
    lines = len(fp.readlines())
    print("TOtal Number of lines:", lines)

##################################################################################################################

#958

# Python count the number of lines in a text file using enumerate

with open(r"myfile.txt",'r') as fp:
    for count, line in enumerate(fp):
        pass
print("Total number of lines:",count+1)

###################################################################################################################

#959

'''
Use loop and counter to count lines in python
'''

file = open("gfg.txt","r")
Counter = 0

Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print('This is the number of lines in the file')
print(Counter)

##################################################################################################################

#960

'''
Use the loop and sum functions to count lines in python
'''

with open(r"myfile.txt",'r') as fp:
    lines = sum(1 for ine in fp)
    print('Total Number of lines:', lines)

##################################################################################################################