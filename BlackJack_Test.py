#import BlackJack_Project as fp
from BlackJack_Project import Player, Card, decide_winner
from BlackJack_GameRunner import run_game

def test_Player_winning():
    player1 = Player('Alex', 1000)
    dealer1 = Player('Noname', 1000)
    player1.add_card_to_hand(Card('Diamonds', 1))
    player1.add_card_to_hand(Card('Spades', 10))
    dealer1.add_card_to_hand(Card('Diamonds', 10))
    dealer1.add_card_to_hand(Card('Spades', 6))

    assert decide_winner(dealer1, player1)[0] == 'player'




def test_player_has_blackjack():
    test_cards = [Card('Spades', 1), Card('Diamonds', 10), Card('Hearts', 10), Card('Hearts', 12)]
    output_accumulator = []
    run_game(test_cards=test_cards[::-1], is_user_human=False, computer_input=['ALex', 'b', '10', 'c'][::-1],
             output_accumulator=output_accumulator)
    assert output_accumulator[-4] == 'ALex wins'


def test_dealer_busts():
    test_cards = [Card('Spades', 10), Card('Diamonds', 10), Card('Hearts', 10), Card('Hearts', 3), Card('Diamonds', 13)]
    output_accumulator = []
    run_game(test_cards=test_cards[::-1], is_user_human=False, computer_input=['ALex', 'b', '10', 's', 'c'][::-1],
             output_accumulator=output_accumulator)
    assert output_accumulator[-5] == 'Dealer got busted!'


def test_push():
    test_cards = [Card('Spades', 10), Card('Diamonds', 10), Card('Hearts', 10), Card('Hearts', 12)]
    output_accumulator = []
    run_game(test_cards=test_cards[::-1], is_user_human=False, computer_input=['ALex', 'b', '10', 's', 'c'][::-1],
             output_accumulator=output_accumulator)
    assert output_accumulator[-4] == 'Push'


def test_cashout_at_start():
    test_cards = [Card('Spades', 10), Card('Diamonds', 10), Card('Hearts', 10), Card('Hearts', 12)]
    output_accumulator = []
    run_game(test_cards=test_cards[::-1], is_user_human=False, computer_input=['ALex', 'c'][::-1],
             output_accumulator=output_accumulator)
    assert output_accumulator[-1] == 'Game is Over! You won:, 1000,0, 0, 0, 0'


def test_ace_correct_function():
    test_cards = [Card('Spades', 1), Card('Diamonds', 8), Card('Hearts', 10), Card('Hearts', 12), Card('Hearts', 7)]
    output_accumulator = []
    run_game(test_cards=test_cards[::-1], is_user_human=False, computer_input=['ALex', 'b', '10', 'h', 's', 'c'][::-1],
             output_accumulator=output_accumulator)
    assert output_accumulator[12] == 'The sum of your current hand is: 16'

def test_double():
    test_cards = [Card('Spades', 2), Card('Diamonds', 8), Card('Hearts', 8), Card('Hearts', 12), Card('Hearts', 9)]
    output_accumulator = []
    run_game(test_cards=test_cards[::-1], is_user_human=False, computer_input=['ALex', 'b', '30', 'd', 'c'][::-1],
             output_accumulator=output_accumulator)
    assert output_accumulator[-1] == 'Game is Over! You won:, 1060,1, 0, 0, 0'

def vafouskos():
    pass