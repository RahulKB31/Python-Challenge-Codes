#738

'''
Python Counter to find the size of largest subset of anagram words
'''

from collections import Counter

def maxAnagramSize(input):
    input = input.split(" ")

    for i in range(0, len(input)):
        input[i] = ''.join(sorted(input[i]))

    freqDict = Counter(input)

    print(max(freqDict.values()))

if __name__ == "__main__":
    input = 'ant magenta magnate tan gnamate'
    maxAnagramSize(input)

##############################################################################################################

#739

'''
Using dictionary
'''

def largest_anagram_subset_size(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)

    max_count = max([len(val) for val in anagram_dict.values()])

words = ['ant','magenta','magnate','tan','gnamate']

print(largest_anagram_subset_size(words))

###############################################################################################################

#740

'''
Using lambda
'''

from collections import Counter

words = ['cars','bikes','arcs','steer']

max_anagrams = max(
    list(
        map(
            lambda x: sum(
                map(
                    lambda y: Counter(y) == Counter(x), words
                )
            ),words
        )
    ),default=0
)

print(max_anagrams)

####################################################################################################################











































































































































































































