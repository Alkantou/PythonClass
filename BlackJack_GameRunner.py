from BlackJack_Project import Deck, Card, Player, decide_winner
from typing import List


def game_is_not_over(player):
    if player.current_hand_value() < 21:
        return True
    elif player.current_hand_value() > 21:
        print('Got Busted!')

        return False
    else:
        print('BlackJack!')
        return False


def my_input(is_user_human: bool, computer_input: List[str], input_message: str):
    if is_user_human:
        x = input(input_message)
        return x
    else:
        return computer_input.pop()

def my_print(is_user_human: bool, output_accumulator:List[str],output_message:str):
    if is_user_human:
        print(output_message)
    else:
        output_accumulator.append(output_message)


def run_game(test_cards=None, is_user_human=True, computer_input: List[str] = None, output_accumulator:List[str]=None):
    deck = Deck(test_cards)
    player1 = Player(my_input(is_user_human, computer_input, 'If you want riches beyond imagination enter your name:'),
                     1000)
    dealer = Player('dealer', 0)

    while True:

        decision1 = my_input(is_user_human, computer_input,
                             'Welcome to Black Jack, %s! Would you like to place a bet or cash out? \n'
                             'Your current balance is: %s DOLLA (OUR money)!'
                             ' Press b for bet or c for cash out:' % (
                                 player1.player_name, player1.balance))

        if decision1 == 'b':
            x = int(my_input(is_user_human, computer_input, "Place your Bet:"))
            if x == 0:
                my_print(is_user_human,output_accumulator,'You are broke!')
                continue
            y = player1.place_bet(bet_amount=x)
            my_print(is_user_human,output_accumulator,'Current Balance is:' + str(player1.balance))








        elif decision1 == 'c':

            break
            # if player1.balance <= 1000:
            #     print('You think you are smart? You will not go away with OUR money!')
            #     decision1 = 'b'
            #
            #     continue
            # else:
            #     break
        else:
            # raise ValueError('Wrong Command!')
            my_print(is_user_human,output_accumulator,'Wrong Command. Press b to bet or c to cash out...Are you Stupid?')

            continue

        current_hand = deck.hit()
        player1.add_card_to_hand(current_hand)
        current_hand = deck.hit()
        player1.add_card_to_hand(current_hand)

        dealer_hand = deck.hit()
        dealer.add_card_to_hand(dealer_hand)
        dealer_hand = deck.hit()
        dealer.add_card_to_hand(dealer_hand)

        # If player blackJack reveal cards of dealer and decide winner as
        # follows if dealer has BlackJack, dealer wins, otherwise player wins.

        my_print(is_user_human,output_accumulator,player1.player_name + " you have %s " % player1.current_hand)
        my_print(is_user_human,output_accumulator,str.format('Dealer has %s' % dealer.current_hand[0], 'and a <Hidden Card>'))
        while game_is_not_over(player1):
            decision2 = my_input(is_user_human, computer_input,
                                 'Would you like to hit or stand? Press h to hit or s to stand:')
            if decision2 == 'h':
                current_hand = deck.hit()
                player1.add_card_to_hand(current_hand)
                my_print(is_user_human,output_accumulator,str.format('Your cards are:', player1.current_hand))

                my_print(is_user_human,output_accumulator,"The sum of your current hand is:", str(player1.current_hand_value()))





            elif decision2 == 's':
                while dealer.current_hand_value() <= 17:
                    dealer_hand = deck.hit()
                    dealer.add_card_to_hand((dealer_hand))
                    my_print(is_user_human,output_accumulator,"Dealer's cards are:", str(dealer.current_hand))
                else:
                    if dealer.current_hand_value() < 21:
                        my_print(is_user_human,output_accumulator,"Dealer's sum of cards is:", dealer.current_hand_value())
                        break
                    elif dealer.current_hand_value() == 21:
                        my_print(is_user_human,output_accumulator,"Dealer hit a BlackJack:", dealer.current_hand_value())
                        break
                    else:
                        my_print(is_user_human,output_accumulator,'Dealer got busted!')
                        break

            else:
                # raise ValueError('Wrong Command!')
                my_print(is_user_human,output_accumulator,'Wrong Command. Are you stupid?')

        decide_winner(dealer, player1)

        player1.reset_hand()
        dealer.reset_hand()

    my_print(is_user_human,output_accumulator,str.format('Game is Over! You won:', player1.balance, player1.wins, player1.losses, player1.pushes, player1.busts))
