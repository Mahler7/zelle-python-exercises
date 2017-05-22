def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    n = eval(input("Enter the number of years you will invest: "))

    print("{0} {1:10}".format("Year", "Value"))
    print("{0} {1:10.2f}".format(0, principal))
    for i in range(n):
        principal = principal * (1 + apr)
        print("{0} {1:10.2f}".format(i + 1, principal))


main()