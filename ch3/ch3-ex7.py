import math

def main():
    print("This program calculates the distance of a line between two points.")
    x1, y1 = eval(input("Enter the x and y coordinates of the first point, separated by a comma: "))
    x2, y2 = eval(input("Enter the x and y coordinates of the second point, separated by a comma: "))
    distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    print("The distance of your line is", distance)

main()