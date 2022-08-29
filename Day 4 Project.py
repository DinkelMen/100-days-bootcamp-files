import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image = [rock, paper, scissors]
my_turn = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_turn = random.randint(0, 2)
if my_turn < 0 or my_turn > 2:
    print(' You typed an invalid number. You lose.')
else:
    print(image[my_turn])

    print('Computer chose:')

    print(image[computer_turn])

    if my_turn == computer_turn:
        print("It's a draw!")
    elif my_turn == 0 and computer_turn == 1:
        print('You lose!')
    elif my_turn == 0 and computer_turn == 2:
        print('You win!')
    elif my_turn == 1 and computer_turn == 0:
        print('You win!')
    elif my_turn == 1 and computer_turn == 2:
        print('You lose!')
    elif my_turn == 2 and computer_turn == 0:
        print('You lose!')
    elif my_turn == 2 and computer_turn == 1:
        print('You win!')
