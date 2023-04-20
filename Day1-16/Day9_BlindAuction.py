import art.blindauction_art
import os

os.system('cls')

add_another = "y"
all_bids = {}
welcome = "*** !!! Welcome to the Blind Auction!! ***"

while add_another == "y":
  print(f"{blindauction_art.logo}\n{welcome}")
  name = input("\nWhat is your name?: ")
  bid = int(input(f"\nWhat is your bid, {name}?: €"))
  all_bids[name] = bid
  add_another = input("\nDo you want to add another bidder, y or n?: ")
  os.system('cls')

highest_bid = 0
highest_bidder = ""

for name in all_bids:
  if all_bids[name] > highest_bid:
    highest_bid = all_bids[name]
    highest_bidder = name

print(f"{blindauction_art.logo}\n{welcome}")
print(f"\nThe winner with a bid of €{highest_bid}, is {highest_bidder}. Congratulations!!\n")