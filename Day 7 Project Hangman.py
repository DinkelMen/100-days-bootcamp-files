import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
      |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel", "elephant", "snake"]

chosen_word = random.choice(word_list)
display = []
print(logo)
for x in chosen_word:
    display.append('_')
print(''.join(display))
word_length = len(chosen_word)

old_guess = []
n = 0

while '_' in display and n < 7:
    guess = input('Назовите букву: \n').lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess in old_guess:
        print(f'Ты уже пробовал букву {guess}. Попробуй другую.')
    elif guess not in chosen_word:
        print(f'Твой выбор {guess}. Такой буквы нет.')
        n += 1
    else:
        print(f'Откройте букву {guess}.')

    old_guess.append(guess)
    print(''.join(display))
    print(stages[n])

if n == 7:
    print('Ты проиграл.')
else:
    print('Автомобиль!')


