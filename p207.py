#969

'''
Python - Append content of one text file to another
'''

firstfile = input("Enter the name of first file")
secondfile = input("Enter the name of second file")

# opening both the files in read only mode to read initial contents
f1 = open(firstfile,'r')
f2 = open(secondfile,'r')

#printing the contents of the file before appending
print('content of first file before appending', f1.read())
print('content of the seconf file before appending', f2.read())

#closing the files
f1.close()
f2.close()

# opening first file in append mode and second file in read mode
f1 = open(firstfile,'a+')
f2 = open(secondfile,'r')

#opening the contents of the second file to the first file
f1.write(f2.read())

# relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)

#printing the contents of the files after appending
print('content of first file after appending',f1.read())
print('content of second file after appending',f2.read())

#closing the files
f1.close()
f2.close()

#######################################################################################################################

#970

# Append the content of one text file to another using the shutil module

import shutil


def append_files_method2(file1_path, file2_path):
    with open(file1_path,'r') as file1:
        with open(file2_path,'a') as file2:
            shutil.copyfileobj(file1,file2)

file1_path = 'file1.txt'
file2_path = 'file2.txt'
append_files_method2(file1_path,file2_path)

#####################################################################################################################