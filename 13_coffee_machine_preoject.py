MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def is_resource_suffecient(drink_inggrdients):
    for item in drink_inggrdients:
        if drink_inggrdients[item]>resources[item]:
            print(f"Sorryb there ois no {item}")
            return False
    return True

def process_coins():
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))

    quarters_in_dollar = quarters * 0.25
    dimes_in_dollar = dimes * 0.10
    nickels_in_dollar = nickels * 0.05
    pennies_in_dollar = pennies * 0.01

    total_user_money = quarters_in_dollar + dimes_in_dollar + nickels_in_dollar + pennies_in_dollar
    return total_user_money

def is_transaction_succesfull(total_user_money,drink_cost):
    if total_user_money>=drink_cost:
        balance_money=total_user_money-drink_cost
        print(f"ahere is your change:{balance_money:.2f}💲")
        resources["money"]+=drink_cost
        return True
    else:
        print(f"Sorry that's not enough money.Money refunded{total_user_money}💲")
        return False
def make_coffe(drink_name,drink_ingredients):
    for item in drink_ingredients:
        resources[item]-=drink_ingredients[item]
    print(f"Here is your {drink_name}☕.Enjoy!")

def restock(ingredient_name):
    amount = int(input(f"How much {ingredient_name} to add?: "))
    resources[ingredient_name] += amount
    print(f"Restock has done successfully {resources[ingredient_name]} of {ingredient_name}.")
machine_on=True

while machine_on:
    user=input("What would you like to have? ( espresso / latte/ cappuccino):").lower()

    if user=="off":
        machine_on=False
        print("Coffee machione turned off.")
    
    elif user == "water" or user == "milk" or user == "coffee":
        restock(user)

    elif user=="report":
        print(f"coffee:{resources['coffee']}\nwater:{resources['water']}\nmilk:{resources['milk']}\nmoneyt:{resources['money']}")
    
    elif user=="espresso" or user=="latte" or user=="cappuccino":
        drink=MENU[user]

        if is_resource_suffecient(drink["ingredients"]):
            total_user_money=process_coins()

            if is_transaction_succesfull(total_user_money,drink["cost"]):
                make_coffe(user,drink["ingredients"])
