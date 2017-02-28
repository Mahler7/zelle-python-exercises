def main():
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the yearly interest rate: "))
    period = eval(input("Enter the number of times the interest is compounded each year: "))
    
    interest = rate / period
    
    for i in range(10 * period):
        principal = principal * (1 + interest)
        print(principal)
        print(interest)


    print("The value in 10 years is:", principal)

main()