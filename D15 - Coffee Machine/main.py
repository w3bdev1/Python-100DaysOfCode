from menu import MENU

flavours: list[str] = ['espresso', 'latte', 'cappuccino']

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def is_sufficient(flavour):
    for ingredient, required_amount in MENU[flavour]["ingredients"].items():
        if required_amount > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Insert coins.")
    q = int(input("Quarters: "))
    d = int(input("Dimes: "))
    n = int(input("Nickel: "))
    p = int(input("Pennies: "))
    return q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01


def is_successful_transaction(money_supplied, flavour):
    price = MENU[flavour]["cost"]
    if money_supplied < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_supplied > price:
        print(f"Here is ${money_supplied - price:.2f} dollars in change. ")
        return True
    else:
        return True


def make_coffee(flavour):
    for ingredient, required_amount in MENU[flavour]["ingredients"].items():
        resources[ingredient] -= required_amount

    global money
    money += MENU[flavour]["cost"]

    print(f"Here is your {flavour}. Enjoy!")


turned_off = False
while not turned_off:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        report()
    elif user_input == "off":
        print("Turning it off.")
        turned_off = True
    elif user_input not in flavours:
        print("Invalid input!")
    elif is_sufficient(user_input):
        money_given = process_coins()
        if is_successful_transaction(money_given, user_input):
            make_coffee(user_input)
