def energy_requirements(temperatures):
    for i in temperatures:
        if i < 60:
            print(i, "is a heating degree day")
        elif i > 80:
            print(i, "is a cooling degree day")
        elif i >= 60 and i <= 80:
            print(i, "is neither a cooling or heating degree day")

def inputs():
    validNumber = False
    temperatures = []
    while validNumber == False:
        temperature = input("Enter an average temperature for a day (<Enter to quit>) ")
        if temperature != "": temperatures.append(int(temperature))
        try:
            while temperature != "":
                temperature = input("Enter an average temperature for a day (<Enter to quit>) ")
                if temperature != "": temperatures.append(int(temperature))
            validNumber = True
        except NameError:
            print("Please enter a valid number")
    return temperatures

def intro():
    print("This program keeps a running total of") 
    print("heating degree days and cooling degree days")

def main():
    intro()
    temperatures = inputs()
    energy_requirements(temperatures)

main()