#115

'''
Program to print ASCII value of a character
'''

c = 'g'
print("The ASCII value of " + c + "is", ord(c))

####################################################################################################

#116

print("Enter a string:", end="")
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)

#######################################################################################################

#117

'''
Replace every character of string by character whose ASCII value is K times more than it
'''

# Function to move string character
def encode(s, k):

    # changed string
    newS = ""

    # iterate for every characters
    for i in range(len(s)):

        #ASCII value
        val = ord(s[i])

        #store the duplicate
        dup = k

        # if k-th ahead character exceed 'z'
        if val + k>122:
            k -= (122-val)
            k = k % 26
            newS += chr(96 + k)

        else:
            newS += chr(val + k)

        k = dup

    # print the new string
    print(newS)

# driver code
str = "abc"
k = 28

encode(str, k)

####################################################################################################

#118

'''
Substring with maximum ASCII sum when some ASCII values are redefined
'''

import sys

# Function to find maximum sum string
def maxSum(w, x, b, n):
    ans = ""
    res = ""

    # If length of the given string is 1 we can return the string
    # It will be maximum in itself
    if (len(w) == 1):
        return w

    maxi = -1 * sys.maxsize
    sum, s = 0, 0

    mp = dict()

    # Taking unordered map to store new ascii value of character in x[]
    for i in range(len(w)):
        # store the string in ans
        ans = ans + w[i]
        temp = ""

        # if we find any redefined value of char of string w, we will add that value to the sum
        # else add its predefined value
        if w[i] in mp.keys():
            sum = sum + mp[w[i]]
        else:
            sum = sum + ord(w[i])

        # If anytime we find sum is getting negative clear the values stored in ans and make sum = 0 again
        if (sum < 0):
            sum = 0
            ans = ""

        # If sum is greater than maximum maxi will be updated as sum and new result would be string
        # stored in ans
        if (sum > maxi):
            maxi = sum
            res = ans

    return res

W = "abcde"
N = 1
X = ['c']
B = [-1000]

print(maxSum(W,X,B,N))

########################################################################################################

#119

'''
Program to print ASCII value of all digits of a given number
'''

def convertToASCII(N):
    while (N > 0):
        d = N % 10
        print(d, "(" + str(d + 48) + ")")
        N = N // 10

if __name__ == "__main__":
    N = 36
    convertToASCII(N)

#########################################################################################################

#120

'''
Python program to print words from a sentence with highest and lowest ASCII value of characters
'''

def averageValue(s):

    # stores the sum of ASCII value of all characters
    sumChar = 0

    # Traverse the string
    for i in range(len(s)):

        # increment sumchar by ord(s[i])
        sumChar += ord(s[i])

    #return the average
    return sumChar // len(s)

# Function to find words with maximum and minimum average of ascii values
def printMinMax(string):

    # stores the words of the string S seperated by spaces
    lis = list(string.split(" "))

    # stores the index of word in lis[] with maximum average
    maxID = 0

    # stores the index of word in lis[] with minimum average
    minID = 0

    #stores the maximum average of ASCII value of characters
    maxi = -1

    #stores the minimum average of ASCII value of characters
    mini = 1e9

    # traverse the list lis
    for i in range(len(lis)):

        # stores the average of word at index i
        curr = averageValue(lis[i])

        # if curr is greater than maxi
        if(curr > maxi):
            #update maxi and maxID
            maxi = curr
            maxID = i

        #if curr is lesser than mini
        if(curr < mini):
            # update mini and minID
            mini = curr
            minID = i

    #print string at minId in lis
    print("Minimum average ascii word =", lis[minID])

    #print string at maxID in lis
    print("Maximum average ascii word = ", lis[maxID])

#Driver code
s = "every momemt is fresh beginning"
printMinMax(s)

########################################################################################################

#121

'''
Total character pairs from two strings, with equal number of set bits in their ascii value
'''

# functon to get no of set bits in binary representation of positive integer n

def countSetBits(n):
    count = 0
    while (n):
        count += n and 1
        n >>= 1
    return count

