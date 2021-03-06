import math

def main():
    print("This program finds the real solutions to a quadratic.")
    print()

    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print()
        print("The solutions are:", root1, root2)
    except ValueError:
        print("\nThe equation has no real roots.")


main()