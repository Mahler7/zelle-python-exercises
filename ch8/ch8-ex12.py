def energy_requirements(temperatures):
    for i in temperatures:
        if i < 60:
            print(i, "is a heating degree day")
        elif i > 80:
            print(i, "is a cooling degree day")
        elif i >= 60 and i <= 80:
            print(i, "is neither a cooling or heating degree day")

def readFile(infile):
    line = infile.readline()
    temperatures = []
    while line != "":
        temperatures.append(int(line))
        line = infile.readline()
    return temperatures

def getFile():
    filename = input("Enter the name of the file: ")
    infile = open(filename, 'r')
    return infile

def intro():
    print("This program keeps a running total of") 
    print("heating degree days and cooling degree days")

def main():
    intro()
    infile = getFile()
    temperatures = readFile(infile)
    energy_requirements(temperatures)

main()