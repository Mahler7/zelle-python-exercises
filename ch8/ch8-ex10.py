#File Readline Loop
def mpg_total(averages):
    leg = 1
    for i in averages:
        print("For Leg {0} the average mpg was {1}".format(leg, i))
        leg = leg + 1
    total_average = sum(averages) / len(averages)
    print("For {0} legs of driving, the average mpg was {1}".format(leg - 1, total_average))

def mpg_averages(miles, gas):
    mpg = miles / gas
    return mpg

def readFile(infile):
    line = infile.readline()
    averages = []
    while line != "":
        miles, gas = line.split()
        mpg = mpg_averages(int(miles), int(gas))
        averages.append(mpg)
        line = infile.readline()
    mpg_total(averages)

def getFile():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    return infile

def intro():
    print("This program calculates the fuel efficiency of a multileg journey")

def main():
    intro()
    infile = getFile()
    readFile(infile)

main()