import math

def volume(radius):
    v = (4 / 3) * math.pi * (radius ** 3)
    return v

def surfacearea(radius):
    a = 4 * math.pi * radius ** 2
    return a

def inputs():
    radius = eval(input("Please enter a radius: "))
    return radius

def intro():
    print("This program calculates the volume and surface area of a sphere")

def main():
    intro()
    radius = inputs()
    v = volume(radius)
    a = surfacearea(radius)
    print("Sphere volume: {0}, Sphere surface area: {1}".format(v, a))

main()