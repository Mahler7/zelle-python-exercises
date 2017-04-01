def main():
    print("This program finds the cube of the first natural numbers")
    n = eval(input("Enter the number of natural numbers you would like to cube: "))
    cube = 0
    for i in range(n):
        cube = cube + (i ** 3)
    print("The cube of your numbers is", cube)

main()