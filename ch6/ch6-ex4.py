def sumN(n):
    sum = 0
    for i in range(n):
        sum = sum + i
    return sum

def sumNCubes(n):
    sum = 0
    for i in range(n):
        sum = sum + i ** 3
    return sum

def inputs():
    n = eval(input("Enter a number: "))
    return n

def intro():
    print("This program gets the sums of n natural numbers")
    print("and sums of the cubes of n natural numbers.")

def main():
    intro()
    n = inputs()
    sum_natural = sumN(n)
    sum_cubes = sumNCubes(n)
    print("The sum of your natural numbers is {0}".format(sum_natural))
    print("and the summed cube of your natural numbers is {0}".format(sum_cubes))

main()