# Blackjack game in Python terminal 
import random

# Setting up player name
player_name = input('Enter your name:')
print('Hello, ' + player_name + "let's play Blackjack!")

# Setting up card deck 
jack = 10
king = 10
queen = 10
#future adation to include ace as 1 also
ace = 11
card_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, jack, jack, jack, jack, queen, queen, queen, queen, king, king, king, king, ace, ace, ace, ace]

player_cards_list = []
dealer_cards_list = []

def card_deal():
    player_cards_1 = random.choice(card_deck)
    player_cards_2 = random.choice(card_deck)
    player_cards_list.append(player_cards_1)
    player_cards_list.append(player_cards_2)
    dealer_cards_1 = random.choice(card_deck)
    dealer_cards_2 = random.choice(card_deck)
    dealer_cards_list.append(dealer_cards_1)
    dealer_cards_list.append(dealer_cards_2)
    print(player_name + "'s cards are " + str(player_cards_list))
    print("Dealer's first card is " + str(dealer_cards_list[0]))

card_deal()