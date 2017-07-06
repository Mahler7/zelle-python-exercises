# 2 rounds
# first round win with 7 or 11, lose with 2, 3, or 12
# if win/lose not determined go to second round
# player must re roll point number before rolling 7 to win, roll 7 player loses

import random

def main():
    intro()
    n = inputs()
    playerWins, playerLosses = simCraps(n)
    printResults(playerWins, playerLosses)

def intro():
    pass

def inputs():
    validNumber = False
    while validNumber == False:
        try:
            n = eval(input("Enter the number of games you want to simulate: "))
            if n > 0.99:
                validNumber = True
            else:
                print("Please enter a number 1 or greater")
        except NameError:
            print("Please enter a valid number")
    return n

def simCraps(n):
    playerWins = 0
    playerLosses = 0
    for i in range(n):
        checkWin, roll = round1()
        if checkWin == "playerWon":
            playerWins = playerWins + 1
        elif checkWin == "playerLost":
            playerLosses = playerLosses + 1
        else:
            checkWin = round2(roll, checkWin)
            if checkWin == "playerWon":
                playerWins = playerWins + 1
            elif checkWin == "playerLost":
                playerLosses = playerLosses + 1
    return playerWins, playerLosses

def round1():
    roll = rollDice()
    gameRound = 1
    checkWin = gameOver(gameRound, roll, point='')
    return checkWin, roll

def round2(point, checkWin):
    gameRound = 2
    while checkWin == "point":
        roll = rollDice()
        checkWin = gameOver(gameRound, roll, point)
    return checkWin

def gameOver(gameRound, roll, point):
    if gameRound == 1:
        if roll == 2 or roll == 3 or roll == 12:
            #print("Player lost")
            return "playerLost"
        elif roll == 7 or roll == 11:
            #print("Player won")
            return "playerWon"
        else:
            return "point"
    else:
        if roll == point:
            #print("Player won")
            return "playerWon"
        elif roll == 7:
            #print("Player lost")
            return "playerLost"
        else:
            return "point"


def rollDice():
    die1 = random.randrange(1,7,1)
    die2 = random.randrange(1,7,1)
    roll = die1 + die2
    return roll

# def rollDice():
#     validRoll = False
#     while validRoll == False:
#         try:
#             userRoll = input("Press enter to roll ")
#             if userRoll == '':
#                 die1 = random.randrange(1,7,1)
#                 die2 = random.randrange(1,7,1)
#                 validRoll = True
#             else:
#                 print("You need to press enter to roll")
#         except ValueError:
#             print("You must press enter to roll")
    
#     roll = die1 + die2
#     print("You rolled a", roll)
#     return roll

def printResults(playerWins, playerLosses):
    n = playerWins + playerLosses
    print("\nFor {0} games of Craps".format(n))
    print("The player won {0} games with a {1:0.2%} win percentage".format(playerWins, playerWins / n))

main()