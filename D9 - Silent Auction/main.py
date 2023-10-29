import os
bids = {}

def add_bidding():
    name = input("What's your name? ").strip()
    bid_amount = int(input("What's your bid? ₹").strip())
    bids[name] = bid_amount

def find_highest_bidder():
    highest_bid = 0
    highest_bidder = ""

    for bidder, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder

    print(f"The winner is {highest_bidder} with a bid of ₹{highest_bid}!")

end_of_bid = False
while not end_of_bid:
    add_bidding()
    again = input("Are there any more bidders? [y/n]: ").strip().lower()
    if again == 'n':
        end_of_bid = True
    os.system("clear")

find_highest_bidder()