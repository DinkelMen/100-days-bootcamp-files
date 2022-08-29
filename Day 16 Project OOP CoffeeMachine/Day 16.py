from turtle import Turtle, Screen
from prettytable import PrettyTable
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'], 'l')
table.add_column('Type', ['Electric', 'Water', 'Fire'], 'r')
print(table)

# my_screen = Screen()
# my_screen.exitonclick()


