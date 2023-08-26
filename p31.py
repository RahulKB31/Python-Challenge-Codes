#173

'''
Python program to interchange first and last elements in a list
'''

# Find the length of the list and simply swap the first elemetn with (n-1)th element

def swapList(newList):
    size = len(newList)

    # swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

newList = [12,35,9,56,24]

print(swapList(newList))

############################################################################################################

#174

'''
The last element of the list can be referred as list[-1]. Therefore we can swap list[0] with list[-1]
'''

def swapList(newList):

    newList[0], newList[-1] = newList[-1], newList[0]

    return newList

newList = [12,35,9,56,24]
print(swapList(newList))

###########################################################################################################

#175

'''
Swap the first and last element is using tuple variable. Store the first and last element as a
pair in a tuple variable, say get and unpack those elements with first and last element in that list.
Now the first and last values in that list are swapped
'''

def swapList(list):
    # storing the first and last element as a pair in a tuple variable get
    get = list[-1], list[0]

    #unpacking those elements
    list[0], list[-1] = get
    return list

newList = [12,35,9,56,24]
print(swapList(newList))

#############################################################################################################

#176

'''
Using * operand. This operand proposes a change to iterable unpacking syntax, allowing to specify a catch all name
which will be assigned a list of all items not assigned to a regular name.
'''

list = [1,2,3,4]

a, *b, c = list
print(a)
print(b)
print(c)

#############################################################################################################

#177

#swap function
def swapList(list):
    start, *middle, end = list
    list = [end, *middle, start]

    return list

newList = [12,35,9,56,24]
print(swapList(newList))

##############################################################################################################

#178

'''
Swap the first and last elements is to use the inbuilt function list.pop(). Pop the first element and store
it in a variable. Similarly pop the last element and store it in another variable.
Now insert the two popped element at each others original position.
'''

def swapList(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0,last)
    list.append(first)

    return list

newList = [12,35,9,56,24]

print(swapList(newList))

##############################################################################################################

#179

'''
Using slicing
'''

def swap_first_last_3(lst):
    # check if list has at least 2 elements
    if len(lst) >= 2:
        # swap the first and last elements using slicing
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst

# Intializing the input
inp = [12,35,9,56,24]

#printing the original input
print("The original input is:", inp)

result = swap_first_last_3(inp)

# Printing the result
print("The output after swap first and last is:", result)

########################################################################################################























































































































