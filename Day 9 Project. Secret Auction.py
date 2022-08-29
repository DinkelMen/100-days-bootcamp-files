from replit import clear
print('Welcome to the secret auction program.')
dictant = {}

should_continue = True
while should_continue:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    dictant[bid] = name
    mex = max(dictant.keys())
    name = dictant[mex]

    restart = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if restart == "no":
        should_continue = False
    clear()
print(f'The winner is {name} with a bid of ${mex}')

