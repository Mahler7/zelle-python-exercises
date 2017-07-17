from sphere import Sphere

def main():
    print("This program calculates the volume and surface area of a sphere.")
    radius = eval(input("Please enter a radius: "))
    sphere = Sphere(radius)

    print("The volume is", sphere.volume(), " and the surface area is", sphere.surfaceArea())

main()