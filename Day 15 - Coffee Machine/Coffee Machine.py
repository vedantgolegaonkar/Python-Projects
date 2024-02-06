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
    },
}

import os
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def process_coins():
    print("Insert the coins")
    total = int(input("How many quarter? ")) * 0.25 + int(input("How many dimes? ")) * 0.1 + int(input("How many nickel? ")) * 0.05 + int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(payment_recieved, drink_cost):
    if payment_recieved >= drink_cost:
        change = round(payment_recieved - drink_cost, 2)
        print(f"Here's your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money, Money refunded")
        return False
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your drink - {drink_name} 🍵")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Thank you 🙂")
        is_on = False
    if choice == "report":
        print(f"Water:  {resources['water']}")
        print(f"Milk:   {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money:  ${profit}")
    else:
        drink = MENU[choice]
        if resource_sufficient(drink['ingredients']):
            payment = process_coins()
            os.system("cls")
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])