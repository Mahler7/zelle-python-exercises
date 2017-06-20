def print_fibonacci(n, fib_value):
    return "The Fibonacci value for {0} is {1}".format(n, fib_value)

def get_fibonacci(n):
    fib_value = 0
    fib1 = 0
    fib2 = 1
    for i in range(n - 1):
        fib_value = fib1 + fib2
        fib1 = fib2
        fib2 = fib_value
    return fib_value


def inputs():
    validData = False
    while validData == False:
        try:
            n = eval(input("Enter a number: "))
            if n > 0:
                validData = True
            else:
                validData = False
        except NameError:
            print("Please enter a valid number")
    return n

def intro():
    print("This program computes and outputs the nth Fibonacci number")

def main():
    intro()
    n = inputs()
    fib_value = get_fibonacci(n)
    statement = print_fibonacci(n, fib_value)
    print(statement)

main()