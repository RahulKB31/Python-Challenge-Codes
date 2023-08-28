<<<<<<< HEAD
#761

'''
Python counter and dictionary intersection example ( make a string using deletion and rearrangement)
'''

from collections import Counter

def makeString(str1, str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    result = dict1 & dict2

    return result == dict1

if __name__ == "__main__":
    str1 = "AAABDJKDLKSHISHEK"
    str2 = "jdhkjfghdfjghljadkjKJDFLKJG"
    if(makeString(str1, str2) == True):
        print("Possible")
    else:
        print("Not Possible")

################################################################################################################

























































=======
#761

'''
Python counter and dictionary intersection example ( make a string using deletion and rearrangement)
'''

from collections import Counter

def makeString(str1, str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    result = dict1 & dict2

    return result == dict1

if __name__ == "__main__":
    str1 = "AAABDJKDLKSHISHEK"
    str2 = "jdhkjfghdfjghljadkjKJDFLKJG"
    if(makeString(str1, str2) == True):
        print("Possible")
    else:
        print("Not Possible")

################################################################################################################

























































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
