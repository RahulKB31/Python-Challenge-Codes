<<<<<<< HEAD
#763

'''
Scraping and finding Ordered Words in a dictionary using Python
'''

import requests

def getWords():
    url = "http://wiki.puzzlers.org/pub/wordlists/unixdict.txt"

    fetchData = requests.get(url)

    wordList = fetchData.content

    wordList = wordList.decode("utf-8").split()

    return wordList

def isOrdered():

    collection = getWords()

    collection = collection[16:]
    word = ''

    for word in collection:
        result = 'Word is Ordered'
        i = 0
        l = len(word) - 1

        if (len(word) < 3):
            continue

        while i < 1:
            if (ord(word[i]) > ord(word[i+1])):
                result = "Word is not ordered"
                break

            else:
                i += 1

        if (result == "Word is ordered"):
            print(word, ':',result)

if __name__ == "__main__":
=======
#763

'''
Scraping and finding Ordered Words in a dictionary using Python
'''

import requests

def getWords():
    url = "http://wiki.puzzlers.org/pub/wordlists/unixdict.txt"

    fetchData = requests.get(url)

    wordList = fetchData.content

    wordList = wordList.decode("utf-8").split()

    return wordList

def isOrdered():

    collection = getWords()

    collection = collection[16:]
    word = ''

    for word in collection:
        result = 'Word is Ordered'
        i = 0
        l = len(word) - 1

        if (len(word) < 3):
            continue

        while i < 1:
            if (ord(word[i]) > ord(word[i+1])):
                result = "Word is not ordered"
                break

            else:
                i += 1

        if (result == "Word is ordered"):
            print(word, ':',result)

if __name__ == "__main__":
>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
    isOrdered()