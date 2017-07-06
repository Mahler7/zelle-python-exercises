#win at 25 and by 2 points, only score on serve
# print intro
# get inputs teamA and teamB win probability and number of games
# simulate n games using probabilities
# print results
from random import random

def main():
    intro()
    a, b, n = inputs()
    winsA, winsB = volleyball_sim(a, b, n, rally=False)
    rallyWinsA, rallyWinsB = volleyball_sim(a, b, n, rally=True)
    print_results(winsA, winsB, rallyWinsA, rallyWinsB)

def intro():
    print("This program simulates a game of volleyball and rally volleyball between two")
    print("teams called 'A' and 'B'. The abilities of each team is")
    print("indicated by a probability (a number between 0 and 1) The")
    print("program determines whether rally scoring gives a team an advantage.")
    print("Team A always has the first serve")

def inputs(): 
    print("Team A")
    a = getTeamProb()
    print("Team B")
    b = getTeamProb()
    n = getNumberOfGames()
    return a, b, n

def getTeamProb():
    validNumber = False
    while validNumber == False:
        try:
            teamProb = eval(input("Enter the team's probability of winning the serve (0-1): "))
            if teamProb >= 0 and teamProb <= 1:
                validNumber = True
            else:
                print("Please enter a number between 0 and 1")
        except NameError:
            print("Please enter a valid number")
    return teamProb

def getNumberOfGames():
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

def volleyball_sim(a, b, n, rally):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simGame(a, b, rally)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simGame(a, b, rally):
    scoreA = 0
    scoreB = 0
    serving = 'A'
    while not gameOver(scoreA, scoreB, rally):
        if serving == 'A' and rally == True:
            if random() < a:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
                serving = 'B'
        elif serving == 'B' and rally == True:
            if random() < b:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
                serving = 'A'
        elif serving == 'A' and rally == False:
            if random() < a:
                scoreA = scoreA + 1
            else:
                serving = 'B'
        elif serving == 'B' and rally == False:
            if random() < b:
                scoreB = scoreB + 1
            else:
                serving = 'A'
    return scoreA, scoreB

def gameOver(scoreA, scoreB, rally):
    if rally == False:
        return (scoreA >= 15 and scoreA - scoreB >= 2) or (scoreB >= 15 and scoreB - scoreA >= 2)
    elif rally == True:
        return (scoreA >= 25 and scoreA - scoreB >= 2) or (scoreB >= 25 and scoreB - scoreA >= 2)

def print_results(winsA, winsB, rallyWinsA, rallyWinsB):
    n = winsA + winsB
    print("\nFor {0} games simulated".format(n))
    print("Team A won {0} games with a {1:0.2%} win rate".format(winsA, winsA / n))
    print("Team B won {0} games with a {1:0.2%} win rate".format(winsB, winsB / n))
    print("Team A won {0} rally games with a {1:0.2%} win rate".format(rallyWinsA, rallyWinsA / n))
    print("Team B won {0} rally games with a {1:0.2%} win rate".format(rallyWinsB, rallyWinsB / n))

main()