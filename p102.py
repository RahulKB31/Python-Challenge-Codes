<<<<<<< HEAD
#689

'''
Ways to sort list of dictionaries by values in Python - Using itemgeter
'''

from operator import itemgetter

list = [{"name": "Nandini", "age":20},
        {"name":"Manjeet", "age":20},
        {"name":"Nikhil", "age":19}]

print("The list printed sorting by age: ")
print(sorted(list, key=itemgetter('age')))

print("\r")

print("The list printed sorting by age and name: ")
print(sorted(list, key = itemgetter('age','name')))

print("\r")

print("The list printed sorting by age in descending order:")
print(sorted(list, key = itemgetter('age'),reverse=True))

=======
#689

'''
Ways to sort list of dictionaries by values in Python - Using itemgeter
'''

from operator import itemgetter

list = [{"name": "Nandini", "age":20},
        {"name":"Manjeet", "age":20},
        {"name":"Nikhil", "age":19}]

print("The list printed sorting by age: ")
print(sorted(list, key=itemgetter('age')))

print("\r")

print("The list printed sorting by age and name: ")
print(sorted(list, key = itemgetter('age','name')))

print("\r")

print("The list printed sorting by age in descending order:")
print(sorted(list, key = itemgetter('age'),reverse=True))

>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
################################################################################################################