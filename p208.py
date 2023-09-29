#972

'''
Python program to copy odd lines of one file to another
'''

#copy odd lines of ones file to another file in python

def copy_odd_lines(input_file, output_file):
    with open(input_file,'r') as infile, open(output_file,'w') as outfile:
        for line_number, line in enumerate(infile,1):
            if line_number % 2 != 0:
                outfile.write(line)

input_file_name = 'input.txt'
output_file_name = 'output.txt'
copy_odd_lines(input_file_name,output_file_name)

######################################################################################################################

#973

'''
Python to write specific lines from one file to another file
'''

def copy_specific_lines(input_file, output_file, line_numbers):
    with open(input_file,'r') as infile, open(output_file,'w') as outfile:
        for line_number, line in enumerate(infile,1):
            if line_number in line_numbers:
                outfile.write(line)

input_file_name = 'input.txt'
output_file_name = 'output.txt'
lines_to_copy = [1,2]
copy_specific_lines(input_file_name,output_file_name, lines_to_copy)

######################################################################################################################