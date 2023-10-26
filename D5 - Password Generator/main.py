import string
import random

print('Welcome to Pyssword Generator!')

num_of_letters = int(input('How many letters you want? '))
num_of_numbers = int(input('How many numbers you want? '))
num_of_symbols = int(input('How many symbols you want? '))

letters = string.ascii_letters
numbers = list(range(0,10))
symbols = [chr(i) for i in range(33, 48)] # ascii 33-47

password = ''

# generate letters
for x in range(num_of_letters):
    letter_index = random.randint(0, len(letters) - 1)
    password += letters[letter_index]

# generate numbers
for x in range(num_of_numbers):
    numbers_index = random.randint(0, len(numbers) - 1)
    password += str(numbers[numbers_index])

# generate symbols
for x in range(num_of_symbols):
    symbols_index = random.randint(0, len(symbols) - 1)
    password += symbols[symbols_index]

password_randomized = ''.join(random.sample(password, len(password)))

print(f"Your password is {password_randomized}")
