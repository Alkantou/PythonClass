#import BlackJack_Project as fp
from BlackJack_Project import Player, Card, decide_winner

def test_Player_winning():
    player1 = Player('Alex', 1000)
    dealer1 = Player('Noname', 1000)
    player1.add_card_to_hand(Card('Diamonds', 1))
    player1.add_card_to_hand(Card('Spades', 10))
    dealer1.add_card_to_hand(Card('Diamonds', 10))
    dealer1.add_card_to_hand(Card('Spades', 6))

    assert decide_winner(dealer1, player1) == 'player1'

from BlackJack_console import run_game




