#974

'''
Python Program to merge two files into a third file
'''

# Program to merge two files into new file
# Naive Approach to merge two files into a third file

data = data2 = ""

with open('file1.txt') as fp:
    data = fp.read()

with open('file2.txt') as fp:
    data2 = fp.read()

data += "\n"
data += data2

with open('file3.txt','w') as fp:
    fp.write(data)

#####################################################################################################################

#975

'''
Program to merge two files into a third file using a for loop
'''

filenames = ['file1.txt','file2.txt']

with open('file3.txt','w') as outfile:
    for names in filenames:
        with open(names) as infile:
            outfile.write(infile.read())

        outfile.write("\n")

#####################################################################################################################

#976

'''
Program to merge two files into a thrid file using the shutil module
'''

import shutil

def merge_files_with_shutil(file1,file2,merged_file):
    with open(merged_file,'wb') as outfile:
        for filename in [file1, file2]:
            with open(filename,'rb') as infile:
                shutil.copyfileobj(infile,outfile)

file1 = 'file1.txt'
file2 = 'file2.txt'
merged_file = 'merged_file.txt'
merge_files_with_shutil(file1,file2,merged_file)

#####################################################################################################################

#977

'''
Program to merge two files into a third file using os module
'''

import os

def merge_files_with_os(file1,file2,merged_file):
    with open(merged_file,'w') as outfile:
        for filename in [file1, file2]:
            with open(filename,'r') as infile:
                for line in infile:
                    outfile.write(line)

file1 = 'file1.txt'
file2 = 'file2.txt'
merged_file = 'merged_file.txt'
merge_files_with_os(file1,file2,merged_file)

#####################################################################################################################



















