import random

names_str = input('Give me a list of names separated by comma: ')
names_list = names_str.split(', ')

index = random.randint(0, len(names_list) - 1)
print(f"Random name: {names_list[index]}")