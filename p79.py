#581

'''
Python count the number of matching characters in a pair of string
'''

def commonfun(str1, str2):
    return(len(set((str1)).intersection(set(str2))))

string1 = "ASDF"
string2 = "WERTF"

no_of_common_character = commonfun(string1.lower(),string2.lower())
print("No of common characters are: ", no_of_common_character)

###############################################################################################################

#582

def count(str1, str2):
    #Initialize an empty dictionary to keep track
    char_count = {}

    #iterate over each character in str1
    for char in str1:
        #if the character is already in the dictionary increment the count
        if char in char_count:
            char_count[char] += 1
        #otherwise add the character to the dictionary with a count of 1
        else:
            char_count[char] = 1

    #Initialize a counter variable to 0
    counter = 0

    #iterate over each character in str2
    for char in str2:
        if char in char_count and char_count[char] > 0:
            counter += 1
            char_count[char] -= 1

    #print the number of matching characters
    print("No of matching characters are: " + str(counter))

if __name__ == "__main__":
    str1 = "dfkdjhfsjkghfjg"
    str2 = "asdffghfjkghf"
    count(str1,str2)

##############################################################################################################



















































































































































































































































