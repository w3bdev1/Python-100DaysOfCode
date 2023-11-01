import random

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

# Choose 2 card for player
player_cards = random.choices(list(cards.keys()), k=2)

# Choose 1 card for computer
computer_cards = random.choices(list(cards.keys()), k=1)