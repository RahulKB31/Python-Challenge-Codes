#29

'''
Write a function that takes two file objects as arguments and compares the files that they refer to line-byline.
The two files are expected to have similar contents and the same number of lines.
The function should attempt to open the two files
The function should print the line numbers of any lines that are not the same in both files.
For example if the file contents were
ABCDEFGH
IJKLMN0
YZ
and
ABCDEFGH
PQRSTUX
YZ
The function should output something like “Line 2 was different”
Write code to test your function. The file names should be obtained from the user; if a file cannot be opened
the user should be asked to supply a different file name.
'''

def ex1Fun(f1, f2):
    """
    compares 2 files and outputs line numbers of lines that are different
    arguments: 2 file objects
    return: nothing
    Possible exception: IOError
    """

    lineNum = 0
    line1 = f1.readline()
    while len(line1.strip()) > 0:
        line2 = f2.readline()
        lineNum += 1
        if line1 != line2:
            print("Line", lineNum, "was different")
        line1 = f1.readline()

opened = False
while not opened:
    fName1 = input("name of first file: ")
    try:
        f1 = open(fName1)
        opened = True
    except:
        print("Error opening file; please supply another file name")

opened = False # reuse same variable
while not opened:
    fName2 = input("Name of second file: ")
    try:
        f2 = open(fName2)
        opened = True
    except:
        print("Error opening file, please supply another file name")

try:
    ex1Fun(f1, f2)
except:
    print("Error reading from file")

####################################################################################################

#30

'''
Write a function that takes as arguments a character and a file
name. The function should open the file, read its contents and
return the number of occurrences of the character.
Test with files containing (i) just one line; (ii) several lines and (iii)
no lines.
'''

inFile = open("test.txt",'r')
outFile = open("outtest.txt",'w')
lineCount = 0
blankLineCount = 0

for line in inFile:
    line2 = line.strip()
    if len(line2) == 0:
        blankLineCount += 1
        print(line2, file=outFile)
    else:
        print(lineCount+1, line, file = outFile, end = '')
        lineCount += 1

inFile.close()
print("There were", lineCount+blankLineCount, "lines in the file:", blankLineCount, "were blank", file=outFile)
outFile.close()

########################################################################################################

#31

'''
Write a program that:
- asks the user to enter the name of a file
- tells the user whether this file exists or not
If the file does not exist, your program should display on the
screen the names of files in the current directory (one per line).
'''

import os
fileName = input("Enter file name: ")
if os.path.exists(fileName)
    print("The file exist")
else:
    print("The file does not exist. Files that do exist are")
    for name in os.listdir(os.getcwd()):
        print(name)

#######################################################################################################

#32

'''
Write a program in which the user is presented with options to:
1 – Create and write to a file
2 – Show a file on the screen
3 – Exit
The program should use a loop in which the user is allowed to select an
option.
If option 1 or 2 is chosen, the program should ask the user for the file
name.
Option 1 should create a file and allow the user to write as many lines of
text as the user would like in this file.
Option 2 should show the content of a file on the screen.
After processing an option (apart from 3) your program should show the
menu again.
The program should give appropriate error messages if files could not be
opened.
'''

def getOption():
    '''
    present menu and get option choice from user
    :return: integer in range 1-3
    '''
    print("Options are")
    print("1 create and write to a file")
    print("2 Read a file")
    print("3 Exit program")
    while True:   # keep looping until valid input has been returned
        try:
            option = int(input("Select option: "))
            if 1 <= option <=3:
                return option
            else:
                print("Out of range - try again")
        except:
            print("Input an integer - try again")

looping = True
while looping:
    opt = getOption()
    if opt == 3:
        looping = False
    else:
        name = input("Enter file name: ")
        try:
            if opt == 1:
                f = open(name, 'w')
                while True:
                    line = input("Supply line of text (use * to finish): ")
                    if line == '*':
                        break
                    print(line, file = f)
                f.close()
            else: # option must be 2 since getOption always returns a valid option
                f = open(name)
                for line in f:
                    # if line ends with a new line remove it since print adds a new line
                    if line[-1] == '\n':
                        line = line[:-1]
                    print(line)
                f.close()
        except:
            print("Failed to open", name)

##########################################################################################################
































