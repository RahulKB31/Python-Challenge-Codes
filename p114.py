<<<<<<< HEAD
#734

'''
Print anagrams together in Python using list and Dictionary
'''

def allAnagram(input):

    dict = {}

    for strVal in input:

        key = "".join(sorted(strVal))

        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key] = []
            dict[key].append(strVal)

    output = ""
    for key,value in dict.items():
        output = output + ' '.join(value) + ' '

    return output

if __name__ == "__main__":
    input = ['cat','dog','tac','god','act']
    print(allAnagram(input))

=======
#734

'''
Print anagrams together in Python using list and Dictionary
'''

def allAnagram(input):

    dict = {}

    for strVal in input:

        key = "".join(sorted(strVal))

        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key] = []
            dict[key].append(strVal)

    output = ""
    for key,value in dict.items():
        output = output + ' '.join(value) + ' '

    return output

if __name__ == "__main__":
    input = ['cat','dog','tac','god','act']
    print(allAnagram(input))

>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
#############################################################################################################