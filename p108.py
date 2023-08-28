<<<<<<< HEAD
#708

'''
Dictionary and counter in Python to find winner of election
'''

from collections import Counter

def winner(input):

    votes = Counter(input)
    dict = {}

    for value in votes.values():
        dict[value] = []

    for (key,value) in votes.items():
        dict[value].append(key)

    maxVote = sorted(dict.keys(), reverse=True)[0]

    if len(dict[maxVote]) > 1:
        print(sorted(dict[maxVote])[0])
    else:
        print(dict[maxVote][0])

if __name__ == "__main__":
    input = ['john','johnny','jackire','johnny','john','john']
    winner(input)

################################################################################################################

#709

from collections import Counter

votes = ['john','johnny','jackire','johnny','john','john']

vote_count = Counter(votes)

max_votes = max(vote_count.values())

lst = [i for i in vote_count.keys() if vote_count[i] == max_votes]

print(sorted(lst)[0])

###################################################################################################################



































































=======
#708

'''
Dictionary and counter in Python to find winner of election
'''

from collections import Counter

def winner(input):

    votes = Counter(input)
    dict = {}

    for value in votes.values():
        dict[value] = []

    for (key,value) in votes.items():
        dict[value].append(key)

    maxVote = sorted(dict.keys(), reverse=True)[0]

    if len(dict[maxVote]) > 1:
        print(sorted(dict[maxVote])[0])
    else:
        print(dict[maxVote][0])

if __name__ == "__main__":
    input = ['john','johnny','jackire','johnny','john','john']
    winner(input)

################################################################################################################

#709

from collections import Counter

votes = ['john','johnny','jackire','johnny','john','john']

vote_count = Counter(votes)

max_votes = max(vote_count.values())

lst = [i for i in vote_count.keys() if vote_count[i] == max_votes]

print(sorted(lst)[0])

###################################################################################################################



































































>>>>>>> 411c1dae0476b61d9837f2ef36555e5ad68e8cf4
