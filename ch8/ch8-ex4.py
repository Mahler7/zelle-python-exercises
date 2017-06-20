def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def syracuse(n):
    while n != 1:
        eooVal = even_or_odd(n)
        if eooVal == "Even":
            n = n / 2
        elif eooVal == "Odd":
            n = (3 * n) + 1
        print(int(n))

def inputs():
    validNumber = False
    while validNumber == False:
        try:
            n = eval(input("Enter a starting number: "))
            if n < 1:
                print("Number must be greater than 1")
            else:
                validNumber = True
        except NameError:
            print("Enter a valid number")
    return n

def intro():
    print("This program prints the Syracuse sequence for a starting number")

def main():
    intro()
    n = inputs()
    syracuse(n)

main()