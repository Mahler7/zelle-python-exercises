import math

def main():
    print("This program determines the length of a ladder required to reach a given height.")
    angle = eval(input("Enter the angle of the ladder: "))
    height = eval(input("Enter the height of the house: "))
    radians = angle * (math.pi / 180)
    length = height / math.sin(radians)
    print("The length of the ladder needs to be", length)

main()
