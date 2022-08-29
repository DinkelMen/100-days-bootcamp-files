""" Задание на https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=
Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"""


def turn_left():
    pass


def move():
    pass


def at_goal():
    pass


def front_is_clear():
    pass


def right_is_clear():
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def left_is_clear():
    turn_left()
    if front_is_clear():
        turn_right()
        return True
    else:
        turn_right()
        return False


while not at_goal():
    if right_is_clear() and front_is_clear() and left_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
