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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_money(cost):
    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickles = int(input("Enter the number of nickles: "))
    pennies = int(input("Enter the number of pennies: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    balance_user = total - cost
    if total > cost:
        return balance_user
    else:
        print("Not enough money,Refunded")


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


profit = 0

is_on = True
while is_on:
    user_input = input("What would you like? (Espresso,latte,cappuccino): ").lower()
    if user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_input == "cappuccino":
        drink = MENU["cappuccino"]
        if is_resource_sufficient(drink["ingredients"]):
            balance = check_money(3.0)
            if balance >= 0:
                resources['water'] -= 250
                resources['milk'] -= 100
                resources['coffee'] -= 24
                print(f"Here is your cappuccino ☕ and the balance of {round(balance, 2)},Enjoy")
                profit += 3.0
    elif user_input == "latte":
        drink = MENU["latte"]
        if is_resource_sufficient(drink["ingredients"]):
            balance = check_money(2.5)
            if balance >= 0:
                resources['water'] -= 200
                resources['milk'] -= 150
                resources['coffee'] -= 24
                print(f"Here is your latte ☕ and the balance of {round(balance, 2)},Enjoy")
                profit += 2.5
    elif user_input == "espresso":
        drink = MENU["espresso"]
        if is_resource_sufficient(drink["ingredients"]):
            balance = check_money(1.5)
            if balance >= 0:
                resources['water'] -= 50
                resources['coffee'] -= 18
                print(f"Here is your coffee ☕ and the balance of {round(balance, 2)},Enjoy")
                profit += 1.5

    elif user_input == "exit":
        is_on = False
    else:
        print("Invlaid Input")
