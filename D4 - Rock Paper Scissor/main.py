import random

# Rock Paper Scissors ASCII Art (https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe)

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

moves = [rock, paper, scissor]

user_choice_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. "))

# logic
if user_choice_index >= 3 or user_choice_index < 0:
    print("Invalid move! You lose.")
else:
    user_choice = moves[user_choice_index]

    computer_choice_index = random.randint(0, len(moves) - 1)
    computer_choice = moves[computer_choice_index]

    print("Your Move:")
    print(user_choice)
    print("")
    print("Computer's Move:")
    print(computer_choice)

    if user_choice_index == computer_choice_index:
        print("Draw")
    else:
        if user_choice_index == 0:
            ## Rock loses to paper
            if computer_choice_index == 1:
                print("Computer Wins")
            ## Rock beats scissor
            elif computer_choice_index == 2:
                print("You Win")
        if user_choice_index == 1:
            ## Paper beats rock
            if computer_choice_index == 0:
                print("You Win")
            ## Paper loses to scissot
            elif computer_choice_index == 2:
                print("Computer Wins")
        if user_choice_index == 2:
            ## Scissor loses to rock
            if computer_choice_index == 0:
                print("Computer Wins")
            ## Scissor beats paper
            elif computer_choice_index == 1:
                print("You Win")