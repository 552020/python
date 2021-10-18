from art import logo
from art import vs
import os 
from game_data import data
import random

score = 0
print(logo)

def user_is_right(score_f, logo, os):
	score_f += 1
	os.system('clear')
	print(logo)
	print(f'You\'re right. Current score: {score_f}.')
	return score_f
def user_is_wrong(os, score):
	os.system('clear')
	print(f'Sorry that\'s wrong. Final score: {score}.')


while True: 
	a_item = random.choice(data)
	b_item = random.choice(data)
	
	name_a_item = a_item['name']
	name_b_item = b_item['name']

	description_a_item = a_item['description']
	description_b_item = b_item['description']
	followers_a_item = a_item['follower_count']
	followers_b_item = b_item['follower_count']
	country_a_item = a_item['country']
	country_b_item = b_item['country']
	
	print(f'Compare A: {name_a_item}, a {description_a_item}, from {country_a_item}   ...')
	print(vs)
	print(f'Compare B: {name_b_item}, a {description_b_item}, from {country_b_item}.')
	print(f'Pssst, {name_a_item} has {followers_a_item} Million followers, {name_b_item} has {followers_b_item} Million followers.')

	user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

	if (user_choice == 'a'):
		if (followers_a_item > followers_b_item):
			score = user_is_right(score, logo, os)	
		else:
			user_is_wrong(os, score)
			break
	if (user_choice == 'b'):
		if (followers_b_item > followers_a_item):
			score = user_is_right(score, logo, os)	
		else:
			user_is_wrong(os, score)
			break

