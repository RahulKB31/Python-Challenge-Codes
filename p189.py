#928

'''
Check if an URL is valid or not using Regular Expression
'''

import re

def isValidURL(str):

    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?"+ "[a-zA-Z0-9@:%._\\+~#?&//=]"+ "{2,256}\\.[a-z]" + "{2,6}\\.[a-z]"+
             "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\ + ._\\+~#?&//=]*)")

    p = re.compile(regex)

    if (str == None):
        return False

    if(re.search(p, str)):
        return True
    else:
        return False

url = "https://ww.geeksforgeeks.com"

if(isValidURL(url) == True):
    print("Yes")
else:
    print("No")

####################################################################################################################