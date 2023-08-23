#764

'''
Possible words using given characters in Python
'''

def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict

def possible_words(lwords,charSet):
    for word in lwords:
        flag = 1
        chars = charCount(word)
        for key in chars:
            if key not in charSet:
                flag = 0
            else:
                if charSet.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)

if __name__ == "__main__":
    input = ['goo','bat','me','eat','goal','boy','run']
    charSet = ['e','o','a','a','m','g','l']
    possible_words(input, charSet)

###############################################################################################################

#765

def find_words(dictionary, characters, word=''):
    if word in dictionary:
        print(word)

    for char in characters:
        new_characters = characters.copy()
        new_characters.remove(char)
        find_words(dictionary, new_characters, word+char)

dictionary = ['goo','bat','me','eat','goal','boy','run']
characters = ['e','o','a','a','m','g','l']
find_words(dictionary, characters)

###########################################################################################################

#766

def possible_words(Dict, arr):
    arr_set = set(arr)
    result = []
    for word in Dict:
        if set(word).issubset(arr_set):
            result.append(word)
    return result

Dict = ['goo','bat','me','eat','goal','boy','run']
arr = ['e','o','a','a','m','g','l']
print(possible_words(Dict, arr))

###############################################################################################################

























































































































































































