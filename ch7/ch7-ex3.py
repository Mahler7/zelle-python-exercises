def grade(score):
    if score > 89 and score < 101:
        return "A"
    elif score > 79 and score < 90:
        return "B"
    elif score  > 69 and score < 80:
        return "C"
    elif score > 59 and score < 70: 
        return "D"
    elif score < 60:
        return "F"
    else:
        return "Please enter a number 0-100"

def inputs():
    score = eval(input("Enter a quiz score (0-100): "))
    return score

def intro():
    print("This program accepts a quiz score (0-100) and returns a grade")

def main():
    intro()
    score = inputs()
    letter_grade = grade(score)
    print("The grade is {0}".format(letter_grade))

main()