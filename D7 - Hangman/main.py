import random
import ascii_art
import wordlist

# Initialize
print(ascii_art.logo)
stages = ascii_art.stages
words = wordlist.words

# choose random word
chosen_word = random.choice(words)

# dashed chars
dashed_chars = ['_' for _ in range(len(chosen_word))]

# check lives
lives_used = 0
max_lives = len(stages) - 1

# ask user to guess a letter
end_of_game = False

while not end_of_game:
    print(stages[lives_used])
    print(' '.join(dashed_chars))

    guess = input('\nGuess a letter: ').lower()
    for id, letter in enumerate(chosen_word):
        if letter == guess:
            dashed_chars[id] = letter
    
    if guess not in chosen_word:
        lives_used += 1

    if '_' not in dashed_chars:
        end_of_game = True
        print(' '.join(dashed_chars))
        print('You win!')
    
    if lives_used == max_lives:
        print(stages[lives_used])
        print(' '.join(dashed_chars))
        end_of_game = True
        print('You lost!')
        print(f"Correct word: {chosen_word}")