def main():
    print("This program determines the sum of numbers entered by a user.")
    n = eval(input("How many numbers would you like to sum: "))
    sum = 0
    for i in range(n):
        number = eval(input("Enter a number: "))
        sum = sum + number
    print("Your total sum is", sum)

main()