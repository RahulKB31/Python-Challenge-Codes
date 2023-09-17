#942

'''
Categorize Password as Strong or Weak using Regex in Python
'''

import re

def password(v):
    if v == "\n" or v == " ":
        return "Password cannot be a newline or space!"

    if 9 <= len(v) <= 20:
        # check for occurance of a character three or more times in a row
        if re.search(r'(.)\1\1',v):
            return "Weak Password: Same character repeats 3 or 4 times in a row"

        # check for occurance of same string pattern (minimum of two character length)
        if re.search(r'(..)(.*?)\1',v):
            return "Weak Password: same string pattern repitition"
        else:
            return "Strong Password!"

    else:
        return "Password length must be 9-20 characters!"

def main():
    print(password("Qggf!@ghf3"))
    print(password("Gggksforgeeks"))
    print(password("aaabnillgu"))
    print(password("Aasd!feasn"))
    print(password("772*hd897"))
    print(password(" "))

if __nam__ == '__main__':
    main()

####################################################################################################################