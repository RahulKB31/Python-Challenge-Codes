#645

'''
Python | Check for URL in a String
'''

import re
def Find(string):

    regex = r"(?i)\b((?:hettps?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}"
    url = re.findall(regex, string)
    return [x[0] for x in url]

string = 'My Profile: https://www.youtube.com/watch?v=qGQQesfQ3gw&ab_channel=KrishNaik is a portal of https://www.youtube.com/'
print("Urls: ", Find(string))

################################################################################################################

#646

'''
Using startswith() method
'''

def Find(string):
    x = string.split()
    res = []
    for i in x:
        if i.startswith("https:") or i.startswith("http:"):
            res.append(i)

    return res

string = 'My Profile: https://www.youtube.com/watch?v=qGQQesfQ3gw&ab_channel=KrishNaik is a portal of https://www.youtube.com/'
print("Urls: ", Find(string))

################################################################################################################

#647

'''
Using find() method
'''

def Find(string):
    x = string.split()
    res = []
    for i in x:
        if i.find("https:")==0 or i.find('http:')==0:
            res.append(i)
    return res

string = 'My Profile: https://www.youtube.com/watch?v=qGQQesfQ3gw&ab_channel=KrishNaik is a portal of https://www.youtube.com/'
print("Urls: ", Find(string))

################################################################################################################

#648

'''
Using the urlparse() function from urllib.parse
'''

from urllib.parse import urlparse

string = 'My Profile: https://www.youtube.com/watch?v=qGQQesfQ3gw&ab_channel=KrishNaik is a portal of https://www.youtube.com/'

words = string.split()

urls = []
for word in words:
    parsed = urlparse(word)
    if parsed.scheme and parsed.netloc:
        urls.append(word)

print("URLs: ", urls)

###############################################################################################################

#649

'''
Using reduce()
'''

from functools import reduce

def merge_url_lists(url_list1, url_list2):
    return url_list1 + url_list2

def find_urls_in_string(string):
    x = string.split()
    return [i for i in x if i.find("https:")==0 or i.find("https:")==0]

string1 = 'My Profile: https://www.youtube.com/watch?v=qGQQesfQ3gw&ab_channel=KrishNaik is a portal of https://www.youtube.com/'
string2 = 'Some more text without URLs'

string_list = [string1, string2]

url_list = reduce(merge_url_lists, map(find_urls_in_string, string_list))

print("Urls: ", url_list)

################################################################################################################

























































































































































































