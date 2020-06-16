from BlackJack_GameRunner import run_game
from BlackJack_Project import Card

test_cards = [Card('Spades', 1), Card('Diamonds', 10), Card('Hearts', 10), Card('Hearts', 12)]
output_accumulator = []
run_game(test_cards=test_cards[::-1], is_user_human=False, computer_input=['ALex', 'b', '10', 'c'][::-1],
         output_accumulator=output_accumulator)

# run_game()
print(output_accumulator)