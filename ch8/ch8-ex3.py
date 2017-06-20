def doubled_investment(principal, interest_rate):
    doubleInvestment = principal * 2
    years = 0
    while principal <= doubleInvestment:
        principal = principal * (1 + interest_rate)
        years = years + 1
    return principal, years

def get_principal():
    validPrincipal = False
    while validPrincipal == False:
        try:
            principal = eval(input("Enter the principal: "))
            if principal < 0:
                validPrincipal = False
                print("Principal must be greater than 0")
            else:
                validPrincipal = True
        except ValueError:
            print("Please enter a valid number")
        except NameError:
            print("Please enter a valid number")
    return principal

def get_interest_rate():
    validInterestRate = False
    while validInterestRate == False:
        try:
            interest_rate = eval(input("Enter the interest rate: "))
            if interest_rate < 0:
                validInterestRate = False
                print("Principal must be greater than 0")
            else:
                validInterestRate = True
        except ValueError:
            print("Please enter a valid number")
        except NameError:
            print("Please enter a valid number")
    return interest_rate

def inputs():
    principal = get_principal()
    interest_rate = get_interest_rate()
    return principal, interest_rate

def intro():
    print("This program determines how long it takes for an investment to double")
    print("given the annualized interest rate.")

def main():
    intro()
    principal, interest_rate = inputs()
    investment, years = doubled_investment(principal, interest_rate)
    print("Your investment will double in {0} years, and the total amount invested will be ${1:0.2f}".format(years, investment))

main()