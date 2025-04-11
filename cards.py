from enum import Enum

class CardSuit(Enum):
    DIAMONDS = 'Diamonds'
    HEARTS = 'Hearts'
    CLOVERS = 'Clovers'
    SPADE = 'Spades'

class Cards:

    def __init__(self, suit: CardSuit, value: int) -> None:
        self.suit = suit
        self.color = 'Red' if suit == CardSuit.DIAMONDS or suit == CardSuit.HEARTS else 'black'
        self.value = value
    
    def __str__(self) -> str:

        return f'{self.value} of {self.suit.name}'
