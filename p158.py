<<<<<<< HEAD
#864

'''
Python program for pigeonhole sort
'''

def pigeonhole_sort(a):
    my_min = min(a)
    my_max = max(a)
    size = my_max - my_min +1

    holes = [0] * size

    for x in a:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1

a = [7,4,6,7,3,2,1,7,8,9,6]
print("Sorted order is: ", end= " ")

pigeonhole_sort(a)

for i in range(0, len(a)):
    print(a[i], end=" ")

=======
#864

'''
Python program for pigeonhole sort
'''

def pigeonhole_sort(a):
    my_min = min(a)
    my_max = max(a)
    size = my_max - my_min +1

    holes = [0] * size

    for x in a:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1

a = [7,4,6,7,3,2,1,7,8,9,6]
print("Sorted order is: ", end= " ")

pigeonhole_sort(a)

for i in range(0, len(a)):
    print(a[i], end=" ")

>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
###################################################################################################################