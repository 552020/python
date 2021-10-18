MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "espresso":
        if not check_resources("espresso"):
            break
        coin_sum = insert_coin('espresso')
        if check_coins(coin_sum, 'espresso'):
            money += MENU['espresso']['cost']
            make('espresso')
            print("Your espresso is ready!")

    if choice == "latte":
        if not check_resources("latte"):
            break
        coin_sum = insert_coin('latte')
        if check_coins(coin_sum, 'latte'):
            money += MENU['latte']['cost']
            make('latte')
            print("Your latte is ready!")

    if choice == "cappuccino":
        if not check_resources("cappuccino"):
            break
        coin_sum = insert_coin('cappuccino')
        if check_coins(coin_sum, 'cappuccino'):
            money += MENU['cappuccino']['cost']
            make('cappuccino')
            print("Your cappuccino is ready!")

    if choice == "off":
        is_on = False
        print("Goodbye!")
    if choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}") 
