import random
import ascii_art

cards = {
    'A': 11,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

# Initialize
print(ascii_art.logo)

# Choose 2 card for player
player_cards = random.choices(list(cards.keys()), k=2)
print(f"Your hand: {player_cards}")

# Choose 1 card for computer
computer_cards = random.choices(list(cards.keys()), k=1)
print(f"Opponent's hand: {computer_cards}")

# Check value in hand
def calculate_hand(cards_in_hand):
    total = 0
    for card in cards_in_hand:
        total += cards[card]
    return total
def calculate_player_hand():
    return calculate_hand(player_cards)
def calculate_computer_hand():
    return calculate_hand(computer_cards)

# Check result
def result():
    player_hand = calculate_player_hand()
    computer_hand = calculate_computer_hand()
    print(f"Result: Your hand - {player_hand}, Opponent's hand - {computer_hand}")
    if player_hand > 21:
        print("You lose!")
    elif player_hand == computer_hand:
        print("Draw!")
    elif computer_hand == 21:
        print("You lose!")
    elif computer_hand > 21 or player_hand == 21:
        print("You win!")
    elif player_hand > computer_hand:
        print("You win!")
    else:
        print("You lose!")

# New card for player
end_of_pick = False
while not end_of_pick:
    picks_another = input('Do you want to pick another card? [y/n] ').lower()
    if picks_another == 'y':
        player_cards.append(random.choice(list(cards.keys())))
        print(f"Your hand: {player_cards}")
    else:
        end_of_pick = True
        break
    
    if calculate_player_hand() >= 21:
        end_of_pick = True

# New card for computer
if calculate_player_hand() <= 21:
    while calculate_computer_hand() < 21:
        computer_cards.append(random.choice(list(cards.keys())))
    print(f"Opponent's hand: {computer_cards}")

result()
    
