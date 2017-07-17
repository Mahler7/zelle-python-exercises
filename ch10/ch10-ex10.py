from cube import Cube

def main():
    print("This program calculates the volume and surface area of a cube.")
    side = eval(input("Enter the length of a cube's side: "))
    cube = Cube(side)
    print("The volume is", cube.volume(), " and the surface area is", cube.surfaceArea())

main()
