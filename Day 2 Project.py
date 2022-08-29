
""" Tip calculator"""

print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill? $'))
tips = int(input('How much tip would you like to give? %'))
people_num = int(input('How many people to split the bill? '))
check = round((total_bill + (total_bill * (tips / 100))) / people_num, 2)
print(f'Each person should pay: {check}$')
