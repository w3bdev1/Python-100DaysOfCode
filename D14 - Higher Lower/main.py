import random
data = __import__('game-data').data
from art import logo, vs

# Pick 2 random person
persons = random.choices(data, k=2)
print(f"A: {persons[0]}")
print(f"B: {persons[1]}")

# Print out their details
print(f"""
Compare A: {persons[0]['name']} -- {persons[0]['description']} from {persons[0]['country']}
{vs}
Against A: {persons[1]['name']} -- {persons[1]['description']} from {persons[1]['country']}
"""
)

# User chooses
user_choice = input("Who has more followers? Type 'A' or 'B': ")

if user_choice == 'A':
    choice_index = 0
else:
    choice_index = 1

# If wrong game ends

# If right, 2nd choice become 1st and pick another random choice

def user_won():
    other_index = 1 if choice_index == 0 else 0
    choice_follower_count = persons[choice_index]['follower_count']
    other_follower_count = persons[other_index]['follower_count']
    return choice_follower_count > other_follower_count

if user_won():
    print("You win")
else:
    print("You lose!")

# Repeat