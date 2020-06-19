from BlackJack_Project import Deck, Card, Player, decide_winner
from typing import List


def game_is_not_over(player):
    if player.current_hand_value() < 21:
        return True, None
    elif player.current_hand_value() > 21:
        return False, 'Got Busted!'
    else:
        return False, 'BlackJack!'


def my_input(is_user_human: bool, computer_input: List[str], input_message: str, output_accumulator: List[str]):

    if is_user_human:
        x = input(input_message)
        return x
    else:
        output_accumulator.append(input_message)
        input1 = computer_input.pop()
        output_accumulator.append(input1)
        return input1

def my_print(is_user_human: bool, output_accumulator:List[str],output_message:str):
    if is_user_human:
        print(output_message)
    else:
        output_accumulator.append(output_message)


def run_game(test_cards=None, is_user_human=True, computer_input: List[str] = None, output_accumulator:List[str]=None):
    deck = Deck(test_cards)
    player1 = Player(my_input(is_user_human, computer_input, 'If you want riches beyond imagination enter your name:',
                              output_accumulator),
                     1000)
    dealer = Player('dealer', 0)

    while True:

        decision1 = my_input(is_user_human, computer_input,
                             'Welcome to Black Jack, %s! Would you like to place a bet or cash out? \n'
                             'Your current balance is: %s DOLLA (OUR money)!'
                             ' Press b for bet or c for cash out:' % (
                                 player1.player_name, player1.balance), output_accumulator)

        if decision1 == 'b':
            x = int(my_input(is_user_human, computer_input, "Place your Bet:", output_accumulator))
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
            my_print(is_user_human, output_accumulator,
                     'Wrong Command. Press b to bet or c to cash out...Are you Stupid?')

            continue

        player1.first_draw_of_cards(deck)
        dealer.first_draw_of_cards(deck)

        # If player blackJack reveal cards of dealer and decide winner as
        # follows if dealer has BlackJack, dealer wins, otherwise player wins.

        my_print(is_user_human, output_accumulator, player1.player_name + " you have %s " % player1.current_hand)
        my_print(is_user_human, output_accumulator,
                 str.format('Dealer has %s' % dealer.current_hand[0] + ' and a <Hidden Card>'))
        first_time = True
        while game_is_not_over(player1)[0]:
            options = ['hit', 'stand', 'double'] if first_time else ['hit', 'stand']

            options_message = ' or '.join(options)
            options2 = ['h to hit', 's to stand', 'd to double'] if first_time else ['h to hit', 's to stand']
            options2_message = ' or '.join(options2)
            first_time = False
            decision2 = my_input(is_user_human, computer_input,
                                 f'Would you like to {options_message}? Press {options2_message}:',
                                 output_accumulator)
            if decision2 == 'h':
                player1.take_card_from_deck(deck)
                my_print(is_user_human, output_accumulator, str.format('Your cards are: %s' % player1.current_hand))

                my_print(is_user_human, output_accumulator, str.format("The sum of your current hand is: %s" %
                                                                       player1.current_hand_value()))
            elif decision2 == 's' or decision2 == 'd':
                if decision2 == 'd':
                    player1.take_card_from_deck(deck)
                    player1.balance -= player1.current_bet
                    player1.current_bet = 2 * player1.current_bet

                current_hands = dealer.dealer_draw_till_17(deck)
                for current_hand in current_hands:
                    my_print(is_user_human, output_accumulator, str.format("Dealer's cards are: %s" % current_hand))
                else:
                    if dealer.current_hand_value() < 21:
                        my_print(is_user_human, output_accumulator,
                                 str.format("Dealer's sum of cards is: %s" % dealer.current_hand_value()))
                        break
                    elif dealer.current_hand_value() == 21:
                        my_print(is_user_human, output_accumulator, "Dealer hit a BlackJack: %s" %
                                 dealer.current_hand_value())
                        break
                    else:
                        my_print(is_user_human, output_accumulator, 'Dealer got busted!')
                        break

            else:
                # raise ValueError('Wrong Command!')
                my_print(is_user_human, output_accumulator, 'Wrong Command. Are you stupid?')

        _, message = decide_winner(dealer, player1)
        my_print(is_user_human, output_accumulator, message)

        player1.reset_hand()
        dealer.reset_hand()

    my_print(is_user_human,output_accumulator,str.format(f'Game is Over! You won:, {player1.balance},{player1.wins}, {player1.losses}, {player1.pushes}, {player1.busts}'))
