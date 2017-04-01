import math

def main():
    print("This program calculates the area of a triangle given the length of its three sides.")
    a, b, c = eval(input("Enter the length of the three sides of the triangle separated by a comma: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area of your triangle is", area)

main()
