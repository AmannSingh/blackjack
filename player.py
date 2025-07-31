from deck import Deck


#function to calculate the score of player hand
def calculateScore(cards:Deck) -> int:
    total= 0
    aces = 0 

    for card in cards.deck:

        if card.value == 'J' or card.value == 'Q' or card.value == 'K':
            total += 10
        elif card.value == 'A':
            total += 11
            aces += 1
        else:
            total+= int(card.value)

        if total > 21:
            total -= 10
            aces -= 1
 
    return total

class Player:

    def __init__(self) -> None:
        self.hands: list[Deck] = [Deck()]
        self.current_hand_index: int = 0
        
    
    def get_hand_value(self, hand_index: int = 0) -> int:
        hand = self.hands[hand_index]
        return calculateScore(hand)
        
    def clear_hands(self) -> None:
        self.hands = [Deck()]
        self.current_hand_index = 0
        
    def is_bust(self, hand_index: int = 0) -> bool: 
        return self.get_hand_value(hand_index) > 21
        
        
    def __str__(self):
        
        output = []
        
        for i, hand in enumerate(self.hands, start=1):
            
            card_str = ', '.join(str(card) for card in hand.deck)
            value = self.get_hand_value(i-1)
            output.append(f"Hand {i}: {card_str} Total score: {value}")
                   
        return '\n'.join(output)
    
   


    