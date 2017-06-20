def euclids(m, n):
    while m != 0:
        n, m = m, n % m
    return n

def inputs():
    validNumber = False
    while validNumber == False:
        try:
            m = eval(input("Enter the number you want to divide: "))
            n = eval(input("Enter the number you want to divide by: "))
            if m > 0 and n > 0:
                validNumber = True
            else:
                print("Both numbers must be larger than 0")
        except NameError:
            print("Enter a valid number")
    return m, n

def intro():
    print("This program finds the greatest common divisor")
    print("using Euclid's algorithm")

def main():
    intro()
    m, n = inputs()
    gcd = euclids(m, n)
    print("The greatest common denominator for {0} and {1} is {2}".format(m, n, gcd))

main()