from deck import Deck
from player import Player

def getHandTotal(cards:Deck) -> int:
    total= 0
    aces = 0 

    for card in cards.cards:

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

class Game:

    def __init__(self):
        self.player = Player()
        self.computer = Player()


if __name__ == "__main__":
    
    deck = Deck()
    deck.createDeck()
    deck.shuffleDeck()
    p1= Player()
    p1.cards.addCard(deck.dealCard())
    p1.cards.addCard(deck.dealCard())
    p1.total = getHandTotal(p1.cards)
    
    print(f'player1 {p1}')
   
   
    