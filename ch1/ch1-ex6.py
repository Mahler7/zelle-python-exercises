def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * x * (1 - x)
        x = 3.9 * (x - x * x)
        x = 3.9 * x - 3.9 * x * x
        print(x)
        print("------------")
        print(x)
        print("------------")
        print(x)
        print("------------")

main()
