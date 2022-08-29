from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

count = 0
contin = 'yes'

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
latte = menu.menu[0]
espresso = menu.menu[1]
cappuccino = menu.menu[2]

while contin == 'yes':
    drink = input('What would you like? (espresso/latte/cappuccino): ')
    if drink == 'latte':
        coffee = latte
    elif drink == 'espresso':
        coffee = espresso
    elif drink == 'cappuccino':
        coffee = cappuccino
    elif drink == 'report':
        coffee_maker.report()
        money_machine.report()
        continue
    elif drink == 'off':
        print('Coffee machine stopped. Good bye!')
        break

    can_make = coffee_maker.is_resource_sufficient(coffee)
    if not can_make:
        break

    print(f'{drink} cost ${coffee.cost}')

    enough_li_money = money_machine.make_payment(coffee.cost)
    if not enough_li_money:
        break

    coffee_maker.make_coffee(coffee)

    contin = input('Do you want one more coffee? Type "yes" or "no": ').lower()
