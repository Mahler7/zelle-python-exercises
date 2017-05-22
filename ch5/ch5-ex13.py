def main():
    print("This program determines the grade of a 5 point quiz by loading a file.")

    infileName = input("Enter file to open: ")
    outfileName = input("Enter a file grades should go in: ")
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    grades = ['F','F','D','C','B','A']
    for number in infile:
        grade = 'Your grade is {0}'.format(grades[int(number)])
        print(grade, file=outfile)

    infile.close()
    outfile.close()

    print("Grades ave been written to", outfileName)

main()