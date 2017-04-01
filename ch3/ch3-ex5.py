def main():
    print("This program determines the shipping cost of an order of Konditoeri coffee.")
    lbs = eval(input("How many pounds of coffee will you order: "))
    cost = (10.5 + .86) * lbs + 1.5
    print("The cost of your order is", cost)

main()
