def grade(score):
    if score == 5:
        return "A"
    elif score == 4:
        return "B"
    elif score  == 3:
        return "C"
    elif score == 2: 
        return "D"
    elif score == 1 or score == 0:
        return "F"
    else:
        return "Please enter a number 0-5"

def inputs():
    score = eval(input("Enter a quiz score (0-5): "))
    return score

def intro():
    print("This program accepts a quiz score (0-5) and returns a grade")

def main():
    intro()
    score = inputs()
    letter_grade = grade(score)
    print("The grade is {0}".format(letter_grade))

main()