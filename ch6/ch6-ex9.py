def grades(score):
    grade = "F" * 60 + "D" * 10 + "C" * 10 + "B" * 10 + "A" * 11
    return grade[score]

def inputs():
    score = eval(input("Enter a quiz score (0-100): "))
    return score

def intro():
    print("This program determines the grade of a 100 point quiz.")

def main():
    intro()
    score = inputs() 
    grade = grades(score)
    print('Your grade is {0}'.format(grade))

main()