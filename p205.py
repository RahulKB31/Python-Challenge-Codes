#964

'''
Eliminating repeated lines from a file using python
'''

def remove_duplicates(input_file,output_file):
    lines_seen = set()
    with open(output_file,'w') as output_file:
        with open(input_file,'r') as in_file:
            for line in in_file:
                if line not in lines_seen:
                    out_file.write(line)
                    lines_seen.add(line)

input_file = open('lorem_input.txt','r')
output_file = open('lorem_output.txt','w')
remove_duplicates(input_file,output_file)

###################################################################################################################

#965

# Eliminating repeated lines from a file using a set

outputFile = open('lorem_output.txt','w')
inputFile = open('lorem_input.txt','r')

lines_seen_so_far = set()

for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)

        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()

##################################################################################################################

#966

# Eliminating repeated lines from a file using pandas

import pandas as pd

def remove_duplicates(input_file,output_file):
    df = pd.read_csv(input_file, header=None)
    df.drop_duplicates(inplace=True)
    df.to_csv(output_file,header=False, index= False)

outputFile = open('lorem_output.txt','w')
inputFile = open('lorem_input.txt','r')
remove_duplicates(input_file,output_file)

###################################################################################################################
