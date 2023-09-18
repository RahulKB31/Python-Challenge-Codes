#947

'''
Python - Get number of characters, words, spaces and lines in a file
'''

def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0
    with open(fname,'r') as f:
        for line in f:
            num_lines += 1
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1
                    word = "N"
                elif (letter == ' '):
                    num_spaces += 1
                    word = 'Y'

                for i in letter:
                    if (i != " " and i != "\n"):
                        num_charc += 1

    print("Number of words in text file:", num_words)
    print("Number of lines in text file:", num_lines)
    print("Number of characters in text file:", num_charc)
    print("Number of spaces in text file:", num_spaces)

if __name__ == '__main__':
    fname = 'File1.txt'
    try:
        counter(fname)
    except:
        print('File not found')

####################################################################################################################

#948

'''
Find the number of characters in a file using python
'''

import os

def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0
    with open(fname,'r') as f:
        for line in f:
            # seperating a line from \n character and storing again in line
            line = line.strip(os.linesep)

            #splitting the line
            wordslist = line.split()

            #incrementing value of num_lines
            num_lines = num_lines + 1

            #incrementing value of num_word
            num_words = num_words + len(wordslist)

            # incrementing value of num_char
            num_charc = num_charc + sum(1 for c in line if c not in (os.linesep,' '))

            # incrementing value of num_space
            num_spaces = num_spaces + sum(1 for s in line if s in (os.linesep,' '))

    print("Number of words in text file:", num_words)
    print("Number of lines in text file:", num_lines)
    print("Number of characters in text file:", num_charc)
    print("Number of spaces in text file:", num_spaces)


if __name__ == '__main__':
    fname = 'File1.txt'
    try:
        counter(fname)
    except:
        print('File not found')

###################################################################################################################





















































