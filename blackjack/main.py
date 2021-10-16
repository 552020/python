import random
from art import logo 
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_is_on = True
player_cards = []
current_score_player = 0
dealer_cards = []
current_score_dealer = 0
new_card = 0

def init_new_game():
	global player_cards
	global current_score_player
	global dealer_cards
	global current_score_dealer
	global game_is_on
	player_cards = []
	current_score_player = 0
	dealer_cards = []
	current_score_dealer = 0
	game_is_on = True

def draw_new_card(player):
		global new_card
		new_card = random.choice(cards)
		if (player == 'player'):
			player_cards.append(new_card)
			global current_score_player
			current_score_player = sum(player_cards)
			if (len(player_cards) > 1 and len(player_cards) < 3):
				print(f'Your cards are {player_cards} and your current score is {current_score_player}.')
			
		if (player == 'dealer'):
			dealer_cards.append(new_card)
			global current_score_dealer
			current_score_dealer = sum(dealer_cards)

def check_sum(player):
	global game_is_on
	global new_card
	if (player == 'player'):
		if (current_score_player <= 21):
			print(f'The new card you draw is a {new_card}. Your cards are {player_cards} and your current score is {current_score_player}.')	
			
		elif((current_score_player > 21) and (11 in player_cards)):
			player_cards[player_cards.index(11)] = 1
			print(f'The new card you draw is a {new_card}. Your cards are {player_cards} and your current score is {current_score_player}.')
		else:
			print(f'The new card you draw is a {new_card}. Your score is {current_score_player}. You lose. ')
			game_is_on = False
			
	if (player == 'dealer'):
		if (current_score_dealer <= 21):
			print(f'Your score: {current_score_player} - Computer score: {current_score_dealer}')
			
		elif((current_score_dealer > 21) and (11 in player_cards)):
			dealer_cards[dealer_cards.index(11)] = 1
		else:
			print(f'Computer\'s score is {current_score_dealer}. You won. ')
			game_is_on = False

def has_blackjack():
	global game_is_on
	global current_score_dealer
	global current_score_player
	if (current_score_dealer == 21):
		print("Computer has blackjack. You lose.")
		game_is_on = False
		return True
	if (current_score_player == 21 and current_score_dealer < 21):
		print("You have blackjack. You win.")
		game_is_on = False
		return True

def dealer_turn():
	global game_is_on
	if (current_score_dealer < 17):
		draw_new_card('dealer')
		if game_is_on: 
			check_sum('dealer')
	if (current_score_dealer >= 17 and current_score_dealer <= 21):
		print('Dealer is good.')

def check_scores():
	if (current_score_player > current_score_dealer):
		print(f'Your score: {current_score_player} - Computer score: {current_score_dealer}. You win.')
	elif (current_score_player == current_score_dealer):
		print(f'Your score: {current_score_player} - Computer score: {current_score_dealer}. It\'s a tie.')
	else: 
		print(f'Your score: {current_score_player} - Computer score: {current_score_dealer}. You lose.')
	global game_is_on
	game_is_on = False

def play_blackjack():
	global game_is_on
	should_continue = True
	while should_continue:
		init_new_game()
		should_continue_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
		if (should_continue_input == 'n' ):
			break
		draw_new_card('player')
		draw_new_card('player')
		draw_new_card('dealer')
		draw_new_card('dealer')
		print(f'Computer\'s first card: {dealer_cards[0]} ' )
		print(f'Secret hint: Current score player: {current_score_player} - Current score computer:  {current_score_dealer}')
		if has_blackjack():
			return
		
		while game_is_on:
			should_get_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
			if (should_get_new_card == 'y'):
				draw_new_card('player')
				if has_blackjack():
					return
				check_sum('player')
				if game_is_on:
					dealer_turn()
			if (should_get_new_card == 'n'):
				dealer_turn()
				if has_blackjack():
					return
				if game_is_on:
					check_scores()

play_blackjack()