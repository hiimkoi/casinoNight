'''
Casino War Threading Game in Python
Created by: Kyle Guieb & Daniel Quintana Menjivar
version 0.1a

We opted for an object-oriented approach and ease of flexibility
for designing our project. Python's OpenMP-like threading support is
used.

-TODO-
TODO: Rank cards (2 lowest card, 10 is highest number, then Jack, Queen King, Ace is the highest card)
TODO: Create the player: They have a (randomized) money amount, and a current card
TODO: Create the dealer: They only have a current card
TODO: Playing the game:
The player will have a amount of money to bet, they will bet a random amount of money
Immediately, the bet will be subtracted from their money count (Keep how much they bet)
One by one? The dealer will compare their card with the player (or the other way around, whichever is easier to implement)
If they win, they will add the amount they bet times 2 (player.money = bet*2)
If they lose, they will add 0 to their money pile (or maybe just nothing happens cause it's already gone)
if there is a tie:
Randomly choose: Forfeit half or go to war
If forfeit half: add amount they bet * (1/2) back to their money count
If war: minus same bet amount from player, deal new cards to player & dealer, play as normal, if tie, repeat until
it finishes
Once a round finishes, check player money count, if < 1, remove player, otherwise repeat the game, until 30 rounds
'''

import random
import threading  # standard Python library for "OpenMP-ness"


class Card:  # Class Card created for use in Deck of cards
    def _init_(self, rank, suit):  # instance variables rank and suit of card
        self.rank = rank
        self.suit = suit

    def __str__(self):  # redefining string method for use of printing card name
        return "%s of %s" % (self.rank, self.suit)

    def getValue(self):  # method returns the integer value of a card for Casino War Game
        if not isinstance(self.rank, str):  # string ranks are special cases
            return self.rank - 1  # non string ranks get their numeric values - 1 because of ace
        else:
            if self.rank == "Jack":  # all other card ranks need to be given special care
                return 10
            elif self.rank == "Queen":
                return 11
            elif self.rank == "King":
                return 12
            else:  # case for Ace
                return 13


def makeDeck():  # function builds 6 deck of cards for playing a game of Casino War
    ranks = [_ for _ in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    deck = []  # empty deck using list
    for i in range(6):  # need 6 decks of cards for a proper game of casino war
        for rank in range(len(ranks)):  # each with their corresponding rank
            for suit in range(len(suits)):  # and suit
                newCard = Card()
                newCard.suit = suits[suit]
                newCard.rank = ranks[rank]
                deck.append(newCard)
    return deck


class Dealer:  # Dealer class contains the dealer's card
    def __init__(self):
        self.card = None  # setter method takes care of this
        self.houseWinnings = 0  # just for geeky fun keep track of the winnings siphoned from the players

    def __str__(self):  # overwritten string RV for dealer class used in printing
        return "Dealer has %s" % self.card

    def assignCard(self, card):  # setter method assigns instance variable card
        self.card = card

    def plays(self, player):  # method performs the card judgment aka the actually game part of the game
        playerValue = player.card.getValue()  # grab corresponding card values for judgement
        dealerValue = self.card.getValue()
        if dealerValue == playerValue:  # player and dealer ties
            if player.goToWar():  # player decides to go to war
                return False
            else:  # player forfeits
                player.money += player.bet / 2  # return half of player's bet to their money
                player.bet = 0
        elif dealerValue < playerValue:  # player wins
            print("Player #%i wins $%.2f!" % (player.id, 2 * player.bet))
            player.money += player.bet * 2  # player receives twice their bet
            player.bet = 0
        else:  # player lost
            print("Player #%i loses $%.2f!" % (player.id, player.bet))
            self.houseWinnings += player.bet  # nothing really happens but I keep track of the winnings for stats
            player.bet = 0


class Player:  # Player class contains a corresponding players card and how much money they have

    def __init__(self, id):
        self.id = id  # verifying which player this is
        self.money = getMoney()  # on construction receives random money wad
        self.bet = 0  # tracks betting amount
        self.card = None  # card player is assigned during game

    def __str__(self):  # overwritten string RV for player class used in printing
        return "Player #%i has %s, and $%.2f" % (self.id, self.card, self.money)

    def makeBet(self):  # method randomly assigns a bet value and subtracts it from the players total money
        betAmount = random.randint(1, self.money + 1)
        self.money -= betAmount
        self.bet = betAmount
        print("Player #%i has made a $%.2f bet" % (self.id, self.bet))

    def hasBusted(self):  # method checks to see if player has any money left to play or if player has busted
        if self.money <= 0:
            print("Player #%i has busted!" % self.id)
            return True
        else:
            return False

    def assignCard(self, card):  # setter method assigns card to player
        self.card = card

    def goToWar(self):  # method randomly decides for the player in the case of a tie, if player goes to war or forfeits
        return random.choice([True, False])


def getMoney():  # method generates a random amount of money from $500 - $2000
    return float(random.randint(500, 2001))


def playGame():  # main method that plays the game
    deck = makeDeck()  # creates deck of cards

    random.shuffle(deck)  # shuffles deck of cards NOTE: consider moving this to makeDeck

    # round 1
    dealer = Dealer()

    # print("Dealer has: %s" % dealer.card)

    # generate random money amount $500-2000

    # money = float(random.randint(500, 2001))
    # print(money)

    # initialize 3 players

    theHouse = 0

    players = []
    for i in range(3):
        players.append(Player(i + 1))
        # print(players[i])

    numOfRounds = 1
    while (len(players) > 1):

        print("Start of round #%i" % numOfRounds)
        dealer.assignCard(deck.pop())
        print(dealer)

        for player in players:
            player.makeBet()
            player.assignCard(deck.pop())
            print(player)
            dealer.plays(player)

            if player.hasBusted():
                players.remove(player)

        print("End of round #%i\n" % numOfRounds)
        numOfRounds += 1

    # i = 1
    # for card in deck:
    #     print("Card#%i %s of %s" % (i, card.rank, card.suit))
    #     i += 1


if __name__ == "__main__":
    playGame()
