'''
Casino War Threading Game in Python
Created by: Kyle Guieb & Daniel Quintana Menjivar
version 0.1a

We opted for an object-oriented approach and ease of flexibility
for designing our project. Python's OpenMP-like threading support is
used.

-TODO-


'''

import random

class Card:
    def _init_(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):  # redefining string method for use of printing card name
        return "%s of %s" % (self.rank, self.suit)


def makeDeck():
    ranks = [_ for _ in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    deck = []
    for i in range(6):
        for rank in range(len(ranks)):
            for suit in range(len(suits)):
                newCard = Card()
                newCard.suit = suits[suit]
                newCard.rank = ranks[rank]
                deck.append(newCard)
    return deck

class Dealer:
    def __init__(self, card):
        self.card = card

class Player:
    def __init__(self, card, money):
        self.card = card
        self.money = money



deck = makeDeck()

random.shuffle(deck) #must shuffle deck

#round 1
dealer = Dealer(deck.pop())

print("Dealer has: %s" % dealer.card)

#generate random money amount $500-2000

money = float(random.randint(500, 2001))
print(money)


# i = 1
# for card in deck:
#     print("Card#%i %s of %s" % (i, card.rank, card.suit))
#     i += 1

#TODO: Rank cards (2 lowest card, 10 is highest number, then Jack, Queen King, Ace is the highest card)
#TODO: Create the player: They have a (randomized) money amount, and a current card
#TODO: Create the dealer: They only have a current card
#TODO: Playing the game:
# The player will have a amount of money to bet, they will bet a random amount of money
# Immediately, the bet will be subtracted from their money count (Keep how much they bet)
# One by one? The dealer will compare their card with the player (or the other way around, whichever is easier to implement)
# If they win, they will add the amount they bet times 2 (player.money = bet*2)
# If they lose, they will add 0 to their money pile (or maybe just nothing happens cause it's already gone)
# if there is a tie:
#   Randomly choose: Forfeit half or go to war
#   If forfeit half: add amount they bet * (1/2) back to their money count
#   If war: minus same bet amount from player, deal new cards to player & dealer, play as normal, if tie, repeat until
#   it finishes
# Once a round finishes, check player money count, if < 1, remove player, otherwise repeat the game, until 30 rounds

#
# def playGame():
#     #play the game
#
#
# if __name__ == "__main__":
#     playGame()