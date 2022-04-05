import math

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


def check_resources(drink):
    water_needed = MENU[drink]["ingredients"]["water"]
    coffee_needed = MENU[drink]["ingredients"]["coffee"]
    if water_needed < resources["water"] and coffee_needed < resources["coffee"]:
        if drink == 'latte' or drink == 'cappuccino':
            milk_needed = MENU[drink]["ingredients"]["milk"]
            if milk_needed < resources["milk"]:
                return True
        else:
            return True
    else:
        return False


def calculate_coins(quarter, dime, nickel, penny):
    quarter_total = .25 * quarter
    dime_total = .1 * dime
    nickel_total = .05 * nickel
    penny_total = .01 * penny
    return round((quarter_total + dime_total + nickel_total + penny_total), 2)


def check_funds(coins, drink):
    if coins >= MENU[drink]["cost"]:
        return True
    else:
        return False


def make_change(coins, drink):
    return coins - MENU[drink]["cost"]


#def make_drink(drink):



# TODO: 1. Prompt user "what would you like (espresso/latte/cappuccino):"
order = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 2. Turn off coffee machine at prompt - ends execution
# TODO: 3. Print report of resources (water, milk, coffee, money) when prompted
#if order == 'off':
    #exit()
#elif order == 'report':
    #print(f"Water: {} \nCoffee: {} \nMilk: {} \nMoney: {}")
# TODO: 4. After order, check available resources
if not check_resources(order):
    print(f"Sorry there is not enough X")
# TODO: 5. if not enough resources, print message "Sorry there is not enough X"
# TODO: 6. Prompt user to enter coins (quarters, dimes, nickels, pennies)
else:
    print("Please enter coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    #print(f"{quarters}, {nickels}, {dimes}, {pennies}")
# TODO: 7. Calculate value of all coins entered (function) - fix missing trailing 0
    total = calculate_coins(quarters, dimes, nickels, pennies)
    print(f"${total:.2f}")
# TODO: 8. Check if user has entered enough money "Sorry that's not enough money. Money refunded."
    if not check_funds(total, order):
            print("Sorry that's not enough money. Money refunded.")
    else:
        resources["money"] = MENU[order]["cost"]
        #print(resources)
# TODO: 9. Cost of drink added to machine total
# TODO: 10. Change calculated "Here is X dollars in change." rounded to 2 decimals. (function)
        change = make_change(total, order)
        print(f"Here is ${change:.2f} dollars in change.")
# TODO: 11. Make drink by deducting the resources form the machine (function)
        
# TODO: 12. Print "Here is your X. Enjoy!" and coffee emoji
print(f"Here is your {order}. Enjoy!")
# TODO: 13. Cycle back to order prompt. (while)
