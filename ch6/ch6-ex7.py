def fibonacci(n):
    fib_value = 0
    fib1 = 0
    fib2 = 1
    while fib_value <= n:
        fib_value = fib1 + fib2
        if fib_value <= n:
            print(fib_value)
        else:
            break
        fib1 = fib2
        fib2 = fib_value

def inputs():
    n = eval(input("Enter a number to see all the Fibonacci values up to that number: "))
    return n

def intro():
    print("This program computes the nth Fibonacci number.")

def main():
    intro()
    n = inputs()
    fibonacci(n)

main()