import random
import os
data = __import__('game-data').data
from art import logo, vs

# Initialization
print(logo)
persons = random.choices(data, k=2)

def user_won(choice_id):
    other_index = 1 if choice_index == 0 else 0
    choice_follower_count = persons[choice_index]['follower_count']
    other_follower_count = persons[other_index]['follower_count']
    return choice_follower_count > other_follower_count

def print_rivalry():
    print(f"Compare A: {persons[0]['name']} -- {persons[0]['description']} from {persons[0]['country']}")
    print(vs)
    print(f"Compare B: {persons[1]['name']} -- {persons[1]['description']} from {persons[1]['country']}")

user_score = 0
end_of_game = False
while not end_of_game:
    print_rivalry()
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if user_choice == 'A':
        choice_index = 0
    else:
        choice_index = 1

    if user_won(choice_index):
        os.system('clear')
        print(logo)
        print("You're correct!")
        user_score +=1
        print(f"SCORE: {user_score}")
        persons.pop(0)
        persons.append(random.choice(data))
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")
        end_of_game = True