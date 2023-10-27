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
print(f'Chosen: {chosen_word}')

# dashed chars
dashed_chars = ['_' for _ in range(len(chosen_word))]
print(dashed_chars)

# check lives
lives_used = 0
max_lives = len(stages) - 1

# ask user to guess a letter
end_of_game = False

while not end_of_game:
    print(stages[lives_used])

    guess = input('Guess a letter: ').lower()
    for id, letter in enumerate(chosen_word):
        if letter == guess:
            dashed_chars[id] = letter
    
    if guess not in chosen_word:
        lives_used += 1

    print(dashed_chars)

    if '_' not in dashed_chars:
        end_of_game = True
        print('You win!')
    
    if lives_used == max_lives:
        print(stages[lives_used])
        end_of_game = True
        print('You lost!')