from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def input_order(menu):
    while True:
        order = input(f"What would you like? ({menu.get_items()}): ").lower()
        # unreadable code in next line creates a formatted list of all menu items and the words off and report
        if order not in menu.get_items().rsplit('/', 1)[0].split('/') + ['off', 'report']:
            print("Not a valid selection.")
        else:
            return order


def main():
    menu = Menu()
    coffee_machine = CoffeeMaker()
    money = MoneyMachine()
    while (order := input_order(menu)) != 'off':
        if order == 'report':
            coffee_machine.report()
            money.report()
            continue

        drink = menu.find_drink(order)

        if coffee_machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)

        print('')


if __name__ == '__main__':
    main()
