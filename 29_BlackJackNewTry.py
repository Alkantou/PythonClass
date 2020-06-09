import random
from typing import List


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

    def deal(self):
        single_card = self.cards.pop()

class Hand:

    def __init__(self):
