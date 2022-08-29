import random

logo = """
   _____                          _______  _               _   _                    _                 
  / ____|                        |__   __|| |             | \ | |                  | |                
 | |  __  _   _   ___  ___  ___     | |   | |__    ___    |  \| | _   _  _ __ ___  | |__    ___  _ __ 
 | | |_ || | | | / _ \/ __|/ __|    | |   | '_ \  / _ \   | . ` || | | || '_ ` _ \ | '_ \  / _ \| '__|
 | |__| || |_| ||  __/\__ \\__ \    | |   | | | ||  __/   | |\  || |_| || | | | | || |_) ||  __/| |   
  \_____| \__,_| \___||___/|___/    |_|   |_| |_| \___|   |_| \_| \__,_||_| |_| |_||_.__/  \___||_|
  """

print(logo)
print('Welcome to the number guessing game!')
the_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
difficulty = input('Choose a difficulty. Type "easy" or "hard": ').lower()

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

print(f'You have {attempts} attempts remaining to guess the number.')

while attempts != 0:
    guessed_number = int(input('Make a guess: '))

    if guessed_number > the_number:
        attempts -= 1
        if attempts == 0:
            print('You are out of attempts. You lose!')
            break
        print(f'Too high!\nGuess again!\nYou have {attempts} attempts remaining to guess the number.')
    elif guessed_number < the_number:
        attempts -= 1
        if attempts == 0:
            print('You are out of attempts. You lose!')
            break
        print(f'Too low!\nGuess again!\nYou have {attempts} attempts remaining to guess the number.')
    else:
        print(f'You got it! The answer was {guessed_number}!\nYou have got {attempts} attempts left.')
        break
