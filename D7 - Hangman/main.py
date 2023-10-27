import random

words = ['salutation', 'reverence', 'pulvarize']

# choose random word
chosen_word = random.choice(words)

# ask user to guess a letter
guess = input('Guess a letter: ').lower()

for letter in chosen_word:
    if letter == guess:
        print('Present')
    else:
        print('Absent')