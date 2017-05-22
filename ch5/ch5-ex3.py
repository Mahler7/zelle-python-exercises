def main():
    print("This program determines the grade of a 100 point quiz.")
    score = eval(input("Enter a quiz score (0-100): "))

    grade = "F" * 60 + "D" * 10 + "C" * 10 + "B" * 10 + "A" * 11
    print('Your grade is {0}'.format(grade[score]))

main()