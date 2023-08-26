#749

'''
Python Dictionary to find mirror characters in a string
'''

def mirrorChars(input, k):
    original = 'akfjhsdjkdbnljghjkndkfnbdfnbjgnb'
    reverse = 'djhvfjsghorgonfvndflgfdhgldfghldf'
    dictChars = dict(zip(original, reverse))

    # seperate out characters after length k to change characters in mirror
    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''

    #change into mirror
    for i in range(0, len(suffix)):
        mirror = mirror + dictChars[suffix[i]]

    #concat prefix and mirrored part
    print(prefix+mirror)

if __name__ == "__main__":
    input = 'paradox'
    k = 3
    mirrorChars(input,k)

#################################################################################################################