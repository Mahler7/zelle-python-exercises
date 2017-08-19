import random

suits = ['Spades','Clubs','Diamonds','Hearts']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Deck:
    """This class returns a deck of 52 playing cards
    It also shuffles, deals, and keeps track of the cards left"""
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        self.deck = []
        self.removed = []

    def newDeck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(rank + ' of ' + suit)
        return self.deck

    def shuffle(self):
        self.deck = random.sample(self.deck, 52)
        return self.deck

    def dealCard(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.removed = self.removed.append(card)
        return card

    def cardsLeft(self):
        count = 0
        for i in self.deck:
            count = count + 1
        return count
        

