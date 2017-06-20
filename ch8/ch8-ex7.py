def goldbach_values(primes, n):
    highValue = n / 2
    for i in primes:
        if i <= highValue and n - i in primes:
            print("Prime values {0} + {1} = {2}".format(i, (n - i), n))

def get_primes(n):
    p = 2
    primes = []
    while p <= n:
        if is_prime(p):
            primes.append(p)
        p = p + 1
    goldbach_values(primes, n)

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
            if n <= 0:
                print("Please enter a value greater than 0")
            elif n % 2 != 0:
                print("Please enter an even number")
            elif n > 0: 
                validNumber = True
        except NameError:
            print("Enter a valid number")
    return n

def intro():
    print("This program executes the Goldbach conjecture")
    print("by finding the two prime numbers that add up to the even value")

def main():
    intro()
    n = inputs()
    get_primes(n)

main()