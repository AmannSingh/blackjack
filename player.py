from deck import Deck

class Player:

    def __init__(self) -> None:
        self.cards: Deck = Deck()
        self.total: int = 0

    def __str__(self):
        return f'\ntotal:{self.total}\ncards:\n{str(self.cards)}'
    
   


    