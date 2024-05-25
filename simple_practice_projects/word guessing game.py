import random

words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']
word = random.choice(words)
letter = random.choice(word[int(len(word)/2)])
for char in word:
    if char == letter:
        print(char, end = '')
    else:
        print('_')