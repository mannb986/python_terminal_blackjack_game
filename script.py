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

game_cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, jack, jack, jack, jack, queen, queen, queen, queen, king, king, king, king, ace, ace, ace, ace]
random.shuffle(game_cards)

player_cards_list = []
dealer_cards_list = []


#Game play

def blackjack_game():

    #first deal of player's  2 cards and removing those cards from the deck
    i = 0
    while i < 2:
        p_card = random.choice(game_cards)
        player_cards_list.append(p_card)
        game_cards.remove(p_card)
        i += 1

    #first deal of dealer's 2 cards removing those cards from the deck
    j= 0
    while j < 2:
        d_card = random.choice(game_cards)
        dealer_cards_list.append(d_card)
        game_cards.remove(d_card)
        j += 1

    #player's two cards displayed and one of the dealer's cards is displayed
    print(player_name + "'s cards are " + str(player_cards_list))
    print("Dealer's first card is " + str(dealer_cards_list[0]))
    print("Your total is " + str(sum(player_cards_list)))

    #scoring blackjack from first deal
    if sum(player_cards_list) == 21:
        return print("You win " + player_name + " you scored BlackJack")
    
    #player draw
    player_draw = input('Do you want to draw a card, yes or no?')

    while player_draw == 'yes' and sum(player_cards_list) <22:
        card = random.choice(game_cards)
        player_cards_list.append(card)
        game_cards.remove(card)
        print(player_cards_list)
        print("Your total is " + str(sum(player_cards_list)))
        if sum(player_cards_list) >21:
            return print('Sorry you are bust, dealer wins')
        else:
            player_draw = input('Do you want to draw a card, yes or no?')

    #dealer draw
    print("Dealer to draw:")
    print(dealer_cards_list)
    while sum(dealer_cards_list) < 17:
        d_card = random.choice(game_cards)
        dealer_cards_list.append(d_card)
        game_cards.remove(d_card)
        print(dealer_cards_list)
        if sum(dealer_cards_list) > 21:
            return print('Delaer bust ' + player_name + ' you WIN!')

    print("Dealer total is " + str(sum(dealer_cards_list)))

    #comparing scores and deciding who wins
    if sum(player_cards_list) > sum(dealer_cards_list):
        print(player_name + ' you WIN!')
    elif sum(player_cards_list) == sum(dealer_cards_list): 
       print("It's a draw!")
    else:
        print ('Sorry dealer wins')




blackjack_game()
