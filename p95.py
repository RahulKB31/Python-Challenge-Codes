<<<<<<< HEAD
#657

'''
String slicing in Python to check if a string can become empty by recursive deletion
'''

def checkEmpty(input, pattern):

    if len(input) == 0 and len(pattern) == 0:
        return 'true'

    if len(pattern) == 0:
        return 'false'

    while (len(input) != 0):
        index = input.find(pattern)
        if (index ==(-1)):
            return 'false'

        input = input[0:index] + input[index + len(pattern):]

    return 'true'

if __name__ == "__main__":
    input = "GEEGEEKSKS"
    pattern = "GEEKS"
    print(checkEmpty(input, pattern))
=======
#657

'''
String slicing in Python to check if a string can become empty by recursive deletion
'''

def checkEmpty(input, pattern):

    if len(input) == 0 and len(pattern) == 0:
        return 'true'

    if len(pattern) == 0:
        return 'false'

    while (len(input) != 0):
        index = input.find(pattern)
        if (index ==(-1)):
            return 'false'

        input = input[0:index] + input[index + len(pattern):]

    return 'true'

if __name__ == "__main__":
    input = "GEEGEEKSKS"
    pattern = "GEEKS"
    print(checkEmpty(input, pattern))
>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
    