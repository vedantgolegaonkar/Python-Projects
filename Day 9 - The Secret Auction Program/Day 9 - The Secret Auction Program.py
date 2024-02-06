from art import logo
import os
print(logo)

bid ={}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner =""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid amount of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid price?: $"))
    bid[name] = price
    should_continue = input("Are there any other bidders? ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bid)
    elif should_continue == "yes":
        os.system('cls')