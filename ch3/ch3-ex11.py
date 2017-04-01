def main():
    print("This program finds the sum of the first natural numbers")
    n = eval(input("Enter the number of natural numbers you would like to sum: "))
    sum = 0
    for i in range(n):
        sum = sum + i
    print("The sum of your numbers is", sum)

main()