import random

words = ['salutation', 'reverence', 'pulvarize']

# choose random word
chosen_word = random.choice(words)

# dashed chars
dashed_chars = ['_' for _ in range(len(chosen_word))]
print(dashed_chars)

# ask user to guess a letter
guess = input('Guess a letter: ').lower()

for id, letter in enumerate(chosen_word):
    if letter == guess:
        dashed_chars[id] = letter

print(dashed_chars)