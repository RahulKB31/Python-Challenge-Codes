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