# function to return the count of valid pairs
def totalPairs(s1, s2):
    count = 0
    arr1 = [0] * 7
    arr2 = [0] * 7

    # store frequency of number of set bits for s1
    for i in range(len(s1)):
        set_bits = countSetBits(ord(s1[i]))
        arr1[set_bits] += 1

    # store frequency of number of set bits for s2
    for i in range(len(s2)):
        set_bits = countSetBits(ord(s2[i]))
        arr2[set_bits] += 1

    # calculate total pairs
    for i in range(1,7):
        count += (arr1[i] * arr2[i])

    # return the count of valid pairs
    return count

# Driver code
if __name__ == "__main__":
    s1 = "geeks"
    s2 = "forgeeks"
    print(totalPairs(s1,s2))

#########################################################################################################

#122

'''
Program to convert given Binary to its equivalent ASCII character string
'''

# Function to convert binary to decimal
def binaryToDecimal(n):
    num = n
    # stores the decimal value
    dec_value = 0

    # Intitializing base value to 1
    base = 1

    le = len(num)
    for i in range(le - 1, -1, -1):

        # if the current bit is 1
        if (num[i] == "1"):
            dec_value += base
        base = base * 2

    # Return answer
    return dec_value

# FUnction to convert binary to ASCII
def setStringtoASCII(str):

    # to store size of s
    N = int(len(str))

    # if given string is not a valid string
    if (N % 8 != 0):
        return "Not Possible!"

    # to store final answer
    res = ""

    # Loop to iterate through string
    for i in range(0,N,8):
        decimal_values = binaryToDecimal(str[i:i+8])

        # append the ASCII character equivalent to current values
        res += chr(decimal_values)

    return res

#Driver code
if __name__ == "__main__":

    s = "01100000101100010"
    print(setStringtoASCII(s))

#########################################################################################################

#123

'''
Count and print the alphabets having ASCII value in the range[l,r]
'''
# Function to count the number of characters whose ascii value is in range[l,r]

def CountCharacters(str1, l, r):

    # Inititalizing the count to 0
    cnt = 0

    len1 = len(str1)
    for i in str1:

        # increment the count if the value is less
        if (1 <= ord(i) and ord(i) <= r):
            cnt = cnt + 1
            print(i, end = " ")

    # return the count
    return cnt

# Driver code
if __name__ == "__main__":
    str1 = "geeksforgeeks"
    l = 102
    r = 111

    print("Characters with ASCII values" + "in the range [l,r] are")
    print("\nand their count is", CountCharacters(str1, l, r))

#######################################################################################################

#124

'''
Count and print the alphabets having ASCII value not in the range(l,r)
'''

def CountCharacters(str, l, r):

    # Intializing the count to 0
    cnt = 0

    # using map to print a character only once
    m = {}
    length = len(str)
    for i in range(0, length):

        # Increment the count if the value is less
        if (not(1 <= ord(str[i]) and  ord(str[i]) <= r)):
            cnt += 1
            if ord(str[i]) not in m:
                m[ord(str[i])] = 0
                print(str[i], end = " ")
            m[ord(str[i])] += 1


    # return cnt
    return cnt

# Driver code

if __name__ == "__main__":
    str = "geekforgeeks"
    str = str.strip()
    l = 102
    r = 111
    print("Characters with ASCII values", end = "")
    print("not in the range [l,r]\n", "in the given setting are: ", end = "")
    print("\n and their count is", CountCharacters(str, l, r))

#######################################################################################################

#125

'''
Convert hexadecimal value string to ASCII value string
'''

def hexToASCII(hexx):

    # intializing the ASCII code string as empty
    ascii = ""

    for i in range(0, len(hexx), 2):

        #extract two characters from hex string
        part = hexx[i:i + 2]

        #chanage it into base 16 and typecast as the character
        ch = chr(int(part, 16))

        #add this char to final ASCII string
        ascii += ch

    return ascii

# Driver code
if __name__ == "__main__":

    # print the ASCII string
    print(hexToASCII("6765656b73"))

#####################################################################################################

#126

'''
Minimize ASCII values sum afer removing all occurances of one character
'''

def get_minimized_sum(s):
    min_sum = flaot('inf')
    n = len(s)

    for i in range(n):
        temp = ""
        for j in range(n):
            if s[j] != s[i]:
                temp += s[j]

        curr_sum = sum(ord(c) for c in temp)
        min_sum = min(min_sum, curr_sum)

    return min_sum

s = "geeksforgeeks"
print(get_minimized_sum(s))

##########################################################################################################


























































