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

def inputs():
    validNumber = False
    averages = []
    while validNumber == False:
        try: 
            numbers = input("Enter your miles traveled and the gallons of gas used (<Enter> to quit) >> ")
            while numbers != "":
                miles, gas = numbers.split()
                mpg = mpg_averages(int(miles), int(gas))
                averages.append(mpg)
                numbers = input("Enter miles traveled and the gallons of gas used (<Enter> to quit) >> ")
            validNumber = True
        except NameError:
            print("Please enter a valid number")
        except ValueError:
            print("Two values seperated by a space must be entered or a valid number must be entered")
    mpg_total(averages)

def intro():
    print("This program calculates the fuel efficiency of a multileg journey")

def main():
    intro()
    mpg = inputs()

main()