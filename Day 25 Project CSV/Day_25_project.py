import csv
import pandas
from turtle import Turtle
import turtle
FONT = ("Courier", 8, "normal")
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperature = []
#     for i in data:
#         if i[1] != 'temp':
#             temperature.append(int(i[1]))
# print(temperature)

# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

# temp_list = data['temp'].to_list()
# average = sum(temp_list) / len(temp_list)
# print(round(average, 2))

# print(data['temp'].max())

# print(data[data.temp == data['temp'].max()])

# fahrenheit = data[data.day == 'Monday'].temp * 1.8 + 32
# print(fahrenheit)

# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# data1 = pandas.DataFrame(data_dict)
# print(data1)

# black_fur = []
# red_fur = []
# gray_fur = []
# squirrels = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# squirrels_color = squirrels['Primary Fur Color']
# for i in squirrels_color:
#     if i == 'Black':
#         black_fur.append(i)
#     elif i == 'Gray':
#         gray_fur.append(i)
#     elif i == 'Cinnamon':
#         red_fur.append(i)
#
#
# print(len(black_fur))
# print(len(gray_fur))
# print(len(red_fur))


screen = turtle.Screen()
screen.title('U.S. States Game')
screen.addshape('blank_states_img.gif')

turtle.shape('blank_states_img.gif')


state_list = []
with open('50_states.csv') as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row != ['state', 'x', 'y']:
            state_list.append(row)

tom = Turtle()
tom.hideturtle()
tom.penup()
tim = Turtle()
tim.hideturtle()
tim.penup()
x = 0
y = 0
state_name = ''
game_on = True
states_guessed = 0

while game_on:
    answer_state = screen.textinput('U.S. States Game', "Enter state's name").title()
    if answer_state == 'Exit':
        break
    for state in state_list:
        for n in state:
            if answer_state == n:
                x = int(state[1])
                y = int(state[2])
                state_name = state[0]
                states_guessed += 1
                tim.goto(x, y)
                tim.write(f'{state_name.title()}', align='center', font=FONT)
                state_list.remove(state)
                tom.goto(0, -300)
                tom.clear()
                tom.write(f'States guessed: {states_guessed}/50', align='center', font=("Courier", 20, "normal"))

    if len(state_list) == 0:
        print('You win')
        game_on = False
turtle.mainloop()
