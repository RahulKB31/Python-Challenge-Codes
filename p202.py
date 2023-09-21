#955

'''
how to obtain the line number in which given word is present using python
'''

# Get line number in which the given word is present through iteration

def find_word_line_number(filename, target_word):
    line_number = 0
    with open(filename,'r') as file:
        for line in file:
            line_number += 1
            if target_word in line:
                return line_number

    # if word is not found in the file return none
    return none

filename = 'file.txt'
word_to_find = 'hello'
line_number = find_word_line_number(filename, word_to_find)
if line_number is not None:
    print(f"The word '{word_to_find}' is present in line number: {line_number}")
else:
    print(f"THe word '{word_to_find}' is not found in the file")

####################################################################################################################

#956

'''
Obtain the line number in which the given word is present through enumerate
'''

def find_word_in_file(file_path,target_word):
    try:
        with open(file_path,'r') as file:
            for line_number, line in enumerate(file, start=1):
                if target_word in line:
                    return line_number

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occured: {e}")
    return None

file_path = "file.txt"
word_to_find = "Abhishekh"
result = find_word_in_file(file_path,word_to_find)
if result:
    print(f"The word {word_to_find} was found in the line number: {result}")
else:
    print(f"The word {word_to_find} was not found in the file")

###################################################################################################################