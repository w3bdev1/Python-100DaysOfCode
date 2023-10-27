import random

words = ['salutation', 'reverence', 'pulvarize']

# ASCII Art (https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c)

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# choose random word
chosen_word = random.choice(words)

# dashed chars
dashed_chars = ['_' for _ in range(len(chosen_word))]
print(dashed_chars)

# ask user to guess a letter
end_of_game = False

while not end_of_game:
    guess = input('Guess a letter: ').lower()

    for id, letter in enumerate(chosen_word):
        if letter == guess:
            dashed_chars[id] = letter

    print(dashed_chars)

    if '_' not in dashed_chars:
        end_of_game = True
        print('You win!')