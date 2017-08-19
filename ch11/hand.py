class Hand(Deck):
    
    def __init__(self):
        self.deck = []
        self.removed = []

    def add(self, card):
        self.cards.append(card)