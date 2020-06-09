# Milestone Project 2 - Blackjack Game
# In this milestone project you will be creating a Complete BlackJack Card Game in
# Python.
import random
from typing import List


#
# Here are the requirements:
#
# You need to create a simple text-based BlackJack game
# The game needs to have one player versus an automated dealer.
# The player can stand or hit.
# The player must be able to pick their betting amount.
# You need to keep track of the player's total money.
# You need to alert the player of wins, losses, or busts, etc...
# And most importantly:
#
# You must use OOP and classes in some portion of your game. You can not
# just use functions in your game. Use classes to help you define the Deck
# and the Player's hand. There are many right ways to do this, so explore it
# well!
# Feel free to expand this game. Try including multiple players. Try adding
# in Double-Down and card splits! Remember to you are free to use any resources
# you want.
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.cards = []
        for c in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for n in range(1, 14):
                self.cards.append(Card(c, n))
        random.shuffle(self.cards)


class Player:

    def __init__(self, player_name, balance):
        self.player_name = player_name
        self.balance = balance
        self.current_hand: List[Card] = []
        self.current_bet = 0
        self.wins = 0
        self.losses = 0
        self.busts = 0

    def place_bet(self, bet_amount):
        if bet_amount > self.balance:
            raise ValueError("Insufficient Funds!")
            # print()
        self.current_bet = bet_amount
        self.balance -= self.current_bet

    def add_card_to_hand(self, card: Card):
        self.current_hand.append(card)

    def current_hand_value(self) -> int:
        sum = 0
        for c in self.current_hand:
            sum += c.rank


class Dealer:

    def __init__(self):
        self.deck = Deck()

    def serve(self):
        hit = self.deck.cards.pop()
        return hit


class BlackJack:

    def __init__(self, player: Player):
        self.player = player
        self.dealer = Dealer()

    def next_round(self):
        bet_amount = input('Place Bet:')
        self.player.place_bet(int(bet_amount))


blackjack = BlackJack(Player('Militiadis', 1000))

while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    deck = Deck()

    player_hand = Dealer()
    player_hand.serve()



