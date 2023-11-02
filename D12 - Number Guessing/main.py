import random
from ascii_art import logo

# Intialize
numbers = list(range(1,101))
print(logo)
print("Welcome to number guesser!")

# Pick number
print("I'm thinking of a number between 1 and 100")
correct_number = random.choice(numbers)
# print(f"Correct number: {correct_number}")

# Set difficulty
attempts = 0
difficulty = input("Choose difficulty level. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Invalid difficulty level!")

print(f"{difficulty.title()} difficulty: {attempts} attempts to guess.")

# Game Loop
while attempts > 0:
    guess = int(input("Your guess: "))

    if guess == correct_number:
        print(f"You got it! Answer was {correct_number}")
        break
    elif guess > correct_number:
        print(f"Too high")
        attempts -= 1
    elif guess < correct_number:
        print(f"Too low")
        attempts -= 1
    
    if attempts > 0:
        print(f"You've {attempts} attempt(s) to guess.")
    else:
        print('You\'ve run out of guesses. You lose.')