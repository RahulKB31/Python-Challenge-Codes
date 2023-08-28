<<<<<<< HEAD
#865

'''
Python program for cocktail sort
'''

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False

        for i in range(start,end):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1],a[i]
                swapped = True

        if (swapped == False)

            break

        swapped = False
        end = end -1

        for i in range(end-1, start-1,-1):
            if (a[i]> a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        start = start + 1

a = [1,3,5,6,9,4,2,0,9,8,6,5]
cocktailSort(a)
print("Sorted array is")
for i in range(len(a)):
    print("%d" %a[i])

################################################################################################################




























































=======
#865

'''
Python program for cocktail sort
'''

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False

        for i in range(start,end):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1],a[i]
                swapped = True

        if (swapped == False):

            break

        swapped = False
        end = end -1

        for i in range(end-1, start-1,-1):
            if (a[i]> a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        start = start + 1

a = [1,3,5,6,9,4,2,0,9,8,6,5]
cocktailSort(a)
print("Sorted array is")
for i in range(len(a)):
    print("%d" %a[i])

################################################################################################################




























































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
