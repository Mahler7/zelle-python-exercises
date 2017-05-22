def main():
    print("This program determines the grade of a 5 point quiz.")
    score = eval(input("Enter a quiz score (0-5): "))

    grades = ['F','F','D','C','B','A']
    print('Your grade is {0}'.format(grades[score]))

main()