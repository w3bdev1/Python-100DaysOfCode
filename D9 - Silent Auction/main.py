import os
import ascii_art

# Initialize
print(ascii_art.logo)
print("Welcome to Silent Auction!")
bids = {}

def add_bidding():
    name = input("What's your name? ").strip()
    bid_amount = int(input("What's your bid? ₹").strip())
    bids[name] = bid_amount

def find_highest_bidder():
    highest_bid, highest_bidder = max((v, k) for k, v in bids.items())
    print(f"The winner is {highest_bidder} with a bid of ₹{highest_bid}!")

end_of_bid = False
while not end_of_bid:
    add_bidding()
    again = input("Are there any more bidders? [y/n]: ").strip().lower()
    if again == 'n':
        end_of_bid = True
    os.system("clear")

find_highest_bidder()