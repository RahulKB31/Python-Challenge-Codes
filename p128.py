#772

'''
Python - Maximum and Minimum K elements in Tuple
'''

# Using sorted() + loop

test_tup = (5,20,3,7,6,8)

print("The original tuple is: " + str(test_tup))

K = 2

res = []
test_tup = list(sorted(test_tup))

for idx,val in enumerate(test_tup):
    if idx < K or idx >= len(test_tup) - K:
        res.append(val)
res = tuple(res)

print("The extracted values: " + str(res))

################################################################################################################

#773

'''
Using list slicing + sorted()
'''

test_tup = (5,20,3,7,6,8)

print("The original tuple is: " + str(test_tup))

K = 2

test_tup = list(test_tup)
temp = sorted(test_tup)
res = tuple(temp[:K] + temp[-K:])

print("The extracted values: " + str(res))

#################################################################################################################

#774

'''
Using heapq module
'''

import heapq
test_tup = (5,20,3,7,6,8)

print("The original tuple is: " + str(test_tup))
K = 2

smallest = heapq.nsmallest(K,test_tup)
largest = heapq.nlargest(K,test_tup)
result = tuple(sorted(smallest + largest))
print("The extracted values: " + str(result))

################################################################################################################

#775

'''
Using the built-in functions min() and max() and a loop to extract the K elements
'''

test_tup = (5,20,3,7,6,8)

print("The original tuple is: " + str(test_tup))

K = 2

min_val = min(test_tup)
max_val = max(test_tup)

min_list = []
max_list = []

for elem in test_tup:
    if elem <= max_val:
        if len(max_list) < K:
            max_list.append(elem)
        else:
            max_list.remove(min(max_list))
            max_list.append(elem)
        max_val = max(max_list)
    if elem >= min_val:
        if len(min_list) < K:
            min_list.append(elem)
        else:
            min_list.remove(max(min_list))
            min_list.append(elem)
        min_val = min(min_list)

result = tuple(min_list + max_list)

print("The extracted values: " + str(result))

#################################################################################################################

#776

'''
Using while loop + sort()
'''

tup = (0,1,2,3,4,5,6,7,8,9,0)

print('Given tuple is: ',tup)

min1 = []
max1 = []

tup = list(tup)

k = 2
i = 0

while i < k:
    min1.append(min(tup))
    tup.remove(min(tup))
    i = i + 1

i = 0
while i < k:
    max1.append(max(tup))
    tup.remove(max(tup))
    i = i + 1

res = min1 + max1
res.sort()

res = tuple(res)

print('The minimum',k,'and maximum', k, 'elements in the tuple are', res)

################################################################################################################

#777

'''
Using a loop and two lists
'''

tup = (5,20,3,7,6,8)
k = 2

max_k_elements = []
min_k_elements = []

for elem in tup:
    max_k_elements.append(elem)
    max_k_elements.sort(reverse=True)
    if len(max_k_elements) > k:
        max_k_elements.pop()

    min_k_elements.append(elem)
    min_k_elements.sort()
    if len(min_k_elements) > k:
        min_k_elements.pop()

print('Maximum',k,'elements:', max_k_elements)
print('Minimum',k, 'elements:',min_k_elements)

##################################################################################################################




































































































































































































