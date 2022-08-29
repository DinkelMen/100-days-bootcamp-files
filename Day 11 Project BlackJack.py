import random

cards_values = [2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10,
                10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 'ace', 'ace', 'ace', 'ace']
dealer_hand = []
user_hand = []
print('Welcome to BlackJack game!')


def deal_dealer():
    dealer_hand.append(random.choice(cards_values))
    cards_values.remove(dealer_hand[-1])
    if dealer_hand[-1] == 'ace':
        if sum(dealer_hand[0:-1]) <= 10:
            dealer_hand[-1] = 11
        else:
            dealer_hand[-1] = 1


def deal_user():
    user_hand.append(random.choice(cards_values))
    cards_values.remove(user_hand[-1])
    if user_hand[-1] == 'ace':
        if sum(user_hand[0:-1]) <= 10:
            user_hand[-1] = 11
        else:
            user_hand[-1] = 1


dealer_blackjack = 0
deal_user()
deal_user()
deal_dealer()
deal_dealer()
print(user_hand, dealer_hand)

if sum(dealer_hand) == 21 and dealer_hand[-1] == 11:
    print('BlackJack! Dealer wins!')
    raise SystemExit

if sum(user_hand) == 21 and user_hand[-1] == 11:
    print('BlackJack! User wins!')
    raise SystemExit

print(f'User hand value {sum(user_hand)}\nDealer first card value {dealer_hand[-1]}')

decision = ''
while decision != 'no':
    decision = input('Wants more cards? Type "yes" or "no": ')
    if decision == 'yes':
        deal_user()
        print(f'Next user value = {user_hand[-1]}')
        if sum(user_hand) > 21:
            decision = 'no'
            print(f'User hand value = {sum(user_hand)}')
            raise SystemExit


while sum(dealer_hand) < 17:
    deal_dealer()
    print(f'Dealer next value {dealer_hand[-1]}')
    if sum(dealer_hand) == 21 and dealer_hand[-1] == 11:
        print('BlackJack! Dealer win!')
        raise SystemExit


if sum(user_hand) > 21 and sum(dealer_hand) > 21:
    print('Its a draw!')
elif sum(user_hand) > 21:
    print('User lose!')
elif sum(dealer_hand) > 21:
    print('User Win!')
else:
    if sum(user_hand) == 21 and user_hand[-1] == 11:
        print('Blackjack! User win!')
    elif sum(user_hand) < sum(dealer_hand):
        print(f'Dealer hand value = {sum(dealer_hand)}\nUser hand value = {sum(user_hand)}\nUser lose!')
    elif sum(user_hand) > sum(dealer_hand) :
        print(f'Dealer hand value = {sum(dealer_hand)}\nUser hand value = {sum(user_hand)}\nUser Win!')
