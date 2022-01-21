from random import randint


print('BLACKJACK')
print('---------')


def random_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    no = randint(0, 12)
    return cards[no]


def add_dealer_cards(card_1, card_2):
    return card_1 + card_2


def add_user_cards(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_dealer_and_user(dealer, user):
    if dealer < user <= 21:
        print(f'you win')
    elif user == dealer:
        print(f'it is a draw')
    elif dealer > user:
        print(f'you lose')
    elif user > 21:
        print('i said you lose')
    elif user == 21:
        print('i said you win')
    elif dealer > 21:
        print('you win')


def game_mode():
    print('BLACKJACK')
    print('---------')

    user_lists_of_cards = []

    global sum_of_user

    user_card_1 = random_cards()
    user_lists_of_cards.append(user_card_1)
    dealer_card_1 = random_cards()
    print(f'\ndealers first card = {dealer_card_1}')

    playing = True
    while playing:
        user_card_2 = random_cards()
        user_lists_of_cards.append(user_card_2)
        sum_of_user = add_user_cards(user_lists_of_cards)
        print(f'you have cards of {user_lists_of_cards} and a total of {sum_of_user}')
        if sum_of_user > 21:
            playing = False
        next_action = input('hit or stand: ')
        if next_action == 'stand':
            print(f'your sum card is {sum_of_user}')
            playing = False

    while True:
        dealer_card_2 = random_cards()
        sum_of_dealer = add_dealer_cards(dealer_card_1, dealer_card_2)
        if sum_of_dealer > 21:
            break
        if sum_of_dealer <= 16:
            dealer_card_1 = sum_of_dealer
        if sum_of_dealer >= 17:
            print(f'dealers total is {sum_of_dealer}')
            compare_dealer_and_user(sum_of_dealer, sum_of_user)
            break


while input('do you want to play a new game, "yes" or "no": ') == 'yes':
    game_mode()
