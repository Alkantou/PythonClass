# Milestone Project 2 - Blackjack Game
# In this milestone project you will be creating a Complete BlackJack Card Game in
# Python.
import random
from typing import List


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        if self.rank == 11:
            return 'Jack of ' + self.suit
        elif self.rank == 12:
            return 'Queen of ' + self.suit
        elif self.rank == 13:
            return 'King of ' + self.suit

        return str(self.rank) + ' of ' + self.suit

    def __repr__(self):
        return self.__str__()


class Deck:

    def __init__(self, test_cards = None ):

        if test_cards is not None:
            self.cards = test_cards
        else:
            self.cards = []
            for c in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                for n in range(1, 14):
                    self.cards.append(Card(c, n))
            random.shuffle(self.cards)

    def __repr__(self):
        return str(len(self.cards)) + ' Cards ' + str(self.cards)

    def hit(self):
        hit1 = self.cards.pop()
        return hit1


class Player:

    def __init__(self, player_name, balance: int):
        self.player_name = player_name
        self.balance = balance
        self.current_hand: List[Card] = []
        # self.current_hand_numbers = []
        self.current_bet = 0
        self.wins = 0
        self.losses = 0
        self.busts = 0
        self.pushes = 0

    def bet_won_or_lost(self,bet_won):
        if bet_won is True:
            self.balance += 2 * self.current_bet
            return "Your current balance is:" + str(self.balance)


    def place_bet(self: int, bet_amount: int) -> int:
        if bet_amount > self.balance:
            raise ValueError("Insufficient Funds!")
            # print()
        self.current_bet = bet_amount
        self.balance -= self.current_bet

    def add_card_to_hand(self, card: Card):
        self.current_hand.append(card)
        # self.current_hand_numbers.append(card.rank)

    def current_hand_value(self) -> int:
        sum = 0
        for c in self.current_hand:
            if c.rank > 10:  # Figures
                sum += 10
            elif c.rank != 1:
                sum += c.rank

        for c in self.current_hand:
            if c.rank == 1:
                if sum + 11 > 21:
                    sum += 1
                else:
                    sum += 11
        return sum

    def reset_hand(self):
        self.current_hand = []

    def return_balance(self):
        self.balance += self.current_bet

    def first_draw_of_cards(self, deck):
        for _ in range(2):
            self.take_card_from_deck(deck)

    def take_card_from_deck(self, deck):
        current_hand = deck.hit()
        self.add_card_to_hand(current_hand)

    def dealer_draw_till_17(self, deck):
        current_hands = []
        while self.current_hand_value() <= 17:
            self.take_card_from_deck(deck)
            current_hands.append(self.current_hand.copy())
        return current_hands

    # Test: Create a Player. create card 1, 2, 3, Call player_add_card_to_hand 1,2,3
    # asser


class Dealer:

    def __init__(self):
        self.deck = Deck()


class BlackJack:

    def __init__(self, player: Player):
        self.player = player
        self.dealer = Dealer()

    def next_round(self):
        bet_amount = input('Place Bet:')
        self.player.place_bet(int(bet_amount))


def decide_winner(input_dealer, input_player)->str:

    if (input_dealer.current_hand_value() < input_player.current_hand_value() \
        and input_player.current_hand_value() <= 21) or input_dealer.current_hand_value() > 21:

            input_player.wins += 1

            input_player.bet_won_or_lost(True)

            return "player", str.format(f"{input_player.player_name} wins")

    elif input_dealer.current_hand_value() == input_player.current_hand_value():
        input_player.pushes += 1


        input_player.return_balance()
        return "push", 'Push'
    else:
        if input_player.current_hand_value() > 21:
            input_player.busts += 1
        input_player.losses += 1


        return 'dealer', 'Delaer wins!'



 # def decide_winner_0(input_dealer, input_player)->str:
 #
 #      if input_dealer.current_hand_value() == input_player.current_hand_value() == 21:
 #         print("We have a push")
 #         push_count += 1
 #         return 'push'
 #         pass# A function for the first 2 cards winning?


def split(player):
    if player.current_hand[0] == player.current_hand[1]:
        f = input('There is a split! Would you like to split the cards? Press y or n')
        if f == 'y':
            pass
        else:
            pass


