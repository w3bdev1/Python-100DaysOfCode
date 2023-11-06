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


user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

if user_input == "report":
    report()
elif user_input == "off":
    pass
elif (user_input in flavours) and is_sufficient(user_input):
    print(f"Creating {user_input}")
