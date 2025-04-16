from deck import Deck
from player import Player

def calculateScore(cards:Deck) -> int:
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

# Take user input choices:
#   1. Hit -> get another card 
#        i. calculate score 
#   2. Stand -> keep cards   
#   3. if user recieves two of the same cards prompt to split 
#      user plays with two cards 
#
# Dealer must continue to hit while under the score of 17
#


class Game:

    def __init__(self, deck):
        self.deck = deck
        self.player = Player()
        self.computer = Player()

    def hitOrStand(self):
        print("Would you like to hit or stand?")
        hit = input("Enter 1 to hit or 0 to stand:")

        if hit:
            self.player.cards.addCard(self.deck.dealCard())
            self.player.total = calculateScore(self.player.cards)            
            print(p1)
    
    

if __name__ == "__main__":
    
    deck = Deck()
    deck.createDeck()
    deck.shuffleDeck()
    p1= Player()
    p1.cards.addCard(deck.dealCard())
    p1.cards.addCard(deck.dealCard())
    p1.total = calculateScore(p1.cards)
    
    print(f'player1 {p1}')
   
   
    