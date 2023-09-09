#912

'''
Python Regex to extract maximum numeric value from a string
'''

import re

def extractMax(input):

    # \d+ is a regular expression which means one or more digit
    numbers = re.findall('\d+', input)

    numbers = map(int, numbers)
    print(max(numbers))

if __name__ == "__main__":
    input = '100sjdfhsk567kvj983'
    extractMax(input)

##################################################################################################################























































































