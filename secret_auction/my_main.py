
import os
from art import logo

print

secret_auction = {}
bidders = []
winner_dict = {}
winner = ''
auction_end = False

print(logo)

def clear():
    os.system('cls')

while not auction_end:
	
	def new_bid():
		
		name = input('What\'s your name?\n')
		bid = int(input("What's your bid?\n$"))
		last_bidder = input("Are you the last bidder? [yes/no] \n")

		if last_bidder == "yes":
			global auction_end
			auction_end = True
		secret_auction[name] = bid
		
		bidders.append(name)
		

	new_bid()
	clear()
	# print(secret_auction)
	# print(bidders)


print('End of the bid!')
highest_bid = 0
winner = ''
for bidder in bidders:
	print(secret_auction[bidder])
	print(highest_bid)
	if secret_auction[bidder] > highest_bid:
		highest_bid = secret_auction[bidder] 
		winner = bidder
	
	
print(f'The winner is {winner}')
# print(secret_auction)