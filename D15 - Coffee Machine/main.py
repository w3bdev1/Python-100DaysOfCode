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


user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

if user_input == report:
    report()