from random import shuffle
from cards import *

class Deck:

    def __init__(self) -> None:
        self.cards: list[Cards] = []

    def __str__(self) -> str:

        return  '\n'.join( str(card) for card in self.cards)
    
    def addCard(self, card: Cards) -> None:
        self.cards.append(card)

    def createDeck(self) -> None:
        values = ['2','3','4', '5', '6', '7', '8','9', '10', 'J', 'Q', 'K', 'A']
        
        for suit in CardSuit:
            for val in values:
                self.cards.append(Cards(suit,val))
    
    def shuffleDeck(self) -> None:
        shuffle(self.cards)

    def dealCard(self) -> Cards:
        return self.cards.pop() if self.cards else None

   