#603

'''
Find words which are greater than given length k
'''

def string_k(k, str):

    #create the empty string
    string = []

    text = str.split(" ")

    for x in text:
        if len(x) > k:
            string.append(x)

    return string

k = 3
str = "geek for geeks"
print(string_k(k, str))

##############################################################################################################

#604

'''
Using list comprehension
'''

sentence = "hello geeks for geeks is computer science portal"
length = 4
print([word for word in sentence.split() if len(word) > length])

##########################################################################################################

#605

'''
Using lambda function
'''

S = "hello geeks for geeks is computer science portal"
K = 4
s = S.split(" ")
l = list(filter(lambda x: (len(x) > K), s))

##############################################################################################################

#606

'''
Using the enumerate function
'''

sentence = "hello geeks for geeks is computer science portal"
length = 4
s = sentence.split()
print([a for i,a in enumerate(s) if len(a) > length])

#############################################################################################################























































































































