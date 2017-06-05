def classified(credits):
    if credits <= 6:
        return "Freshman"
    elif credits > 6 and credits <= 15:
        return "Sophmore"
    elif credits > 15 and credits <= 25:
        return "Junior"
    elif credits > 25:
        return "Senior"

def inputs():
    credits = eval(input("Enter the number of credits earned: "))
    return credits

def intro():
    print("This program calculates class standing according to credits earned.")

def main():
    intro()
    credits = inputs()
    level = classified(credits)
    print("The student is a {0}".format(level))

main()