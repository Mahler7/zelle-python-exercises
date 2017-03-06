import math

def main():
    print("This program calculates the cost per square inch of a circular pizza.")
    d = eval(input("Enter the diameter of your pizza: "))
    price = eval(input("Enter the price of your pizza: "))
    area = math.pi * (d / 2) ** 2
    cost_per_square_inch = price / area
    print("The cost per square inch for your pizza is", cost_per_square_inch)

main()
