import data


def input_coins(coin):
    while True:
        try:
            if 0 <= (coins := int(input(f"How many {coin}?: "))):
                return coins
            print("That is not valid.")
        except ValueError:
            print("That is not valid.")


def input_coffee_choice():
    while True:
        selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if selection not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
            print("Not a valid selection.")
        else:
            return False if selection == 'off' else selection


def check_sufficient_resources(selection):
    # check every ingredient in the selected coffee against how many of that ingredient we have in the machine
    for ing in data.MENU[selection]['ingredients']:
        if not data.resources[ing] >= data.MENU[selection]['ingredients'][ing]:
            print(f"Sorry there is not enough {ing}.")
            return False
    return True


def report():
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g")
    print(f"Profit: {data.resources['profit']}")


def insert_money():
    money_inserted = 0
    money_inserted += input_coins('quarters') * 0.25
    money_inserted += input_coins('dimes') * 0.1
    money_inserted += input_coins('nickles') * 0.5
    money_inserted += input_coins('pennies') * 0.01
    return float(format(money_inserted, '.2f'))


def make_coffee(selection):
    for ing in data.MENU[selection]['ingredients']:
        data.resources[ing] -= data.MENU[selection]['ingredients'][ing]
    return selection


def main():
    while selection := input_coffee_choice():
        if selection == 'report':
            report()
            continue

        if not check_sufficient_resources(selection):
            continue

        cost = data.MENU[selection]['cost']
        if not (money_inserted := insert_money()) >= cost:
            print("Sorry that's not enough money. Money refunded.")
            continue
        else:
            print(f"Here is ${format(money_inserted - cost, '.2f')} dollars in change.")
        data.resources['profit'] += cost

        print(f"Here is your {make_coffee(selection)}. Enjoy!")


if __name__ == "__main__":
    main()
