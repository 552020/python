from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
    account_name = account_a['name']
    account_descr = account_a['description']
    account_country = account_a['country']
    return (f' {account_name}, a {account_descr}, from {account_country} ')

def check_answer(guess, a_followers, b_followers):
    """" Take the user guess and follower counts and returns if they got it right """
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b' 

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)



    print("Compare A: {format_data(account_a)}")
    print(vs)
    print("Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else: 
        game_should_continue = False
        print (f"Sorry, that's wrong. Finals score: {score}")
