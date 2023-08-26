#750

'''
Counting the frequencies in a list using dictionary in Python
'''

# Counting the frequencies in a list using a loop

def CountFrequency(my_list):

    #creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("%d: %d" % (key, value))

if __name__ == "__main__":
    my_list = [1,1,1,2,2,2,2,5,5,5,5,5,3,4,5,2,2,2,3,3,3]
    CountFrequency(my_list)

############################################################################################################

#751

'''
Count the frequencies in a list using list.count()
'''

import operator

def CountFrequency(my_list):
    freq = {}
    for items in my_list:
        freq[items] = my_list.count(items)

    for key, value in freq.items():
        print("%d: %d" %(key, value))

if __name__ == "__main__":
    my_list = [1,1,1,2,2,2,2,5,5,5,5,5,3,4,5,2,2,2,3,3,3]
    CountFrequency(my_list)

##################################################################################################################

#752

'''
Count the frequencies in a list using dict.get()
'''

def CountFrequency(my_list):
    count = {}
    for i in [1,1,1,2,2,2,2,5,5,5,5,5,3,4,5,2,2,2,3,3,3]:
        count[i] = count.get(i, 0) + 1
    return count

if __name__ == "__main__":
    my_list = [1,1,1,2,2,2,2,5,5,5,5,5,3,4,5,2,2,2,3,3,3]
    CountFrequency(my_list)

###############################################################################################################

















































































































































