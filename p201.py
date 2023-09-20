#952

'''
Python | Finding 'n' character words in a Text file
'''

# Finding a given word in text file using split and list comprehension

def find_words_with_three_chars(file_path):
    with open(file_path,'r') as file:
        content = file.read()
        words = content.split()

        words_with_three_chars = [word for word in words if len(word) == 3]
        return words_with_three_chars

file_name = "file1.txt"
result = find_words_with_three_chars(file_name)
print("Words containing three characters:")
print(result)

####################################################################################################################

#953

'''
Search of a given word in a text file using regular expression
'''

import re

def find_n_character_words(file_path,n):
    with open(file_path,'r') as file:
        content = file.read()

    pattern = r'\b\w{' + str(n) + r'}\b'
    words_with_n_chars = re.findall(pattern, content)

    return words_with_n_chars

file_name = 'file.txt'
n =3
result = find_n_character_words(file_name, n)

print(f"Words containing {n} characters:")
print(result)

###################################################################################################################

#954

'''
Get words containing three characters in a file using generator function
'''

def generate_n_character_words(file_path,n):
    with open(file_path,'r') as file:
        for line in file:
            for word in line.split():
                if len(word) == n:
                    yield word

file_name = "File.txt"
n = 3
result_generator = generate_n_character_words(file_name,n)

print(f"Words containing {n} characters:")
for word in result_generator:
    print(word)

##################################################################################################################