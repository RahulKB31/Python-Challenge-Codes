<<<<<<< HEAD
#762

'''
Python dictionary, set and counter to check if frequencies can become same
'''

from collections import Counter

def allSame(input):
    dict = Counter(input)

    same = list(set(dict.values()))

    if len(same)>2:
        print('No')
    elif len(same)==2 and same[1]-same[0]>1:
        print('No')
    else:
        print('Yes')

if __name__ == "__main__":
    input = 'xxxxuyyyyzzt'
    allSame(input)

=======
#762

'''
Python dictionary, set and counter to check if frequencies can become same
'''

from collections import Counter

def allSame(input):
    dict = Counter(input)

    same = list(set(dict.values()))

    if len(same)>2:
        print('No')
    elif len(same)==2 and same[1]-same[0]>1:
        print('No')
    else:
        print('Yes')

if __name__ == "__main__":
    input = 'xxxxuyyyyzzt'
    allSame(input)

>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
##############################################################################################################