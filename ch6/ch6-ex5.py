import math

def pizzaArea(d):
    area = math.pi * (d / 2) ** 2
    return area

def pizzaCost(price, area):
    cost_per_square_inch = price / area
    return cost_per_square_inch

def inputs():
    d = eval(input("Enter the diameter of your pizza: "))
    price = eval(input("Enter the price of your pizza: "))
    return d, price

def intro():
    print("This program calculates the cost per square inch of a circular pizza.")

def main():
    intro()
    d, price = inputs()
    area = pizzaArea(d)
    cost_per_square_inch = pizzaCost(price, area)
    
    print("The area of your pizza is", area)
    print("The cost per square inch for your pizza is", cost_per_square_inch)

main()