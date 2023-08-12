#209

'''
Reversing a List in Python
'''

# Reverse Array using the slicing

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

lst = [10,11,12,13,14,15]
print(Reverse(lst))

########################################################################################################

#210

'''
Reverse list by swapping present and last numbers at a time
'''

def list_reverse(arr, size):

    # if only one element present, then return the array
    if (size == 1):
        return arr

    #if only two elements present, then swap both the numbers
    elif (size==2):
        arr[0], arr[1] = arr[1], arr[0]
        return arr

    # if nore than two elements present then swap first and last numbers
    else:
        i = 0
        while(i<size//2):

        #swap present and preceding numbers at time and jump to second element after swap
            arr[i],arr[size-i-1]=arr[size-i-1],arr[i]

        #skip if present and preceding numbers indexes are same
            if((i!=i+1 and size-i-1 != size-i-2) and (i!=size-i-2 and size-i-1 != i+1)):
                arr[i+1],arr[size-i-2] = arr[size-i-2],arr[i+1]
            i+=2
        return arr

arr= [1,2,3,4,5]
size = 5
print("Original list: ",arr)
print("Reversed list: ", list_reverse(arr,size))

#############################################################################################################

#211

'''
Reverse array using the reversed() and reverse() built-in-function
'''

lst = [10,11,12,13,14,15]
lst.reverse()
print("Using reverse() ", lst)
print("Using reversed() ", list(reversed(lst)))

####################################################################################################

#212

'''
Reverse a list using a two pointer approach
'''

#reversing a list using to pointer approach
def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left<right):
        #swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr

arr = [1,2,3,4,5,6,7]
print(reverse_list(arr))

########################################################################################################

#213

'''
Reverse a list using the insert() function
'''

#input list
lst = [10,11,12,13,14,15]

#the above input can also be given as
#lst = list(map(int, input().split())
l = [] #empty list

#iterate to reverse the list
for i in lst:
    #reversing the list
    l.insert(0,i)
#printing result
print(l)

##################################################################################################

#214

'''
Reverse a list using list comprehension
'''

original_list = [10,11,12,13,14,15]
new_list = [original_list[len(original_list) - i] for i in range(1, len(original_list)+1)]
print(new_list)

#####################################################################################################

#215

'''
Reverse a list using Numpy
'''

import numpy as np

#input list
my_list = [4,5,6,7,8,9]

#convert the list to a 1D numpy array
my_array = np.array(my_list)

#reverse the order of the array
reversed_array = my_array[::-1]

#convert the reversed array to a list
reversed_list = reversed_array.tolist()

#print the reversed list
print(reversed_list)

##########################################################################################################










































































































































































































































