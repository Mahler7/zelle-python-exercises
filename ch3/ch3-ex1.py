import math

def main():
    print("This program calculates the volume and surface area of a sphere.")
    r = eval(input("Please enter a radius: "))
    volume = (4 / 3) * math.pi * (r ** 3)
    surface_area = 4 * math.pi * (r ** 2)
    print("The volume is", volume, " and the surface area is", surface_area)

main()