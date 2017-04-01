def main():
    print("This program calculates the slope of a line between two points.")
    x1, y1 = eval(input("Enter the x and y coordinates of the first point, separated by a comma: "))
    x2, y2 = eval(input("Enter the x and y coordinates of the second point, separated by a comma: "))
    slope = (y2 - y1) / (x2 - x1)
    print("The slope of your line is", slope)

main()