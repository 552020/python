import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
games_images = [rock, paper, scissors]

user_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')
computer_choice = str(random.randint(0,2))

if int(user_choice) > 2 or int(user_choice) < 0:
	print('You typed an invalid number. You lose.')
else: 
	print('Your choice:')
	print(games_images[int(user_choice)])
		

print('Computer chose:')
print(games_images[int(computer_choice)])

if user_choice == computer_choice:
	print('It\'s a tie')
if user_choice == '0' and computer_choice == '1':
	print('You lose.')
if user_choice == '0' and computer_choice == '2':
	print('You win.')
if user_choice == '1' and computer_choice == '0':
	print('You win.')
if user_choice == '1' and computer_choice == '2':
	print('You lose.')
if user_choice == '2' and computer_choice == '0':
	print('You lose.')
if user_choice == '2' and computer_choice == '1':
	print('You win.')

