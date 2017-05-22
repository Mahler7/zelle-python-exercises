def main():
    print("This program counts the lines, words, and characters contained in a file.")
    infileName = input("Enter a file name to read: ")
    outfileName = input("Enter a file to display the counts to: ")
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    lines = []
    words = []
    word_count = 0
    characters = []

    for line in infile:
        lines.append(line)
        words = line.split()
        word_count = word_count + len(words)
        for character in line:
            characters.append(character)


    counts = "This file contains {0} lines, {1} words, and {2} characters".format(len(lines), word_count, len(characters))

    print(counts, file=outfile)

    infile.close()
    outfile.close()
    print("Counts have been written to", outfileName)

main()