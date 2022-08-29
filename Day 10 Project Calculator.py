# def format_name(f_name, l_name):
#     return f_name.title() + ' ' + l_name.title()
#
#
# bd = format_name('DIMA', 'borOdin')
# print(bd)

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print(logo)

decision = ''

num1 = float(input('Enter the first number '))

while decision != 'x':

    for operation in operations:
        print(operation)

    operation_symbol = input('Pick an operation from the lines above ')

    num2 = float(input('Enter the next number '))

    answer = operations[operation_symbol](num1, num2)
    print(f'{num1} {operation_symbol} {num2} = {answer}')

    decision = input(f'Type "y" to continue calculating with {answer}, type "n" to start a new calculation or'
                     f' type "x" to finish all calculations: ')

    if decision == 'n':
        num1 = float(input('Enter the first number '))
        continue
    elif decision == 'y':
        num1 = answer
    else:
        print('Good bye!')
