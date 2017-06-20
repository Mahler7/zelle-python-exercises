import math

def print_prime(n):
    p = 2
    while p <= n:
        if is_prime(p):
            print(p)
        p = p + 1

def is_prime(n):
    i = 2
    isPrime = False
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
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
    print("This program finds all the prime values up to a certain number")

def main():
    intro()
    n = inputs()
    print_prime(n)

main()