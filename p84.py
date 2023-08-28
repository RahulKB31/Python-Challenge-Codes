<<<<<<< HEAD
#602

'''
Generating random strings until a given string is generated
'''

import string
import random
import time

#all possible characters including lowercase, uppercase and special symbols
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + '., !?;:'

# string to be generated
t = 'geek'

attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(t)))

attemptNext = ''

completed = False
iteration = 0

while completed == False:
    print(attemptThis)

    attemptNext = ''
    completed = True

    # Fix the index if matches with the strings to be generated
    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += t[i]

iteration += 1
attemptThis = attemptNext
time.sleep(0.1)

print("Target matched after" + str(iteration) + " iterations")

##############################################################################################################






























































































































































































































=======
#602

'''
Generating random strings until a given string is generated
'''

import string
import random
import time

#all possible characters including lowercase, uppercase and special symbols
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + '., !?;:'

# string to be generated
t = 'geek'

attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(t)))

attemptNext = ''

completed = False
iteration = 0

while completed == False:
    print(attemptThis)

    attemptNext = ''
    completed = True

    # Fix the index if matches with the strings to be generated
    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += t[i]

iteration += 1
attemptThis = attemptNext
time.sleep(0.1)

print("Target matched after" + str(iteration) + " iterations")

##############################################################################################################






























































































































































































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
