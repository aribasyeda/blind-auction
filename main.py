from replit import clear
from art import logo

print(logo)

print("✨ Welcome to the silent auction program! ✨\n")

bids = {}

bidding_finished = False

while not bidding_finished:
  
  name = input("👉 What is your name? \n")
  bid = int(input("👉 What is your bid in £? \n"))
  
  bids.update({name : bid})
  
  user_choice = input("❓ Are there any other bidders? Type 'yes or 'no'\n").lower()
  
  if user_choice == "yes":
    clear()
    
  elif user_choice == "no":
    clear()
    bidding_finished = True
    
    winner = max(bids, key=bids.get)
    highest_bid = bids[winner]
    
    print(f"The winner is {winner} with a bid of £{highest_bid}.")
