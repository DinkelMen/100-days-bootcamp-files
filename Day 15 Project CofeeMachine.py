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

# print(MENU["latte"]['cost']) -> 2.5

water = 300
milk = 200
coffee = 100
money = 0


def report():
    print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}')


def insert_coins():
    print('Please insert coins.')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))
    sum_value = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return sum_value


count = 0
contin = 'yes'

while contin == 'yes':
    wish = input('What would you like? (espresso/latte/cappuccino): ')

    if wish == 'report':
        report()
        continue

    if wish == 'off':
        print('Coffee machine stopped. Good bye!')
        break

    for i in MENU[wish]['ingredients']:
        if i == 'water' and MENU[wish]['ingredients'][i] > water:
            print('Sorry, there is not enough water.')
            count += 1
        elif i == 'coffee' and MENU[wish]['ingredients'][i] > coffee:
            print('Sorry, there is not enough coffee.')
            count += 1
        elif i == 'milk' and MENU[wish]['ingredients'][i] > milk:
            print('Sorry, there is not enough milk.')
            count += 1

    if count != 0:
        break

    print(f'{wish} cost = ${MENU[wish]["cost"]}')

    inserted_coins = insert_coins()

    if inserted_coins < MENU[wish]['cost']:
        print(f'Not enough money. Here is your money back {round(inserted_coins, 2)}.')
        break
    else:
        if inserted_coins == MENU[wish]['cost']:
            print(f'Here is your {wish}. Enjoy it)')
        else:
            print(f'Here is your {wish}. Enjoy it)')
            change = round((inserted_coins - MENU[wish]["cost"]), 2)
            print(f'Here is ${change} in change')

    water -= MENU[wish]['ingredients']['water']
    coffee -= MENU[wish]['ingredients']['coffee']
    if 'milk' in MENU[wish]['ingredients']:
        milk -= MENU[wish]['ingredients']['milk']
    money += MENU[wish]['cost']

    contin = input('Do you want one more coffee? Type "yes" or "no": ').lower()
