import math

def print_number(isPrime):
    if isPrime == True:
        return "Number is prime"
    elif isPrime == False:
        return "Number is not prime"

def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
        print(i)
    return True

def inputs():
    validNumber = False
    while validNumber == False:
        try:
            n = eval(input("Enter a number: "))
            if n > 2:
                validNumber = True
            else:
                print("Enter a number larger than 2")
        except NameError:
            print("Enter a valid number")
    return n

def intro():
    print("This program determines whether a number is prime")

def main():
    intro()
    n = inputs()
    isPrime = is_prime(n)
    statement = print_number(isPrime)
    print(statement)

main()