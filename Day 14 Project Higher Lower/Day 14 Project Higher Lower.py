import random
from Game_data_for_day_14 import logo, vs, data


def random_choice():
    random_dict = random.choice(data)
    index = data.index(random_dict)
    followers = data[index]['follower_count']
    data.remove(random_dict)
    return f'{data[index]["name"]}, a {data[index]["description"]} from {data[index]["country"]}', followers


print(logo)
# # while True:
value1 = random_choice()
contin = True

score = 0

while contin:
    print(f'Compare A: {value1[0]}, hint: {value1[1]}')

    print(vs)

    value2 = random_choice()
    print(f'Against B: {value2[0]}, hint {value2[1]}')

    decision = input('Who has more followers? Type "A" or "B": ').upper()

    if decision == 'A' and value1[1] > value2[1]:
        score += 1
        print(f'You are right. Current score: {score}.\n')
    elif decision == 'B' and value2[1] > value1[1]:
        score += 1
        value1 = value2
        print(f'You are right. Current score: {score}.\n')
    else:
        contin = False
        print(f'Sorry, that is wrong. Your score {score}.')
