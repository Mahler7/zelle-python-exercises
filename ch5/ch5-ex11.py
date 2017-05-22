def main():
    print("This program illustrates a chaotic function for two values and prints a table")
    x = eval(input("Enter your first number (between 0 and 1): "))
    y = eval(input("Enter your second number (between 0 and 1): "))
    n = eval(input("Enter the number of times you would like to run the chaos function: "))
    print("Index {0} Value 1 {1} Value 2 {2}".format(x,y,n))
    print("---------------------------------")
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        
        print("{0:5} {1:15.6f} {2:10.6f}".format(i + 1, x, y))

main()