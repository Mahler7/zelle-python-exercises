def main():
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years invested: "))
    investment = eval(input("Enter what you would like to invest every year: "))

    for i in range(years):
        principal = principal * (1 + apr) + investment


    print("The value in", years, "years is:", principal)

main()