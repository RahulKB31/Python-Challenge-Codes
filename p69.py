<<<<<<< HEAD
#507

'''
String Programs

Python program to check if a string is palindrome or not
'''

def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

#################################################################################################################

#508

'''
Using iterative method
'''

def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

##############################################################################################################

#509

def isPalindrone(s):
    rev = ''.join(reversed(s))

    if (s == rev):
        return True
    return False

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

############################################################################################################

#510

'''
Using one extra variable
'''

x = 'malayalam'
w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes")
else:
    print("No")

###############################################################################################################

#511

'''
Using flag
'''

st = "malayalam"
j = -1
flag = 0
for i in st:
    if i != st[j]:
        flag = 1
        break
    j = j - 1

if flag == 1:
    print("No")
else:
    print("Yes")

###############################################################################################################

#512

'''
Using recursion
'''

def isPalindrome(s):

    s = s.lower()
    l = len(s)

    if l < 2:
        return True

    elif s[0] == s[l - 1]:
        return isPalindrone(s[l: l - 1])

    else:
        return False

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

###############################################################################################################


























































































































































=======
#507

'''
String Programs

Python program to check if a string is palindrome or not
'''

def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

#################################################################################################################

#508

'''
Using iterative method
'''

def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

##############################################################################################################

#509

def isPalindrone(s):
    rev = ''.join(reversed(s))

    if (s == rev):
        return True
    return False

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

############################################################################################################

#510

'''
Using one extra variable
'''

x = 'malayalam'
w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes")
else:
    print("No")

###############################################################################################################

#511

'''
Using flag
'''

st = "malayalam"
j = -1
flag = 0
for i in st:
    if i != st[j]:
        flag = 1
        break
    j = j - 1

if flag == 1:
    print("No")
else:
    print("Yes")

###############################################################################################################

#512

'''
Using recursion
'''

def isPalindrome(s):

    s = s.lower()
    l = len(s)

    if l < 2:
        return True

    elif s[0] == s[l - 1]:
        return isPalindrone(s[l: l - 1])

    else:
        return False

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

###############################################################################################################


























































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
