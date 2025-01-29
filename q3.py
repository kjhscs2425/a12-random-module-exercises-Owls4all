suits = "♠♥♣♦"
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
from utility import *
import random as r
deck = []
# Make a deck of cards
# `deck` should be a list of strings with a value and a suit, e.g. "4♣"
#YOUR CODE HERE
def shuffleDeck():
    global deck
    deck = []
    for suit in suits:
        for value in values:
            place=r.randint(0,len(deck))
            insert(value+suit,place,deck)
    
#shuffle your `deck` and print it out
#YOUR CODE HERE
shuffleDeck()
print(deck)
# sample a hand of 5 cards and print it out
# (WITHOUT replacement -- no repeats!)
#YOUR CODE HERE
shuffleDeck()
hand = []
for i in range(5):
    hand.append(deck[0])
    deck.__delitem__(0)
print(hand)
print(deck)