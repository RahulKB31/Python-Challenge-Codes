#939

'''
Python program to check the validity of a password
'''

import re
password = "R@m@_fOrtu9e$"
flag = 0
while True:
    if (len(password)<=8):
        flag = -1
        break
    elif not re.search("[a-z]",password):
        flag = -1
        break
    elif not re.search("[A-Z]",password):
        flag = -1
        break
    elif not re.search("[0-9]",password):
        flag = -1
        break
    elif not re.search("[_@$]",password):
        flag = -1
        break
    elif re.search("\s",password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password")

###################################################################################################################

#940

l,u,p,d = 0,0,0,0
s = "R@m@_fOrtu9e$"
if (len(s) >= 8):
    for i in s:
        # counting lowercase alphabets
        if (i.islower()):
            l+=1

        # counting uppercase alphabets
        if (i.isupper()):
            u+=1

        # counting digits
        if (i.isdigit()):
            d+=1

        # counting the mentioned special characters
        if(i=='@' or i=='$' or i=='_'):
            p+=1
if(l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
    print("Valid Password")
else:
    print("Invalid Password")

####################################################################################################################

#941

l,u,p,d = 0,0,0,0
s = "R@m@_fOrtu9e$"
capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets = "abcdefghijklmnopqrstuvwxyz"
specialchars="$@_"
digits="0123456789"
if (len(s) >= 8):
    for i in s:
        if (i in smallalphabets):
            l+=1
        if (i in capitalalphabets):
            u+=1
        if (i in digits):
            d+=1

        if(i in specialchars):
            p +=1
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
    print("Valid Password")
else:
    print("Invalid Password")

####################################################################################################################


















