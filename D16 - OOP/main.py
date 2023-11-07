from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turned_off = False
while not turned_off:
    user_input = input(f"What would you like? ({menu.get_items()}): ").lower()

    if user_input == 'off':
        turned_off = True
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if (drink is not None and
                coffee_maker.is_resource_sufficient(drink) and
                money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)
