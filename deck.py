from random import shuffle
from cards import *

class Deck:

    def __init__(self) -> None:
        self.deck: list[Cards] = []

    def __str__(self) -> str:

        return  '\n'.join( str(card) for card in self.deck)
    
    def addCard(self, card: Cards) -> None:
        self.deck.append(card)

    def createDeck(self) -> None:
        values = ['2','3','4', '5', '6', '7', '8','9', '10', 'J', 'Q', 'K', 'A']
        
        for suit in CardSuit:
            for val in values:
                self.deck.append(Cards(suit,val))
    
    def shuffleDeck(self) -> None:
        shuffle(self.deck)

    def dealCard(self) -> Cards:

        if self.deck:
            return self.deck.pop()
        else:
            self.createDeck()
            return self.deck.pop()
        

   