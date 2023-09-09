#915

'''
Python regex to find sequence of one upper case letter followed by lower
'''
import re
from collections import Counter

def most_occr_element(word):

    # re.findall will extract all the elements from the string and make a list
    arr = re.findall(r'[0-9]+',word)

    # to store maxm frequency
    maxm = 0

    # to store maxm element of most frequency
    max_elem = 0

    c = Counter(arr)

    for x in list(c.keys()):
        if c[x] >= maxm:
            maxm = c[x]
            max_elem = int(x)

    return max_elem

if __name__ == "__main__":
    word = 'geek55of55geek4kasfd32rs'
    print(most_occr_element(word))

################################################################################################################