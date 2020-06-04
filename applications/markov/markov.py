import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()



# TODO: analyze which words can follow other words
# Your code here
index = None
words = words.split()

words_that_can_follow = {}

for word in words: 
    if index is not None:
        if index not in words_that_can_follow:
            words_that_can_follow[index] = []
        words_that_can_follow[index].append(word)
    index = word



# TODO: construct 5 random sentences
# Your code here

starting_words = []

ending_word = []

for word in words: 
    if word[0].isupper() or word[0] == '"':
        starting_words.append(word)


for word in words:
    if word[-1] == '.' or word[-1] =='?' or word[-1] =='!':
        ending_word.append(word)
    elif len(word) > 1 and (word[-2] == '.' or word[-2] =='?' or word[-2] =='!'):
        ending_word.append(word)

for i in range(5):
    print(f'Sentance {i}: ')
    word = random.choice(starting_words)
    isStopped = False
    while isStopped == False:
        print(word, end=" ")
        if word not in ending_word:
            nextWord = random.choice(words_that_can_follow[word])
            word = nextWord
        else:
            isStopped = True
    print("\n")