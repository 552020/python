MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def check_resources(drink):
    missing_resources = []
    if resources['water'] < MENU[drink]['ingredients']['water']:
        missing_resources.append('water')
    if resources['milk'] < MENU[drink]['ingredients']['milk']:
        missing_resources.append('milk')
    if resources['coffee'] < MENU[drink]['ingredients']['coffee']:
        missing_resources.append('coffee')
    if len(missing_resources) == 1:
        print(f'Sorry, there is not enough {missing_resources[0]}.')
    if len(missing_resources) == 2:
        print(f'Sorry, there is not enough {missing_resources[0]} and {missing_resources[1]}.')
    if len(missing_resources) == 3:
        print(f'Sorry, there is not enough {missing_resources[0]}, {missing_resources[1]} and {missing_resources[2]}.')
    # print(missing_resources)
    if len(missing_resources) > 0:
        # print('False from check resources')
        return False
    else:
        return True


def insert_coin(drink):
    print(f"The {drink} costs $ {MENU[drink]['cost']}.")
    print('Please insert coins.')
    quarters = int(input('How many quarters? '))
    dims = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))
    coins_sum = quarters * 0.25 + dims * 0.1 + nickles * 0.05 + pennies * 0.01
    print(f"{round(coins_sum, 2)}")
    return round(coins_sum, 2)


def check_coins(coin_sum_f, drink):
    if coin_sum_f < MENU[drink]['cost']:
        print(f"Sorry, you've inserted only $ {coin_sum_f}. That's not enough. Money refunded")
        return False
    if coin_sum_f == MENU[drink]['cost']:
        return coin_sum_f
    if coin_sum_f > MENU[drink]['cost']:
        change = round(coin_sum_f - MENU[drink]['cost'], 2)
        print(f"You've inserted {float(coin_sum_f):.2f}: Here are $ {change:.2f} in change.")
        return coin_sum_f


def make(drink):
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['milk'] -= MENU[drink]['ingredients']['milk']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']


while True:
    choice_list = ["espresso", "latte", "cappuccino", "off", "report"]
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice not in choice_list:
            print(f"Your input '{user_choice}'(sic) is not valid. "
                  f"Please choose between 'espresso', 'latte' or 'cappuccino', or exit the program with 'off'.")
        else:
            break

    if not check_resources(user_choice):
        break
    coin_sum = insert_coin(user_choice)
    if check_coins(coin_sum, user_choice):
        money += MENU[user_choice]['cost']
        make(user_choice)
        print(f"Your {user_choice} is ready!")
    # if user_choice == "espresso":
    #     if not check_resources("espresso"):
    #         break
    #     coin_sum = insert_coin('espresso')
    #     if check_coins(coin_sum, 'espresso'):
    #         money += MENU['espresso']['cost']
    #         make('espresso')
    #         print("Your espresso is ready!")

    # if user_choice == "latte":
    #     if not check_resources("latte"):
    #         break
    #     coin_sum = insert_coin('latte')
    #     if check_coins(coin_sum, 'latte'):
    #         money += MENU['latte']['cost']
    #         make('latte')
    #         print("Your latte is ready!")
    #
    # if user_choice == "cappuccino":
    #     if not check_resources("cappuccino"):
    #         break
    #     coin_sum = insert_coin('cappuccino')
    #     if check_coins(coin_sum, 'cappuccino'):
    #         money += MENU['cappuccino']['cost']
    #         make('cappuccino')
    #         print("Your cappuccino is ready!")

    if user_choice == "off":
        print("Goodbye!")
    if user_choice == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
