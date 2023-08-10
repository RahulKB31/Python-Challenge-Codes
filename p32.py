#180

'''
Python program to swap two elements in a list
'''

# Swap 2 elements in a list using comma assignment
# swap function

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 -1, pos2-1))

######################################################################################################

#181

'''
Using inbuilt list.pop() function to swap two elements in a list
'''

def swapPositions(list, pos1, pos2):

    #popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)

    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list

# Driver function
List = [23,65,19,90]
pos1, pos2 = 1,3

print(swapPositions(List, pos1-1, pos2-1))

############################################################################################################

#182

'''
Swap two elements in a list using tuple variable
'''

def swapPositions(list, pos1, pos2):
    # storing the two elements as a pair in a tuple variable get
    get = list[pos1], list[pos2]

    #unpacking those elements
    list[pos2], list[pos1] = get
    return list

List = [23,65,19,90]
pos1, pos2 = 1,3
print(swapPositions(List, pos1-1,pos2-1))

#############################################################################################################

#183

'''
Swap two elements in a list using temp variable
'''

def swapPostions(lis, pos1, pos2):
    temp = lis[pos1]
    lis[pos1] = lis[pos2]
    lis[pos2] = temp
    return lis

# Driver function
List = [23,65,19,90]
pos1, pos2 = 1,3
print(swapPositions(List, pos1-1,pos2-1))

##################################################################################################

#184

'''
Swap two elements in a list using enumerate
'''

def swapPositions(lis, pos1, pos2):
    for i,x in enumerate(lis):
        if i == pos1:
            elem1 = x
        if i == pos2:
            elem2 = x
    lis[pos1] = elem2
    lis[pos2] = elem1
    return lis

List = [23,65,19,90]
pos1, pos2 = 1,3
print(swapPositions(List, pos1-1, pos2-1))

#######################################################################################################

























































































































