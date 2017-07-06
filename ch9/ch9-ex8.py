#Get 21 points or as close to as possible without going over
#Face cards = 10 points, Aces = 1 or 11, Numbers = numbers
#Dealer takes cards until it reaches value of 17
#Dealer Ace counts as 11 when Dealer score is between 17 and 21
#Dont have to keep track of the cards
#Need hasAce Boolean that tells whether or not a hand contains an ace
#Program simulates multiple games of black jack and estimates the probability that the dealer will bust

import random

def main():
    intro()
    n = inputs()
    dealerBusts, playerBusts = simBlackJack(n)
    printBustResults(n, dealerBusts, playerBusts)

def intro():
    print("This program simulates multiple games of Black Jack")
    print("and estimates the probability that the dealer will bust")

def inputs():
    validNumber = False
    while validNumber == False:
        try:
            n = eval(input("Enter the number of Black Jack games to simulate: "))
            if n >= 1:
                validNumber = True
            else:
                print("Please enter a number greater than 0")
        except NameError:
            print("Please enter a valid number")
    return n

def simBlackJack(n):
    dealerBusts = 0
    playerBusts = 0
    for i in range(n):
        busted, dealerScore, playerScore, dealerHand, playerHand = blackJackGame()
        if busted == "Dealer":
            dealerBusts = dealerBusts + 1
        elif busted == "Player":
            playerBusts = playerBusts + 1
        printResults(i + 1, dealerScore, playerScore, dealerHand, playerHand)
    return dealerBusts, playerBusts

def blackJackGame():
    dealerHand, playerHand = dealHand()
    dealerScore = checkScore(dealerHand)
    playerScore = checkScore(playerHand)
    busted = "Not Busted"

    while not gameOver(dealerScore, playerScore): 
        card = getCard()
        dealerHand.append(card)
        dealerScore = checkScore(dealerHand)
        if dealerScore > 21:
            busted = "Dealer"
            break
        playerHand.append(card)
        playerScore = checkScore(playerHand)
        if playerScore > 21:
            busted = "Player"
            break
    return busted, dealerScore, playerScore, dealerHand, playerHand

def dealHand():
    dealerCard1 = getCard()
    dealerCard2 = getCard()
    playerCard1 = getCard()
    playerCard2 = getCard()
    dealerHand = [dealerCard1, dealerCard2]
    playerHand = [playerCard1, playerCard2]
    return dealerHand, playerHand

def checkScore(hand):
    handscore = 0
    for i in hand:
        if i == 'K' or i == 'Q' or i == 'J':
            handscore = handscore + 10
        elif i == 'A':
            if handscore >= 10:
                handscore = handscore + 1
            else:
                handscore = handscore + 11
        else:
            handscore = handscore + int(i)
    return handscore

def getCard():
    deck = list("2"*4 + "3"*4 + "4"*4 + "5"*4 + "6"*4 + "7"*4 + "8"*4 + "9"*4 + "J"*4 + "Q"*4 + "K"*4 + "A"*4)
    deck.extend(("10", "10", "10", "10"))
    card = random.choice(deck)
    return card

def gameOver(dealerScore, playerScore):
    return dealerScore >= 17 or playerScore >= 17

def printResults(n, dealerScore, playerScore, dealerHand, playerHand):
    print("Game {0} | Dealer Hand: {1} Score: {2}".format(n, dealerHand, dealerScore))
    print("Game {0} | Player Hand: {1} Score: {2}".format(n, playerHand, playerScore))

def printBustResults(n, dealerBusts, playerBusts):
    print("For {0} games of Black Jack".format(n))
    print("Dealer busted {0} games or {1:0.2%} of the time".format(dealerBusts, dealerBusts / n))
    print("Player busted {0} games or {1:0.2%} of the time".format(playerBusts, playerBusts / n))


main()