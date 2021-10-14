import os
from art import logo


bids = {}
# bidders = []
bidding_finished = False

print(logo)

def clear():
    os.system('cls')

while not bidding_finished:
			
	name = input('What\'s your name?\n')
	price = int(input("What's your bid?\n$ "))
	should_continue = input("Are you the last bidder? [yes/no] \n")

	if should_continue == "yes":
		bidding_finished = True
	bids[name] = price
	# bidders.append(name)
		
	clear()
	# print(bids)
	# print(bidders)

print('End of the auction!')
highest_bid = 0
winner = ''
## First try with array bidders

# for bidder in bidders:
# 	print(bids[bidder])
# 	print(highest_bid)
# 	if bids[bidder] > highest_bid:
# 		highest_bid = bids[bidder] 
# 		winner = bidder

## Second try without array bidders
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder
	
print(f'The winner is {winner}')
# print(bids)