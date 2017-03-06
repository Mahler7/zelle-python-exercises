def main():
    print("This program calculates the molecular weight of a hydrocarbon.")
    h = eval(input("Enter the number of hydrogen atoms: "))
    c = eval(input("Enter the number of carbon atoms: "))
    o = eval(input("Enter the number of oxygen atoms: "))

    weight = (h * 1.0079) + (c * 12.011) + (o * 15.9994)
    print("The weight of your hydrocarbon is", weight)

main()