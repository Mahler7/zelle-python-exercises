import math

def triangleArea(s, a, b, c):
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def sides(a, b, c):
    s = (a + b + c) / 2
    return s

def inputs():
    a, b, c = eval(input("Enter the length of the three sides of the triangle separated by a comma: "))
    return a, b, c

def intro():
    print("This program calculates the area of a triangle given the length of its three sides.")

def main():
    intro()
    a, b, c = inputs()
    s = sides(a, b, c)
    area = triangleArea(s, a, b, c)
    print("The area of your triangle is", area)

main()


