# Blackjack game in Python terminal 
import random

# Setting up player name
player_name = input('Enter your name:')
print('Hello, ' + player_name + " let's play Blackjack!")

# Setting up card deck 
jack = 10
king = 10
queen = 10

#future adation to include ace as 1 also
ace = 11

card_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, jack, jack, jack, jack, queen, queen, queen, queen, king, king, king, king, ace, ace, ace, ace]

player_cards_list = []
dealer_cards_list = []


#Game play
def blackjack_game(deck_of_cards):
    random.shuffle(deck_of_cards)
    #first deal of player's  2 cards and removing those cards from the deck
    i = 0
    while i < 2:
        p_card = random.choice(card_deck)
        player_cards_list.append(p_card)
        card_deck.remove(p_card)
        i += 1

    #first deal of dealer's 2 cards removing those cards from the deck
    j= 0
    while j < 2:
        d_card = random.choice(card_deck)
        dealer_cards_list.append(d_card)
        card_deck.remove(d_card)
        j += 1

    #player's two cards displayed and one of the dealer's cards is displayed
    print(player_name + "'s cards are " + str(player_cards_list))
    print("Dealer's first card is " + str(dealer_cards_list[0]))

    #scoring blackjack from first deal
    if sum(player_cards_list) == 21:
        print("You win " + player_name + " you scored BlackJack")


blackjack_game(card_deck)