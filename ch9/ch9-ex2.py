from random import random

def main():
    printIntro()
    probA, probB, m, n = getInputs()
    matchWinsA, matchWinsB, totalWinsA, totalWinsB, totalShutoutsA, totalShutoutsB = simMMatches(probA, probB, m, n)
    printSummary(matchWinsA, matchWinsB, totalWinsA, totalWinsB, m, n, totalShutoutsA, totalShutoutsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print("players called 'A' and 'B'. The abilities of each player is")
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve")

def getInputs():
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    m = eval(input("How many matches to simulate? "))
    n = eval(input("How many games per match? "))
    return a, b, m, n

def simMMatches(probA, probB, m, n):
    totalMatchWinsA = 0
    totalMatchWinsB = 0
    totalShutoutsA = 0
    totalShutoutsB = 0
    totalWinsA = 0
    totalWinsB = 0
    while totalMatchWinsA < m and totalMatchWinsB < m:
        winsA, winsB, shutoutA, shutoutB = simNGames(n, probA, probB)
        totalWinsA = totalWinsA + winsA
        totalWinsB = totalWinsB + winsB  
        totalShutoutsA = totalShutoutsA + shutoutA
        totalShutoutsB = totalShutoutsB + shutoutB
        if winsA > winsB:
            totalMatchWinsA = totalMatchWinsA + 1
        elif winsB > winsA:
            totalMatchWinsB = totalMatchWinsB + 1
    return totalMatchWinsA, totalMatchWinsB, totalWinsA, totalWinsB, totalShutoutsA, totalShutoutsB

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    shutoutA = 0
    shutoutB = 0
    matchWin = n / 2
    while winsA <= matchWin and winsB <= matchWin:
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
            if scoreB == 0:
                shutoutA = shutoutA + 1
        else:
            winsB = winsB + 1
            if scoreA == 0:
                shutoutB = shutoutB + 1
    return winsA, winsB, shutoutA, shutoutB

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(scoreA, scoreB):
    return scoreA == 15 or scoreB == 15

def printSummary(matchWinsA, matchWinsB, winsA, winsB, m, n, shutoutsA, shutoutsB):
    print("\nMatches simulated:", m)
    print("Games per match simulated:", n)
    print("Match wins for A: {0} ({1:0.1%})".format(matchWinsA, matchWinsA / m))
    print("Match wins for B: {0} ({1:0.1%})".format(matchWinsB, matchWinsB / m))
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA / (n * m)))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB / (n * m)))
    print("Shutouts for A: {0} ({1:0.1%})".format(shutoutsA, shutoutsA / (n * m)))
    print("Shutouts for B: {0} ({1:0.1%})".format(shutoutsB, shutoutsB / (n * m)))

if __name__ == '__main__': main()