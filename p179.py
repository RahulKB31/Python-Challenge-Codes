#911

'''
The most occuring number in a string using Regex in Python
'''

import re
from collections import Counter

def most_occr_element(word):

    #re.findall will extract all the elements from strings and a list
    arr = re.findall(r'[0-9]+', word)

    # to store maxm frequency
    maxm = 0

    # to store maxm element of most frequency
    max_elem = 0

    #counter wil store all the number with their frequencies c = Count((55,2),(2,1),(3,1))
    c = Counter(arr)

    # store all the keys of counter in a list in which first would be our required element
    for x in list(c.keys()):
        if c[x] >= maxm:
            maxm = c[x]
            max_elem = int(x)

    return max_elem

if __name__ == "__main__":
    word = 'geek55of55gee4ksabcd3dr2x'
    print(most_occr_element(word))

##################################################################################################################




















































