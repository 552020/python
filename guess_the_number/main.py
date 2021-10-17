#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)
should_continue = True
def play_game():

	print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100. You have to guess this number.')
	attempts = 0
	the_number = random.randint(1, 100)
	game_is_over = False

	def check_answer(user_guess_ca, the_number_ca): 
		if (user_guess_ca == the_number_ca):
			return True
			
		if (user_guess_ca != the_number_ca):
			# return attempts - 1
			return False
		

	while (attempts == 0):
		difficulty_input = input("Choose a difficulty. Type 'easy' or 'hard': ")

		if (difficulty_input == 'easy'):
			attempts = 10
		elif (difficulty_input == 'hard'):
			attempts = 5
		else: 
			("The entered value was invalid: please choose between 'easy' and 'hard'")

	while not game_is_over:
		user_guess = int(input('Make a guess: '))
		if check_answer(user_guess, the_number):
			print('Got it. You win!')
			# game_is_over = True
			break
		if not check_answer(user_guess, the_number):
			attempts -= 1
			if attempts == 0:
				print('Wrong guess: You lose.')
				# game_is_over = True
				break
			if (user_guess > the_number):
				print('Too high!')		
			if (user_guess < the_number):
				print('Too low!')


	play_again = input("Wanna play again? Enter 'y' or 'n' ")
	if (play_again == 'y'):
		play_game()
	else:
		global should_continue
		should_continue = False
		print('Goodbye.')

while should_continue:
	play_game()	