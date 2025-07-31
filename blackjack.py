from deck import Deck
from player import Player


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

# Take user input choices:
#   1. Hit -> get another card 
#        i. calculate score 
#   2. Stand -> keep cards   
#        i. calculate score
#   3. if user recieves two of the same cards prompt to split 
#      user plays with two cards 
#
# Dealer must continue to hit while under the score of 17
#


class Game:

    def __init__(self, deck):
        self.deck = deck
        self.player = Player()
        self.dealer = Player()

    def hitOrStand(self):
        print("Would you like to hit or stand?")
        hit = input("Enter 1 to hit or 0 to stand:")

        for i, hand in enumerate(self.player.hands):
            
            if hit:
                hand.addCard(self.deck.dealCard())
                self.player.totals[i] = calculateScore(hand)
                       
            else:
                self.player.totals[i] = calculateScore(hand)
        
    def split(self):
        
        
        for hand in self.player.hands:
            
            if hand.deck[0] == hand.deck[1]:
                print("Would you like to split?")
                split = input("Enter 1 to split or 0 to stand")
                
                if split:
                    new_hand = Deck()
                    new_hand.addCard(hand.deck.pop(1))
                    self.player.hands.append(new_hand)
            
    

if __name__ == "__main__":
    
    deck = Deck()
    deck.createDeck()
    deck.shuffleDeck()
    p1= Player()
    
    p1.hands[0].addCard(deck.dealCard())
    p1.hands[0].addCard(deck.dealCard())
    
    p1.totals.append(calculateScore(p1.hands[0]))
    
    print(f'player1 {p1}')
   
   
    