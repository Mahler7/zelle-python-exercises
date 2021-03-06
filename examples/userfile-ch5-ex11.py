def main():
    print("This program creates a file ofusernames from a")
    print("file of names.")

    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in?")

    infile = open(infileName, "r")
    outfileName = open(outfileName, "w")

    for line in infile:
        first, last = line.split()
        uname = (first[0] + last[:7]).lower()
        print(uname, file=outfile)

    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

main()