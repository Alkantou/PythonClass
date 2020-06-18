#import BlackJack_Project as fp
from BlackJack_Project import Player, Card, decide_winner

def test_Player_winning():
    player1 = Player('Alex', 1000)
    dealer1 = Player('Noname', 1000)
    player1.add_card_to_hand(Card('Diamonds', 1))
    player1.add_card_to_hand(Card('Spades', 10))
    dealer1.add_card_to_hand(Card('Diamonds', 10))
    dealer1.add_card_to_hand(Card('Spades', 6))

    assert decide_winner(dealer1, player1)[0] == 'player'

from BlackJack_console import run_game


def test_player_has_blackjack():
    test_cards = [Card('Spades', 1), Card('Diamonds', 10), Card('Hearts', 10), Card('Hearts', 12)]
    output_accumulator = []
    run_game(test_cards=test_cards[::-1], is_user_human=False, computer_input=['ALex', 'b', '10', 'c'][::-1],
             output_accumulator=output_accumulator)
    assert output_accumulator[-4] == 'ALex wins'

