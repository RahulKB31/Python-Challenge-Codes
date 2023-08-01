#11

# Write a function that takes as an argument a list containing numbers and returns true if the numbers in the
# list are in ascending order and returns false otherwise.
# Write code to call this function with several different lists, outputting the results returned by the function.

def checkascending(numList):
    '''
    returns true if numbers in numList are in ascending order
    assumes that adjacent equal elements are allowed
    argument: numList: list of numbers
    '''

    # number of pairs of adjacent elements is 1 less than the length of the list
    for i in range(0, len(numList)-1):
        if numList[i] > numList[i+1]:
            # will return False immediately if any adjacent pair is out of order
            return False
        # cannot return True until all pairs are checked
    return True

print(checkascending([1,2,2]))
print(checkascending([1,2,3,4,5,6,7,8,9,10,25,42,69,111]))
print(checkascending([1,2,3]))
print(checkascending([2,3,1]))
print(checkascending([9,7,5]))
print(checkascending([7]))
print(checkascending([1]))

#########################################################################################################

#12

# Write a function that takes as an argument a list of strings and returns a tuple containing two lists. The first
# list in the tuple should contain all of the strings in the original list that have length less than 5, and the
# second should contain all of the strings that have length greater than 7. (The len function which we have
# seen for lists can be applied to strings so, for example, len(”Hello”) would return 5.
# Write code to call this function with several different lists, outputting the returned lists.

def shortAndLongStrings(strList):
    '''
    returns lists containing all strings in strList with length<5
    and all strings in strList with length>7
    argument: strList: list of strings
    return: tuple containing 2 lists of strings
    '''
    shorts = []
    longs = []
    for string in strList:
        if len(string) < 5:
            shorts.append(string)
        elif len(string) > 7:
            longs.append(string)
    return shorts, longs

print(shortAndLongStrings(['hello','and','goodbye','x','longstring','verylongstring','x','ce156']))

#########################################################################################################

#13

# Modify your solution to exercise 3 so that the strings which are placed in the returned lists are also removed
# from the original list.
# Modify the calling code so that it also outputs the modified version of the original list

def shortAndLongString(strList):
    '''
    returns lists containing all strings in strList with length<5
    and all strings in strList with length>7
    also removes those strings from strList
    argument: strList: lst of strings
    return: tuple containing 2 lists of strings
    '''
    shorts = []
    longs = []
    for string in strList:
        if len(string) < 5:
            shorts.append(string)
        elif len(string) > 7:
            longs.append(string)
    # remove short and long strings from strList
    for string in shorts:
        strList.remove(string)
    for string in longs:
        strList.remove(string)
    return shorts, longs

myList = ['hello','and','goodbye','x','longstring','verylongstring','x','ce156']
print(shortAndLongString(myList))
print("Final contents of myList", myList)

##########################################Version 2#################################################

#14

def shortAndLongString(strList):
    '''
    returns lists containg all strings in strList with length<5
    and all strings with length > 7
    also removes those strings from strList
    argument: strList: list of strings
    return: tuple containing 2 lists of strings
    '''
    shorts = []
    longs = []
    # iterate through a copy of strList, since its not safe to remove
    # items form a list while iterating through it
    # remember we can use L[:] to get a copy of L
    for string in strList[:]:
        if len(string) < 5:
            shorts.append(string)
            strList.remove(string)
        elif len(string) > 7:
            longs.append(string)
            strList.remove(string)
    return shorts, longs

myList = ['hello','and','goodbye','x','longstring','verylongstring','x','ce156']
print(shortAndLongString(myList))
print("Final contents of myList", myList)

######################################################################################################

#15

# Now repeat the previous exercise by writing a function to
# generate the reversed list without using reverse. (You will need
# to use a loop to generate the new list element-by-element)

def reverseList(myList):
    '''
    returns a list which contains the elements of mylist in reverse order
    '''
    result = []
    # add elements at the front of the list so the last elements of myList
    # will end up at the front of result
    for i in myList:
        result.insert(0,i)
    return result

print(reverseList([3,4,5,6]))

########################################################################################################

#16 Different version

def reverseList(myList):
    '''
    returns a list which contains the elements of myList in reverse order
    '''
    result = []
    # start at end of original list appending items to result list
    # need a range with steps of -1 starting from len(mylist-1) ending at 0
    for i in range(len(myList)-1, -1,-1):
        result.append(myList[i])
    return result

#test example
print(reverseList([3,4,9,2]))

###########################################################################################################

#17

# Write a function that returns the sum of all the numbers in a
# list (the list should be passed to the function as an
# argument); you should assume that all of the elements of
# the list are indeed numbers.
# Test it with several different lists, outputting the results.

def sum_liat(alist):
    total = 0
    for i in alist:
        total += i
    return total

##############################################################################################################

#18

# Write a function to calculate and print the quotient and
# remainder of each of the elements of a tuple of numbers
# divided by the a given divisor, using divmod. Each pair of
# numbers should be output as a tuple.
# Test it with the following date
# atuple=(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# divisor = 7

def myfun(tup,divisor):
    for i in tup:
        t = divmod(i, divisor)
        print(t)

atuple = (10,20,30,40,50,60,70,80,90,100)
myfun(atuple,7)

####################################################################################################





































