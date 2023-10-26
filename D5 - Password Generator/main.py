import string
import random

print('Welcome to Pyssword Generator!')

num_of_letters = int(input('How many letters you want? '))
num_of_numbers = int(input('How many numbers you want? '))
num_of_symbols = int(input('How many symbols you want? '))

letters = string.ascii_letters
symbols = [chr(i) for i in range(33, 48)] # ascii 33-47
numbers = [chr(i) for i in range(48, 58)] # ascii 48-57

# generate letters
random_letters = ''.join(random.choices(letters, k=num_of_letters))

# generate numbers
random_numbers = ''.join(random.choices(numbers, k=num_of_numbers))

# generate symbols
random_symbols = ''.join(random.choices(symbols, k=num_of_symbols))

password = random_letters + random_numbers + random_symbols

password_randomized = ''.join(random.sample(password, len(password)))

print(f"Your password is {password_randomized}")
