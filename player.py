from deck import Deck

class Player:

    def __init__(self) -> None:
        self.hands: list[Deck] = [Deck()]
        self.totals: list[int] = []

    def __str__(self):
        
        output = []
        
        for i, hand in enumerate(self.hands, start=1):
            
            card_str = ', '.join(str(card) for card in hand.deck)
            
            output.append(f"Hand {i}: {card_str} Total score: {self.totals[i-1]}")
                   
        return '\n'.join(output)
    
   


    